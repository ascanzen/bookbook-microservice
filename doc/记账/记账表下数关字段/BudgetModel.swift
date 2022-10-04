//
//  BudgetModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2020/8/2.
//  Copyright © 2020 chuncheng jia. All rights reserved.
//

import UIKit

//预算
class BudgetModel: NSObject {

    //前四项存在数据库中，后面的title等为方便用
    var addTime = ""
    var updateTime = ""
    //类别id
    var classTime = ""
    //金额
    var amount = ""
    
    //标题
    var title = ""
    //图标
    var logo = ""
    //剩余预算
    var remain = ""
    //支出
    var cost = ""

}
