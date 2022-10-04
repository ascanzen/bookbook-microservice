//
//  AccountMultimediaModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2021/10/19.
//  Copyright © 2021 chuncheng jia. All rights reserved.
//

import UIKit

//记账多媒体Model
class AccountMultimediaModel: NSObject {

    //(13位时间戳)
    var addTime = ""
    //(13位时间戳)
    var updateTime = ""
    
    //外键：对应记账addTime
    var accountAddTime = ""
    //媒体类型：1000-图片 1001-音频 1002-视频
    var type = AccountMultimediaType.AccountMultimediaTypePhoto
    //对应服务端地址
    var serverUrl = ""
    //排序
    var sortingNum = 0
}
