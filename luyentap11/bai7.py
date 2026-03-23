import csv

ten=input()
tuoi=input()
id=input()

# txt
f=open("nv.txt","w",encoding="utf-8")
f.write(ten+" "+tuoi+" "+id)
f.close()

# csv
f=open("nv.csv","w",newline="",encoding="utf-8")
w=csv.writer(f)
w.writerow(["ten","tuoi","id"])
w.writerow([ten,tuoi,id])
f.close()