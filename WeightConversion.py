# 在这个文件下编写代码，题目具体要求见README.md文件
#千克与英镑重量转换
ZHstr=input("请输入带有单位要转换的质量：")
if ZHstr[-2] in ['k'] or ZHstr[-2] in ['千']:
    R = (eval (ZHstr[0:-2]) *2.2046 )
    print("转换后的质量为{:.3f}英镑".format(R))
elif ZHstr[-2] in ['p'] or ZHstr[-2] in ['英']:
    M = (eval (ZHstr[0:-2] /2.2046 ))
    print("转换后的质量为{:.3f}千克".format(M))
else:
    print("输入的格式错误")
