CSS Unit Convertor
-------------

Inspired by [cssrem](https://github.com/flashlizi/cssrem).

从CSS的一种单位值转另一种单位值的Sublime Text 3自动完成插件。

插件效果如下：

![效果演示图](css-unit-convertor.gif)

## 安装

* 下载本项目，比如：git clone https://github.com/r569594043/css-unit-convertor
* 进入packages目录：Sublime Text -> Preferences -> Browse Packages...
* 复制下载的css-unit-convertor目录到刚才的packges目录里。
* 重启Sublime Text。

## 配置参数

参数配置文件：Sublime Text -> Preferences -> Package Settings -> css-unit-convertor

* `number` - 原始单位转目标单位的操作数，默认为100。
* `operator` - 原始单位转目标单位的操作符，默认为/。
* `from_unit` - 原始单位，默认为px。
* `to_unit` - 目标单位，默认为rem。
* `max_fraction_length` - 原始单位转目标单位的小数部分的最大长度，默认为8。
* `available_file_types` - 启用此插件的文件类型。默认为：[".css", ".less", ".sass", ".scss", ".html", ".php"]。

### 设计图是640px

* 640px -(`/100`)-> 6.4rem
* 640px -(`/6.4`)-> 100vw
* 640px -(`/24`)-> 26.66666667rem
* 6.4rem -(`*100`)-> 640px
* 6.4rem -(`*15.625`)-> 100vw
* 6.4rem -(`/0.24`)-> 26.66666667rem
* 100vw -(`*6.4`)-> 640px
* 100vw -(`/15.625`)-> 6.4rem
* 100vw -(`/3.75`)-> 26.66666667rem
* 26.66666667rem -(`*24`)-> 640px
* 26.66666667rem -(`*0.24`)-> 6.4rem
* 26.66666667rem -(`*3.75`)-> 100vw

### 设计图是750px

* 750px -(`/100`)-> 7.5rem
* 750px -(`/7.5`)-> 100vw
* 750px -(`/24`)-> 31.25rem
* 7.5rem -(`*100`)-> 750px
* 7.5rem -(`/0.075`)-> 100vw
* 7.5rem -(`/0.24`)-> 31.25rem
* 100vw -(`*7.5`)-> 750px
* 100vw -(`*0.075`)-> 7.5rem
* 100vw -(`/3.2`)-> 31.25rem
* 31.25rem -(`*24`)-> 750px
* 31.25rem -(`*0.24`)-> 7.5rem
* 31.25rem -(`*3.2`)-> 100vw

## Thanks
Thanks to [cssrem](https://github.com/flashlizi/cssrem).