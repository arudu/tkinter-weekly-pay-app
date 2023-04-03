import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="What state do you live in?")
label.pack()

state_entry = tk.Entry(root, width=10)
state_entry.pack()

label = tk.Label(root, text="All answers should be in number format ex. 200 or 200.00")
label.pack()

label = tk.Label(root, text="What's your income for monday?")
label.pack()

num1_entry = tk.Entry(root, width=20)
num1_entry.pack()

label = tk.Label(root, text="What's your income for tuesday?")
label.pack()

num2_entry = tk.Entry(root, width=20)
num2_entry.pack()

label = tk.Label(root, text="What's your income for wednesday?")
label.pack()

num3_entry = tk.Entry(root, width=20)
num3_entry.pack()

label = tk.Label(root, text="What's your income for thursday?")
label.pack()

num4_entry = tk.Entry(root, width=20)
num4_entry.pack()

label = tk.Label(root, text="What's your income for friday?")
label.pack()

num5_entry = tk.Entry(root, width=20)
num5_entry.pack()

label = tk.Label(root, text="What's your income for saturday?")
label.pack()

num6_entry = tk.Entry(root, width=20)
num6_entry.pack()

label = tk.Label(root, text="What's your income for sunday?")
label.pack()

num7_entry = tk.Entry(root, width=20)
num7_entry.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

tax_result_label = tk.Label(root, text="Tax amount: ")
tax_result_label.pack()

remainder_result_label = tk.Label(root, text="Weekly pay amount: ")
remainder_result_label.pack()

def add_numbers():
	global result
	num1 = float(num1_entry.get())
	num2 = float(num2_entry.get())
	num3 = float(num3_entry.get())
	num4 = float(num4_entry.get())
	num5 = float(num5_entry.get())
	num6 = float(num6_entry.get())
	num7 = float(num7_entry.get())
	result = round( num1 + num2 + num3 + num4 + num5 + num6 + num7, 2)
	result_label.config(text="Result: $" + str(result))

def tax():
	global result
	global tax_result
	tax_result = round(result * 0.06, 2)
	tax_result_label.config(text="Tax Amount: $" + str(tax_result))

def remainder():
	global result
	global tax_result
	remainder_result = round(result - tax_result, 2)
	remainder_result_label.config(text="After taxes: $" +str(remainder_result))

button = tk.Button(root, text="Get total", command=add_numbers)
button.pack()

tax_button = tk.Button(root, text="Get tax amount", command=tax)
tax_button.pack()

remainder_button = tk.Button(root, text="Weekly pay after taxes", command=remainder)
remainder_button.pack()

root.mainloop()
