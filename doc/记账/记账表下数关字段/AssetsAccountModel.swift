//
//  AssetsAccountModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2020/8/19.
//  Copyright © 2020 chuncheng jia. All rights reserved.
//

import UIKit

//资产账户
@objc class AssetsAccountModel: NSObject {

    var addTime = ""
    var updateTime = ""
    
    //资产类型
    var assetsType = AssetsAccountType.AssetsAccountTypeCreditCard
    
    //金额
    var currentAmount = ""
    var totalAmount = "" //仅针对信用卡类型,表示信用卡额度
    var cardNumber = "" //银行卡号后四位
    var noteStr = "" //备注
    
    var needAdd = true //计入总资产(默认为true)
    
    //标题
    @objc var title = ""
    //图标
    var logo = ""
}
