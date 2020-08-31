import random

"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the
elements that are common between the lists (without duplicates).
 Make sure your program works on two lists of different sizes.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

overlap = [num for num in a if num in b]

# for num in a:
#     if num in b:
#         overlap.append(num)

print(f'{overlap}\n')

"""
Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure
 this out at this point - we’ll get to it soon)
"""
rand_list_a = [random.randint(10, 20) for i in range(0, random.randint(5,20))]
rand_list_b = [random.randint(10, 20) for i in range(0, random.randint(5,20))]
rand_overlap = [num for num in rand_list_a if num in rand_list_b]
print(rand_overlap)
