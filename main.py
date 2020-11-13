from tkinter import *

# Main variables
operator = ""
memory = []

# handle button click for numbers
def btnClick(numbers, op):
        if len(op) < 8:
                global operator 
                operator = operator + str(numbers)
                textInput.set(operator)

# clear current number
def btnClear():
        global operator
        operator = ""
        textInput.set(operator)

# clear all memory
def btnClearAll():
        global operator
        global memory
        operator = ""
        memory.clear()
        textInput.set(operator)

# flip the sign of the current number
def signSwap(arg):
        if arg[0] == "-":
                print("negative")
                global operator 
                operator = operator[1:]
                textInput.set(operator)
        else:
                print("positive")
                operator = "-" + operator
                textInput.set(operator)

# calculate the operation and return result
def calculate():
        global memory
        global operator
        op = memory.copy()
        if len(memory) == 3:
                if memory[1] == "+":
                        print("addition")
                        answer = int(op[0]) + int(op[2])
                        return str(answer)
                elif memory[1] == "-":
                        print("subtraction")
                        answer = int(op[0]) - int(op[2])
                        return str(answer)
                elif memory[1] == "*":
                        print("multiplication")
                        answer = int(op[0]) * int(op[2])
                        return str(answer)
                elif memory[1] == "/":
                        print("division")
                        print(op)
                        answer = int(memory[0]) // int(memory[2])
                        return str(answer)

# get the operation type (multiply, divide, add, subtract)
def operation(op):
        global memory
        global operator

        if op == "=":
                if len(memory) == 2:
                        if operator == "":
                                operator = memory[0]
                                memory.clear()
                                textInput.set(operator)
                        else:
                                memory.append(operator)
                                operator = calculate()
                                memory.clear()
                                textInput.set(operator)

        elif len(memory) == 2:
                memory.append(operator)
                operator = calculate()
                memory.clear()
                textInput.set(operator)
        else:
                memory.append(operator)
                memory.append(op)
                operator=""
                textInput.set(operator)

# square the current number
def square():
        global operator
        global memory
        if len(memory) == 0 and operator == "":
                print("not possible")
        elif operator != "":
                answer = int(operator)
                answer = answer * answer
                operator = str(answer)
                textInput.set(operator)

# check the values in memory
def printOperands():
        print(memory)

# initialize GUI
calculator = Tk()
calculator.title("Calculator")
textInput = StringVar()

# Space for displaying current number
txtDisplay = Entry(calculator, font=('arial', 20), textvariable=textInput, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

# all buttons rendered below with linked lambda functions
btnSquared = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="x^2", command=lambda:square()).grid(row=1, column=0)
btnClear = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="C", command=btnClear).grid(row=1, column=1)
btnAllClear = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="AC", command=btnClearAll).grid(row=1, column=2)
btnDivide = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="/", command=lambda:operation("/")).grid(row=1, column=3)

btn7 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="7", command=lambda:btnClick(7, operator)).grid(row=2, column=0)
btn8 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="8", command=lambda:btnClick(8, operator)).grid(row=2, column=1)
btn9 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="9", command=lambda:btnClick(9, operator)).grid(row=2, column=2)
btnMultiplication = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="*", command=lambda:operation("*")).grid(row=2, column=3)

btn4 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="4", command=lambda:btnClick(4, operator)).grid(row=3, column=0)
btn5 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="5", command=lambda:btnClick(5, operator)).grid(row=3, column=1)
btn6 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="6", command=lambda:btnClick(6, operator)).grid(row=3, column=2)
btnSubtraction = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="-", command=lambda:operation("-")).grid(row=3, column=3)

btn1 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="1", command=lambda:btnClick(1, operator)).grid(row=4, column=0)
btn2 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="2", command=lambda:btnClick(2, operator)).grid(row=4, column=1)
btn3 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="3", command=lambda:btnClick(3, operator)).grid(row=4, column=2)
btnAddition = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="+", command=lambda:operation("+")).grid(row=4, column=3)

btnPlusMinus = Button(calculator, padx=16, fg="black", font=('arial', 20),text="+/-", command=lambda:signSwap(operator)).grid(row=5, column=0)
btn0 = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="0", command=lambda:btnClick(0, operator)).grid(row=5, column=1)
btnDecimal = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="chk", command=lambda:printOperands()).grid(row=5, column=2)
btnEquals = Button(calculator, padx=16, fg="black", font=('arial', 20, 'bold'),text="=", command=lambda:operation("=")).grid(row=5, column=3)

# keep the calculator GUI open until closed
calculator.mainloop()

