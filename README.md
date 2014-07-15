# fcitx-xhup

## cheat sheet
小鹤双拼的 cheat sheet。支持编码、字词的双向查询。

## mb file for fcitx
小鹤双拼的形码可以挂载在百度、搜狗等输入法上使用，都是用的自定义短语的方式。
Fcitx 里面也可以加载自定义短语，这个文件位于 `/usr/share/fcitx/pinyin/pySym.mb` 和
`$HOME/.config/fcitx/pinyin/pySym.mb`。老版本的 fcitx 不清楚，4.2 以后都是。

格式特别简单

    # code character
    miss 汖两覔，惷到奣@_@...

我使用百度输入法的挂载文件做了一份码表，可以放到挂载到 fcitx 里面使用。

如果想体验更纯粹的双形，fcitx 有 table 输入法，加载这份码表后可以实现四码自动上屏，
和飞扬版很像啊，哈哈

### 安装使用

`codetable` 里面有一个安装脚本 `install.sh`，可以选择只挂载到拼音输入法里，
也可以选增加一个 table 输入法（FlyPy），或者都装上。

    ./install pinyin
    ./install table
    ./install all

