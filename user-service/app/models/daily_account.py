from sqlalchemy import Column, String, Float, Integer, Boolean
from app.db import Base


class DailyAccountModel(Base):
    __tablename__ = "daily_accounts"
    id = Column(Integer, primary_key=True, index=True)

    user = Column(String)

    syncTime = Column(Integer)

    # 标题
    title = Column(String)
    # 备注
    note = Column(String)

    addTime = Column(Integer)
    updateTime = Column(Integer)
    # 记的某天账时间
    accountTime = Column(Integer)

    # 收入/支出 true:收入 false:支出
    income = Column(Boolean)
    # 金额
    amount = Column(Float)

    # 类别id
    classTime = Column(Integer)
    # 所属账本(内存账本model的addTime)
    accountBook = Column(Integer)

    # 从XX资产支出(内存资产model的addTime)
    assetsAddTime = Column(Integer)

    # 导入来源(内存导入表model的addTime：13位时间戳，此值为空表示并不是导入来的，若有值表示是导入来的)
    importAddTime = Column(Integer)

    # 是否为报销账单(若为报销账单，则不计入统计页收入或支出项，报销项为单独统计)
    submitAccountFlag = Column(Boolean)
    # 下面三项值只有当submitAccountFlag为true时才有意义
    # 若为报销账单，此账单是否为已报销状态
    submitAccountFinished = Column(Boolean)
    # 若为报销账单，记录报销时间(内存13位时间戳)
    submitAccountTime = Column(Integer)
    # 此单报销金额(比如可能花费了100元，但报销的时候只报了95元，可能与上面的amount值不同,但绝大部分情况需要与amount值相同)
    submitAccountAmount = Column(Integer)
    # 只有submitAccountFlag为true即为报销账单 ，且submitAccountFinished报销时，此值才有意义，表示报销入账的资产addTime(为空或13位时间戳)
    submitAssetsAddTime = Column(Integer)
