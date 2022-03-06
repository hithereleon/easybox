#导入模块
from logging import exception
import os
import time
import random
import string
import tkinter
import tkinter as tk
import requests
import math
import tkinter.messagebox
import sys
#定义退出
def exit():
	print("已退出")
	os.system("cls")
	menu()
#定义菜单
def menu():
	os.system("cls")
	print("你好，欢迎使用eb工具箱")
	time.sleep(1)
	gongneng = input("请选择你要使用的功能\n1.工具箱 2.题库训练 3.退出\n")
	time.sleep(1)
	if gongneng == '1':
		eb()
	elif gongneng == '2':
		question()
	elif gongneng == '3':
		sys.exit(0)
	else:
		menu()
#定义工具箱界面
def eb():
	os.system("cls")
	print("欢迎来到工具箱，请选择功能")
	tool = input("1.两数相除求余数\n2.强密码生成器\n3.99乘法表\n4.计算器\n5.翻译器\n6.退出\n")
	if tool == '1':
		time.sleep(1)
		yushu()
	elif tool == '2':
		psw1()
	elif tool == '3':
		nn()
	elif tool == '4':
		calculat()
	elif tool == '5':
		trans()
	elif tool == '6':
		menu()
	else:
		eb()
#定义题库
def question():
	os.system("cls")
	print("欢迎来到题库训练，请选择你要刷的题")
	topic = input("1.乘法练习\n2.除法练习\n3.乘方练习\n4.退出\n")
	if topic == '1':
		multi()
	elif topic == '2':
		divi()
	elif topic == '3':
		power()
	elif topic == '4':
		menu()
	else:
		question()
#定义余数工具
def yushu():
	print("答案显示格式(商,余数)")
	first = int(input("请输入被除数"))
	second = int(input("请输入除数"))
	print(divmod(first,second))
	os.system("pause")
	eb()
#定义强密码
def password():
		password=string.ascii_letters+string.digits
		passwdask = random.randint(8,16)
		key = random.sample(password,passwdask)
		keys = ''.join(key)
		return keys
def psw1():
	num = random.randint(4,10)
	password()
	print("为您提供了"+ str(num) +"个密码，请查收\n")
	for x in range(int(num)):
		print(password())
	os.system("pause")
	eb()
#99乘法表
def nn():
	for i in range(1,10):
		for j in range(1,i + 1):
					mul = i * j
					print("%s * %s = %s" %(i,j,mul),end=" ")
		print()
	time.sleep(10)
	eb()
#定义乘法练习
def multi():
	hard = input("请选择难度:\na.简单\nb.难\n")
	if hard == 'a':
		a = random.randint(10,40)
		b = random.randint(10,40)
	elif hard == 'b':
		a = random.randint(100,400)
		b = random.randint(100,400)
	else:
		multi()
	answer = input(str(a)+"x"+str(b)+"=?")
	if answer == str(a*b):
		print("你做对了")
		time.sleep(2)
	else:
		print("你做错了")
		time.sleep(2)
	question()
