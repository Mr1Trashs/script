import os
import colorama
from colorama import Fore, Style
import psutil
import random
import ctypes
import sys

colorama.init()

# Твои переменные
matrix_letters = 'ABCDEFGHIJKLMOPQRSTUVWXUZabcdefghijklmnopqrstuvwxyz1234567890[{(/\.,)}]'
red = Fore.RED
green = Fore.GREEN
res = Style.RESET_ALL

def is_root():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def rem_res():
    commands = [
        r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /f',
        r'reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableTaskMgr /f',
        r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /f',
        r'reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableRegistryTools /f',
        r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" /v DisableCMD /f',
        r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /f',
        r'reg delete "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /f',
        r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoRun /f',
        r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoViewContextMenu /f',
        r'reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoFolderOptions /f',
        r'reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\taskmgr.exe" /v Debugger /f',
        r'reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\regedit.exe" /v Debugger /f',
        r'reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\cmd.exe" /v Debugger /f',
        r'reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\msconfig.exe" /v Debugger /f'
    ]
    for cmd in commands:
        # Если команда завершилась с ошибкой (код не 0), вызываем исключение для блока except
        if os.system(cmd) != 0:
            raise Exception("Registry error")

def openauto_floaders():
    os.system('start shell:startup')
    os.system('start shell:common startup')

def openauto_taskschd():
    os.system('start taskschd.msc')

def openauto_regedit1():
    path = r"Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run"
    os.system(f'reg add "HKCU\Software\Microsoft\Registry" /v "LastKey" /t REG_SZ /d "{path}" /f')
    os.system("start regedit")

def openauto_regedit2():
    path = r"Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    os.system(f'reg add "HKCU\Software\Microsoft\Registry" /v "LastKey" /t REG_SZ /d "{path}" /f')
    os.system('start regedit')

def PIDaction1(pid_val): 
    psutil.Process(int(pid_val)).kill()

def PIDaction2(pid_val):
    os.system(f'taskkill /F /PID {pid_val}')

def BootRepair():
    print("\n[ SYSTEM BOOT REPAIR ]")
    print("1. GPT (UEFI / Modern BIOS)")
    print("2. MBR (Legacy / Old BIOS)")
    print("3. Check Disk")
    choice = input("\nSelect Type > ")
    if choice == "1":
        os.system("bcdboot C:\\Windows")
    elif choice == "2":
        os.system("bootrec /fixmbr")
        os.system("bootrec /fixboot")
        os.system("bootrec /rebuildbcd")
    elif choice == "3":
        os.system("chkdsk C: /f /r")

def FUN():
    print('\n|1.matrix\n|2.exit')
    fm = input('@root\\>>')
    if fm == "1":
        print('Enter how long is matrix')
        try:
            cnt = int(input('@root\\>>'))
            os.system('cls')
            for _ in range(cnt):
                line = "".join(random.choice(matrix_letters) for _ in range(50))
                print(f"{green}{line}{res}")
            input("\nPress Enter to return...")
        except:
            pass

# Основной цикл программы
while True:
    os.system('cls')
    
    # Проверка на админа
    if not is_root():
        print(f"{red}Start program with root!{res}")
        input("Press Enter to exit...")
        sys.exit()

    print(f'''{green}
┌────────────────────────────────────────┐
│            Unlocker V0.1               │
│                                        │
│             Main menu                  │
│                                        │
│  1.Remove all restrictions             │
│  2.Auto runs                           │
│  3.Taskmgr                             │ 
│  4.Fix MBR/GPT                         │
│  5.FUN                                 │
│  6.Exit                                │
└────────────────────────────────────────┘{res}
    ''')

    Main_menu = input(r'@root\\Unlocker\\>')

    if Main_menu == "1":
        os.system('cls')
        try:
            rem_res()
            print(f'{green}Success{res}')
        except:
            print(f'{red}Error{res}')
        input("\nPress Enter...")

    elif Main_menu == "2":
        os.system('cls')
        print('''                                        
│ 1. open autoruns floaders             
│ 2. open taskschd                        
│ 3. open Autorun (regedit)                
│ 4. open Winlogon                        
            ''')
        am = input(r'@root\\Unlocker\\>>')
        if am == "1":
            openauto_floaders()
        elif am == "2":
            openauto_taskschd()
        elif am == "3":
            openauto_regedit1()
        elif am == "4":
            openauto_regedit2()

    elif Main_menu == "3":
        os.system('cls')
        os.system('tasklist')
        print('\nInput PID')
        target_pid = input('@root\\Unlocker\\>>')
        print('\n| 1. Kill task\n| 2. Restart task')
        pa = input('@root\\Unlocker\\>>')
        try:
            if pa == "1":
                PIDaction1(target_pid)
            elif pa == "2":
                PIDaction2(target_pid)
        except:
            print(f'{red}Error{res}')
        input("\nPress Enter...")

    elif Main_menu == "4":
        os.system('cls')
        BootRepair()
        input("\nPress Enter...")

    elif Main_menu == "5":
        os.system('cls')
        FUN()

    elif Main_menu == "6":
        sys.exit()