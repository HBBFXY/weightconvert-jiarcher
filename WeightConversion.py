# 在这个文件下编写代码，题目具体要求见README.md文件
#千克与英镑重量转换
Weight_input = input()
if Weight_input [-2:] in ['kg','KG']:
    pound = (eval(Weight_input[0:-2])) * 2.2046
    print("对应的英制重量为{:.3f}磅".format(pound))
elif Weight_input [-2:] in ['pd','PD']:
    kilogram = (eval(Weight_input[0:-2])) * 0.4535
    print("对应的公制重量为{:.3f}公斤".format(kilogram))
else:
    print("请输入格式错误")
