

from re import X
import tkinter as tk
import random


#hit var
x = 0

class player :
    def __init__(self , username , coin = 0 ) :
        self.userN = username
        self.coin = coin
    def  randcoin(self) :
        m = random.choice([5,10,15,20])
        return m
    def moni_moni(self):
        self.coin += self.randcoin()


    def mainw(self) :

        root = tk.Tk()
        root.geometry('800x600')
        bgph = tk.PhotoImage(file='background.png')
        bg = tk.Label(root , image= bgph)
        bg.pack()
        
        coinIM = tk.Label(root )
        coinIM.place(x= 1 , y = 1)
        coinL = tk.Label(root , text = 'Coins:')
        coinL.place(x= 2, y=5)
        #-----------------
        coinvar = tk.Label(root, text = self.coin)
        
        f1= tk.PhotoImage(file='killframe1.png')
        f2 =tk.PhotoImage(file='killframe2.png')
        f3 = tk.PhotoImage(file='killframe3.png')
        frame1= tk.Label(root, image= f1 , relief = 'flat')
        frame2= tk.Label(root, image=f2)
        frame3 = tk.Label(root,image=f3)
        hpi1 = tk.PhotoImage(file='hp1.png')
        hpi2 = tk.PhotoImage(file='hp2.png')
        hpi3 = tk.PhotoImage(file='hp3.png')
        hpi4 = tk.PhotoImage(file='hp4.png')
        hpi5 = tk.PhotoImage(file='hp5.png')
        hpi6 = tk.PhotoImage(file='hp6.png')
        hp1 = tk.Label(root ,image = hpi1 )
        hp2 = tk.Label(root ,image = hpi2 )
        hp3 = tk.Label(root ,image = hpi3 )
        hp4 = tk.Label(root ,image = hpi4 )
        hp5 = tk.Label(root ,image = hpi5 )
        hp6 = tk.Label(root ,image = hpi6 )
        frame1.place(x=340 , y=150)
        hp1.place(x=300 , y=1)


        def kill():
            self.moni_moni()
            coinvar.config(text= self.coin)
            coinvar.place(x=45 , y =5)

            frame2.place(x=340 , y= 150)
        def hit() :
            global x
            x = x +1
            if x == 1 :
                hp1.place_forget()
                hp2.place(x= 300 , y= 1)
            elif x == 2 :
                hp2 .place_forget()
                hp3.place(x=300 , y=1)
            elif x == 3 : 
                hp3.place_forget()
                hp4.place(x=300 , y=1)
            elif x== 4 : 
                hp4.place_forget() 
                hp5.place(x=300 , y=1)
            elif x == 5 :
                hp5.place_forget()
                hp6.place(x=300 , y=1)
                kill()

            
        def respawn():
            global x
            x = 0
            hp6.place_forget()
            hp1.place(x=300 , y=1)
            frame2.place_forget()
            frame1.place(x= 340 , y= 150)

            
        B1 = tk.Button(root , text= 'Kill !!' , width= 10 , height= 1 , command=  hit)
        B1.place(x=363 , y= 500)
        B2 = tk.Button(root , text= 'more mob', command= respawn)
        B2.place(x= 370 , y=550 )
        root.mainloop()

p1= player('peepee')
p1.mainw()