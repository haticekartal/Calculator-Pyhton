import tkinter as tk

def collect():
    n1 = float(number1.get())
    n2 = float(number2.get())
    result.configure(text = str(n1+n2))

def sub():
    n1 = float(number1.get())
    n2 = float(number2.get())
    result.configure(text=str(n1 - n2))

def mul():
    n1 = float(number1.get())
    n2 = float(number2.get())
    result.configure(text=str(n1 * n2))

def div():
    n1 = float(number1.get())
    n2 = float(number2.get())
    result.configure(text=str(n1 / n2))



pencere=tk.Tk()
pencere.title('Calculator')
pencere.geometry("350x400")

calc = tk.Label(pencere, text= "**Welcome to Calculator**", font="courier 15 italic", width=30, justify="center", fg='purple')
calc.place(x=-15, y=20)
result = tk.Label(pencere, text="Result", font=" courier 16 bold", width=30, justify="center", fg='pink')
result.place(x=-30, y=50)

number1 = tk.Entry(pencere, font="courier 14 bold", width=15, justify="right", bg='pink')
number1.place(x=90, y=110)
number2 = tk.Entry(pencere, font="courier 14 bold", width=15, justify="right", bg='pink')
number2.place(x=90, y=150)

button1 = tk.Button(pencere, text="+",font="courier 14 bold", width=7, command=collect, bg='red')
button1.place(x=130, y=190)

button2 = tk.Button(pencere, text="-",font="courier 14 bold", width=7, command=sub, bg='yellow')
button2.place(x=130, y=230)

button3 = tk.Button(pencere, text="*",font="courier 14 bold", width=7, command=mul, bg='green')
button3.place(x=130, y=270)

button4 = tk.Button(pencere, text="/",font="courier 14 bold", width=7, command=div, bg='blue')
button4.place(x=130, y=310)




pencere.mainloop()

