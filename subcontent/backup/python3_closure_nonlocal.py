#!/usr/bin/python3

##python3 闭包 与 nonlocal

#如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，
#那么内部函数就被认为是闭包(closure)

def A_():
	var = 0
	def clo_B():
		var_b = 1   # 闭包的局部变量
		var = 100
		print(var) # 引用外部的var , 但是不会改变var 的值
	return clo_B
#clo_B是一个闭包

#nonlocal 关键字

def A_():
	var = 0
	def clo_B():
		nonlocal var   # nonlocal关键字 指定var 不是闭包的局部变量
		var = var + 1   # 若 不使用nonlocal 关键字 , 则此行代码会出现错误

		
