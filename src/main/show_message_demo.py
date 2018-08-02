import tkinter

import tkinter.messagebox



def showMsg(): #提示框
    
    tkinter.messagebox.showinfo('提示', '123')
    tkinter.messagebox.showwarning('警告', '234')
    tkinter.messagebox.showerror('错误', '345')



if __name__ == "__main__":
    showMsg()
    print("+++++++")
