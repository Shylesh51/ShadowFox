# Variables

# Q1
# pi = 22/7
# print(type(pi))

# Q2
# for = 4
# print(for)     //Cannot use for as a variable as it is a chosen keyword

# Q3
# p = int(input())
# r = float(input())
# t = 3
#
# print((p*r*t)/100)


# Numbers

# Q1
# a = 145
# b = 'o'
# text = "The value of a is {}, {} is stored inside b"
# print(text.format(a, b))

# Q2 + Bonus
# r = 84
# area = 3.14*(r**2)
# print(f"{area} m^2")
#
# water_presnt = area * 1.4
# print(f"{round(water_presnt)} litres")

# Q3
# d = 490
# t = 7
# s = d//t
# print(f"My speed is: {s} m/s")


# List
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print(f"Number of members in justice league currently: {len(justice_league)}")  # 1
print()

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)  # 2
print()

curr_index = justice_league.index("Wonder Woman")
ele = justice_league.pop(curr_index)
new_index = 0
res = justice_league.insert(new_index, ele)
print(justice_league)  # 3
print()

new_members = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league[:] = new_members
print(justice_league)  # 5
print()

print(sorted(justice_league))
print(f"{justice_league[0]} is the new Leader")  # 6 + Bonus


# If Condition

# Q1
Height = float(input("Enter Height:"))
Weight = float(input("Enter Weight:"))

BMI = Weight / (Height ** 2)

if BMI >= 30:
    print("Obesity")
elif 24 < BMI < 30:
    print("Overweight")
elif 18.5 <= BMI < 25:
    print("Normal")
else:
    print("Underweight")

# Q2
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city_name = input("Enter city name:")

if city_name in Australia:
    print(f"{city_name} is in Australia")
elif city_name in UAE:
    print(f"{city_name} is in UAE")
else:
    print(f"{city_name} in India")

# Q3
first_city = input("Enter first city name:")
second_city = input("Enter second city name:")

if first_city and second_city in Australia:
    print("Both cities belong to Australia")
elif first_city and second_city in UAE:
    print("Both cities belong to UAE")
elif first_city and second_city in India:
    print("Both cities belong to India")
else:
    print("They don't belong to the same country")


# For Loop

# Q1
import random

a = 0
b = 0
c = 0
prev_roll = 0
rolls = 100
for i in range(rolls):
    curr_roll = random.randint(1,6)

    if curr_roll == 6:
        a += 1
        if prev_roll == 6:
            c += 1

    if curr_roll == 1:
        b += 1

    prev_roll = curr_roll

print("Number of times 6 was rolled: ", a)  # 1

print("Number of times 1 was rolled: ", b)  # 2

print("Number of times two 6s were rolled: ", c)  #3


# Q2
def workout():
    jumping_jacks = 100
    per_set = 10

    for i in range(0, jumping_jacks, per_set):
        if input("Are you tired? (yes/no):").strip().lower() == "yes":
            if input("Do you want to skip the remaining sets? (yes/no): ").strip().lower() == "yes":
                print(f"You have completed {i + per_set} jumping jacks.")
                break

        else:
            print(f"You have completed all {jumping_jacks} jumping jacks!")


workout()