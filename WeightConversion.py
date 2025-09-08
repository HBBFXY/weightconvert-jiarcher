# 在这个文件下编写代码，题目具体要求见README.md文件
#千克与英镑重量转换
def main():
    s = input().strip()
    unit = s[-2:]
    num_str = s[:-2]
    try:
        value = float(num_str)
    except:
        print("输入格式错误")
        return

    if unit == 'kg':
        result = value * 2.2046
        print(f"对应的英制重量为{result:.3f}磅")
    elif unit == 'pd':
        result = value / 2.2046
        print(f"对应的公制重量为{result:.3f}公斤")
    else:
        print("单位输入错误，请输入kg或pd")

if __name__ == "__main__":
    main()
