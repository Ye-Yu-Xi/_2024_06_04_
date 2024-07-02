import random

def allNames() ->list:
    names_list = []
    with open("names.txt",encoding="utf-8") as file:
        for line in file:
            names_list.append(line[:3])
            
first_name = input("請輸入您的姓:")
count = int(input("請輸入您要的筆數:"))
random_names = random.choices(names_list,k=count)    #K=要抓幾個(預設是一個)
for name in random_names:
    print(first_name + name[-2:])     #2:13:00