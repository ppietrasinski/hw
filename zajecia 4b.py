my_list = [1,2,3,4,5,6,7]
my_new_list = my_list[0:3]

# for i in range(11, 28):
#     print(i, i**3)

# for _ in range(10):
#     print('python jest super')
#
#
#
#
# print(' ')
# print(' ')
# print(' ')
# i = 1
# while i <= 10:
#     print('python jest super')
#     i += 1
#
# lis = [1,2,3,4,5,6,7,8]
# numbers = [3, 12, 55, 178, 1300, 6789, 19200]
#
# for i in numbers:
#     print(i, i * 3)
#
# ___ = 12
# print(__)

n = 1
#
# for i in 'testing789 fsdw 66':
#     print(i) if i.isdigit() else print(i.upper())

numbers = [3, 12, 55, 178, 1300, 6789, 19200]
for n in numbers:
    if n % 3 == 0:
        print(n)

def my_func1():
    print('costam')

def my_func2():
    print('costam2')

case_dict = {
    'a': my_func1,
    'b': my_func1
}

case_dict['b']()