#coding:utf-8
file = open("C:/Projects/financeanalyze/wechat.txt","r",encoding="utf-8")
out = open("C:/Projects/financeanalyze/wechat2.txt","w",encoding="utf-8")
record = []
a = 0
count = 1
for line in file:
    if (line.isspace() or len(line)==0):
        continue
    line=line.strip()
    record.append(line)
    a = a + 1
    out.write(line)
    out.write("’")
    if(a==3):
        out.write("\n")
        print(count)
        count = count + 1
        print(record)
        record=[]
        a=0
out.close()

