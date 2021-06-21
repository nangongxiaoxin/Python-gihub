import os
f = open("学生成绩表.txt",'r') #以只读方式打开所在目录下的 学生成绩表.txt
line=f.readline()
print(line,end='')
line=f.readline()
#while循环进行处理输出
while line:
    print(line,end='')  
    maths=int(line[7:10])#获取该行指定位置的字符并转换为int型
    english=int(line[10:13])
    computer=int(line[15:18])
    print ('该生成绩为：',maths+english+computer,'\n')
    line=f.readline()
f.close()#关闭文件
os.system("pause")#屏幕暂停
