
#introduction to payup and inputs
print('=' * 40)

hello = 'Welcome to PayUp'
print(hello)
print()
event = input('What is the occasion? ')
cost = float(input('How much did it cost? '))
tip = float(input('What percentage was the tip? '))
people = int(input('How many people are splitting the bill? '))

print("Here is the total cost breakdown")
print()

# This is another way to do the math, This was is shorter and more efficient. 

# breakdown = cost * (1 + tip / 100)
# print('Total Cost: $', breakdown)
# per_person = breakdown / people
# print('Cost per person: $', per_person)

#Total cost breakdown

print('=' * 40)
print()
welcome = ('Here is the total cost breakdown')
print(welcome)
print()
print(f'Cost: ${cost}')
print()
service = cost * (tip / 100)
print(f'Service: ${service}')
print()
total = cost + service
print(f'Total: ${total}')   
print()
share = total / people
print(f'Cost per person: ${share}')
print()
print('Thank you for using PayUp!')
print()
print('=' * 40)
