#importing all the modules used in the code
from PlantObjects import Plant as P
from PlantObjects import UserInputs as UI
import tkinter as tk
from PIL import Image, ImageTk

class PlantApp(tk.Tk):
    """ PlantApp initialises a TkInstance
    The show_frame method unpacks all the frames except for the one that needs to be shown """
    def __init__(self,expandchoice,flag=False,master=None):
        super().__init__()

        self.title('Growing Oxygen')
        self.resizable(True, True)
        self.expandedChoice=expandchoice

        # creating a container
        


        # Create an overall title and pack it into the top of the container
        if flag:
          print(flag)
          container = tk.Frame(self)
          container.pack()
          title_label = tk.Label(container,
                                text="Growing Oxygen",
                                bg="green", fg="white",
                                font=("Arial", 10))
          title_label.pack()

        # Initialise frames to an empty dictionary
        self.frames = {}

        # Set up frames for each of the page classes
        pages = (Page1, Page2, PlantContainer,PlantExpand)
        for F in pages:
            frame = F(self)
            self.frames[F] = frame
        print(self.frames)
        self.show_frame(Page1)

    # Function to show the desired game class, which is a subclass of tk.Frame
    def show_frame(self, current_frame):
        print("show_frame")
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[current_frame].pack(fill=tk.X)
    def clear_frame(self):
      for widgets in self.winfo_children():
        widgets.destroy()


class Page1(tk.Frame):
    def __init__(self, master=None):
      
        super().__init__(master)
        self.master = master
        self.screenwidth=self.master.winfo_screenwidth()
        self.screenheight=self.master.winfo_screenheight()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.plant_reccomendation_choice = tk.Button(self, text="plant reccomendations",
                                          command=lambda:self.master.show_frame(Page2))
        self.plant_reccomendation_choice.grid (row=2,column=4,padx=10, pady=10)
    


class Page2(tk.Frame):
  def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.screenwidth=self.master.winfo_screenwidth()
        self.screenheight=self.master.winfo_screenheight()
        self.pack()
        self.plant_reccomendation()
        self.master.config(bg='green')
  
  def plant_reccomendation(self):
      #buttons for setting temperature
      self.templabel=tk.Label(self,text="What is the temperature \n of the location?",bg="green",fg="white")
      self.templabel.grid(row=2,column=1)
      self.tempbutton1 = tk.Button(self, text="18°C",bg='#826644',
                                          command=lambda:david.settemp(18))
      self.tempbutton1.grid(row=2,column=2,padx=1, pady=3)
      self.tempbutton2 = tk.Button(self, text="20°C",bg='#826644',
                                          command=lambda:david.settemp(20))
      self.tempbutton2.grid(row=2,column=3,padx=1, pady=3)
      self.tempbutton3 = tk.Button(self, text="22°C",bg='#826644',
                                          command=lambda:david.settemp(22))
      self.tempbutton3.grid(row=2,column=4,padx=1, pady=3)
      self.tempbutton4 = tk.Button(self, text="24°C",bg='#826644',
                                          command=lambda:david.settemp(24))
      self.tempbutton4.grid(row=2,column=5,padx=1, pady=3)
      self.tempbutton5 = tk.Button(self, text="26°C",bg='#826644',
                                          command=lambda:david.settemp(26))
      self.tempbutton5.grid(row=2,column=6,padx=1, pady=3)
      #slider for ease of care

      self.easelabel=tk.Label(self,text="How easy do you want \n the plant care to be?",bg="green",fg="white")
      self.easelabel.grid(row=3,column=1)
      self.easeslider=tk.Scale(self,from_=0,to=10,length=450,tickinterval=5,orient='horizontal',bg="#67AB9F",
                                          command=  self.setease)
      self.easeslider.grid(row=3,column=2,columnspan = 5)
      #buttons for size
      self.sizebutton1=tk.Button(self,text="Small",bg="#67AB9F",
                                  command=lambda : david.setsize(0))
      self.sizebutton1.grid(row=3,column = 8,padx=2, pady=3 )
      self.sizebutton2=tk.Button(self,text="Medium",bg="#67AB9F",
                                  command=lambda : david.setsize(1))
      self.sizebutton2.grid(row=3,column = 9,padx=2, pady=3 )
      self.sizebutton3=tk.Button(self,text="Big",bg="#67AB9F",
                                  command=lambda : david.setsize(2))
      self.sizebutton3.grid(row=4,column = 8,padx=2, pady=3 )
      self.sizebutton3=tk.Button(self,text="Huge",bg="#67AB9F",
                                  command=lambda : david.setsize(3))
      
      self.sizebutton3.grid(row=4,column = 9,padx=2, pady=3 )
      self.sizelabel=tk.Label(self,text='how large do you want \nthe plant to be?',bg='green',fg='white')
      self.sizelabel.grid(row=2,column=8,columnspan=2)
      #buttons for brightness
      self.brightlabel=tk.Label(self,text='what is the brightness\n of the locaion?',bg='green',fg='white')
      self.brightlabel.grid(row=4,column=1)
      self.brightbutton1=tk.Button(self,text="Full\n Sun",bg='#D3AA32',
                                  command=lambda:david.setbright(5))
      self.brightbutton1.grid(row=4,column=2)

      self.brightbutton2=tk.Button(self,text="Bright\n Sun",bg='#D3AA32',
                                  command=lambda:david.setbright(4))
      self.brightbutton2.grid(row=4,column=3)
      
      self.brightbutton3=tk.Button(self,text="Semi\n Sun",bg='#D3AA32',
                                  command=lambda:david.setbright(3))
      self.brightbutton3.grid(row=4,column=4)      

      self.brightbutton4=tk.Button(self,text="Little\n Sun",bg='#D3AA32',
                                  command=lambda:david.setbright(2))
      self.brightbutton4.grid(row=4,column=5)

      self.brightbutton5=tk.Button(self,text="No\n Sun",bg='#D3AA32',
                                  command=lambda: david.setbright(1))
      self.brightbutton5.grid(row=4,column=6)
      #done button for next Page
      self.DoneButton=tk.Button(self,text='Done',bg='green',fg='yellow',width=95,
                                command = lambda : self.attributesdone())
      self.DoneButton.grid(row=5,column=1,columnspan=9)

  def setease(self,val):
    david.setease(val)

  def attributesdone(self):
    print('done',david.temperature,david.ease,david.size,david.brightness)
    self.master.show_frame(PlantContainer)

