import json
dic={"Name":"Abhishek",
 "Designation": "CEO of navgurukul",
 "gender":"male",
 "age":29}
with open("meraki7.json","w") as file:
    json.dump(dic,file,indent=4)