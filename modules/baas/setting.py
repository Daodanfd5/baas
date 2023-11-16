render = {
    "base": {
        "name": "功能设置"
    },
    "base.package": {
        "type": "sel",
        "name": "游戏服务器",
        "desc": "目前仅支持国服 官服和B站",
        "items": [
            {
                "value": "com.RoamingStar.BlueArchive",
                "name": "国服官包"
            },
            {
                "value": "com.RoamingStar.BlueArchive.bilibili",
                "name": "国服B站"
            }
        ]
    },
    "base.serial": {
        "type": "txt",
        "name": "模拟器 Serial",
        "desc": "常见的模拟器 Serial 可以查询下方列表</br> Serial：</br>- 蓝叠模拟器 127.0.0.1:5555</br>- 蓝叠模拟器4 "
                "Hyper-v版，填\"bluestacks4-hyperv\"自动连接，多开填\"bluestacks4-hyperv-2\"以此类推</br>- 蓝叠模拟器5 "
                "Hyper-v版，填\"bluestacks5-hyperv\"自动连接，多开填\"bluestacks5-hyperv-1\"以此类推</br>- 夜神模拟器 127.0.0.1:62001</br>- "
                "夜神模拟器64位 127.0.0.1:59865\n- MuMu模拟器/MuMu模拟器X 127.0.0.1:7555\n- MuMu模拟器12 127.0.0.1:16384</br>- 逍遥模拟器 "
                "127.0.0.1:21503</br>- 雷电模拟器 emulator-5554 或 127.0.0.1:5555</br>- "
                "WSA，填\"wsa-0\"使游戏在后台运行，需要使用第三方软件操控或关闭（建议使用scrcpy操控）</br>如果你使用了模拟器的多开功能，它们的 Serial 将不是默认的，可以在 "
                "console.bat 中执行 `adb devices` 查询，或根据模拟器官方的教程填写",
    },
    "base.ss_rate": {
        "type": "num",
        "name": "截图频率(秒)",
        "desc": "执行两次截图之间的最小间隔，限制在 0.1 ~ 0.3，对于高配置电脑能降低 CPU 占用",
        "opts": {
            "min": "0",
            "max": "1",
            "step": "0.1"
        }
    }
}
