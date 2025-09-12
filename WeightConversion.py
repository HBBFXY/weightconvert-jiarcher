# 在这个文件下编写代码，题目具体要求见README.md文件
#千克与英镑重量转换

ZHstr=input("")

if ZHstr[-2] in ['k'] or ZHstr[-2] in ['千'] or ZHstr[-2] in ['公']:
    R = (eval (ZHstr[0:-2]) *2.2046 )
    print("对应的英制重量为{:.3f}英镑".format(R))
elif ZHstr[-2] in ['p'] or ZHstr[-2] in ['英']:
    M = (eval (ZHstr[0:-2] /2.2046 ))
    print("对应的公制重量为{:.3f}公斤".format(M))
else:
    print("输入的格式错误")
