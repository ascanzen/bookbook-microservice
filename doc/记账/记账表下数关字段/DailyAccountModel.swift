//
//  DailyAccountModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2020/7/12.
//  Copyright © 2020 chuncheng jia. All rights reserved.
//

import UIKit

//记账model
class DailyAccountModel: NSObject {

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
    
    //导入来源(内存导入表model的addTime：13位时间戳，此值为空表示并不是导入来的，若有值表示是导入来的)
    var importAddTime = ""
    
    //是否为报销账单(若为报销账单，则不计入统计页收入或支出项，报销项为单独统计)
    var submitAccountFlag = false
    //下面三项值只有当submitAccountFlag为true时才有意义
    //若为报销账单，此账单是否为已报销状态
    var submitAccountFinished = false
    //若为报销账单，记录报销时间(内存13位时间戳)
    var submitAccountTime = ""
    //此单报销金额(比如可能花费了100元，但报销的时候只报了95元，可能与上面的amount值不同,但绝大部分情况需要与amount值相同)
    var submitAccountAmount = ""
    //只有submitAccountFlag为true即为报销账单 ，且submitAccountFinished报销时，此值才有意义，表示报销入账的资产addTime(为空或13位时间戳)
    var submitAssetsAddTime = ""
}
