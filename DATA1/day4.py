#x = input('Enter String: ')

#rev = x[::-1]

#if x == rev:
#    print('True')
#    print(x)
#else:
#    print('False')



#data = [2,14,123,52,125,34,100]
#data_max = max(data)
#remove_the_highest = ([i1 - i2 for i1,i2 in zip(data,data_max)])

#print(remove_the_highest)
#print(data_max)

#Question:
#Write a Python function that takes a list of numbers and returns the second largest number in the list.

#Give it a try! 🚀

#data = [2,14,123,52,125,34,100]

#data_max = max(data)
#data.remove(data_max)
#second_largest = max(data)

#print(second_largest)
from collections import Counter

data = [1, 3, 2, 3, 4, 1, 3, 2, 1, 1,6]

frequency = Counter(data)

print(frequency)


for item,count in frequency.items():
    print(f'{item}: {count}')
