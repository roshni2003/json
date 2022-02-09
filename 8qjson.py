import json
emp1={"name":"neelam","designation":"programer","age":24,"salary":2400}
emp2={"name":"komal","designation":"trainer","age":24,"salary":20000}
emp3={"name":"anuradha","designation":"HR","age":25,"salary":40000}
emp4={"name":"abhishek","designation":"manager","age":29,"salary":63000}
m=[]
m.append(emp1)
m.append(emp2)
m.append(emp3)
m.append(emp4)
with open("meraki8.json","w")as file:
    json.dump(m,file,indent=4)