import os

# 账号地址
free_config = "https://free-ss.site/v/443.json"
# 项目目录
home_dir = os.path.dirname(os.path.dirname(__file__))
# 程序目录
bin_dir = home_dir+"/bin"
# v2ray 代理目录
v2ray_dir = bin_dir+"/v2ray"
# chrome 浏览器自动化引擎， 支持版本71-73
chrome_driver = bin_dir+"/chromedriver.exe"
