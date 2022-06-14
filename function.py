with open ('text.txt') as f:
  data=f.read()
keylist=[]
firstline=data[data.find('(')+1:data.find(')')].replace(" ",'').split(',')
counter1=1
b=2
counter2=1
for i in firstline:
  keylist.append([i,"a"+str(counter1)])
  counter1+=1
  
for i in range (len(data)):
  if data[i]=='=' and data[i-1] not in "*%/=-+" and data[i+1]!='=':
    while data[i-b]!=' ':
      b+=1 
    if data[i+1]!='[' and data[i+1:i+3]!=' [':
      keylist.append([data[i-b+1:i],'a'+str(counter1)])
      counter1+=1
    else:
      keylist.append([data[i-b+1:i],"R"+str(counter2)])
      counter2+=1
    
for i in keylist:
  data=data.replace(i[0], i[1])
print(data)
