from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry('500x330')


n1 = 0
n2 = 0
op = None
res = StringVar()

def getvalue(a):
    global n1
    global n2
    global res
    if op is None:
        number = n1*10 + a
        n1 = number
    else:
        number = n2 * 10 + a
        n2 = number
    res.set(str(number))

def getop(a):
    global op
    op = a
    res.set(str(op))


def clears():
    global n1,n2,op
    n1 = 0
    n2 = 0
    op = None
    res.set('0')

def calculate():
    if op == '-':
        res.set(str(n1 - n2))
    elif op == '+':
        res.set(str(n1 + n2))
    elif op == '/':
        res.set(str(n1 / n2))
    else:
        res.set(str(n1 * n2))

window.config(bg='black')
msg = Entry(window,bd=20,textvariable=res,relief='sunken',font=("Helvetica", 20))
msg.grid(columnspan=4,ipadx=80,ipady=10)  # Expand horizontally
button7 = Button(text=7,width=15,height="2",bg='lightgrey',command =lambda: getvalue(7))
button7.grid(row=1, column=0 , pady = 1)
button8 = Button(text=8,width=15,height="2",bg='lightgrey',command =lambda: getvalue(8))
button8.grid(row=1, column=1 , pady = 1)
button9 = Button(text=9,width=15,height="2",bg='lightgrey',command =lambda: getvalue(9))
button9.grid(row=1, column=2 , pady = 1)
buttonsym1 = Button(text='/',width=15,height="2",bg='lightgrey',command =lambda: getop('/') )
buttonsym1.grid(row=1, column=3 , pady = 1)

button4 = Button(text=4,width=15,height="2",bg='lightgrey',command =lambda: getvalue(4))
button4.grid(row=2, column=0 , pady = 1)
button5 = Button(text=5,width=15,height="2",bg='lightgrey',command =lambda: getvalue(5))
button5.grid(row=2, column=1 , pady = 1)
button6 = Button(text=6,width=15,height="2",bg='lightgrey',command =lambda: getvalue(6))
button6.grid(row=2, column=2 , pady = 1)
buttonsym2 = Button(text='*',width=15,height="2",bg='lightgrey', command =lambda: getop('*'))
buttonsym2.grid(row=2, column=3 , pady = 1)

button1 = Button(text=1,width=15,height="2",bg='lightgrey',command =lambda: getvalue(1))
button1.grid(row=3, column=0 , pady = 1)
button2 = Button(text=2,width=15,height="2",bg='lightgrey',command =lambda: getvalue(2))
button2.grid(row=3, column=1 , pady = 1)
button3 = Button(text=3,width=15,height="2",bg='lightgrey',command =lambda: getvalue(3))
button3.grid(row=3, column=2 , pady = 1)
buttonsym3 = Button(text='-',width=15,height="2",bg='lightgrey', command =lambda: getop('-'))
buttonsym3.grid(row=3, column=3 , pady = 1)


button0 = Button(text=0,width=15,height="2",bg='lightgrey',command =lambda: getvalue(0))
button0.grid(row=4, column=0 , pady = 1)
buttonsym4 = Button(text='clear',width=15,height="2",bg='lightgrey',command=clears)
buttonsym4.grid(row=4, column=1 , pady = 1)
buttonsym5 = Button(text='=',width=15,height="2",bg='lightgrey',command = calculate)
buttonsym5.grid(row=4, column=2 , pady = 1)
buttonsym6 = Button(text='+',width=15,height="2",bg='lightgrey',command =lambda: getop('+'))
buttonsym6.grid(row=4, column=3 , pady = 1)


mainloop()
