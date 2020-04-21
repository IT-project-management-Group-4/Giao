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
'''���ݿ�'''
# ����һ�����Ӷ������ӵ��������ݿ�
conn = sqlite3.connect("python.db")
# ����һ���α���󣬵�����execute����������ִ��SQL���
sql = conn.cursor()
try:
    sql.execute('''CREATE TABLE VOCABULARY
                (
                        WORD TEXT,
                        Chinese TEXT)''')
except:
    sql.execute("INSERT INTO VOCABULARY VALUES('*','*')")

#################################################
'''������'''
top = tkinter.Tk()
top.title('�Ҳ���ҩ��')
top.geometry('500x400+400+200')
top.resizable(0, 0)  # ������ı䴰��
lb = tkinter.Label(top, text='�� ӭ ʹ �� Ӣ �� �� �� ѧ ϰ ϵ ͳ')  # ��ӭ����
lb.place(relx=0.3, rely=0.05, width=200, height=50)  # ������
menubar = tkinter.Menu(top)
# ������һ���յĲ˵���Ԫ
filemenu = tkinter.Menu(menubar, tearoff=0)  # tearoff��Ϊ����
# �������涨��Ŀղ˵�����Ϊ`File`�����ڲ˵����У�����װ���Ǹ�������
################################################
'''�˵�ģ��'''
def help():
    tkinter.messagebox.askokcancel(title='������HELP��', message='�Ҿ�����ô�򵥵ĳ�����Ҫ�����ĵ�\n����������ϵ���߼ƿ�1707�ű���')
def bug():
    tkinter.messagebox.askokcancel(title='��֪bug', message='��һ���򵥵����')
menubar.add_cascade(label='�˵�', menu=filemenu)
filemenu.add_command(label='����', command=help)
filemenu.add_command(label='bug', command=bug)
'''����'''
def text():  # �����ı���
    txt.delete('1.0', 'end')
    txt.insert(END, '����֢״')
    f = Entry(top, show=None)
    f.place(relx=0.3, rely=0.5, relwidth=0.3, relheight=0.07)
    g = Button(top, text='ȷ��', command=lambda: find(f.get()))  # ���ܰ���
    g.place(relx=0.6225, rely=0.53, anchor=W, width=40, height=22)
b = Button(top, text='��ҽ��', command=text)
b.grid(column=6, row=2)
b.place(relx=0.54, rely=0.248, anchor=W, width=80, height=40)
#################################################
#��ҩ#
def text1():  # �����ı���
    txt.delete('1.0', 'end')
    txt.insert(END, '����ҩƷ')
    f = Entry(top, show=None)
    f.place(relx=0.3, rely=0.5, relwidth=0.3, relheight=0.07)
    g = Button(top, text='ȷ��', command=lambda: find(f.get()))  # ���ܰ���
    g.place(relx=0.6225, rely=0.53, anchor=W, width=40, height=22)
b = Button(top, text='��ҩ', command=text1)
b.grid(column=6, row=2)
b.place(relx=0.34, rely=0.248, anchor=W, width=80, height=40)
################################################################3
'''��ʾģ��'''
txt = Text(top)
txt.place(relx=0.3, rely=0.6, relheight=0.2, relwidth=0.4)
####################################################
'''�˳�ϵͳģ��'''
def on_closing():  # �˳���������
    top.destroy()
    sql.close()
    # 5.�ر����ݿ�����
    conn.close()
c = Button(top, text='�˳�ϵͳ', bg="blue", command=on_closing)
c.grid(column=6, row=2)
c.place(relx=0.43, rely=0.88, anchor=W, width=80, height=40)
top.protocol("WM_DELETE_WINDOW", on_closing)
top.config(menu=menubar)  # ��������룬���ܽ��˵�����ʾ
top.mainloop()