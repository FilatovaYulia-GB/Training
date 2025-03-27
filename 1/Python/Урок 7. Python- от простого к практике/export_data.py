# модуль экспорта данных 

def expp(last_name):
    with open('info.txt', 'r', encoding='utf-8') as f:
        info_list = f.read().splitlines()
        for person in info_list:
            if last_name in person:
                print(person)
                