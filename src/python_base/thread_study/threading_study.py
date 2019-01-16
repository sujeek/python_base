# import time, threading
#
# balance = 0
# lock = threading.Lock()
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#     print balance
#
# def run_thread(n):
#     for i in range(n):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#         #time.sleep(0.01)
#
#
# t1 = threading.Thread(target=run_thread, args=(5000000,))
# t2 = threading.Thread(target=run_thread, args=(2000000,))
# t3 = threading.Thread(target=run_thread, args=(8000000,))
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()

#--------------------------------------------------------
#
# import threading
#
# import threading, time
#
# def Seeker(cond, name):
#     time.sleep(2)
#     cond.acquire()
#     print('%s :eyes is close'% name)
#     cond.notify()
#     cond.wait()
#     for i in range(3):
#         print('%s is finding!!!'% name)
#         time.sleep(2)
#     cond.notify()
#     cond.release()
#     print('%s :I am win'% name)
#
# def Hider(cond, name):
#     cond.acquire()
#     cond.wait()
#     for i in range(2):
#         print('%s is hiding!!!'% name)
#         time.sleep(3)
#     print('%s :I hidden'% name)
#     cond.notify()
#     cond.wait()
#     cond.release()
#     print('%s :you Find me'% name)
#
#
# if __name__ == '__main__':
#     cond = threading.Condition()
#     seeker = threading.Thread(target=Seeker, args=(cond, 'seeker'))
#     hider = threading.Thread(target=Hider, args=(cond, 'hider'))
#     seeker.start()
#     hider.start()
