class PlantContainer(tk.Frame):

  def __init__(self, master):
    super().__init__(master)
    self.master = master

    self.frames = [ PlantBox(self, plant) for plant in Plantlist]
    for pb in self.frames:
      pb.pack(side=tk.LEFT, padx=5, pady=5)



class PlantBox(tk.Frame):
  

  def __init__(self,master, plant):
    super().__init__(master)
    self.master = master  
    self.name=plant.name
    with Image.open(plant.image) as im:
      im_resized = im.resize((100, 300))
      im_resized.show()
      self.image=ImageTk.PhotoImage(im_resized)
      #self.image=tk.PhotoImage(file=Plantlist[val].image)
    self.imagelabel=tk.Label(self,image=self.image)
    self.imagelabel.pack()
    self.boxtitle=tk.Label(self,text=self.name,fg='yellow',font='bold')
    self.boxtitle.pack()
    self.expandbutton=tk.Button(self,text='expand',bg='cyan',command=lambda:self.expand(plant))
    self.expandbutton.pack()
  def expand(self,pl):

    print(f'expand {self.name}')
    self.master.master.clear_frame()
    self.master.master.__init__(pl)
    
    self.master.master.show_frame(PlantExpand)

class PlantExpand(tk.Frame):
  
  def __init__(self,master=None):

    super().__init__(master)
    p=self.master.expandedChoice
    print ('hiiiiiiiiiii',p.name)
    self.master = master  
    self.name=p.name
    with Image.open(p.image) as im:
      im_resized = im.resize((100, 300))
      im_resized.show()
      self.image=ImageTk.PhotoImage(im_resized)
    self.imagelabel=tk.Label(self,image=self.image)
    self.imagelabel.pack(side=tk.LEFT)
    self.textbox=tk.Label(self,bg='#D3AA32',text=
    f'''Temperature range: {p.mintemp} - {p.maxtemp} \n 
    Brightness level: {p.brightness}
    Size: {p.size}
    Ease of care: {p.ease}''',font=(44))
    self.textboxtitle=tk.Label(self,text=p.name,font='bold')
    self.textboxtitle.pack(side=tk.TOP)
    self.textbox.pack(side=tk.LEFT)
    self.minimisebutton=tk.Button(self,text='mimimise',bg='cyan',command=lambda:self.master.show_frame(PlantContainer))
    self.minimisebutton.pack(side=tk.TOP)

rec_list=[0,1]
Plantlist=[
  P('Devils Ivy',24,18,3,2,9,'Alevelproject-GrowingOxygen-mk1\image folder/devils ivy.PNG'),
  P ('Peace Lily',26,20,4,1,7,'Alevelproject-GrowingOxygen-mk1\image folder/Peace Lily.png'),
  P('Snake Plant',24,18,4,3,4,'Alevelproject-GrowingOxygen-mk1\image folder/snake plant.png')
]




david=UI(None,None,None,None)
print (david.temperature)
app = PlantApp(Plantlist[1],True,david)
#app.config(bg="green")
app.mainloop()






# class PlantBox(tk.Frame):
#   def __init__(self,val,master):
#     super().__init__(master)
#     self.master = master  
#     self.name=Plantlist[val].name
#     self.image=tk.PhotoImage(file=Plantlist[val].image)
#     self.imagelabel=tk.Label(image=self.image)
#     self.imagelabel.pack()
#     self.boxcreate()
#     #self.pack()
#   def boxcreate(self):
#     self.boxtitle=tk.Label(self,text=self.name,fg='yellow',font='bold')
#     self.boxtitle.pack()