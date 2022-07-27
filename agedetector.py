print("How you want to calculate the year when you will turn 100")
print("1) Birth year")
print("2) Age")
birthday = int(input("Enter the option"))
total_age = 100
current = 2022

if birthday == 1:
    person = int(input("Enter your birth year"))
    print(f'You will turn 100 in {person + total_age} and currently you are {current - person} years old')

elif birthday == 2:
    person = int(input("Enter your age"))
    how_far_age = total_age - person
    print(f'You will turn 100 in {current + how_far_age}')