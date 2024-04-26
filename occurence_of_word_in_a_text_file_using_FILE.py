f=open("textfiledemo.txt","rt")
paragraph=f.read()
split=paragraph.split()
count=0
ip=input("enter word : ")
for i in split:
    if i.lower() == ip.lower():
        count += 1

print("occurence",count)
f.close()

            

