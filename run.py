import os
from src.utils import home_dir

if os.name == "nt":
    os.system("%s/venv/Scripts/python.exe  %s/src/v2ray.py" %(home_dir, home_dir))
else:
    os.system("python3 %s/src/v2ray.py" % home_dir)
