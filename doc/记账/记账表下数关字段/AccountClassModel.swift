//
//  AccountClass.swift
//  MyMoney
//
//  Created by chuncheng jia on 2020/7/12.
//  Copyright © 2020 chuncheng jia. All rights reserved.
//

import UIKit

//记账类别
class AccountClassModel: NSObject {

    var addTime = ""
    var updateTime = ""
    
    //标题
    var title = ""
    //图标
    var logo = ""
    
    //收入/支出 true:收入 false:支出
    var income:Bool = false

    //是否为添加状态
    var showFlag = true
    //是否自定义
    var customFlag = false

}
