
print("hello world!")       # 字符串  可以用英文的单引号也可以用双引号
print(23333)                # 整数
print(2.3333)               # 小数
print(True)                 # 布尔值  true   false
print(())                   # 元组
print([])                   # 数组
print({})                   # 字典


print("哈哈",2333,2.333)      # 串联
print ("哈哈"+"嘻嘻")         # 字符串的拼接
print("哈哈"*100)             # 字符串拼接的倍数
print(((1+2)*100-9.9)/2)      # 字符串的运算
print(2>3)                    #布尔值 判断正确与否 否即false
print(2<3)                    #布尔值 判断正确与否 是即true



#变量
#赋值
name = "张三"                       #把张三赋值给了名字叫name的变量
print(name)

a= input("请输入：")   
b= input("请输入：")              #input 获取用户输入的内容
print("input获取的内容：",a+b)



#数据格数的转换
print(type("哈哈"))               #type  获取数据的类型
print(type(23333))
print(type(2.3333))
print(type(()))
print(type([]))
print(type({}))

a = str(2333)                  #把数值转换成字符串
print(type(a))

a= float(input("请输入："))                #input 获取用户输入的内容 再将内容转换为小数格式
b= float(input("请输入："))            
print("input获取的内容：",a+b)



#数据的长度
a='hhhhhh'
print(len(a))

a= str(input("请输入："))                #input 获取用户输入的内容 再将内容转换为小数格式
b= str(input("请输入："))            
print(len(a+b))