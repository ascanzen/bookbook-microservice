//
//  AssetsActionModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2020/8/20.
//  Copyright © 2020 chuncheng jia. All rights reserved.
//

import UIKit

//资产操作Model
class AssetsActionModel: NSObject {
    
    var addTime = ""
    var updateTime = ""
    
    //对应资产Model的addTime
    var assetsAddTime = ""
    
    //金额
    var currentAmount = ""
        
    //操作账单addTime 若有值，则表示从当前账单的操作，若无值，表示主动更新余额
    var dailyAccountAddTime = ""
    
    //来自于报销入账操作(若为true，即报销入账时，上面dailyAccountAddTime也会有值)
    var fromSubmitAccount = false

    //是否为转账操作(下面四个为转账需要,只有fromTransfer为true时，下面几个值有才有用)
    var fromTransfer = false
    //若为转账操作，则transferIncome true表示转入账户，false表示转出账户
    var transferIncome = false
    //转账资产的addTime(来源)
    var transferFromAddTime = ""
    //转账资产的addTime(转账目的)
    var transferToAddTime = ""
    
    //单笔存钱addTime(若为存钱操作，则此需要有值)
    var saveMoneySubAddTime = ""
    //是否为存钱操作(下面四个为存钱需要,只有fromSaveMoney为true时，下面几个值有才有用)
    //注意：与转账操作不同,存钱操作时允许用户只选择扣款账户 或 存款账户(即saveMoneyFromAddTime、saveMoneyToAddTime不需要同时有值)
    var fromSaveMoney = false
    //若为存钱操作，则saveMoneyIncome true表示扣款账户，false表示存款账户
    var saveMoneyIncome = false
    //存钱资产的addTime(扣款账户)
    var saveMoneyFromAddTime = ""
    //存钱资产的addTime(存款账户)
    var saveMoneyToAddTime = ""
}