#定义除法练习
def divi():
	hard = input("请选择难度:\na.简单\nb.难(除不尽的求余数)")
	if hard == 'a':
		a = random.randint(10,40)
		b = random.randint(10,40)
	elif hard == 'b':
		a = random.randint(100,400)
		b = random.randint(100,400)
	else:
		divi()
	print("题目为:" + str(a) + "÷" + str(b))
	x = input("请输入商")
	y = input("请输入余数，没有填0")
	if x == str(a//b) and y == str(a%b):
		print("你做对了")
		time.sleep(2)
	else:
		print("你做错了")
		time.sleep(2)
	question()
#定义乘方练习
def power():
	hard = input("请选择难度:a.简单b.难")
	if hard == 'a':
		a = random.randint(1,20)
		b = random.randint(2,10)
	elif hard == 'b':
		a = random.randint(20,50)
		b = random.randint(10,30)
	else:
		power()
	answer = input(str(a)+"^"+str(b)+"=?")
	if answer == str(a**b):
		print("你做对了")
		time.sleep(2)
	else:
		print("你做错了")
		time.sleep(2)
	question()
#定义计算器
def calculat():
	class calculator:
		#界面布局方法
		def __init__(self):
			#创建主界面，并且保存到成员属性中
			self.root = tkinter.Tk()
			self.root.minsize(280, 450)
			self.root.maxsize(280, 470)
			self.root.title('计算器1.0')
			# 设置显式面板的变量
			self.result = tkinter.StringVar()
			self.result.set(0)
			# 设置一个全局变量  运算数字和f符号的列表
			self.lists = []
			# 添加一个用于判断是否按下运算符号的标志
			self.ispresssign = False
			# 界面布局
			self.layout()
			self.root.mainloop()


		

		#计算器主界面摆放
		def layout(self):
			# 显示屏
			result = tkinter.StringVar()
			result.set(0)
			show_label = tkinter.Label(self.root, bd=3, bg='white', font=('宋体', 30), anchor='e', textvariable=self.result)
			show_label.place(x=5, y=20, width=270, height=70)
			# 功能按钮MC
			button_mc = tkinter.Button(self.root, text='MC', command=self.wait)
			button_mc.place(x=5, y=95, width=50, height=50)
			# 功能按钮MR
			button_mr = tkinter.Button(self.root, text='MR', command=self.wait)
			button_mr.place(x=60, y=95, width=50, height=50)
			# 功能按钮MS
			button_ms = tkinter.Button(self.root, text='MS', command=self.wait)
			button_ms.place(x=115, y=95, width=50, height=50)
			# 功能按钮M+
			button_mjia = tkinter.Button(self.root, text='M+', command=self.wait)
			button_mjia.place(x=170, y=95, width=50, height=50)
			# 功能按钮M-
			button_mjian = tkinter.Button(self.root, text='M-', command=self.wait)
			button_mjian.place(x=225, y=95, width=50, height=50)
			# 功能按钮←
			button_zuo = tkinter.Button(self.root, text='←', command=self.dele_one)
			button_zuo.place(x=5, y=150, width=50, height=50)
			# 功能按钮CE
			button_ce = tkinter.Button(self.root, text='CE', command=lambda: self.result.set(0))
			button_ce.place(x=60, y=150, width=50, height=50)
			# 功能按钮C
			button_c = tkinter.Button(self.root, text='C', command=self.sweeppress)
			button_c.place(x=115, y=150, width=50, height=50)
			# 功能按钮±
			button_zf = tkinter.Button(self.root, text='±', command=self.zf)
			button_zf.place(x=170, y=150, width=50, height=50)
			# 功能按钮√
			button_kpf = tkinter.Button(self.root, text='√', command=self.kpf)
			button_kpf.place(x=225, y=150, width=50, height=50)
			# 数字按钮7
			button_7 = tkinter.Button(self.root, text='7', command=lambda: self.pressnum('7'))
			button_7.place(x=5, y=205, width=50, height=50)
			# 数字按钮8
			button_8 = tkinter.Button(self.root, text='8', command=lambda: self.pressnum('8'))
			button_8.place(x=60, y=205, width=50, height=50)
			# 数字按钮9
			button_9 = tkinter.Button(self.root, text='9', command=lambda: self.pressnum('9'))
			button_9.place(x=115, y=205, width=50, height=50)
			# 功能按钮/
			button_division = tkinter.Button(self.root, text='/', command=lambda: self.presscalculate('/'))
			button_division.place(x=170, y=205, width=50, height=50)
			# 功能按钮%
			button_remainder = tkinter.Button(self.root, text='//', command=lambda:self.presscalculate('//'))
			button_remainder.place(x=225, y=205, width=50, height=50)
			# 数字按钮4
			button_4 = tkinter.Button(self.root, text='4', command=lambda: self.pressnum('4'))
			button_4.place(x=5, y=260, width=50, height=50)
			# 数字按钮5
			button_5 = tkinter.Button(self.root, text='5', command=lambda: self.pressnum('5'))
			button_5.place(x=60, y=260, width=50, height=50)
			# 数字按钮6
			button_6 = tkinter.Button(self.root, text='6', command=lambda: self.pressnum('6'))
			button_6.place(x=115, y=260, width=50, height=50)
			# 功能按钮*
			button_multiplication = tkinter.Button(self.root, text='*', command=lambda: self.presscalculate('*'))
			button_multiplication.place(x=170, y=260, width=50, height=50)
			# 功能按钮1/x
			button_reciprocal = tkinter.Button(self.root, text='1/x', command=self.ds)
			button_reciprocal.place(x=225, y=260, width=50, height=50)
			# 数字按钮1
			button_1 = tkinter.Button(self.root, text='1', command=lambda: self.pressnum('1'))
			button_1.place(x=5, y=315, width=50, height=50)
			# 数字按钮2
			button_2 = tkinter.Button(self.root, text='2', command=lambda: self.pressnum('2'))
			button_2.place(x=60, y=315, width=50, height=50)
			# 数字按钮3
			button_3 = tkinter.Button(self.root, text='3', command=lambda: self.pressnum('3'))
			button_3.place(x=115, y=315, width=50, height=50)
			# 功能按钮-
			button_subtraction = tkinter.Button(self.root, text='-', command=lambda: self.presscalculate('-'))
			button_subtraction.place(x=170, y=315, width=50, height=50)
			# 功能按钮=
			button_equal = tkinter.Button(self.root, text='=', command=lambda: self.pressequal())
			button_equal.place(x=225, y=315, width=50, height=105)
			# 数字按钮0
			button_0 = tkinter.Button(self.root, text='0', command=lambda: self.pressnum('0'))
			button_0.place(x=5, y=370, width=105, height=50)
			# 功能按钮.
			button_point = tkinter.Button(self.root, text='.', command=lambda: self.pressnum('.'))
			button_point.place(x=115, y=370, width=50, height=50)
			# 功能按钮+
			button_plus = tkinter.Button(self.root, text='+', command=lambda: self.presscalculate('+'))
			button_plus.place(x=170, y=370, width=50, height=50)


		#计算器菜单功能
		def myfunc(self):
			tkinter.messagebox.showinfo('','请期待2.0')


		#数字方法
		def pressnum(self,num):
			# 全局化变量
			# 判断是否按下了运算符号
			if self.ispresssign == False:
				pass
			else:
				self.result.set(0)
				# 重置运算符号的状态
				self.ispresssign = False
			if num == '.':
				num = '0.'
			# 获取面板中的原有数字
			oldnum = self.result.get()
			# 判断界面数字是否为0
			if oldnum == '0':
				self.result.set(num)
			else:
				# 连接上新按下的数字
				newnum = oldnum + num

				# 将按下的数字写到面板中
				self.result.set(newnum)


		#运算函数
		def presscalculate(self,sign):
			# 保存已经按下的数字和运算符号
			# 获取界面数字
			num = self.result.get()
			self.lists.append(num)
			# 保存按下的操作符号
			self.lists.append(sign)
			# 设置运算符号为按下状态
			self.ispresssign = True


		#获取运算结果
		def pressequal(self):
			# 获取所有的列表中的内容（之前的数字和操作）
			# 获取当前界面上的数字
			curnum = self.result.get()
			# 将当前界面的数字存入列表
			self.lists.append(curnum)
			# 将列表转化为字符串
			calculatestr = ''.join(self.lists)
			# 使用eval执行字符串中的运算即可
			endnum = eval(calculatestr)
			# 将运算结果显示在界面中
			self.result.set(str(endnum)[:10])
			if self.lists != 0:
				self.ispresssign = True
			# 清空运算列表
			self.lists.clear()


		#暂未开发说明
		def wait(self):
			tkinter.messagebox.showinfo('','功能在努力的实现，请期待2.0版本的更新')


		#←按键功能
		def dele_one(self):
			if self.result.get() == '' or self.result.get() == '0':
				self.result.set('0')
				return
			else:
				num = len(self.result.get())
				if num > 1:
					strnum = self.result.get()
					strnum = strnum[0:num - 1]
					self.result.set(strnum)
				else:
					self.result.set('0')


		#±按键功能
		def zf(self):
			strnum = self.result.get()
			if strnum[0] == '-':
				self.result.set(strnum[1:])
			elif strnum[0] != '-' and strnum != '0':
				self.result.set('-' + strnum)


		#1/x按键功能
		def ds(self):
			dsnum = 1 / float(self.result.get())
			self.result.set(str(dsnum)[:10])
			if self.lists != 0:
				self.ispresssign = True
			# 清空运算列表
			self.lists.clear()


		#C按键功能
		def sweeppress(self):
			self.lists.clear()
			self.result.set(0)


		#√按键功能
		def kpf(self):
			strnum = float(self.result.get())
			endnum = math.sqrt(strnum)
			if str(endnum)[-1] == '0':
				self.result.set(str(endnum)[:-2])
			else:
				self.result.set(str(endnum)[:10])
			if self.lists != 0:
				self.ispresssign = True
			# 清空运算列表
			self.lists.clear()


	#实例化对象
	mycalculator = calculator()
	eb()
#定义翻译器
def trans():
	window=tk.Tk()
	window.title("翻译器(如遇报错请忽视，不会影响程序正常运行)")
	window.geometry("497x150+500+500")

	l=tk.Label(window,text="请输入要翻译的内容：",font="微软雅黑 11",height=2)
	l.grid()
	l1=tk.Label(window,text="这就是为你翻译的啦：",font="微软雅黑 11",height=2)
	l1.grid()

	var=tk.StringVar()

	e=tk.Entry(window,width=32)
	e.grid(row=0,column=1)
	e1=tk.Entry(window,textvariable=var,width=32)
	e1.grid(row=1,column=1)



	def click():
		content=e.get()
		data={
			"i": content,
			"from": "AUTO",
			"to": "AUTO",
			"smartresult": "dict",
			"client": "fanyideskweb",
			"doctype": "json",
			"version": "2.1",
			"keyfrom": "fanyi.web",
			"action": "FY_BY_REALTIME",
			"typoResult": "false"
		}
		try:
			response=requests.post("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule",data=data).json()
		except Exception:
			return
		
		# print(response)
		# print(type(response))
		bb=response["translateResult"][0][0]["tgt"]
		# print(bb)
		# print(type(bb))
		var.set(bb)
	try:
		b=tk.Button(window,text="点击翻译",command=click,width=10,font="微软雅黑 12")
	except exception:
		return
	b.grid(columnspan=2)

	window.mainloop()
	eb()


#正式编写
menu()