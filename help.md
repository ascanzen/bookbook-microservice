ssh -Ng -R 64088:localhost:64088 root@hw1.bookbook.net.cn

export https_proxy="http://127.0.0.1:64088"
unset http_proxy