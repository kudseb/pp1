import json

with open("film.json") as file:
    data = json.load(file)
    for k,v in data.items():
        print(k,":",v)
                
x = {
  "name": "John",
  "age": 30,
  "city": "New York",
  "street":"Wallstreet",
  "flatno":"31"
  }
print(x)
y=json.dumps(x,indent=4)
print(y)
with open("jsondump.json",'w') as f:
    f.write(y)