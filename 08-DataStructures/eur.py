import json
with open('euro.json') as file:
    x=json.load(file)
print(f'{"Data":<15}Kurs')
print('===================')
for i in x['rates']:
    print(f"{i['effectiveDate']:<13} {i['mid']}")