# roboter
搭建多真机安卓端自动化测试方案

支持 win/linux/mac + 真机、模拟器

注意，模拟器，需要把 aapt、adb 替换成当前系统环境中的版本即可。

主要介绍：

环境安装：

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
   
  二次开发：
    该模块可直接获取设备、测试package等信息，不用指定
    1. 只需要在 config/devices.yaml 设置设备与服务端口、代测试包等信息
    
        yamls_path 表示任务或用例存放的路径，可随意指定
        
        
        appium:

         - devices: 127.0.0.1:54001
           port: 4726
           server: appium  -p 4726 -bp 4736 -U 127.0.0.1:54001 --log-level info
           platformName: android
           apk_path: data/apk/yingyongbao_7212130.apk
           yamls_path: jobs/yaml/yingyongbao
        #   closed: true

         - devices: 127.0.0.1:54011
           port: 4727
           server: appium  -p 4727 -bp 4737 -U 127.0.0.1:54011 --log-level info
           platformName: android
           apk_path: data/apk/yingyongbao_7212130.apk
           yamls_path: jobs/yaml/yingyongbao
           closed: true

         - devices: 127.0.0.1:54021
           port: 4728
           server: appium  -p 4728 -bp 4738 -U 127.0.0.1:54021 --log-level info
           platformName: android
           apk_path: data/apk/yingyongbao_7212130.apk
           yamls_path: jobs/yaml/yingyongbao
           closed: true
     
    2. 添加用例
        在 jobs 目录下添加对应的
        cat jobs/yaml/yingyongbao/jobs.yaml 
        site: yingyongbao
        job_path: jobs
        jobs: [init.yaml, update.yaml,  search.yaml, download.yaml, install.yaml]
        
        #jobs表示要执行的任务或用例
        
        具体用例或任务内容
        
        具体的操作选项同selenium by_id,by_ids, by_name,by_class, by_xpath.....
        
        如下：
        
        cat jobs/yaml/yingyongbao/jobs/init.yaml 
        ---


        -
          element_info: com.huawei.systemmanager:id/btn_allow
          find_type: by_id
          operate_type: click
          sleeps: 2

        -
          element_info: //android.widget.TextView[@text="去授权"]
          find_type: by_xpath
          operate_type: click

        -
          element_info: com.android.packageinstaller:id/permission_allow_button
          find_type: by_id
          operate_type: click
          sleeps: 2

        -
          element_info: com.android.packageinstaller:id/permission_allow_button
          find_type: by_id
          operate_type: click
          sleeps: 2

        
        
