import time

start_time = time.time()

n = int(input())
F_array = [0, 1]

for i in range(2, n+1):
    F_array.append(F_array[i - 1] + F_array[i - 2])

print(F_array[n])

print("--- %s seconds ---" % (time.time() - start_time))
