n = int(input())
even_list = []
odd_list = []
negative_list = []
positive_list = []

for index in range(n):
    number = int(input())
    if number % 2 == 0 or number == 0:
        even_list.append(number)

    if number % 2 == 1:
        odd_list.append(number)

    if number >= 0:
        positive_list.append(number)
    else:
        negative_list.append(number)
command = input()
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
else:
    print(positive_list)