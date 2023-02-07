import pymem
import keyboard
from pymem import process
import time
from offsets import *

_procces = pymem.Pymem("csgo.exe")
_client = pymem.process.module_from_name(_procces.process_handle, "client.dll").lpBaseOfDll

def Bhop():
    while True:
        try:
            if keyboard.is_pressed("space"):
                player = _procces.read_int(_client + dwLocalPlayer)
                jump = _client + dwForceJump
                player_state = _procces.read_int(player + m_fFlags)

                if player_state == 257: 
                    _procces.write_int(jump, 5)
                    time.sleep(0.1)
                    _procces.write_int(jump, 4)
        except  pymem.exception.MemoryReadError:
            pass

Bhop()
