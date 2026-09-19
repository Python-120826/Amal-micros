input1 = input("Enter first valu: ")
input2 = input("Enter second value: ")

try:
    num1 = float(input1)
    num2 = float(input2)
    result = num1 + num2
    print(result)
except ValueError:
    result = str(input1) + str(input2)
    print(result)


list1 = [1, "a", 3, 'b', 5, '6', 7, '8', 9, 'c']
numbers_list = []
strings_list = [ ]

for item in list1:
    try:
        if isinstance(item, (int, float)) and not isinstance(item, bool):
            numbers_list.append(item)
        else:
            raise TypeError
    except TypeError:
        strings_list.append(item)

print("Numbers list:", numbers_list)
print("Strings list:", strings_list)


food = ["aple", "banana", "kiwi", "avocado", "pie", "cherry"]
fifth = []

for word in food:
    try:
        fifth.append(word[4])
    except IndexError:
        pass

print("fifth letters:", fifth)