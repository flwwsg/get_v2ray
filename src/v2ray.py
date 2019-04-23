# 获取v2ray代理账号
import os
from utils import v2ray_dir, free_config, web_driver, v2ray_program, need_root_permission
import time

config_file = v2ray_dir+"/config.json"
# 获取配置，免费账号每天会更新
web_driver.get(free_config)
# 处理ddos， 目前只要简单的sleep
# 需要应对人机检测
time.sleep(30)
# 刷新页面，获取数据
web_driver.refresh()
# 通过chrome获取json数据
chrome_json = web_driver.find_elements_by_tag_name("pre")
# 通过firefox获取json数据
firefox_json = web_driver.find_elements_by_xpath("//div[@id='json']")
config_source = ""
if len(chrome_json) != 0:
    config_source = chrome_json[0].text
if len(firefox_json) != 0:
    config_source = firefox_json[0].text
web_driver.close()
if config_source == "":
    raise Exception("请在hosts 文件添加104.18.18.18 free-ss.site或者联系flwwsg@qq.com ")
# 更新v2ray配置文件
with open(config_file, "w") as f:
    f.write(config_source)
if need_root_permission():
    raise Exception("需要超级用户权限, 请手动启动%s" % v2ray_program)
os.system(v2ray_program)
