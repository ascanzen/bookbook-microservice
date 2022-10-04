from numpy import tile
import pytest
from crown import *
import datetime
import logging

# DATABASENAME = 'taos_test'
# HOST = 'localhost'
# db = TdEngineDatabase(DATABASENAME,host=HOST,user="root",passwd="taosdata")
logger.setLevel(logging.DEBUG)
DATABASENAME = "taos_tests"
HOST = "hw1.bookbook.net.cn"
PORT = 6041
# 默认端口 6041，默认用户名：root,默认密码：taosdata
db = TdEngineDatabase(
    DATABASENAME, host=HOST, user="root", port=PORT, passwd="taosdata"
)


class DailyAccount(SuperModel):
    id = BinaryField(db_column="id")
    # 标题
    title = BinaryField(db_column="title")
    # 备注
    note = BinaryField(db_column="note")

    addTime = IntegerField(db_column="addTime")
    updateTime = IntegerField(db_column="updateTime")
    # 记的某天账时间
    accountTime = IntegerField(db_column="accountTime")

    # 收入/支出 true:收入 false:支出
    income = BooleanField(db_column="income")
    # 金额
    amount = FloatField(db_column="amount")

    # 类别id
    classTime = IntegerField(db_column="classTime")
    # 所属账本(内存账本model的addTime)
    accountBook = IntegerField(db_column="accountBook")

    # 从XX资产支出(内存资产model的addTime)
    assetsAddTime = IntegerField(db_column="assetsAddTime")

    # 导入来源(内存导入表model的addTime：13位时间戳，此值为空表示并不是导入来的，若有值表示是导入来的)
    importAddTime = IntegerField(db_column="importAddTime")

    # 是否为报销账单(若为报销账单，则不计入统计页收入或支出项，报销项为单独统计)
    submitAccountFlag = BooleanField(db_column="submitAccountFlag")
    # 下面三项值只有当submitAccountFlag为true时才有意义
    # 若为报销账单，此账单是否为已报销状态
    submitAccountFinished = BooleanField(db_column="submitAccountFinished")
    # 若为报销账单，记录报销时间(内存13位时间戳)
    submitAccountTime = IntegerField(db_column="submitAccountTime")
    # 此单报销金额(比如可能花费了100元，但报销的时候只报了95元，可能与上面的amount值不同,但绝大部分情况需要与amount值相同)
    submitAccountAmount = IntegerField(db_column="submitAccountAmount")
    # 只有submitAccountFlag为true即为报销账单 ，且submitAccountFinished报销时，此值才有意义，表示报销入账的资产addTime(为空或13位时间戳)
    submitAssetsAddTime = IntegerField(db_column="submitAssetsAddTime")

    class Meta:
        order_by = ["-ts"]
        database = db
        db_table = "daily_account"
        location = BinaryField(max_length=30)
        groupid = IntegerField(db_column="gid")


def test_create_drop_sontable():
    son = DailyAccount.create_son_table("d1", location="beijing", groupid=3)
    print(db.get_tables())
    assert son.table_exists()
    assert son.drop_table()
    assert not son.table_exists()
    assert DailyAccount.drop_table()
    assert not DailyAccount.supertable_exists()


TableT = DailyAccount.create_son_table("user1", location="beijing", groupid=3)
TableT1 = DailyAccount.create_son_table("user2", location="nanjing", groupid=5)


for i in range(1, 11):
    # time.sleep(30)
    m = TableT(
        title=f"title{i}",
        ts=datetime.datetime.now() - datetime.timedelta(hours=(12 - i)),
    )
    m.save()
