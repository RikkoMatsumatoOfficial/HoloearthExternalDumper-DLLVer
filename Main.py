import PyBass.bass as b
import pathlib as pth
import pymem.process as proc
from pymem import Pymem
import tkinter.filedialog as fd
import ctypes
from ctypes import *
import time
import os
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p
DEBUG_PROCESS = 0x00000001
class STARTUPINFO(Structure):
        _fields_ = [
        ("cb", DWORD),
        ("lpReserved", LPTSTR),
        ("lpDesktop", LPTSTR),
        ("lpTitle", LPTSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute",DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("lpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
        ]
class PROCESS_INFORMATION(Structure):
        _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
        ]
def Main():
    TsunomakiWatame_Mayday = str("TsunomakiWatameMayday.mp3")
    if(b.BASS_INIT(device=-1, freq=48000, flags=0, win=0, dsguid=0)):
        b.BASS_START()
        if(pth.Path(TsunomakiWatame_Mayday).is_file()):
            utf8_watame = bytes(TsunomakiWatame_Mayday, "utf-8")
            ts_watame = b.BASS_StreamCreateFile(mem=0, filename=utf8_watame, offset=0, length=0, flags=0x4)
            b.BASS_ChannelPlay(handle=ts_watame, restart=False)
        else:
            print("Not Founded This Music!!!")
            os._exit(4456)
        ask_openholoearth = fd.askopenfilename(title="Please Find Holoearth.exe", filetypes=[("HoloearthProcess", "Holoearth.exe")])
        if(pth.Path(ask_openholoearth).is_file()):
            print("[+] Process is Founded Successfully!!!")
        else:
            print("[-] Process is not Founded or You Clicked Cancel!!!")
            time.sleep(10)
            os._exit(334)
        startupinfo = STARTUPINFO()
    processinfo = PROCESS_INFORMATION()
    ctypes_createprocess = ctypes.WinDLL("Kernel32")
    processinfo = PROCESS_INFORMATION()
    startupinfo.dwFlags = 0x1
    startupinfo.wShowWindow = 0x0
    startupinfo.cb = sizeof(startupinfo)
    if(ctypes_createprocess.CreateProcessA(bytes(ask_openholoearth, "UTF-8"), None, None, None, None, 0, None, None, byref(startupinfo), byref(processinfo))):
        print("[+] Process Has Been Created!!!")
        print("[+] PID: " + str(processinfo.dwProcessId))
    time.sleep(74)
    HoloearthPymem = Pymem("Holoearth.exe")
    processhandle_holoearth = HoloearthPymem.process_handle
    proc.inject_dll_from_path(processhandle_holoearth, str("HoloearthDumper.dll"))
    print("[+] Injected!!! Please Wait until This DLL is Successfully Dumped all Functions and Offsets!!!")
    time.sleep(24)
    print("[+] Dumped Succesfully!!!")
    print("This Program is Created By RikkoMatsumatoOfficial!!!")
    os._exit(455)

if __name__ == "__main__":
    Main()    
