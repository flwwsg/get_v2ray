import os
from selenium import webdriver


# 账号地址
free_config = "https://free-ss.site/v/443.json"
# 项目目录
home_dir = os.path.dirname(os.path.dirname(__file__))
# 程序目录
bin_dir = home_dir+"/bin"
# v2ray 代理目录
v2ray_dir = ""
# v2ray 执行程序
v2ray_program = ""
#  浏览器自动化引擎， windows 采用chrome支持版本71-72， linux 采用firefox
web_driver = None
if os.name == "nt":
    v2ray_dir = bin_dir+"/v2ray"
    v2ray_program = v2ray_dir+"/v2ray.exe"
    from selenium.webdriver.chrome.options import Options
    opt = Options()
    opt.add_argument("-headless")
    web_driver = webdriver.Chrome(bin_dir + "/chromedriver.exe", chrome_options=opt)
elif os.name == "posix":
    v2ray_dir = bin_dir+"/v2ray-linux"
    v2ray_program = "sudo "+v2ray_dir+"/v2ray"
    from selenium.webdriver.firefox.options import Options
    opt = Options()
    opt.add_argument("-headless")
    web_driver = webdriver.Firefox(executable_path=bin_dir + "/geckodriver", firefox_options=opt)
else:
    raise Exception("system %s does not supported" % os.name)


def need_root_permission():
    if os.name == "nt":
        # windows
        return False
    elif os.name == "posix":
        # linux 平台,需要超级用户权限
        return os.getuid() != 0
