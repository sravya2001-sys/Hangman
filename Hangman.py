from tkinter import *
from PIL import Image, ImageTk
from string import ascii_uppercase
import random
from tkinter import messagebox
#Let's create our project window as below
run=True
while run:
        root=Tk()#creating object to tkinter class (creating a window)
        root.geometry("1050x550")
        root.title('Hangman')
       # root.configure(bg='#ffffff')
        bg=ImageTk.PhotoImage(Image.open('BG.png'))
        a=Label(root,image=bg)
        a.place(x=0,y=0)
        la=Label(root)
        la.place(x=820,y=90)
        l=['apple','banana','orange','watermelon','cherry','strawberry','hangman','invert','python','tkinter','java']
        himg=['1.png','2.png','3.png','4.png','5.png','6.png','7.png']
        l1=[]
        count=0
        i=0
        def close():
                global run
                res=messagebox.askyesno("Hangman","Do you want to continue")
                if res:
                    run=True
                    root.destroy()
                else:
                    run=False
                    root.destroy()
        exited=ImageTk.PhotoImage(Image.open('exit.png'))
        exitbtn=Button(root,image=exited,command=close,bg='#55CFFE')
        exitbtn.place(x=870,y=0)
    
        def checkwin(s):
                global run
                global la
                if s==len(word):
                        wonimg=ImageTk.PhotoImage(Image.open('WIN.png'))
                        la.configure(image=wonimg)
                        la.image=wonimg
                        messagebox.showinfo("Hangman","YOU WON")
                        print(s)
                        res=messagebox.askyesno("Hangman","Do you want to play again???")
                        print(res)
                        if res:
                            run=True
                            count=0
                            root.destroy()
                        else:
                                run=False
                                root.destroy()
        def Hangman():
            global i
            global img
            global la
            if i==0:
                        img=ImageTk.PhotoImage(Image.open(himg[0]))
                        la=Label(root,image=img)
                        la.place(x=820,y=90)
                        i+=1
            elif i!=0 and i<7:
                
                img=ImageTk.PhotoImage(Image.open(himg[i]))
                la.configure(image=img)
                la.image=img
                i+=1
                                

                            
        def play(letter):
            global chances
            global run
            global count
            if chances>0:
                l2.config(text="Remaining chances :"+str(chances))
                chances-=1
                if letter in word:
                        for i in range(0,len(word)):
                            if word[i]==letter:
                                l1[i].config(text=letter)
                                count+=1
                                checkwin(count)
                else:
                        Hangman()
            elif chances==0:
                loseimg=ImageTk.PhotoImage(Image.open('LOSE.png'))
                la.configure(image=loseimg)
                la.image=loseimg
                messagebox.showinfo("Hangman","Chances over")
                res=messagebox.askyesno("Hangman","Do you want to play again???")
                if res:
                    print(res)
                    for i in range(0,len(word)):
                        l1[i].config(text=" _ ")
                    run=True
                    root.destroy()
                else:
                        run=False
                        root.destroy()
        l2=Label(root,text=" ",bg="#7EAE26",fg='#ffffff',font=("arial",30))
        l2.place(x=0,y=500)
        def game():
            global word
            global chances
            global run
            word=random.choice(l)
            chances=len(word)
            print(word)
            x=60
            for i in range(0,len(word)):
                x+=60
                l1.append(Label(root,text=" _ ",bg='#55CFFE',fg='#ffffff',font=("arial",30)))
                l1[i].place(x=x,y='150')
                
            
        img1=ImageTk.PhotoImage(Image.open('A.png'))
        btn1=Button(root,image=img1,bg="#B0E9FD",bd=0,command=lambda:play('a'))
        btn1.place(x=10,y=300)
        img2=ImageTk.PhotoImage(Image.open('B.png'))
        btn2=Button(root,image=img2,bg="#B0E9FD",bd=0,command=lambda:play('b'))
        btn2.place(x=70,y=300)
        img3=ImageTk.PhotoImage(Image.open('C.png'))
        btn3=Button(root,image=img3,bg="#B0E9FD",bd=0,command=lambda:play('c'))
        btn3.place(x=130,y=300)
        img4=ImageTk.PhotoImage(Image.open('D.png'))
        btn4=Button(root,image=img4,bg="#B0E9FD",bd=0,command=lambda:play('d'))
        btn4.place(x=190,y=300)
        img5=ImageTk.PhotoImage(Image.open('E.png'))
        btn5=Button(root,image=img5,bg="#B0E9FD",bd=0,command=lambda:play('e'))
        btn5.place(x=250,y=300)
        img6=ImageTk.PhotoImage(Image.open('F.png'))
        btn6=Button(root,image=img6,bg="#B0E9FD",bd=0,command=lambda:play('f'))
        btn6.place(x=310,y=300)
        img7=ImageTk.PhotoImage(Image.open('G.png'))
        btn7=Button(root,image=img7,bg="#B0E9FD",bd=0,command=lambda:play('g'))
        btn7.place(x=370,y=300)
        img8=ImageTk.PhotoImage(Image.open('H.png'))
        btn8=Button(root,image=img8,bg="#B0E9FD",bd=0,command=lambda:play('h'))
        btn8.place(x=430,y=300)
        img9=ImageTk.PhotoImage(Image.open('I.png'))
        btn9=Button(root,image=img9,bg="#B0E9FD",bd=0,command=lambda:play('i'))
        btn9.place(x=500,y=300)
        img10=ImageTk.PhotoImage(Image.open('J.png'))
        btn10=Button(root,image=img10,bg="#B0E9FD",bd=0,command=lambda:play('j'))
        btn10.place(x=560,y=300)
        img11=ImageTk.PhotoImage(Image.open('K.png'))
        btn11=Button(root,image=img11,bg="#B0E9FD",bd=0,command=lambda:play('k'))
        btn11.place(x=620,y=300)
        img12=ImageTk.PhotoImage(Image.open('L.png'))
        btn12=Button(root,image=img12,bg="#B0E9FD",bd=0,command=lambda:play('l'))
        btn12.place(x=680,y=300)
        img13=ImageTk.PhotoImage(Image.open('M.png'))
        btn13=Button(root,image=img13,bg="#B0E9FD",bd=0,command=lambda:play('m'))
        btn13.place(x=740,y=300)
        img14=ImageTk.PhotoImage(Image.open('N.png'))
        btn14=Button(root,image=img14,bg="#B0E9FD",bd=0,command=lambda:play('n'))
        btn14.place(x=800,y=300)
        img15=ImageTk.PhotoImage(Image.open('O.png'))
        btn15=Button(root,image=img15,bg="#B0E9FD",bd=0,command=lambda:play('o'))
        btn15.place(x=70,y=360)
        img16=ImageTk.PhotoImage(Image.open('P.png'))
        btn16=Button(root,image=img16,bg="#B0E9FD",bd=0,command=lambda:play('p'))
        btn16.place(x=130,y=360)
        img17=ImageTk.PhotoImage(Image.open('Q.png'))
        btn17=Button(root,image=img17,bg="#B0E9FD",bd=0,command=lambda:play('q'))
        btn17.place(x=190,y=360)
        img18=ImageTk.PhotoImage(Image.open('R.png'))
        btn18=Button(root,image=img18,bg="#B0E9FD",bd=0,command=lambda:play('r'))
        btn18.place(x=250,y=360)
        img19=ImageTk.PhotoImage(Image.open('S.png'))
        btn19=Button(root,image=img19,bg="#B0E9FD",bd=0,command=lambda:play('s'))
        btn19.place(x=310,y=360)
        img20=ImageTk.PhotoImage(Image.open('T.png'))
        btn20=Button(root,image=img20,bg="#B0E9FD",bd=0,command=lambda:play('t'))
        btn20.place(x=370,y=360)
        img21=ImageTk.PhotoImage(Image.open('U.png'))
        btn21=Button(root,image=img21,bg="#B0E9FD",bd=0,command=lambda:play('u'))
        btn21.place(x=430,y=360)
        img22=ImageTk.PhotoImage(Image.open('V.png'))
        btn22=Button(root,image=img22,bg="#B0E9FD",bd=0,command=lambda:play('v'))
        btn22.place(x=490,y=360)
        img23=ImageTk.PhotoImage(Image.open('W.png'))
        btn23=Button(root,image=img23,bg="#B0E9FD",bd=0,command=lambda:play('w'))
        btn23.place(x=550,y=360)
        img24=ImageTk.PhotoImage(Image.open('X.png'))
        btn24=Button(root,image=img24,bg="#B0E9FD",bd=0,command=lambda:play('x'))
        btn24.place(x=610,y=360)
        img25=ImageTk.PhotoImage(Image.open('Y.png'))
        btn25=Button(root,image=img25,bg="#B0E9FD",bd=0,command=lambda:play('y'))
        btn25.place(x=670,y=360)
        img26=ImageTk.PhotoImage(Image.open('Z.png'))
        btn26=Button(root,image=img26,bg="#B0E9FD",bd=0,command=lambda:play('z'))
        btn26.place(x=730,y=360)


        game()
        root.mainloop()


