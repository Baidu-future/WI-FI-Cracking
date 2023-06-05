def add(x, y):
    return x + y
# 定义函数用于减法
def subtract(x, y):
    return x - y
# 定义函数用于乘法
def multiply(x, y):
    return x * y
# 定义函数用于除法
def divide(x, y):
    return x / y
print("请选择操作")
print("1. 加法")
print("2. 减法")
print("3. 乘法")
print("4. 除法")
# 获取用户选择的操作
choice = input("请输入操作编号（1/2/3/4）:")
# 获取用户输入的两个数
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))
# 根据用户选择的操作进行计算
if choice == '1':
    result = add(num1, num2)
    print(num1, "+", num2, "=", result)
elif choice == '2':
    result = subtract(num1, num2)
    print(num1, "-", num2, "=", result)
elif choice == '3':
    result = multiply(num1, num2)
    print(num1, "*", num2, "=", result)
elif choice == '4':
    result = divide(num1, num2)
    print(num1, "/", num2, "=", result)
else:
    print("请重新输入有效的操作编号")

