import datetime
from tabulate import tabulate

from twenty_two_and_me.life_path_calculator import life_path_calc, split_reduce


# Creating various reports to calculate chances of being a 22.
# Note: DO NOT COPY - This is temp code to meet the increasing reporting demands of our beloved jazz musician.

start_date = datetime.date(1981, 1, 1)
step_date = datetime.date(1983, 1, 1)
end_date = datetime.date(1983, 12, 31)
step = datetime.timedelta(days=1)

# Track various count numbers, day lists
day_count = 0
day_count_1 = 0
day_count_2 = 0
day_count_3 = 0
day_count_4 = 0
day_count_5 = 0
day_count_6 = 0
day_count_7 = 0
day_count_8 = 0
day_count_9 = 0
day_count_11 = 0
day_count_22 = 0
day_list_22 = []
day_count_33 = 0

while step_date <= end_date:
    lpn = life_path_calc(step_date)
    if lpn == 1:
        day_count_1 += 1
    if lpn == 2:
        day_count_2 += 1
    if lpn == 3:
        day_count_3 += 1
    if lpn == 4:
        day_count_4 += 1
    if lpn == 5:
        day_count_5 += 1
    if lpn == 6:
        day_count_6 += 1
    if lpn == 7:
        day_count_7 += 1
    if lpn == 8:
        day_count_8 += 1
    if lpn == 9:
        day_count_9 += 1
    if lpn == 11:
        day_count_11 += 1
    if lpn == 22:
        reduced_day = split_reduce(step_date.day)
        reduced_month = split_reduce(step_date.month)
        reduced_year = split_reduce(step_date.year)
        display_date = step_date.strftime('%m-%d-%Y')
        day_list_22.append([display_date, reduced_month, reduced_day, reduced_year, lpn])
        day_count_22 += 1
    if lpn == 33:
        day_count_33 += 1
    step_date += step
    day_count += 1


# List of Life Path Number Counts for Given Range of Time

def calc_percent(n, tn):
    print(day_count_1)
    print(day_count)
    print(n)
    print(tn)
    return n * 100 / tn


percentage_data = [
    [1, day_count_1, calc_percent(day_count_1, day_count)],
    [2, day_count_2, calc_percent(day_count_2, day_count)],
    [3, day_count_3, calc_percent(day_count_3, day_count)],
    [4, day_count_4, calc_percent(day_count_4, day_count)],
    [5, day_count_5, calc_percent(day_count_5, day_count)],
    [6, day_count_6, calc_percent(day_count_6, day_count)],
    [7, day_count_7, calc_percent(day_count_7, day_count)],
    [8, day_count_8, calc_percent(day_count_8, day_count)],
    [9, day_count_9, calc_percent(day_count_9, day_count)],
    [11, day_count_11, calc_percent(day_count_11, day_count)],
    [22, day_count_22, calc_percent(day_count_22, day_count)],
    [33, day_count_33, calc_percent(day_count_33, day_count)]
]

print("LIFE PATH PERCENTAGES")
print("Start Date: {}".format(start_date.strftime('%m/%d/%Y')))
print("End Date: {}".format(end_date.strftime('%m/%d/%Y')))
print("Total Days: {}".format(day_count))
print(tabulate(percentage_data, headers=['life path', 'day ct', '%'],
               tablefmt="fancy_grid"))
print("\n\n")
print("LIFE PATH TWO 22 BIRTHDAYS FOR {} - {}".format(start_date.strftime('%m/%d/%Y'), end_date.strftime('%m/%d/%Y')))
print(tabulate(day_list_22, headers=['date', 'day', 'month', 'year', 'life path'],
               tablefmt="fancy_grid"))
