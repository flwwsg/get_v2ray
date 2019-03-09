# 获取v2ray代理账号
import os
from utils import v2ray_dir, free_config, web_driver, v2ray_program, need_root_permission


config_file = v2ray_dir+"/config.json"
# 获取配置，免费账号每天会更新
web_driver.get(free_config)
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
    raise Exception("v2ray 配置有变动！！！")
# 更新v2ray配置文件
with open(config_file, "w") as f:
    f.write(config_source)
if need_root_permission():
    raise Exception("需要超级用户权限, 请手动启动%s" % v2ray_program)
os.system(v2ray_program)
