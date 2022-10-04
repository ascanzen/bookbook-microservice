//
//  AccountLocationModel.swift
//  MyMoney
//
//  Created by chuncheng jia on 2022/3/19.
//  Copyright © 2022 chuncheng jia. All rights reserved.
//

import UIKit

//记账位置Model
class AccountLocationModel: NSObject {

    //(13位时间戳)
    var addTime = ""
    //(13位时间戳)
    var updateTime = ""
    
    //外键：对应记账addTime
    var accountAddTime = ""
    
    //纬度
    var latitude = ""
    //经度
    var longitude = ""
    
    //地址相关属性
    var name = ""               // eg. Apple Inc.
    var thoroughfare = ""       // street name, eg. Infinite Loop
    var subThoroughfare = ""    // eg. 1
    var locality = ""           // city, eg. Cupertino
    var subLocality = ""        // neighborhood, common name, eg. Mission District
    
    var administrativeArea = "" // state, eg. CA
    var subAdministrativeArea = "" // county, eg. Santa Clara
    var postalCode = ""         // zip code, eg. 95014
    var isoCountryCode = ""     // eg. US
    var country = ""            // eg. United States
    
    var inlandWater = ""        // eg. Lake Tahoe
    var ocean = ""              // eg. Pacific Ocean
}
