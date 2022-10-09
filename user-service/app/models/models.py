# coding: utf-8
from sqlalchemy import Boolean, Column, Integer, Table, Text, text, String
from sqlalchemy.sql.sqltypes import NullType
from app.db import Base


class AccountBooksTable(Base):
    __tablename__ = "AccountBooksTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    title = Column(Text)
    logo = Column(Text)
    sortingNum = Column(Integer)


class AccountClassTable(Base):
    __tablename__ = "AccountClassTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    title = Column(Text)
    logo = Column(Text)
    income = Column(Boolean)
    showFlag = Column(Boolean)
    customFlag = Column(Boolean)
    sortingNum = Column(Integer)


class AccountLocationTable(Base):
    __tablename__ = "AccountLocationTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    accountAddTime = Column(Text)
    latitude = Column(Text)
    longitude = Column(Text)
    name = Column(Text)
    thoroughfare = Column(Text)
    subThoroughfare = Column(Text)
    locality = Column(Text)
    subLocality = Column(Text)
    administrativeArea = Column(Text)
    subAdministrativeArea = Column(Text)
    postalCode = Column(Text)
    isoCountryCode = Column(Text)
    country = Column(Text)
    inlandWater = Column(Text)
    ocean = Column(Text)


class AccountMultimediaTable(Base):
    __tablename__ = "AccountMultimediaTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    accountAddTime = Column(Text)
    type = Column(Integer)
    serverUrl = Column(Text)
    sortingNum = Column(Integer)


class AssetsAccountTable(Base):
    __tablename__ = "AssetsAccountTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    assetsType = Column(Integer)
    currentAmount = Column(Text)
    totalAmount = Column(Text)
    cardNumber = Column(Text)
    noteStr = Column(Text)
    title = Column(Text)
    logo = Column(Text)
    needAdd = Column(Boolean)


class AssetsActionTable(Base):
    __tablename__ = "AssetsActionTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    assetsAddTime = Column(Text)
    currentAmount = Column(Text)
    dailyAccountAddTime = Column(Text, server_default=text("''"))
    fromSubmitAccount = Column(Boolean)
    fromTransfer = Column(Boolean)
    transferIncome = Column(Boolean)
    transferFromAddTime = Column(Text)
    transferToAddTime = Column(Text)
    saveMoneySubAddTime = Column(Text)
    fromSaveMoney = Column(Boolean)
    saveMoneyIncome = Column(Boolean)
    saveMoneyFromAddTime = Column(Text)
    saveMoneyToAddTime = Column(Text)


class BudgetClassTable(Base):
    __tablename__ = "BudgetClassTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    classTime = Column(Text)
    amount = Column(Text)


class CardAccountTable(Base):
    __tablename__ = "CardAccountTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    cardType = Column(Integer)
    cardNumber = Column(Text)
    noteStr = Column(Text)
    title = Column(Text)
    logo = Column(Text)
    cardOwner = Column(Text)


class DailyAccountTable(Base):
    __tablename__ = "DailyAccountTable"

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    note = Column(Text)
    addTime = Column(Text)
    updateTime = Column(Text)
    accountTime = Column(Text)
    income = Column(Boolean)
    amount = Column(Text)
    classTime = Column(Text)
    accountBook = Column(Text)
    assetsAddTime = Column(Text)
    importAddTime = Column(Text)
    submitAccountFlag = Column(Boolean, server_default=text("false"))
    submitAccountFinished = Column(Boolean)
    submitAccountTime = Column(Text)
    submitAccountAmount = Column(Text)
    submitAssetsAddTime = Column(Text)


class ImportRecordTable(Base):
    __tablename__ = "ImportRecordTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    logo = Column(Text)
    importTime = Column(Text)
    importCount = Column(Integer)
    sourceType = Column(Integer)


class InvoicesTable(Base):
    __tablename__ = "InvoicesTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    title = Column(Text)
    invoicesNumber = Column(Text)
    address = Column(Text)
    phoneNumber = Column(Text)
    bankName = Column(Text)
    bankNumber = Column(Text)


class QuickTable(Base):
    __tablename__ = "QuickTable"

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    note = Column(Text)
    addTime = Column(Text)
    updateTime = Column(Text)
    accountTime = Column(Text)
    income = Column(Boolean)
    amount = Column(Text)
    classTime = Column(Text)
    accountBook = Column(Text)
    sortingNum = Column(Integer)
    assetsAddTime = Column(Text)


class RecommendNoteTable(Base):
    __tablename__ = "RecommendNoteTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    dailyTime = Column(Text)
    classTime = Column(Text)
    note = Column(Text)


class SaveMoneySubTable(Base):
    __tablename__ = "SaveMoneySubTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    currentAmount = Column(Text)
    saveAddTime = Column(Text)
    fromAccountTime = Column(Text)
    toAccountTime = Column(Text)
    dayTime = Column(Text)
    dayAddTime = Column(Text)
    note = Column(Text)


class SaveMoneyTable(Base):
    __tablename__ = "SaveMoneyTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    beginTime = Column(Text)
    endTime = Column(Text)
    title = Column(Text)
    logo = Column(Text)
    currentAmount = Column(Text)
    totalAmount = Column(Text)
    # TODO 不能有bool列
    # bool = Column(NullType)
    saveType = Column(Integer)
    beginAmount = Column(Text)
    archiveStatus = Column(Boolean)
    sortingNum = Column(Integer)


class TagCategoryTable(Base):
    __tablename__ = "TagCategoryTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    title = Column(Text)
    sortingNum = Column(Integer)


class TagSubShowTable(Base):
    __tablename__ = "TagSubShowTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    sortingNum = Column(Integer)
    tagSubAddTime = Column(Text)
    categoryAddTime = Column(Text)
    dailyAccountAddTime = Column(Text)


class TagSubTable(Base):
    __tablename__ = "TagSubTable"

    id = Column(Integer, primary_key=True)
    addTime = Column(Text)
    updateTime = Column(Text)
    title = Column(Text)
    colorImgStr = Column(Text)
    sortingNum = Column(Integer)
    categoryAddTime = Column(Text)


# t_sqlite_sequence = Table(
#     "sqlite_sequence", metadata, Column("name", NullType), Column("seq", NullType)
# )
