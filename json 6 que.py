# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?
import json
a={
    "Name":"Abhishek",
    "Designation": "CEO of navgurukul",
    "Gender":"male",
   "Age":"29"
}
b=open("ques7.json","x")
b=open("ques7.json","w")
json.dump(a,b,indent=2)