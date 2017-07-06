#!/usr/bin/env python

from dji_sdk.dji_drone import DJIDrone
import dji_sdk.msg
import time
import sys
import math

def _find_getch():
    try:
        import termios
    except ImportError:
        import msvcrt
        return msvcrt.getch

    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    return _getch

def display_main_menu():
    print "----------- < Main menu > ----------"
    print "[c] Obtain control and takeoff"
    print "[v] Landing and Exit"
    print "[w,a,s,d] Forward, left, backward, right"
    print "[i,j,k,l] Up, left turn, down, right turn"
    print "\nuse `rostopic echo` to query drone status"
    print "----------------------------------------"

def main():
    getch = _find_getch()
    drone = DJIDrone()
    display_main_menu()

    while True:
        ch = getch()
        if ch == 'c':
            drone.request_sdk_permission_control()

            drone.takeoff()
            time.sleep(1.0)
        elif ch == 'w':
            drone.vrc_start()
            drone.vrc_control(1024+110, 1024, 1024, 1024)
            time.sleep(0.6)
            drone.vrc_stop()
        elif ch == 's':
            drone.vrc_start()
            drone.vrc_control(1024-110, 1024, 1024, 1024)
            time.sleep(0.6)
            drone.vrc_stop()
        elif ch == 'a':
            drone.vrc_start()
            drone.vrc_control(1024, 1024+110, 1024, 1024)
            time.sleep(0.6)
            drone.vrc_stop()
        elif ch == 'd':
            drone.vrc_start()
            drone.vrc_control(1024, 1024-110, 1024, 1024)
            time.sleep(0.6)
            drone.vrc_stop()
        elif ch == 'i':
            drone.vrc_start()
            drone.vrc_control(1024, 1024, 1024+110, 1024)
            time.sleep(0.6)
            drone.vrc_stop()
        elif ch == 'k':
            drone.vrc_start()
            drone.vrc_control(1024, 1024, 1024-110, 1024)
            time.sleep(0.6)
            drone.vrc_stop()
        elif ch == 'j':
            drone.vrc_start()
            drone.vrc_control(1024, 1024, 1024, 1024-110)
            time.sleep(0.6)
            drone.vrc_stop()
        elif ch == 'l':
            drone.vrc_start()
            drone.vrc_control(1024, 1024, 1024, 1024+110)
            time.sleep(0.6)
            drone.vrc_stop()
        elif ch == 'v':
            #drone.release_sdk_permission_control()
            break
    

    drone.landing()
    
    """
                elif ch == 's':
                    print 'down'
                    drone.vrc_control(1024-660, 1024, 1024, 1024)
                    time.sleep(0.5)
                elif ch == 'a':
                    drone.vrc_control(1024, 1024+660, 1024, 1024)
                elif ch == 'd':
                    drone.vrc_control(1024, 1024-660, 1024, 1024)
                elif ch == 'i':
                    drone.vrc_control(1024, 1024, 1024+660, 1024)
                elif ch == 'k':
                    drone.vrc_control(1024, 1024, 1024-660, 1024)
                elif ch == 'j':
                    drone.vrc_control(1024, 1024, 1024, 1024-660)
                elif ch == 'l':
                    drone.vrc_control(1024, 1024, 1024, 1024+660)
                elif ch == 'c':
                    drone.landing()
                    break
                else :
                    drone.vrc_control(1024, 1024, 1024, 1024)
                    time.sleep(0.5)
    """

if __name__ == "__main__":
    main()
