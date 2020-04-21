#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
from tkinter import *
import sqlite3
import xlrd
import xlwt
from tkinter import filedialog
import tkinter.messagebox

########################################################
'''数据库'''
# 创建一个连接对象，连接到本地数据库
conn = sqlite3.connect("python.db")
# 创建一个游标对象，调用其execute（）方法来执行SQL语句
sql = conn.cursor()
try:
    sql.execute('''CREATE TABLE VOCABULARY
                (
                        WORD TEXT,
                        Chinese TEXT)''')
except:
    sql.execute("INSERT INTO VOCABULARY VALUES('*','*')")

#################################################
'''主界面'''
top = tkinter.Tk()
top.title('我不是药神')
top.geometry('500x400+400+200')
top.resizable(0, 0)  # 不允许改变窗口
lb = tkinter.Label(top, text='欢 迎 使 用 英 语 词 汇 学 习 系 统')  # 欢迎界面
lb.place(relx=0.3, rely=0.05, width=200, height=50)  # 设置字
menubar = tkinter.Menu(top)
# 　定义一个空的菜单单元
filemenu = tkinter.Menu(menubar, tearoff=0)  # tearoff意为下拉
# 　将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
################################################
'''菜单模块'''
def help():
    tkinter.messagebox.askokcancel(title='帮助（HELP）', message='我觉着这么简单的程序不需要帮助文档\n有疑问请联系作者计科1707杜宝乐')
def bug():
    tkinter.messagebox.askokcancel(title='已知bug', message='做一个简单的外壳')
menubar.add_cascade(label='菜单', menu=filemenu)
filemenu.add_command(label='帮助', command=help)
filemenu.add_command(label='bug', command=bug)
'''看病'''
def text():  # 调出文本框
    txt.delete('1.0', 'end')
    txt.insert(END, '输入症状')
    f = Entry(top, show=None)
    f.place(relx=0.3, rely=0.5, relwidth=0.3, relheight=0.07)
    g = Button(top, text='确定', command=lambda: find(f.get()))  # 功能按键
    g.place(relx=0.6225, rely=0.53, anchor=W, width=40, height=22)
b = Button(top, text='看医生', command=text)
b.grid(column=6, row=2)
b.place(relx=0.54, rely=0.248, anchor=W, width=80, height=40)
#################################################
#买药#
def text1():  # 调出文本框
    txt.delete('1.0', 'end')
    txt.insert(END, '输入药品')
    f = Entry(top, show=None)
    f.place(relx=0.3, rely=0.5, relwidth=0.3, relheight=0.07)
    g = Button(top, text='确定', command=lambda: find(f.get()))  # 功能按键
    g.place(relx=0.6225, rely=0.53, anchor=W, width=40, height=22)
b = Button(top, text='买药', command=text1)
b.grid(column=6, row=2)
b.place(relx=0.34, rely=0.248, anchor=W, width=80, height=40)
################################################################3
'''显示模块'''
txt = Text(top)
txt.place(relx=0.3, rely=0.6, relheight=0.2, relwidth=0.4)
####################################################
'''退出系统模块'''
def on_closing():  # 退出进行提醒
    top.destroy()
    sql.close()
    # 5.关闭数据库连接
    conn.close()
c = Button(top, text='退出系统', bg="blue", command=on_closing)
c.grid(column=6, row=2)
c.place(relx=0.43, rely=0.88, anchor=W, width=80, height=40)
top.protocol("WM_DELETE_WINDOW", on_closing)
top.config(menu=menubar)  # 加上这代码，才能将菜单栏显示
top.mainloop()