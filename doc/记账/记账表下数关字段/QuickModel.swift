//
//  QuickModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2021/2/27.
//  Copyright © 2021 chuncheng jia. All rights reserved.
//

import UIKit

//快记Model
class QuickModel: NSObject {

    //标题
    var title = ""
    //备注
    var note = ""
    
    var addTime = ""
    var updateTime = ""
    //记的某天账时间
    var accountTime = ""
    
    //收入/支出 true:收入 false:支出
    @objc var income:Bool = false
    //金额
    var amount = ""
    
    //类别id
    var classTime = ""
    //所属账本(内存账本model的addTime)
    var accountBook = ""
    
    //从XX资产支出(内存资产model的addTime)
    var assetsAddTime = ""
}
