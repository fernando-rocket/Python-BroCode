import time

print(time.ctime(), "--- teste 1") # retorna a data completa atual

print(time.time(), "--- teste 2") # retorna os segundos desde a epoch(1969)

print(time.ctime(time.time()), "--- teste 3")

time_object = time.localtime()
print(time_object[0], time_object[1], time_object[2], "--- teste 4")

local_time = time.strftime("%B %d %Y %H", time_object)
print(local_time, "--- teste 5")

time_string = "20 April, 2020"
time_object2 = time.strptime(time_string, "%d %B, %Y")
print(time_object2, "--- teste 6")

time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string, "--- teste 7")
