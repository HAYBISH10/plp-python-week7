items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

counter = 1
long_items = 0
longest_item = ""

print("Shopping List:")

for item in items:
    print(f"{counter}. {item}")
    counter = counter + 1

    if len(item) > 4:
        long_items = long_items + 1

    if len(item) > len(longest_item):
        longest_item = item

print(f"\nItems with more than 4 letters: {long_items}")
print(f"Longest item name: {longest_item}")
