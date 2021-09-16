import random, time
num = eval(input())
random.seed(time.process_time())
rand_array = [random.randint(1, 100) for i in range(9)]
rand_array.append(num)
random.shuffle(rand_array)
print(rand_array)


