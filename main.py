import math

count_of_logs, count_of_cuts = map(int, input().split())
logs_list = list(map(int, input().split()))
min_log = 0
max_log = max(logs_list)
current_length = 0.0

while math.ceil(min_log) != math.ceil(max_log):  # здесь округление в бОльшую сторону!!

    current_length = (min_log + max_log) / 2
    count = 0

    for i in logs_list:
        count += math.floor(i / current_length)  # сколько разрезов до усреднённого на всех

    if count <= count_of_cuts:
        max_log = current_length

    else:
        min_log = current_length


print(math.ceil(current_length))
