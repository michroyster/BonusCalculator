from tkinter import *

calculator = Tk()
calculator.title("Calculator")
operator = ""
textInput = StringVar()

txtDisplay = Entry(calculator, font=('arial', 20), textvariable=textInput, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

btn7 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="7").grid(row=1, column=0)
btn8 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="8").grid(row=1, column=1)
btn9 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="9").grid(row=1, column=2)
btnMultiplication = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="*").grid(row=1, column=3)

btn4 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="4").grid(row=2, column=0)
btn5 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="5").grid(row=2, column=1)
btn6 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="6").grid(row=2, column=2)
btnSubtraction = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="-").grid(row=2, column=3)

btn1 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="1").grid(row=3, column=0)
btn2 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="2").grid(row=3, column=1)
btn3 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="3").grid(row=3, column=2)
btnAddition = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="+").grid(row=3, column=3)

btnPlusMinus = Button(calculator, padx=16, fg="black", font=('arial', 20),text="+/-").grid(row=4, column=0)
btn0 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="0").grid(row=4, column=1)
btnDecimal = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text=".").grid(row=4, column=2)
btnEquals = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="=").grid(row=4, column=3)

calculator.mainloop()

