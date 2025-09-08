# 在这个文件下编写代码，题目具体要求见README.md文件
#千克与英镑重量转换
import sys

def convert_kg_to_pounds(kg):
    return kg * 2.20462

def convert_pounds_to_kg(pounds):
    return pounds / 2.20462

if __name__ == "__main__":
    # Example usage: python3 main.py 10 kg_to_pounds
    value = float(sys.argv[1])
    direction = sys.argv[2]
    if direction == "kg_to_pounds":
        print(convert_kg_to_pounds(value))
    elif direction == "pounds_to_kg":
        print(convert_pounds_to_kg(value))
    else:
        print("Unknown conversion type")
