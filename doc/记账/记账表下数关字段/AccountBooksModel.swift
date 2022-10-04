//
//  AccountBooksModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2020/7/13.
//  Copyright © 2020 chuncheng jia. All rights reserved.
//

import UIKit

//账本
class AccountBooksModel: NSObject {

    var addTime = ""
    var updateTime = ""
    
    //标题
    var title = ""
    //图标
    var logo = ""
    
    //我的账本显示使用
    //内存记录条数
    var numberCount = "0"
    //结余
    var remainAmount = "0"
    //收入
    var incomeAmount = "0"
    //支出
    var outcomeAmount = "0"
    
    //占比(显示用 无需存数据库)
    var progress:CGFloat = 0.0
}
