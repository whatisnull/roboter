# roboter
搭建多真机安卓端自动化测试方案

支持 win/linux/mac + 真机、模拟器

注意，模拟器，需要把 aapt、adb 替换成当前系统环境中的版本即可。

主要介绍：

centos 7 + python2.7 安装

环境安装
需要至少一部以上安卓手机

1. 安装appium
    1.  下载 node.js 建议最高版本
        https://nodejs.org/download/
    2. tar -xvzf xxx.tar.gz
    3. set classpath
    4. npm install appium
        遇翻墙
            npm install -g cnpm --registry=https://registry.npm.taobao.org
            cnpm install -g appium --unsafe-perm
    5. appium -v

2. 安装 android-sdk
    方法（略）
    一定要注意 android_home

3. 设置手机
    1. 打开 USB调式模式，一般是找到系统版本号连续敲击几下即可打开开发者模式

4. 安装 python 依赖
    pip install -r requirements.txt

注：
   1. 调试微信小程序内嵌页面则依赖 chrome://inspect
   2. 在手机微信端任一聊天窗口输入 debugx5.qq.com
   3. 在手机弹出的选项中选择对应的inspect,即可
   4. apk tools install
        https://ibotpeaches.github.io/Apktool/install/
   5. android platform-tools install
        https://developer.android.com/studio/releases/platform-tools
   6. linux set aapt
        1. unzip xxx/apktool.jar -d apktool
        2. cd apktool
        3. cd prebuilt/aapt
        4. cp aapt /usr/bin
  
  ===========================以下在直接免安装=============================
  
  链接长期有效
  
  此处不用考虑以上部署
  直接下载集成环境
       链接: https://pan.baidu.com/s/1IST0r8MJqeTA-JkvhWFjYw 密码: qc2y
       下载并上传致服务器 /tmp目录下，运行 sh install.sh 即可
       
