#Dependencies
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
import json

#WINDOW
window = ctk.CTk()

#WINDOW SIZE
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 900
appHeight = 800
x = (screenWidth / 2) - (appWidth / 2)
y = (screenHeight / 2) - (appHeight / 2)
window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
window.title("CATSKO")
window.resizable(False, False)

#ACCOUNT FRAME 
loginFrame = tk.Frame(window, bg="")
createAccFrame = tk.Frame(window, bg="")


def toMainPage():
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    home_appWidth = 1440
    home_appHeight = 900
    x = (screenWidth / 2) - (home_appWidth / 2)
    y = (screenHeight / 2) - (home_appHeight / 2)
    window.geometry(f'{home_appWidth}x{home_appHeight}+{int(x)}+{int(y)}')
    window.title("CATSKO")
    window.resizable(False, False)

    loginFrame.place_forget()
    loginBg_label.place_forget()
    loginUsername.place_forget()
    loginPassword.place_forget()
    loginPic.place_forget()

    #HOME PAGE WIDGETS
    #HOMEPAGE
    homePage = tk.Canvas(window, width=1440, height=900, highlightthickness=0, background= "white")
    homePage.place(relheight=1, relwidth=1)

    navigationImagePath = Image.open("Home/NavigationBar.png")
    navigationImageResize = navigationImagePath.resize((336,900))
    navigationImageFinal = ImageTk.PhotoImage(navigationImageResize)

    nav_x = home_appWidth * 0
    nav_y = home_appHeight * 0

    homePage.create_image(nav_x,nav_y, image=navigationImageFinal, anchor=tk.NW)

    headerImagePath = Image.open("Home/Rectangle.png")
    headerImageResize = headerImagePath.resize((1104,300))
    headerImageFinal = ImageTk.PhotoImage(headerImageResize)
    homePage.create_image(336,0, image=headerImageFinal, anchor=tk.NW)

    catsImagePath = Image.open("Home/Cats.png")
    catsImageResize = catsImagePath.resize((293, 175))
    catsImageFinal = ImageTk.PhotoImage(catsImageResize)
    catsButton = homePage.create_image(550, 300, image=catsImageFinal)
    homePage.tag_bind(catsButton, "<Button-1>", toCatsPage())

    applicantsImagePath = Image.open("Home/Applicants.png")
    applicantsImageResize = applicantsImagePath.resize((293, 175))
    applicantsImageFinal = ImageTk.PhotoImage(applicantsImageResize)
    applicantsButton = homePage.create_image(890, 300, image=applicantsImageFinal)
    homePage.tag_bind(applicantsButton, "<Button-1>")

    demographicsImagePath = Image.open("Home/Demographics.png")
    demographicsImageResize = demographicsImagePath.resize((293, 175))
    demographicsImageFinal = ImageTk.PhotoImage(demographicsImageResize)
    demographicsButton = homePage.create_image(1230, 300, image=demographicsImageFinal)
    homePage.tag_bind(demographicsButton, "<Button-1>")

    adminName = ctk.CTkLabel(master=homePage, text="Hello, "+user+".",font=("Poppins Semibold", 32),
                             fg_color="#F3F2F2", text_color="#868686", width=320, height=48)
    adminName.place(x=382, y=115)

    navAdminName = ctk.CTkLabel(master=homePage, text=user, font=("Poppins Semibold", 20),bg_color="transparent",
                             fg_color="#800000", text_color="White", width=134, height=29)
    navAdminName.place(x=91, y=284.89)

    #Create variables to keep garbage values
    homePage.navigationImageFinal = navigationImageFinal
    homePage.headerImageFinal = headerImageFinal
    homePage.catsImageFinal = catsImageFinal
    homePage.applicantsImageFinal = applicantsImageFinal
    homePage.demographicsImageFinal = demographicsImageFinal
    homePage.adminName = adminName

def toCatsPage():

    createAccBg_label.place_forget()



def toCreateAcc():
    createAccFrame.place(relheight=1,relwidth=1)
    createAccBg_label.place(x=0, y=0, relwidth=1, relheight=1)
    loginFrame.place_forget()
    loginBg_label.place_forget()
    loginUsername.place_forget()
    loginPassword.place_forget()
    loginPic.place_forget()


def toLoginAcc():
    loginFrame.place(relheight=1,relwidth=1)
    loginBg_label.place(x=0, y=0, relwidth=1, relheight=1)    
    loginUsername.place(relx=0.25, rely=0.43, anchor="center")
    loginPassword.place(relx=0.25, rely=0.573, anchor="center")
    loginPic.place(relx=0.248,rely=0.70, anchor= CENTER)
    createAccFrame.place_forget()
    createAccBg_label.place_forget()


#LOG IN ACC FUNCTION
def loginfunction():
    global user
    global validuser

    validuser = 0
    user = loginUsername.get()
    ValidPassword = [{"password":loginPassword.get()}]
    with open('data.json', 'r') as f:
        people = json.loads(f.read())
    if user == '' or ValidPassword == '':
        messagebox.showerror(title="Try again", message="Please fill in the required fields")
    elif user != '' or ValidPassword != '':
        for key,val in people.items():
            if user == key and ValidPassword == val:
                validuser = 1
                toMainPage()
            elif user == key and ValidPassword != val:
                validuser = 1
                messagebox.showerror(title="Try again", message= "Wrong Credentials")
        if validuser != 1:
            messagebox.showerror(title="Try again", message= "Wrong Credentials")


# CREATE ACC FUNCTION
def createfunction():
    global newUser
    global newPass
    global validCreate
    newUser = createAccUsername.get()
    newPass = createAccPassword.get()
    newUserSize = len(newUser)
    newPassSize = len(newPass)
    validCreate = 0

    # Opens json data file and Error Handler
    with open('data.json', 'r') as f:
        people = json.loads(f.read())
        if newUser == '' and newPass == '':
            messagebox.showerror(title="Invalid input", message="Please fill in the required fields")
        elif newUser == '' and newPass != '':
            messagebox.showerror(title="Invalid input", message="Username Field Required")
        elif newUser != '' and newPass == '':
            messagebox.showerror(title="Invalid input", message="Password Field Required")
        elif newUserSize < 5 or newPassSize < 5:
            messagebox.showerror(title="Failed", message="Please provide atleast 5 characters for both fields")
        elif newUser != '' and newPass != '':
            for key, val in people.items():
                if newUser != key:
                    validCreate = 1
                elif newUser == key:
                    validCreate = 0
                    messagebox.showerror(title="Failed", message=newUser + " already exist")
                    break

        if validCreate == 1 and newUserSize >= 5 and newPassSize >= 5:
            with open('data.json', 'r') as f:
                data = json.loads(f.read())
                data[newUser] = [{"password": newPass}]
                accounts = json.dumps(data, indent=4)
                with open('data.json', 'w') as f:
                    f.write(accounts)
                validCreate = 0
                messagebox.showinfo(title="Success", message="You have successfully created an account")

#LOGIN ACCOUNT PAGE
loginFrame.place(relheight=1, relwidth=1)

loginPage = tk.Canvas(loginFrame, width=900, height=800, highlightthickness=0)

loginBgPhoto = ctk.CTkImage(light_image=Image.open('Pages/LOGIN PAGE.png'),
                                dark_image=Image.open('Pages/LOGIN PAGE.png'), size=(900,800))


# Create canvas for background image
loginBg_label = ctk.CTkLabel(window, text="", image=loginBgPhoto)
loginBg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create entry widgets
loginUsername = ctk.CTkEntry(loginBg_label, width=390, height=56, corner_radius=20)
loginUsername.configure(placeholder_text="",
                          fg_color="light gray",
                          bg_color="white",
                          border_width=2,
                          border_color="white",
                          text_color="black")
loginUsername.place(relx=0.25, rely=0.43, anchor="center")

loginPassword = ctk.CTkEntry(loginBg_label, width=390, height=56, corner_radius=20)
loginPassword.configure(placeholder_text="",
                            fg_color="light gray",
                            bg_color="white",
                            border_width=2,
                            border_color="white",
                            text_color="black",
                            show="*")
loginPassword.place(relx=0.25, rely=0.573, anchor="center")

#login button
loginImagePath = Image.open("Button/LoginButton.png")
loginImageResize = loginImagePath.resize((199,56))
loginButton = ImageTk.PhotoImage(loginImageResize)
loginPic = Button(loginBg_label, bd=0   ,text="Button", image=loginButton,borderwidth=0,highlightthickness=0, bg='white', command=lambda: loginfunction())
loginPic.place(relx=0.248,rely=0.70, anchor= CENTER)


#register button
RegisterButton = Button(loginBg_label, command=lambda: toCreateAcc())                  
RegisterButton.config(text='Register Here', bd =0, font=('Poppins', 14,'bold'), bg= 'white', fg='#800000', activeforeground='#800000', activebackground='white' )
RegisterButton.place(x=270,y=631)

#CREATE ACCOUNT PAGE
createAccPage = tk.Canvas(createAccFrame, width=900, height=800, highlightthickness=0)

createAccBgPhoto = ctk.CTkImage(light_image=Image.open('Pages/REGISTER PAGE.png'),
                                dark_image=Image.open('Pages/REGISTER PAGE.png'), size=(900,800))

# Create canvas for background image
createAccBg_label = ctk.CTkLabel(window, text="", image=createAccBgPhoto)


#CREATE PAGE WIDGETS

createAccUsername = ctk.CTkEntry(createAccBg_label, width=390, height=56, corner_radius=20)
createAccUsername.configure(placeholder_text="",
                          fg_color="light gray",
                          bg_color="white",
                          border_width=2,
                          border_color="white",
                          text_color="black")
createAccUsername.place(x=35,y=180)

createAccPassword = ctk.CTkEntry(createAccBg_label, width=390, height=56, corner_radius=20)
createAccPassword.configure(placeholder_text="",
                            fg_color="light gray",
                            bg_color="white",
                            border_width=2,
                            border_color="white",
                            text_color="black",
                            show="*")
createAccPassword.place(x=35,y=305)

RegisterAccImagePath = Image.open("Button/RegisterButton.png")
RegisterAccImageResize = RegisterAccImagePath.resize((199,56))
RegisterAccButton = ImageTk.PhotoImage(RegisterAccImageResize)
RegisterAccPic = Button(createAccBg_label, bd=0   ,text="Button", image=RegisterAccButton,borderwidth=0,highlightthickness=0, bg='white', command=lambda: createfunction())
RegisterAccPic.place(x=124,y=450)

BackButton = Button(createAccBg_label, command=lambda: toLoginAcc())                  
BackButton.config(text='Back', bd =0, font=('Poppins', 14,'bold'), bg= 'white', fg='#4A4A4A', activeforeground='#4A4A4A', activebackground='white' )
BackButton.place(x=194,y=540)


window.mainloop()


