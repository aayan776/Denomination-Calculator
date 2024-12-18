from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Denominator calculator")
root.configure(bg = "light blue")
root.geometry("600x400")
#Image
upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
#Labels
label1 = Label(root, image = image, bg = "light blue")
label1.place(x = 180, y = 20)
label2 = Label(root, text = "Hey user! Welcome to Denomination calculator.", bg = "light blue")
label2.place(relx = 0.5, y = 340, anchor = CENTER)
def msg():
    Msgbox = messagebox.showinfo("Alert!", "Do you want to calculate denomination?")
    if Msgbox == "ok":
        topwin()
button2 = Button(root, text = "Let's get started!", command = msg, bg = "brown", fg = "white")
button2.place(x = 260, y = 360)
def topwin():
    top = Toplevel()
    top.title("Denominator Calculator")
    top.configure(bg = "lightblue")
    top.geometry("600x350 + 50 + 50")
    label3 = Label(top, text = "Enter total amount", bg = "light blue")
    entry1 = Entry(top)
    label4 = Label(top, text = "Here are the number of notes for each denomination: ", bg = "light blue")
    #Label
    l1 = Label(top, text = "1000", bg = "light grey")
    l2 = Label(top, text="500", bg="light grey")
    l3 = Label(top, text="200", bg="light grey")
    l4 = Label(top, text="100", bg="light grey")
    l5 = Label(top, text="50", bg="light grey")
    l6 = Label(top, text="10", bg="light grey")
    #Entry
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)
    def calculate():
        try:
            global amount
            amount = int(entry1.get())
            note_1000 = amount // 1000
            amount %= 1000
            note_500 = amount // 500
            amount %= 500
            note_200 = amount // 200
            amount %= 200
            note_100 = amount // 100
            amount %= 100
            note_50 = amount // 50
            amount %= 50
            note_10 = amount // 10
            amount %= 10
            #Delete
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)
            t5.delete(0, END)
            t6.delete(0, END)
            #Insert
            t1.insert(END, str(note_1000))
            t2.insert(END, str(note_500))
            t3.insert(END, str(note_200))
            t4.insert(END, str(note_100))
            t5.insert(END, str(note_50))
            t6.insert(END, str(note_10))
        except ValueError:
            messagebox.showerror("Error!", "Please enter a valid number.")
    button = Button(top, text = "Calculate", command = calculate, bg = "brown", fg = "white")
    #Centering Widgets
    label1.place(x = 230, y = 50)
    entry1.place(x = 200, y = 80)
    button.place(x = 240, y = 120)
    label4.place(x = 140, y = 170)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()
root.mainloop()