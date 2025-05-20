# Импорт библиотек

import requests
import re
import random

from config import list1, sections_array1, link_one

# Очистка html от тегов

CLEANHTML = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
def cleanhtml(raw_html):
  cleantext = re.sub(CLEANHTML, '', raw_html)
  return cleantext

list = list1

sections_array = sections_array1
number = '4FF344'
finder = 'Номер: '

result = ''



for i in range (len(sections_array)):
    print("\nНачало генерации")
    start = -1
    count = 0
    end = -1
    
    req = requests.get(link_one)
    src = req.text
    
    print(src)
    
    lister = []
    
    while True:
        start = src.find('Номер: ', start+1)
        if start == -1:
            break
        end = start + 31
        count += 1
        lister.append(end)
    
    print("Количество вхождений символа в строку: ", count )
    print(f'{sections_array[i]} {list}')
    test = ''
    for i in range(len(lister)):
        for j in range (6):        
            test += req.text[lister[i]+j]
        test+=' '
    test = test.split(" ")
    
    rand = random.randint(0,count-1)
    
    print(test[rand])
    
    number = test[rand]
    
    link_two = f"http://ege.fipi.ru/bank/questions.php?search=1&pagesize=10&proj=AC437B34557F88EA4115D2F374B0A07B&theme=&qlevel=&qkind=&qsstruct=&qpos=&qid={number}&zid=&solved=&favorite=&blind="
    
    req = requests.get(link_two)
    src = req.text
    
        ### print(src)
    tester = ''
    
    tester = re.search('<p class="MsoNormal">(.+?)</p>', src)
    if tester:
        tester = tester.group(1)
    else:
        tester = re.search('<P class=Basis><SPAN>(.+?)</P>', src).group(1)
        

    tester = tester.replace('m:', '')
    tester = tester.replace('math', 'math xmlns="http://www.w3.org/1998/Math/MathML"')
    
    result += f'<p class="MsoNormal">{tester}</p>'
    result += '\n'
    
text = f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Document</title>\n</head>\n<body>\n{result}\n</body>\n</html>'


with open("hello.html", "w", encoding="utf-8") as file:
    file.write(text)
    print("Файл записан")
    