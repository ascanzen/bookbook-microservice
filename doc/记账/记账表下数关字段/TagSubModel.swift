
import UIKit

//标签model
class TagSubModel: NSObject {

    //(13位时间戳)
    var addTime = ""
    //(13位时间戳)
    var updateTime = ""

    //名称
    var title = ""

    //背景色(内存对应的图标名称)
    var colorImgStr = ""
    
    //排序
    var sortingNum = 0

    //外键：对应标签类别addTime
    var categoryAddTime = ""

}
