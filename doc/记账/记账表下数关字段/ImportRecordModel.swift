//
//  ImportRecordModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2021/6/12.
//  Copyright © 2021 chuncheng jia. All rights reserved.
//

import UIKit

//导入记录表
class ImportRecordModel: NSObject {

    var addTime = ""
    var updateTime = ""
    
    var logo = ""
    var importTime = "" //导入时间(内存时间的13位时间戳)
    var importCount = 0
    var sourceType = AccountSourceType.AccountSourceTypeNone

}
