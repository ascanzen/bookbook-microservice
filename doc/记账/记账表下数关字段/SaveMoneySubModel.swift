//
//  SaveMoneySubModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2021/7/11.
//  Copyright © 2021 chuncheng jia. All rights reserved.
//

import UIKit

//存钱单笔model
class SaveMoneySubModel: NSObject {

    var addTime = ""
    var updateTime = ""

    var currentAmount = "0"

    //存钱addTime
    var saveAddTime = ""
    
    //来源
    var fromAccountTime = ""
    //存入
    var toAccountTime = ""
    
    //记的某天账时间(存"yyyy-MM-dd"格式日期)
    var dayTime = ""
    var dayAddTime = "" //记账时当前时间(内存13位时间戳)

    //备注
    var note = ""
    
    //是否已存入(用于页面展示用，无需存入数据库)
    var hasSaved = false
    
    //是否是添加按钮(本地标识，无需存数据库)
    var addFlag = false
}
