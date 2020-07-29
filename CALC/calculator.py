
from tkinter import *
window =Tk()
window.title("Calculator")
def btn_click(item):
	global exp
	exp=exp+str(item)
	input_text.set(exp)
def btn_clear():
	global exp
	exp=''
	input_text.set("")
def btn_equal():
	global exp
	try:result=str(eval(exp))
	except:result="MATH ERROR"
	input_text.set(result)
exp=''
input_text=StringVar()

txtDisplay=Entry(window,font=('arial',18,'bold'),textvariable=input_text,bg='white',bd=35,insertwidth=3,justify='right').grid(columnspan=4)
btn7=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='7',bg="white",command=lambda:btn_click(7)).grid(row=1,column=0)
btn8=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='8',bg="white",command=lambda:btn_click(8)).grid(row=1,column=1)
btn9=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='9',bg="white",command=lambda:btn_click(9)).grid(row=1,column=2)
add=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='+',bg="white",command=lambda:btn_click('+')).grid(row=1,column=3)
btn4=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='4',bg="white",command=lambda:btn_click(4)).grid(row=2,column=0)
btn5=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='5',bg="white",command=lambda:btn_click(5)).grid(row=2,column=1)
btn6=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='6',bg="white",command=lambda:btn_click(6)).grid(row=2,column=2)
sub=Button(window,padx=16,bd=8,fg="black",font=('arial',20,'bold'),text='-',bg="white",command=lambda:btn_click('-')).grid(row=2,column=3)
btn1=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='1',bg="white",command=lambda:btn_click(1)).grid(row=3,column=0)
btn2=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='2',bg="white",command=lambda:btn_click(2)).grid(row=3,column=1)
btn3=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='3',bg="white",command=lambda:btn_click(3)).grid(row=3,column=2)
mul=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='*',bg="white",command=lambda:btn_click('*')).grid(row=3,column=3)
btn0=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='0',bg="white",command=lambda:btn_click(0)).grid(row=4,column=0)
btnclr=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='C',bg="white",command=lambda:btn_clear()).grid(row=4,column=1)
btneql=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='=',bg="white",command=lambda:btn_equal()).grid(row=4,column=2)
div=Button(window,padx=16,bd=8,fg="black",font=('arial',18,'bold'),text='/',bg="white",command=lambda:btn_click('/')).grid(row=4,column=3)



window.mainloop()
