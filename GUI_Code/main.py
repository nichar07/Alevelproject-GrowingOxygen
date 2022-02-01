# importing all the modules used in the code
from Calculations_Code.calculations import PlantSort as PS
from Calculations_Code.Database import PlantList as PL
from PlantObjects import UserInputs as UI
import tkinter as tk
from PIL import Image, ImageTk


class PlantApp(tk.Tk):
    """ PlantApp initialises a TkInstance
    The show_frame method unpacks all the frames except for the one that needs to be shown """

    def __init__(self, expandchoice, flag=False, master=None):
        super().__init__()

        self.title('Growing Oxygen')
        self.resizable(True, True)
        self.expandedChoice = expandchoice

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
        pages = (Menu, UserInputsMenu, PlantContainer)
        for F in pages:
            frame = F(self)
            self.frames[F] = frame
        print(self.frames)
        self.show_frame(self.frames[Menu])

    # Function to show the desired Page class, which is a subclass of tk.Frame
    def show_frame(self, frame_to_show):
        self.forget_frames()
        frame_to_show.pack(expand=True, fill=tk.BOTH)

    def forget_frames(self):
        widgets = self.winfo_children()
        # Forget all the frames
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

    def sort_PlantList(self):
        # sorting the list of Plants
        calculation = PS(david)
        calculation.calculate()
        self.frames[PlantContainer] = PlantContainer(self, calculation)


class Menu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.plant_reccomendation_choice = tk.Button(self, text="plant reccomendations",
                                                     command=lambda: self.master.show_frame(
                                                         self.master.frames[UserInputsMenu]))
        self.plant_reccomendation_choice.grid(row=2, column=4, padx=10, pady=10)


class UserInputsMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.screenwidth = self.master.winfo_screenwidth()
        self.screenheight = self.master.winfo_screenheight()
        self.pack()
        self.plant_reccomendation()
        self.master.config(bg='green')

    def plant_reccomendation(self):
        # Label fot the buttons
        self.templabel = tk.Label(self, text="What is the temperature \n of the location?", bg="green", fg="white")
        self.templabel.grid(row=2, column=1)
        # buttons for setting temperature
        self.tempbutton1 = tk.Button(self, text="18°C", bg='#826644',
                                     command=lambda: david.settemp(18))
        # PLacing the button into the grid
        self.tempbutton1.grid(row=2, column=2, padx=1, pady=3)

        self.tempbutton2 = tk.Button(self, text="20°C", bg='#826644',
                                     command=lambda: david.settemp(20))
        self.tempbutton2.grid(row=2, column=3, padx=1, pady=3)
        self.tempbutton3 = tk.Button(self, text="22°C", bg='#826644',
                                     command=lambda: david.settemp(22))
        self.tempbutton3.grid(row=2, column=4, padx=1, pady=3)
        self.tempbutton4 = tk.Button(self, text="24°C", bg='#826644',
                                     command=lambda: david.settemp(24))
        self.tempbutton4.grid(row=2, column=5, padx=1, pady=3)
        self.tempbutton5 = tk.Button(self, text="26°C", bg='#826644',
                                     command=lambda: david.settemp(26))
        self.tempbutton5.grid(row=2, column=6, padx=1, pady=3)
        # slider for ease of care

        self.easelabel = tk.Label(self, text="How easy do you want \n the plant care to be?", bg="green", fg="white")
        self.easelabel.grid(row=3, column=1)
        self.easeslider = tk.Scale(self, from_=0, to=10, length=450, tickinterval=5, orient='horizontal', bg="#67AB9F",
                                   command=self.setease)  # automatically passes self into the the function so doesn't need to be called
        self.easeslider.grid(row=3, column=2, columnspan=5)
        # buttons for size
        self.sizebutton1 = tk.Button(self, text="Small", bg="#67AB9F",
                                     command=lambda: david.setsize(0))
        self.sizebutton1.grid(row=3, column=8, padx=2, pady=3)
        self.sizebutton2 = tk.Button(self, text="Medium", bg="#67AB9F",
                                     command=lambda: david.setsize(1))
        self.sizebutton2.grid(row=3, column=9, padx=2, pady=3)
        self.sizebutton3 = tk.Button(self, text="Big", bg="#67AB9F",
                                     command=lambda: david.setsize(2))
        self.sizebutton3.grid(row=4, column=8, padx=2, pady=3)
        self.sizebutton3 = tk.Button(self, text="Huge", bg="#67AB9F",
                                     command=lambda: david.setsize(3))

        self.sizebutton3.grid(row=4, column=9, padx=2, pady=3)
        self.sizelabel = tk.Label(self, text='how large do you want \nthe plant to be?', bg='green', fg='white')
        self.sizelabel.grid(row=2, column=8, columnspan=2)
        # buttons for brightness
        self.brightlabel = tk.Label(self, text='what is the brightness\n of the locaion?', bg='green', fg='white')
        self.brightlabel.grid(row=4, column=1)
        self.brightbutton1 = tk.Button(self, text="Full\n Sun", bg='#D3AA32',
                                       command=lambda: david.setbright(5))
        self.brightbutton1.grid(row=4, column=2)

        self.brightbutton2 = tk.Button(self, text="Bright\n Sun", bg='#D3AA32',
                                       command=lambda: david.setbright(4))
        self.brightbutton2.grid(row=4, column=3)

        self.brightbutton3 = tk.Button(self, text="Semi\n Sun", bg='#D3AA32',
                                       command=lambda: david.setbright(3))
        self.brightbutton3.grid(row=4, column=4)

        self.brightbutton4 = tk.Button(self, text="Little\n Sun", bg='#D3AA32',
                                       command=lambda: david.setbright(2))
        self.brightbutton4.grid(row=4, column=5)

        self.brightbutton5 = tk.Button(self, text="No\n Sun", bg='#D3AA32',
                                       command=lambda: david.setbright(1))
        self.brightbutton5.grid(row=4, column=6)
        # done button for next Page
        self.DoneButton = tk.Button(self, text='Done', bg='green', fg='yellow', width=95,
                                    command=lambda: self.attributesdone())
        self.DoneButton.grid(row=5, column=1, columnspan=9)

    def attributesdone(self):
        self.master.sort_PlantList()
        print('done', david.temperature, david.ease, david.size, david.brightness)
        self.master.show_frame(self.master.frames[PlantContainer])

    def setease(self, val):
        david.setease(val)


