key= str("Name")
#a = int(1)
initial_dict= {'Contact1': "Volodymyr",'Contact2': "Nastya",'Contact3': "Andrew",'Contact4': "Yevi",'Contact5': "Test",'Contact6': "Dima" }
my_contacts = {}
while len(my_contacts) <= 15:
  key+='1'
  user = str(input('Enter the name: '))
  my_contacts.update({key:user})
  my_contacts.update(initial_dict)
  print(my_contacts)
  key + '1'

else:
  print('Dictionary is full: ', my_contacts )
