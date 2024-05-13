import datetime

#DD-MM-YYYY
goal, deadline = input('enter your goal with a deadline separated by colon: ').split(':')

                    #module.class_of_the_module.func_of_that_class
deadline_converted = datetime.datetime.strptime(deadline , '%d-%m-%Y')

current_date = datetime.datetime.now()

# how many days do you have left to reach yuor goal?
time_remaining = deadline_converted - current_date
# print(time_remaining) #212 days, 17:53:34.813475

days_remaining = time_remaining.days
hours_remaining = time_remaining.total_seconds()


print(f'Dear user! Time remaining for your goal: {goal} is {days_remaining} days.')
print(f'Dear user! Time remaining for your goal: {goal} is {round(hours_remaining/3600)} hours.')

