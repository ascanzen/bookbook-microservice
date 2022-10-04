//
//  SaveMoneyModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2021/7/4.
//  Copyright © 2021 chuncheng jia. All rights reserved.
//

import UIKit

//存钱model
class SaveMoneyModel: NSObject {

    var addTime = ""
    var updateTime = ""
    
    //开始日期
    var beginTime = ""
    //结束日期
    var endTime = ""

    var title = ""
    var logo = ""
    
    var currentAmount = "0"
    //起始金额
    var beginAmount = "0"
    var totalAmount = "0"
    
    //当前是否是归档状态
    var archiveStatus = false
    
    //当前类型
    var saveType = SaveMoneyType.SaveMoneyTypeIncreasingDays
}
