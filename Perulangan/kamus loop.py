data = {"nama":"agus","umur":19,"pekerjaan":"ngoding"}
for x in data.items():
  print(x)
data = {"nama":"agus","umur":19,"pekerjaan":"ngoding"}
for x in data.values():
  print(x)
# cetak semua data  
for x in data:
  print(x) 
  
child1 = {
  "name" : "zee",
  "year" : 2005
}
child2 = {
  "name" : "christy",
  "year" : 2005
}
child3 = {
  "name" : "marsha",
  "year" : 2005
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y +":", obj[y])
  