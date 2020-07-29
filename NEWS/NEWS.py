from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import tkinter.messagebox as tmb


def every_100(text):
    final_text = ""
    for i in  range(0,len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text +="\n"
    return final_text

root = Tk()


scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)


root.title("Bollywood  News")
root.geometry("800x600")

texts= []
photos= []
for i in range(0,2):
    with open(f"{i+1}.txt") as f:
        text =  f.read()
        texts.append(every_100(text))
    image = Image.open(f"{i+1}.jpg")

    #TODO:resize the image
    image=image.resize((205,205),Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f1 = Frame(root,width=800,height=70)
Label(f1,text="Bollywood News",font="lucida 33 bold").pack()
Label(f1,text=f"Date : {datetime.now().date()}",font="lucida 15 bold").pack()
f1.pack()


f2 =  Frame(root,width=400,height=200)
Label(f2,text=texts[0],font="lucida 10 italic",padx=22,pady=22).pack(side="left")
Label(f2,image=photos[0],anchor="e").pack()

f3 =  Frame(root,width=400,height=200)
Label(f3,text=texts[1],font="lucida 10 italic",padx=33,pady=22).pack(side="right")
Label(f3,image=photos[1],anchor="e").pack()

f2.pack(anchor="w")
f3.pack(anchor="w")

Label(root, text='Subscribe to our Channel', font=("comicsans", 15, "bold")).pack()

form_frame = Frame(root)
form_frame.pack()

userName = StringVar()
userEmail = StringVar()
userPhone = StringVar()

Label(form_frame, text='Name: ', padx=3, pady=3).grid(row=1, column=1)
Label(form_frame, text='Email: ', padx=3, pady=3).grid(row=2, column=1)

Entry(form_frame, textvariable=userName).grid(row=1, column=2)
Entry(form_frame, textvariable=userEmail).grid(row=2, column=2)

Button(form_frame, text='Subscribe', command=lambda: subscribeUser()).grid(row=4, column=1, padx=10, pady=10)

def subscribeUser():
    with open('NewsBlogSubscribers.txt', 'a') as f:
        f.write(f"{userName.get(), userEmail.get()}\n")

def stars():
    tmb.showinfo("Succesfull.","Thank you for submitting stars for our channel")



def rateUs():
    a = tmb.askokcancel("Rate", "Would you like to rate us now?")
    print(a)
    if a==True:
        tmb.showinfo("Rated", "Thank you for taking your time to rate us.")
    else:
        tmb.showinfo("Not Rated", "We are looking forward to serve in much better way.\nThank You!")

def help():
    tmb.showinfo("Help","We are glad that you asked for help.\nWe will soon resolve your issue. Kindly wait for some time.\nThank You")

def error():
    tmb.showerror("Error", "This is an error message.")


myMenuBar = Menu(root)

m1 = Menu(myMenuBar, tearoff=0)
m1.add_command(label='Rate Us', command=rateUs)
m1.add_command(label='Help', command=help)
m1.add_command(label='Error', command=error)

myMenuBar.add_cascade(label='Show', menu=m1)
myMenuBar.add_command(label='Exit', command=quit)
root.config(menu=myMenuBar)

myslider = Scale(root, from_ = 0, to = 10, orient = HORIZONTAL)
Label(root,text="STAR US!!").pack()
myslider.pack()
myslider.set(1)
Button(root, text="Submit",command=stars).pack()


root.mainloop()
