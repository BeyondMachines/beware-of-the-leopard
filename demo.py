import subprocess
import yaml

user_code = input("Type Python code: ")
eval(user_code)

cmd = input("Command to run: ")
subprocess.run(cmd, shell=True)

raw = "key: value"
yaml.load(raw)  