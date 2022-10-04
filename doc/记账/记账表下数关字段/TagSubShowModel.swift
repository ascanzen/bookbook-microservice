
import UIKit

//标签显示model
class TagSubShowModel: NSObject {

    //(13位时间戳)
    var addTime = ""
    //(13位时间戳)
    var updateTime = ""

    //排序
    var sortingNum = 0

    //外键：对应标签addTime
    var tagSubAddTime = ""
    //外键：对应标签类别addTime(也存数据库:主要便于查询标签类别相关的账单记录)
    var categoryAddTime = ""

    //外键：对应账单addTime
    var dailyAccountAddTime = ""
    
    //下面两值用于外部展示用,不存数据库,他们的值是从tagAddTime对应数据库中取得的
    //名称
    var title = ""
    //背景色(内存对应的图标名称)
    var colorImgStr = ""
}
