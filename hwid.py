from sys import stderr, stdin, stdout, platform
import subprocess

if platform == "linux" or platform == "linux2":
    hw = subprocess.check_output(['sudo','cat','/sys/class/dmi/id/product_uuid']).decode().strip()
    print(hw)
elif platform == "win32":
    current_machine_id = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
    print(current_machine_id)