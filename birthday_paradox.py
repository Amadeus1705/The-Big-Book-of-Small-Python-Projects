'''The Birthday Paradox, also called the Birthday Problem,
is the surprisingly high probability that two people will have the same birthday even in a small group of people. 
In a group of 70 people, there’s a 99.9 percent chance of two people having a matching birthday. 
But even in a group as small as 23 people, there’s a 50 percent chance of a matching birthday. 
This program performs several probability experiments to determine the percentages for groups of different sizes. 
We call these types of experiments, in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments'''

group = 23

import datetime,random

def generate_birthdays(number_of_birthdays):
    birthdays = []
    for i in range(number_of_birthdays):
        start = datetime.date(2010,1,1)
        random_days = datetime.timedelta(random.randint(0,364))
        birthdays.append(start+random_days)
    return birthdays

def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # No birthdays are matching
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA
            
MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

while True:
    print('How many birthdays should we generate? (Max 100)')
    response = input(' > ')
    if response.isdecimal() and (0<int(response)<=100):
        number_of_birthdays = int(response)
        break
    
print()

print('Here are the birthdays :')

birthdays = generate_birthdays(number_of_birthdays)

for i,birthday in enumerate(birthdays):
    if i != 0:
        print(',',end='')
    monthName = MONTHS[birthday.month-1]
    date_to_text = f'{birthday.day}-{monthName}'
    print(date_to_text)
print()
print()

match = get_match(birthdays)

print('In this simulation, ')

if match != None:
    monthName = MONTHS[match.month-1]
    date_to_text = f'{match.day}-{monthName}'
    print("Multiple people have birthdays on :",date_to_text)
else:
    print("No matching birthdays found")

# Run through 100,000 simulations:
print('Generating', number_of_birthdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

simMatch = 0  
for i in range(100000):
      if i % 10000 == 0:
          print(i, 'simulations run...')
      birthdays = generate_birthdays(number_of_birthdays)
      if get_match(birthdays) != None:
          simMatch = simMatch + 1
          
print('100,000 simulations run.')
probability = round(simMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of', number_of_birthdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', number_of_birthdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
