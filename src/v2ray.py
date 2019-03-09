# 获取v2ray代理账号
from selenium import webdriver
import os
from utils import v2ray_dir, free_config, chrome_driver


config_file = v2ray_dir+"/config.json"
v2ray_exe = v2ray_dir+"/v2ray.exe"
# 获取配置，免费账号每天会更新
driver = webdriver.Chrome(chrome_driver)
driver.get(free_config)
config_source = driver.find_element_by_tag_name("pre").text
driver.close()
# 更新v2ray配置文件
with open(config_file, "w") as f:
    f.write(config_source)
os.system(v2ray_exe)
