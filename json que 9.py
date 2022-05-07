import json
a={
    "shopping_list":
    {  "chaco":"15",
       "Biscuits":"50",
       "Diary_milk":"30",
       "ice_cream":"20",
        } 
}
w=input("enter the item:")
v=int(input("enter the quantity"))
for i in a:
    for j in a[i]:
        if w in a[i]:
            if j==w and int(a[i][j])>=v:
                r=int(a[i][j])-v
                a[i][j]=str(r)
                break
            elif j!=w:
                print("not avilable")
                break
n=open("ishu.json","w")
json.dump(a,n,indent=4)
