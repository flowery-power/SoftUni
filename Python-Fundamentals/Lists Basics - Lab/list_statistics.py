n = int(input())
positive_list = []
negative_list = []

for n in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)

    else:
        negative_list.append((current_number))
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum(negative_list)}")