run:
	docker-compose restart iot
	docker-compose exec iot python3.9 -m user-service.iot.service

run_web:
	uvicorn user-service.iot.web.main:app --reload --host 0.0.0.0 --port 8000

run_dev:
	cp .env_dev .env
	python3.9 -m user-service.iot.service

deploy_release_imp:
	cp .env_release .env
	rm -fr user-service.tar.gz
	rm -fr user-service/.iot
	tar  cvzf - --exclude '__pycache__' user-service .env Makefile docker-compose.yml Dockerfile >> user-service.tar.gz
	scp ./user-service.tar.gz ubuntu@pbu-iot.zshield.net:/root/bookbook
	ssh ubuntu@pbu-iot.zshield.net "cd /root/bookbook; tar zxvf user-service.tar.gz;docker-compose down; rm -fr user-service/.iot/huey; docker-compose up;"

deploy_test:
	git pull
	cp .env_test .env
	rm -fr user-service.tar.gz
	tar  cvzf - --exclude '__pycache__' user-service .env Makefile docker-compose.yml nginx_config.conf >> user-service.tar.gz
	scp ./user-service.tar.gz root@hw1.bookbook.net.cn:/root/bookbook
	ssh root@hw1.bookbook.net.cn "cd /root/bookbook; tar zxvf user-service.tar.gz; docker-compose down; docker-compose up;"

tlog:
	ssh root@hw1.bookbook.net.cn "cd /root/bookbook/logs; tail -f log.log"

deploy : deploy_test

clear_db:
	python3.9 -m user-service.iot.cmd.clear_database

# docker-compose exec iot python3.9 -m user-service.iot.service


# To use the "confirm" target inside another target,
# use the " if $(MAKE) -s confirm ; " syntax.
deploy_release:
	@if $(MAKE) -s confirm ; then \
    	     deploy_release_imp ; \
	fi
.PHONY: deploy_release

# The CI environment variable can be set to a non-empty string,
# it'll bypass this command that will "return true", as a "yes" answer.
confirm:
	@if [[ -z "$(CI)" ]]; then \
		REPLY="" ; \
		read -p "⚠ Are you sure? [y/n] > " -r ; \
		if [[ ! $$REPLY =~ ^[Yy]$$ ]]; then \
			printf $(_ERROR) "KO" "Stopping" ; \
			exit 1 ; \
		else \
			printf $(_TITLE) "OK" "Continuing" ; \
			exit 0; \
		fi \
	fi
.PHONY: confirm
_WARN := "\033[33m[%s]\033[0m %s\n"  # Yellow text for "printf"
_TITLE := "\033[32m[%s]\033[0m %s\n" # Green text for "printf"
_ERROR := "\033[31m[%s]\033[0m %s\n" # Red text for "printf"

# Notes:
#
# As we're using an "if" statement,
# we need to use ";" and "\" at the end of lines,
# else make would consider each line to be a separate command to call,
# which doesn't work.
# Using ";" and "\" at the end of lines helps make
# interpret this "if" as one single statement/command.
#
# You can replace ";" with "&&" if you need to stop the
# execution process before running next commands.
#
# 

proxy_test:
	ssh root@hw1.bookbook.net.cn "export https_proxy="http://192.168.108.13:7440"; curl www.baidu.com;"