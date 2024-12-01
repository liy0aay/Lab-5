import re
from itertools import zip_longest
import pandas as pd 

RED = "\033[0;31m"
END = "\033[0m"


# задание 1

with open("task1-ru.txt", "r") as file:
    text = file.read()

words_before_comma = re.findall(r'\b\w+(?=,)', text)
text_in_brackets = re.findall(r'\[\s*.*?\s*\]', text)

print(f"{RED}Слова перед запятой:{END} {', '.join(words_before_comma)}\n")
print(f"{RED}Информация в квадратных скобках:{END} {', '.join(text_in_brackets)}\n")



# задание 2

with open("task2.html", "r") as file:
    html_file = file.read()

colors = re.findall(r'#[0-9a-fA-F]{6}', html_file)

print(f"{RED}Найденные цвета:{END} {', '.join(colors)}\n")



# задание 3

with open('task3.txt', 'r') as file:
    data = file.read()

website = re.findall(r'https?://[a-zA-Z0-9.-]+/', data)  
date = re.findall(r'\d{4}-\d{2}-\d{2}', data) 
surname = re.findall(r'[A-Z][a-z]+(?!\d\d@|@)', data)  
email = re.findall(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]{3}', data)
id = list(range(1, 10001))

rows = zip_longest(id, surname, email, date, website) 

data_frame = pd.DataFrame(rows, columns = ["ID", "Surname", "Email", "Date", "Website"])
data_frame.to_csv('data_base.csv', index=False)


# доп задание

with open('task_add.txt', 'r') as file:
    text = file.read()


dates = re.findall (r"(?<!\d)\d{4}[-/.]\d{2}[-/.]\d{2}(?!\d)|(?<!\d)\d{2}[-/.]\d{2}[-/.]\d{4}(?=\D|$|\d{1,3})", text)
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,3}", text)
urls = re.findall(r"https?://[a-zA-Z0-9.-]+\.[a-z]{2,3}", text)


print(f"{RED}Даты:{END}")
for i, date in enumerate(dates, start=1):
    print(f"{i}. {date}")

print(f"\n{RED}Электронные адреса:{END}")
for i, email in enumerate(emails, start=1):
    print(f"{i}. {email}")

print(f"\n{RED}Сайты:{END}")
for i, url in enumerate(urls, start=1):
    print(f"{i}. {url}")
