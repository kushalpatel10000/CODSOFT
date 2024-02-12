#!/usr/bin/env python
# coding: utf-8

# In[7]:


#applocation to develop todo list

#import Tkinter library

from tkinter import *
import tkinter.messagebox


# In[8]:


#creating application window
window=Tk()
window.title('To-do list Application:1.0')


# In[9]:


#frame widget to hold the listbox and the scrollbar
frame_task=Frame(window)
frame_task.pack()


# In[10]:


#using Listbox to hold items in a listbox

listbox_task=Listbox(frame_task,bg="black",fg="white",height=15,width=50,font="Times")
listbox_task.pack(side=tkinter.LEFT)


# In[11]:


#using Scrollbar in case the total list exceeds the size of the given window
scrollbar_task=Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)


# In[16]:


#Now we will using Button (Add, Update{mark} and delete)

add_button=Button(window,text="Add Task",width=50,command=addtask)
add_button.pack(pady=3)

delete_button=Button(window,text="Delete Task",width=50,command=deletetask)
delete_button.pack(pady=3)

update_button=Button(window,text="Mark Task as Completed",width=50,command=markcompletetask)
update_button.pack(pady=3)

window.mainloop()


# In[13]:


#now we will define functions addtask, deletetask, markcompletetask

def addtask():
    #A new window will be pop-up to take input from us
    input_text=""
    def add():
        input_text=entery_task.get(1.0,"end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="warning!",message="Please enter some task to do")
        else:
            listbox_task.insert(END,input_text)
            root1.destroy()
    root1=Tk()
    root1.title("Add Task")
    entery_task=Text(root1,width=40,height=4)
    entery_task.pack()
    button_temp=Button(root1,text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()


# In[14]:


#now we will define function deletetask()

def deletetask():
    #select item and then delete that task
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])


# In[15]:


#define function markcompletetask()

def markcompletetask():
    marked=listbox_task.curselection()
    temp=marked[0]
    temp_marked=listbox_task.get(marked)
    temp_marked=temp_marked+ " ✓"
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)


# In[ ]:





# In[ ]:




