## 思考: 
在python中, 使用面向对象编程更快还是将以下json格式转换成dataframe然后添加新的属性state能让代码更高效完成以下每一个“MainTask”相关属性的检索和计算?

> 面向对象的好处
>  - 将数据和成员方法封装在一起, 增强了代码的模块化和可维护性
>  - 尤其是在模拟复杂的业务逻辑时, 面向对象方法有较大的优势。

坏处:
增加对象的数量会增加遍历、搜索和更新这些对象所需的时间

---

但是处理大量数据的时候, DataFrame效果会更好, 因为其底层是 C 语言. 但是pandas占内存较高!!! --> 尤其是考虑到 optional 任务数量较大, 维持这样一个 Dataframe 需要较大的内存开销.

## 构想
optional 和 mandatory 是 Task 类的子类, 继承了 Task 类的 ID 等公共属性, 同时维持自身的特有属性.


## 数据示例


```json
{
  "ID": "7_2_1",
  "Cohorts": 7,
  "Days": 2,
  "MaxRouteDuration": 21600,
  "MainTasks": [
    {
      "ID": "MT-FWI-1",
      "Day": 2,
      "ServiceTime": 6300,
      "StartTime": 9000,
      "EndTime": 15300,
      "LocationID": 747,
      "Latitude": 51.0675509,
      "Longitude": 13.7764159
      state: 0 --> setState()
    },
    {
      "ID": "MT-FWI-2",
      "Day": 1,
      "ServiceTime": 4500,
      "StartTime": 5400,
      "EndTime": 9900,
      "LocationID": 44,
      "Latitude": 51.0507815,
      "Longitude": 13.724789
    },
    {
      "ID": "MT-FWI-3",
      "Day": 1,
      "ServiceTime": 5400,
      "StartTime": 11700,
      "EndTime": 17100,
      "LocationID": 142,
      "Latitude": 51.0686787,
      "Longitude": 13.7863437
    },
    {
      "ID": "MT-FWI-4",
      "Day": 2,
      "ServiceTime": 6300,
      "StartTime": 7200,
      "EndTime": 13500,
      "LocationID": 328,
      "Latitude": 51.0270898,
      "Longitude": 13.8285576
    },
    {
      "ID": "MT-FWI-5",
      "Day": 2,
      "ServiceTime": 5400,
      "StartTime": 5400,
      "EndTime": 10800,
      "LocationID": 886,
      "Latitude": 51.0496329,
      "Longitude": 13.6542996
    },
    {
      "ID": "MT-FWI-6",
      "Day": 1,
      "ServiceTime": 6300,
      "StartTime": 3600,
      "EndTime": 9900,
      "LocationID": 771,
      "Latitude": 51.0309756,
      "Longitude": 13.7908851
    },
    {
      "ID": "MT-FWI-7",
      "Day": 1,
      "ServiceTime": 5400,
      "StartTime": 8100,
      "EndTime": 13500,
      "LocationID": 855,
      "Latitude": 51.082625,
      "Longitude": 13.7591178882
    },
    {
      "ID": "MT-FWI-8",
      "Day": 2,
      "ServiceTime": 3600,
      "StartTime": 13500,
      "EndTime": 17100,
      "LocationID": 813,
      "Latitude": 51.0277882,
      "Longitude": 13.7601536
    },
    {
      "ID": "MT-FWI-9",
      "Day": 1,
      "ServiceTime": 4500,
      "StartTime": 7200,
      "EndTime": 11700,
      "LocationID": 218,
      "Latitude": 51.0210547,
      "Longitude": 13.7158879
    },
    {
      "ID": "MT-FWI-10",
      "Day": 1,
      "ServiceTime": 5400,
      "StartTime": 9000,
      "EndTime": 14400,
      "LocationID": 857,
      "Latitude": 51.0046365,
      "Longitude": 13.8406999
    },
    {
      "ID": "MT-FWI-11",
      "Day": 2,
      "ServiceTime": 4500,
      "StartTime": 5400,
      "EndTime": 9900,
      "LocationID": 828,
      "Latitude": 51.0479853,
      "Longitude": 13.7321184
    },
    {
      "ID": "MT-FWI-12",
      "Day": 1,
      "ServiceTime": 5400,
      "StartTime": 8100,
      "EndTime": 13500,
      "LocationID": 878,
      "Latitude": 50.99135,
      "Longitude": 13.7894941
    },
    {
      "ID": "MT-FWI-13",
      "Day": 2,
      "ServiceTime": 7200,
      "StartTime": 9000,
      "EndTime": 16200,
      "LocationID": 727,
      "Latitude": 51.0495393,
      "Longitude": 13.7075854
    },
    {
      "ID": "MT-FWI-14",
      "Day": 2,
      "ServiceTime": 5400,
      "StartTime": 7200,
      "EndTime": 12600,
      "LocationID": 235,
      "Latitude": 51.0402257,
      "Longitude": 13.7170067
    }
  ]
}
```
