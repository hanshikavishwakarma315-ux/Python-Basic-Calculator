# simple Python GUI Calculator by Hanshika
import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

display=tk.StringVar()

entry=tk.Entry(root,
textvariable=display,font=("Arial",20))
entry.grid(row=0,column=0,columnspan=4)


expression=""

def press(value):
    global expression
    expression=expression+str(value)
    display.set(expression)

def equal():
        global expression
        try:
            result=str(eval(expression))
            display.set(result)
            expression=result
        except:
            display.set("error")
            expression=""

def clear():
        global expression
        expression=""
        display.set("")

    

buttons= [
('7',1,0),('8',1,1),('9',1,2),
('/',1,3),
('4',2,0),('5',2,1),('6',2,2),
('*',2,3),
('1',3,0),('2',3,1),('3',3,2),
('-',3,3),
('0',4,0),('.',4,1),('=',4,2),
('+',4,3),
('%',5,3)
    ]
for text,row,col in buttons:
        if text == "=":

            tk.Button(root,text=text,width=15,height=4,
            command=equal).grid(row=row,column=col)

        else:
            tk.Button(root,text=text,width=15,height=4,
            command=lambda t=text:press(t)).grid(row=row,column=col)

            tk.Button(root,text="C",width=42,height=3,
                      command=clear).grid(row=6,column=0,columnspan=5)

root.mainloop()

