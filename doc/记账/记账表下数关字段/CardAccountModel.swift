//
//  CardAccountModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2021/5/30.
//  Copyright © 2021 chuncheng jia. All rights reserved.
//

import UIKit

//卡片账户
class CardAccountModel: NSObject {

    var addTime = ""
    var updateTime = ""
    
    //资产类型
    var cardType = CardAccountType.CardAccountTypeSavingCard
    
    //持卡人
    var cardOwner = ""
    
    //卡号
    var cardNumber = ""
    var noteStr = "" //备注
    
    //标题
    var title = ""
    //图标
    var logo = ""
}
