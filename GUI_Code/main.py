# importing all the modules used in the code
from Calculations_Code.calculations import PlantSort as PS
from Calculations_Code.Database import PlantList as PL
from PlantObjects import UserInputs as UI
import tkinter as tk
from PIL import Image, ImageTk


class PlantApp(tk.Tk):
    """ PlantApp initialises a TkInstance
    The show_frame method unpacks all the frames except for the one that needs to be shown """

    def __init__(self):
        super().__init__()

        self.title('Growing Oxygen')
        self.resizable(False, False)

        # creating a container

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
        calculation = PS(GOxygen)
        calculation.calculate()
        # reinitialising the plant container with the new list
        self.frames[PlantContainer] = PlantContainer(self, calculation)


class Menu(tk.Frame):
    def __init__(self, master=None):
        # sets up the master for the frame
        super().__init__(master)
        self.master = master
        # packs the frame
        self.pack()
        # runs the function for packing the widgets into the frame
        self.create_widgets()

    def create_widgets(self):
        # creates a button to show the next frame of the GUI
        self.plant_reccomendation_choice = tk.Button(self, text="plant recommendations",
                                                     command=lambda: self.master.show_frame(
                                                         self.master.frames[UserInputsMenu]))
        # packs the button into a grid
        self.plant_reccomendation_choice.grid(row=2, column=4, padx=10, pady=10)


class UserInputsMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # packing the frame
        self.pack()
        # packing all the widgets
        self.plant_reccomendation()
        self.master.config(bg='green')

    def plant_reccomendation(self):
        # setting up all the series identifies of the radio buttons
        var1 = tk.IntVar(self)
        var2 = tk.IntVar(self)
        var3 = tk.IntVar(self)
        # Label for the buttons
        self.templabel = tk.Label(self, text="What is the temperature \n of the location?", bg="green", fg="white")
        self.templabel.grid(row=2, column=1)
        # buttons for setting temperature
        self.tempbutton1 = tk.Radiobutton(self, text="18-19°C", bg='#826644', value=1,
                                          variable=var1, command=lambda: GOxygen.settemp(18))
        # PLacing the button into the grid
        self.tempbutton1.grid(row=2, column=2, padx=1, pady=3)

        self.tempbutton2 = tk.Radiobutton(self, text="20-21°C", bg='#826644', value=2,
                                          variable=var1, command=lambda: GOxygen.settemp(20))
        self.tempbutton2.grid(row=2, column=3, padx=1, pady=3)
        self.tempbutton3 = tk.Radiobutton(self, text="22-23°C", bg='#826644', value=3,
                                          variable=var1, command=lambda: GOxygen.settemp(22))
        self.tempbutton3.grid(row=2, column=4, padx=1, pady=3)
        self.tempbutton4 = tk.Radiobutton(self, text="24-25°C", bg='#826644', value=4,
                                          variable=var1, command=lambda: GOxygen.settemp(24))
        self.tempbutton4.grid(row=2, column=5, padx=1, pady=3)
        self.tempbutton5 = tk.Radiobutton(self, text="26-27°C", bg='#826644', value=5,
                                          variable=var1, command=lambda: GOxygen.settemp(26))
        self.tempbutton5.grid(row=2, column=6, padx=1, pady=3)
        # slider for ease of care

        self.easelabel = tk.Label(self, text="How easy do you want \n the plant care to be?", bg="green", fg="white")
        self.easelabel.grid(row=3, column=1)
        self.easeslider = tk.Scale(self, from_=0, to=10, length=450, tickinterval=5, orient='horizontal', bg="#67AB9F",
                                   command=self.setease)
        # automatically passes self into the the function so doesn't need to be called
        self.easeslider.grid(row=3, column=2, columnspan=5)
        # buttons for size
        self.sizebutton1 = tk.Radiobutton(self, text="Small", bg="#67AB9F", value=1,
                                          variable=var2, command=lambda: GOxygen.setsize(0))
        self.sizebutton1.grid(row=3, column=8, padx=2, pady=3)
        self.sizebutton2 = tk.Radiobutton(self, text="Medium", bg="#67AB9F", value=2,
                                          variable=var2, command=lambda: GOxygen.setsize(1))
        self.sizebutton2.grid(row=3, column=9, padx=2, pady=3)
        self.sizebutton3 = tk.Radiobutton(self, text="Big", bg="#67AB9F", value=3,
                                          variable=var2, command=lambda: GOxygen.setsize(2))
        self.sizebutton3.grid(row=4, column=8, padx=2, pady=3)
        self.sizebutton4 = tk.Radiobutton(self, text="Huge", bg="#67AB9F", value=4,
                                          variable=var2, command=lambda: GOxygen.setsize(3))

        self.sizebutton4.grid(row=4, column=9, padx=2, pady=3)
        self.sizelabel = tk.Label(self, text='how large do you want \nthe plant to be?', bg='green', fg='white')
        self.sizelabel.grid(row=2, column=8, columnspan=2)

        # buttons for brightness
        self.brightlabel = tk.Label(self, text='what is the brightness\n of the location?', bg='green', fg='white')
        self.brightlabel.grid(row=4, column=1)
        self.brightbutton1 = tk.Radiobutton(self, text="Full\n Sun", bg='#D3AA32', value=1,
                                            variable=var3, command=lambda: GOxygen.setbright(5))
        self.brightbutton1.grid(row=4, column=2)

        self.brightbutton2 = tk.Radiobutton(self, text="Bright\n Sun", bg='#D3AA32', value=2,
                                            variable=var3, command=lambda: GOxygen.setbright(4))
        self.brightbutton2.grid(row=4, column=3)

        self.brightbutton3 = tk.Radiobutton(self, text="Semi\n Sun", bg='#D3AA32', value=3,
                                            variable=var3, command=lambda: GOxygen.setbright(3))
        self.brightbutton3.grid(row=4, column=4)

        self.brightbutton4 = tk.Radiobutton(self, text="Little\n Sun", bg='#D3AA32', value=4,
                                            variable=var3, command=lambda: GOxygen.setbright(2))
        self.brightbutton4.grid(row=4, column=5)

        self.brightbutton5 = tk.Radiobutton(self, text="No\n Sun", bg='#D3AA32', value=5,
                                            variable=var3, command=lambda: GOxygen.setbright(1))
        self.brightbutton5.grid(row=4, column=6)
        # done button for next frame
        self.DoneButton = tk.Button(self, text='Done', bg='green', fg='yellow', width=95,
                                    command=lambda: self.attributesdone())
        self.DoneButton.grid(row=5, column=1, columnspan=9)

    def attributesdone(self):
        # sorting the plant list according to the user inputs
        self.master.sort_PlantList()
        # testing
        print('done', GOxygen.temperature, GOxygen.ease, GOxygen.size, GOxygen.brightness)
        # showing the next frame
        self.master.show_frame(self.master.frames[PlantContainer])

    def setease(self, val):
        # this function since the slider just sent the value anyway
        GOxygen.setease(val)


