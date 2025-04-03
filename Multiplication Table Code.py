#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def multi_gen():
        # multiplication table Generater Software
    # welcomew user
    print("welcome to  multiplication  software")
    user_input=int(input("please enter the  number"))
    
    # num=0:
    # while num<
    
    for i in range(1,11):
        print(user_input,"x",i,"=",user_input*i)
        
    
    # take a number as input
    # generated multiplication table



# import library
import customtkinter as ctk
# create window
window=ctk.CTk()
# create tittle change
window.title('python practice software')

# window size
window.geometry("300x300")
# add text label
ctk.CTkLabel(window,text="multiplictaion table generater",font=("Arial", 16, "bold")).place(x=40,y=60)
# add  button
ctk.CTkButton(window,text="start generating",command=multi_gen).place(x=70,y=150)

# show window
window.mainloop()
#function = is a set of instruction in python in one word


# In[ ]:




