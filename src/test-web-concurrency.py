from selenium import webdriver
import os
from selenium.webdriver.firefox.options import Options
from multiprocessing import Process

opt = Options()
# opt.add_argument("-headless")
# 项目目录
home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 程序目录
bin_dir = home_dir+"/bin"
web_driver = webdriver.Firefox(executable_path=bin_dir + "/geckodriver", firefox_options=opt)
# 多进程
for i in range(10):
    p = Process(target=web_driver.get, args=("http://localhost:3002", ))
    p.start()
    # 等待完成
    p.join()