class PlantContainer(tk.Frame):

    def __init__(self, master, Plist=None):
        super().__init__(master)
        self.master = master
        # setting up the list of box frames depending on if the new plant list has been passed through
        if not Plist:
            self.frames = [PlantBox(self, plant) for plant in Plantlist]
            # packing the frames
            for pb in self.frames:
                pb.pack(side=tk.LEFT, padx=5, pady=5)
        else:
            count = 0
            self.frames = [PlantBox(self, plant) for plant in Plist.PlantList]
            for pb in self.frames:
                # making the display of boxes neater and not just one line
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
        # sets up frames of the two phases
        self.frames = {BoxPhase1: BoxPhase1(self, plant), BoxPhase2: BoxPhase2(self, plant)}
        # packs first phase
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
        # setting up the image display
        with Image.open(plant.image) as im:
            # making sure all the images are the same resolution so not to mess with the proportions of the boxes
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
        # showing the next phase
        self.master.show_frame(self.master.frames[BoxPhase2])


class BoxPhase2(tk.Frame):

    def __init__(self, master, plant):
        #setting up the dictionaries for the integer values of attributes to indix in and retireve strings from
        bright_dict = {1: 'No Sun', 2: 'Little Sun', 3: 'Semi Sun', 4: 'Bright Sun', 5: 'Full Sun'}
        size_dict = {0: 'Small', 1: 'Medium', 2: 'Big', 3: 'Huge'}
        super().__init__(master)
        self.p = plant
        self.master = master
        self.name = self.p.name
        #setting up the image
        with Image.open(self.p.image) as im:
            im_resized = im.resize((100, 300))
            self.image = ImageTk.PhotoImage(im_resized)
        self.imagelabel = tk.Label(self, image=self.image)
        self.imagelabel.pack(side=tk.LEFT)
        #setting up the big textbox with a lot of formatting
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
        self.minimisebutton = tk.Button(self, text='minimise', bg='cyan',
                                        command=lambda: self.contract())
        #same as with phase 1, just the other way
        self.minimisebutton.pack(side=tk.TOP)

    def contract(self):
        self.master.forget_frames()
        self.master.show_frame(self.master.frames[BoxPhase1])


Plantlist = PL

GOxygen = UI(None, None, None, None)

print(GOxygen.temperature)
app = PlantApp()
app.mainloop()