class PlantContainer(tk.Frame):

    def __init__(self, master, Plist=None):
        super().__init__(master)
        self.master = master
        if not Plist:
            self.frames = [PlantBox(self, plant) for plant in Plantlist]
            for pb in self.frames:
                pb.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            count = 0
            self.frames = [PlantBox(self, plant) for plant in Plist.PlantList]
            for pb in self.frames:
                pb.grid(row=count // 3, column=count % 3)
                count += 1

    def forget_frames(self):
        widgets = self.winfo_children()
        # Forget all the frames

        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()


class PlantBox(tk.Frame):
    def __init__(self, master, plant):
        super().__init__(master)
        self.master = master
        self.frames = {BoxPhase1: BoxPhase1(self, plant), BoxPhase2: BoxPhase2(self, plant)}
        self.show_frame(self.frames[BoxPhase1])

    def show_frame(self, frame_to_show):
        self.forget_frames()
        frame_to_show.pack(expand=True, fill=tk.BOTH)

    def forget_frames(self):
        widgets = self.winfo_children()
        # Forget all the frames
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()


class BoxPhase1(tk.Frame):

    def __init__(self, master, plant):
        super().__init__(master)
        self.master = master
        self.name = plant.name

        with Image.open(plant.image) as im:
            im_resized = im.resize((100, 300))
            self.image = ImageTk.PhotoImage(im_resized)
        self.imagelabel = tk.Label(self, image=self.image)
        self.imagelabel.pack()
        self.boxtitle = tk.Label(self, text=self.name, fg='#5BC014', font='bold')
        self.boxtitle.pack()
        self.expandbutton = tk.Button(self, text='expand', bg='cyan', command=lambda: self.expand(plant))
        self.expandbutton.pack()

    def expand(self, pl):
        print(f'expand {self.name}')
        self.master.forget_frames()
        self.master.show_frame(self.master.frames[BoxPhase2])


class BoxPhase2(tk.Frame):

    def __init__(self, master, plant):
        bright_dict = {1: 'No Sun', 2: 'Little Sun', 3: 'Semi Sun', 4: 'Bright Sun', 5: 'Full Sun'}
        size_dict = {0: 'Small', 1: 'Medium', 2: 'Big', 3: 'Huge'}
        super().__init__(master)
        self.p = plant

        self.master = master
        self.name = self.p.name
        with Image.open(self.p.image) as im:
            im_resized = im.resize((100, 300))
            self.image = ImageTk.PhotoImage(im_resized)
        self.imagelabel = tk.Label(self, image=self.image)
        self.imagelabel.pack(side=tk.LEFT)
        self.textbox = tk.Label(self, bg='#D3AA32', text=
        f'''Temperature range: {self.p.mintemp} - {self.p.maxtemp} \n 
    Brightness level: {bright_dict[self.p.brightness]}
    Size: {size_dict[self.p.size]}
    Ease of care: {self.p.ease}
    Pests: {self.p.pests}
    {self.p.careinfo}''', font=(44))
        self.textboxtitle = tk.Label(self, text=self.p.name, font='bold')
        self.textboxtitle.pack(side=tk.TOP)
        self.textbox.pack(side=tk.LEFT)
        self.minimisebutton = tk.Button(self, text='mimimise', bg='cyan',
                                        command=lambda: self.contract())
        self.minimisebutton.pack(side=tk.TOP)

    def contract(self):
        self.master.forget_frames()
        self.master.show_frame(self.master.frames[BoxPhase1])


Plantlist = PL

david = UI(None, None, None, None)

print(david.temperature)
app = PlantApp(Plantlist[1], True, david)
app.mainloop()
