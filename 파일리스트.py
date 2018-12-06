import os

path = './'
file_list = os.listdir(path)
file_list.sort()

for i in file_list:
    if i.find('.txt') is not -1 :
        print(i)