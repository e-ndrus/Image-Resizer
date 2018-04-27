import PIL.Image
import os, sys
import tkinter.filedialog
from tkinter import ttk
import configparser
config = configparser.ConfigParser()
config.read("config.ini")


from tkinter import *

class Application(Frame):
    
    def __init__(self, master=None):
        self.root = tkinter.Tk()
        self.root.geometry("600x300")
        self.root.title("Image Resizer")
        self.orig_dir = os.getcwd()
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    
    def selectFolder(self):
        self.orig_dir = tkinter.filedialog.askdirectory(initialdir="/",  title='Please select a directory with images to resize')
        directory = str(self.orig_dir)

    
    def onEntry(self):
        if self.entry.get() == "":
            self.slabel.config(text="")
            self.slabel.pack()
        else:
            self.slabel.config(text=self.entry.get())
            self.slabel.pack()

    def createWidgets(self):
        self.namelabel = Label(self, text="How to rename the images?")
        self.namelabel.pack()
        self.entry = Entry(self)
        self.entry.pack()
        print(self.entry.get())
        self.root.bind('<Return>', self.parse)
        self.slabel = Label(self, text="")
        self.slabel.pack()
        self.RUN = Button(self)
        self.RUN["text"] = "RUN SCRIPT"
        self.RUN["fg"]   = "red"
        self.RUN["command"] =  self.actions
        self.RUN.pack({"side": "left"})

        self.folderSelector = Button(self)
        self.folderSelector["text"] = "Select Folder"
        self.folderSelector["command"] = self.selectFolder
        self.folderSelector.pack({"side": "left"})   
        self.text = tkinter.Text(self.root)
        self.text.configure(state='normal')
        self.text.insert('end', "")
        self.text.configure(state='disabled')
        self.text.pack()
        
    def parse(self, event):
        self.slabel.config(text=self.entry.get())
        self.slabel.pack()
        
    def actions(self):
        if __name__=="__main__":
            resize_dir = os.getcwd()
            output_dir = resize_dir+os.sep+"resized"
            if not os.path.exists(output_dir):
                os.mkdir(output_dir)
            i = 1    
            for file in os.listdir(self.orig_dir):
                self.resizeImage(str(self.entry.get()), i, file, self.orig_dir,output_dir=output_dir)
                i += 1
            
        
    def resizeImage(self, howToName, i, infile, dir, output_dir="", size=(int(config.get('imSize', 'width')),int(config.get('imSize', 'height')))):
        if self.entry.get() != "":
            outfile = str(self.entry.get())+' '+str(i)
        else: outfile = os.path.splitext(infile)[0]+"_resized"
        extension = os.path.splitext(infile)[1]
    
        if extension.lower()!= ".jpg":
            return
    
        if infile != outfile:
            try :
                print(dir+os.sep+infile)
                im = PIL.Image.open(dir+os.sep+infile)
                im.thumbnail(size, PIL.Image.ANTIALIAS)
                im.save(output_dir+os.sep+outfile+extension,"JPEG")
                self.text.configure(state='normal')
                self.text.insert('end', "\n"+str(infile)+" resized successfully.")
                self.text.configure(state='disabled')
                self.text.pack()

            except IOError:
                print ("cannot reduce image for ", infile)

app = Application()

app.mainloop()