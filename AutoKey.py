import win32api
import win32gui
import time
import win32con

windowName = u"天涯明月刀"

key_map = {
    "1": 49, "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, "7": 55, "8": 56, "9": 57, "0": 58,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90
}

def mouse_click(x):
    win32api.SetCursorPos([x[0]+10,x[1]+10])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    return True

def getHwnd():
    hwnd = win32gui.FindWindow(0,windowName)
    if (hwnd):
        rect = win32gui.GetWindowRect(hwnd)
        return rect[0],rect[1]
    return None，None
 
 
def key_down(key):
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code,win32api.MapVirtualKey(vk_code,0),0,0)
 
 
def key_up(key):
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)
 
 
def key_press(key,timeout=0.5):
    key_down(key)
    time.sleep(timeout)
    key_up(key)

def read_music(name):
    music_list = []
    temp = []
    file = open('.\\'+name+'.txt','r',encoding='utf-8')
    while True:
        ch = file.read(1)
        if not ch:
            break
        else:
            if not temp:
                if ch.isdigit() or ch.isalpha():
                    if ch.isdigit() or ch.isalpha():
                        #音间速度控制
                        music_list.append([ch,0.4])
                    else:
                        music_list.append('sleep')
                    L_ch = ch        
                elif ch == '(':
                    temp.append(ch)
                    continue
                else:
                    music_list.append('sleep')
                    L_ch = ch
            elif ch == ')':
                L_temp = len(temp)
                for i in range(L_temp-1):
                    music_list.append([temp[i+1],0])
                music_list.append('sleep')
                temp = []
            elif ch.isdigit() or ch.isalpha():
                temp.append(ch)
    return music_list


if __name__ == '__main__':
    mouse_click(getHwnd())
    time.sleep(1)
    music_list = read_music('fade')
    for i in music_list:
        if i == 'sleep':
            #节间速度控制
            time.sleep(0.4)
            continue
        key_press(i[0],i[1])
