from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('ToDo List!')
root.geometry("400x400")

# Define our Font

my_font = Font(
    family="Brush Script MT",
    size=20,
    weight="bold")

# Create frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Crate listbox
my_list = Listbox(my_frame,
        font=my_font,
        width=25,
        height=5,
        bg="SystemButtonFace",
        bd=0,
        fg="#464646",
        highlightthickness=0,
        selectbackground="#a6a6a6",
        activestyle="none"
                  
                  )

    
my_list.pack(side=LEFT,fill=BOTH)


# Create dummy list
stuff = ["Walk The Dog","Buy Groceries","Take A Nap"]
# Add dummy list to list box
for itam in stuff:
    my_list.insert(END, itam)

#Create scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

#Add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#Create entry box to add itams to the list
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

#Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#Functions
def delete_itam():
    my_list.delete(ANCHOR)

def add_itam():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)







#Add some buttons
delete_button = Button(button_frame, text="Delete Itam", command=delete_itam)
add_button = Button(button_frame, text="Add Itam", command=add_itam)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)








root.mainloop()
