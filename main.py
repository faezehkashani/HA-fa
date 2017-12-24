import lib
import time

if __name__ == '__main__':
    t1 = int(input("Enter Time delay :"))
    while True:
        lib.check_ip()
        time.sleep(t1)
