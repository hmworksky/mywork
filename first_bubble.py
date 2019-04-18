from airtest.core.api import *
# 通过ADB连接本地Android设备
connect_device("Android:///")
# #安装待测软件apk，路径信息。
# install(r"D:\data\app_package\apk\GameHall-v226.apk")
#开始运行app
start_app("com.pingan.gamehall")
# #点击某个图片，Airtest中基于图像识别语法，图片自己提供。
touch(Template(r"D:\project\front_auto\file\homepage\search_button.png"))
# #滑动语音，开头图片跟结尾图片
# swipe(Template("slide_start.png"), Template("slide_end.png"))
# #添加断言的图片
# assert_exists(Template("success.png"))
# #点击Android上的返回键
# #keyevent("BACK")
# #点击Android上的Home键返回
# #home()
# #uninstall("package_name_of_your_apk")
