import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("Finished eating")
def drink_coffee():
    time.sleep(4)
    print("Finished drinking")
def study():
    time.sleep(5)
    print("Finished studying")

x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

x.join() # se tirar esses join's o active_count vai de 1 para 4
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

