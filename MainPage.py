#Dependencies
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from customtkinter import *
import customtkinter as ctk
from tkinter import messagebox
import json
import addRecord
import mysql.connector
from mysql.connector import Error

ctk.set_widget_scaling(1)
#WINDOW
window = ctk.CTk()


def window_size():
    #LOGIN WINDOW SIZE
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    appWidth = 900
    appHeight = 800
    x = (screenWidth / 2) - (appWidth / 2)
    y = (screenHeight / 2) - (appHeight / 2)
    window.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    window.title("CATSKO")
    window.resizable(False, False)

window_size()

#ACCOUNT FRAME
loginFrame = tk.Frame(window, bg="")
createAccFrame = tk.Frame(window, bg="")

#MAIN WINDOW CANVAS
homePage = tk.Canvas(window, width=1440, height=900, highlightthickness=0, background= "white")
navigatorPage = tk.Canvas(window, width=336, height=900, highlightthickness=0)
catsPage = tk.Canvas(window, width=1440, height=900, highlightthickness=0, background= "white")
applicantsPage = tk.Canvas(window, width=1440, height=900, highlightthickness=0, background= "white")


def setupNavigator():
    global navigatorpageBGFinal, catsko_logoFinal, adminPicFinal
    global homeButtonImageFinal, logoutButtonImageFinal

    #navigator background
    navigatorpageBGPicture = Image.open("Home/Rectangle (1).png")
    navigatorpageBGResized = navigatorpageBGPicture.resize((336,900))
    navigatorpageBGFinal = ImageTk.PhotoImage(navigatorpageBGResized)
    navigatorPage.create_image(0,0, image=navigatorpageBGFinal, anchor=tk.NW)

    #catsko logo
    catsko_logoPicture = Image.open("navigator/catsko_logo.png")
    catsko_logoResized = catsko_logoPicture.resize((45,45))
    catsko_logoFinal = ImageTk.PhotoImage(catsko_logoResized)
    navigatorPage.create_image(50, 50, image=catsko_logoFinal, anchor=tk.CENTER)

    #catsko title
    navigatorPage.create_text(130,52, text="CatsKo", font=("Poppins", 20," bold"),fill="white",anchor="center")

    #admin pic
    adminPicPicture = Image.open("navigator/adminPic.png")
    adminPicResized = adminPicPicture.resize((75,75))
    adminPicFinal = ImageTk.PhotoImage(adminPicResized)
    navigatorPage.create_image(168, 197.5, image=adminPicFinal, anchor=tk.CENTER)

    #admin name
    navigatorPage.create_text(168, 258,text=user,font=("Poppins", 16, "bold"),fill="white",anchor="center")

    #home button
    homeButtonImagePath = Image.open("navigator/homeButton.png")
    homeButtonImageResize = homeButtonImagePath.resize((125,32))
    homeButtonImageFinal = ImageTk.PhotoImage(homeButtonImageResize)
    homeButton = navigatorPage.create_image(80, 388, image=homeButtonImageFinal)
    navigatorPage.tag_bind(homeButton, "<Button-1>", toHomePage)

    #logout button
    logoutButtonImagePath = Image.open("navigator/logoutButton.png")
    logoutButtonImageResize = logoutButtonImagePath.resize((140,32))
    logoutButtonImageFinal = ImageTk.PhotoImage(logoutButtonImageResize)
    logoutButton = navigatorPage.create_image(88, 484, image=logoutButtonImageFinal)
    navigatorPage.tag_bind(logoutButton, "<Button-1>", backtoLoginAcc)

def setupApplicants(event = None):
    global searchbar_logoFinal, sortButtonImageFinal, addButtonImageFinal

    #Search Bar
    searchbar_logoPicture = Image.open("Applicants/SearchBar.png")
    searchbar_logoResized = searchbar_logoPicture.resize((520, 72))
    searchbar_logoFinal = ImageTk.PhotoImage(searchbar_logoResized)
    applicantsPage.create_image(300, 90, image=searchbar_logoFinal)

    applicantsPage.create_text(210, 90, text="Search Applicant ID:", font=("Poppins", 24, "bold"),
                               fill="white")

    addButtonImagePath = Image.open("Applicants/ri_sort-desc.png")
    addButtonImageResize = addButtonImagePath.resize((57, 58))
    addButtonImageFinal = ImageTk.PhotoImage(addButtonImageResize)
    addButton = applicantsPage.create_image(1030, 90, image=addButtonImageFinal)
    applicantsPage.tag_bind(addButton, "<Button-1>", lambda e: addRecord.addtoDB(window))

    sortButtonImagePath = Image.open("Applicants/Vector.png")
    sortButtonImageResize = sortButtonImagePath.resize((36, 28))
    sortButtonImageFinal = ImageTk.PhotoImage(sortButtonImageResize)
    sortButton = applicantsPage.create_image(85, 181, image=sortButtonImageFinal)
    applicantsPage.tag_bind(sortButton, "<Button-1>")

    applicantsPage.create_text(160, 181, text="ID", font=("Poppins", 26, "bold"),
                               fill="Black")

    applicantsPage.create_text(270, 181, text="Name", font=("Poppins", 26, "bold"),
                               fill="Black")

    # Place a CTkEntry on top of the canvas
    searchID = ctk.CTkEntry(
        applicantsPage,
        width=150,
        height=30,
        corner_radius=20,
        fg_color="light gray",
        bg_color="#C27400",
        text_color="black"
    )

    searchID_window = applicantsPage.create_window(390, 75, anchor="nw", window=searchID)

def toMainPage(event=None):
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    home_appWidth = 1440
    home_appHeight = 900
    x = (screenWidth / 2) - (home_appWidth / 2)
    y = (screenHeight / 2) - (home_appHeight / 2)
    window.geometry(f'{home_appWidth}x{home_appHeight}+{int(x)}+{int(y)}')
    window.title("CATSKO")
    window.resizable(False, False)

    navigatorPage.place(x=0, y=0, relheight=1)
    setupNavigator()
    loginFrame.place_forget()
    loginBg_label.place_forget()
    loginUsername.place_forget()
    loginPassword.place_forget()
    loginPic.place_forget()
    catsPage.place_forget()
    applicantsPage.place_forget()

    #HOME PAGE WIDGETS

    #HOME PAGE
    homePage.place(relheight=1, relwidth=1)

    #navigator canvas
    navigatorPage.place(x=0, y=0, relheight=1)

    #background
    headerImagePath = Image.open("Home/Rectangle.png")
    headerImageResize = headerImagePath.resize((1104,300))
    headerImageFinal = ImageTk.PhotoImage(headerImageResize)
    homePage.create_image(336,0, image=headerImageFinal, anchor=tk.NW)

    #cats button
    catsImagePath = Image.open("Home/Cats.png")
    catsImageResize = catsImagePath.resize((293, 175))
    catsImageFinal = ImageTk.PhotoImage(catsImageResize)
    catsButton = homePage.create_image(550, 300, image=catsImageFinal)
    homePage.tag_bind(catsButton, "<Button-1>", toCatsPage)

    #applicants button
    applicantsImagePath = Image.open("Home/Applicants.png")
    applicantsImageResize = applicantsImagePath.resize((293, 175))
    applicantsImageFinal = ImageTk.PhotoImage(applicantsImageResize)
    applicantsButton = homePage.create_image(890, 300, image=applicantsImageFinal)
    homePage.tag_bind(applicantsButton, "<Button-1>", toApplicantsPage)

    #demographics button
    demographicsImagePath = Image.open("Home/Demographics.png")
    demographicsImageResize = demographicsImagePath.resize((293, 175))
    demographicsImageFinal = ImageTk.PhotoImage(demographicsImageResize)
    demographicsButton = homePage.create_image(1230, 300, image=demographicsImageFinal)
    homePage.tag_bind(demographicsButton, "<Button-1>")

    #admin name
    adminName = ctk.CTkLabel(master=homePage, text="Hello, "+user+".",font=("Poppins", 32, "bold"),
                             fg_color="#F3F2F2", text_color="#868686", width=320, height=48)
    adminName.place(x=382, y=115)#


    #CATS PAGE WIDGETS

    #cats label
    catsPage.create_text(382, 88, text="Cats", font=("Poppins", 32," bold"),fill="black",anchor="center")

    #Create variables to keep garbage values
    homePage.headerImageFinal = headerImageFinal
    homePage.catsImageFinal = catsImageFinal
    homePage.applicantsImageFinal = applicantsImageFinal
    homePage.demographicsImageFinal = demographicsImageFinal
    homePage.adminName = adminName

def toHomePage(event=None):
    navigatorPage.place(x=0, y=0, relheight=1)
    setupNavigator()
    loginFrame.place_forget()
    loginBg_label.place_forget()
    loginUsername.place_forget()
    loginPassword.place_forget()
    loginPic.place_forget()
    catsPage.place_forget()
    applicantsPage.place_forget()
    y_scroll.place_forget()

    # HOME PAGE WIDGETS

    # HOME PAGE
    homePage.place(relheight=1, relwidth=1)

    # navigator canvas
    navigatorPage.place(x=0, y=0, relheight=1)

    # background
    headerImagePath = Image.open("Home/Rectangle.png")
    headerImageResize = headerImagePath.resize((1104, 300))
    headerImageFinal = ImageTk.PhotoImage(headerImageResize)
    homePage.create_image(336, 0, image=headerImageFinal, anchor=tk.NW)

    # cats button
    catsImagePath = Image.open("Home/Cats.png")
    catsImageResize = catsImagePath.resize((293, 175))
    catsImageFinal = ImageTk.PhotoImage(catsImageResize)
    catsButton = homePage.create_image(550, 300, image=catsImageFinal)
    homePage.tag_bind(catsButton, "<Button-1>", toCatsPage)

    # applicants button
    applicantsImagePath = Image.open("Home/Applicants.png")
    applicantsImageResize = applicantsImagePath.resize((293, 175))
    applicantsImageFinal = ImageTk.PhotoImage(applicantsImageResize)
    applicantsButton = homePage.create_image(890, 300, image=applicantsImageFinal)
    homePage.tag_bind(applicantsButton, "<Button-1>", toApplicantsPage)

    # demographics button
    demographicsImagePath = Image.open("Home/Demographics.png")
    demographicsImageResize = demographicsImagePath.resize((293, 175))
    demographicsImageFinal = ImageTk.PhotoImage(demographicsImageResize)
    demographicsButton = homePage.create_image(1230, 300, image=demographicsImageFinal)
    homePage.tag_bind(demographicsButton, "<Button-1>")

    # admin name
    adminName = ctk.CTkLabel(master=homePage, text="Hello, " + user + ".", font=("Poppins", 32, "bold"),
                             fg_color="#F3F2F2", text_color="#868686", width=320, height=48)
    adminName.place(x=382, y=115)  #

    # Create variables to keep garbage values
    homePage.headerImageFinal = headerImageFinal
    homePage.catsImageFinal = catsImageFinal
    homePage.applicantsImageFinal = applicantsImageFinal
    homePage.demographicsImageFinal = demographicsImageFinal
    homePage.adminName = adminName

def toCatsPage(event = None):
    createAccFrame.place_forget()
    createAccBg_label.place_forget()
    loginFrame.place_forget()
    loginBg_label.place_forget()
    loginUsername.place_forget()
    loginPassword.place_forget()
    loginPic.place_forget()
    homePage.place_forget()
    applicantsPage.place_forget()

    navigatorPage.place(x=0, y=0, relheight=1)
    setupNavigator()
    catsPage.place(x=336, y=0, width=1104, height=900)
    y_scroll.grid(row=0, column=1, sticky='ns')
    y_scroll.place(relx=1, rely=0, relheight=1, anchor="ne")

def toApplicantsPage(event = None):
    createAccFrame.place_forget()
    createAccBg_label.place_forget()
    loginFrame.place_forget()
    loginBg_label.place_forget()
    loginUsername.place_forget()
    loginPassword.place_forget()
    loginPic.place_forget()
    homePage.place_forget()
    catsPage.place()

    navigatorPage.place(x=0, y=0, relheight=1)
    setupNavigator()
    setupApplicants()
    applicantsPage.place(x=336, y=0, width=1104, height=900)


def toCreateAcc():
    createAccFrame.place(relheight=1,relwidth=1)
    createAccBg_label.place(x=0, y=0, relwidth=1, relheight=1)
    loginFrame.place_forget()
    loginBg_label.place_forget()
    loginUsername.place_forget()
    loginPassword.place_forget()
    loginPic.place_forget()



def backtoLoginAcc(event):
    window_size()
    loginUsername.delete(0, tk.END)
    loginPassword.delete(0, tk.END)
    loginPassword.configure(show = "*")
    createAccUsername.delete(0, tk.END)
    createAccPassword.delete(0, tk.END)
    createAccPassword.configure(show = "*")

    loginFrame.place(relheight=1,relwidth=1)
    loginBg_label.place(x=0, y=0, relwidth=1, relheight=1)
    loginUsername.place(relx=0.25, rely=0.43, anchor="center")
    loginPassword.place(relx=0.25, rely=0.573, anchor="center")
    loginPic.place(relx=0.248,rely=0.70, anchor= CENTER)
    createAccFrame.place_forget()
    createAccBg_label.place_forget()
    homePage.place_forget()
    navigatorPage.place_forget()

def toLoginAcc():
    loginUsername.delete(0, tk.END)
    loginPassword.delete(0, tk.END)
    loginPassword.configure(show = "*")
    createAccUsername.delete(0, tk.END)
    createAccPassword.delete(0, tk.END)
    createAccPassword.configure(show = "*")

    loginFrame.place(relheight=1,relwidth=1)
    loginBg_label.place(x=0, y=0, relwidth=1, relheight=1)
    loginUsername.place(relx=0.25, rely=0.43, anchor="center")
    loginPassword.place(relx=0.25, rely=0.573, anchor="center")
    loginPic.place(relx=0.248,rely=0.70, anchor= CENTER)
    createAccFrame.place_forget()
    createAccBg_label.place_forget()
    homePage.place_forget()
    navigatorPage.place_forget()

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
loginImagePath = Image.open("images/LoginButton.png")
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


#Create entry widgets
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

#register account button
RegisterAccImagePath = Image.open("images/RegisterButton.png")
RegisterAccImageResize = RegisterAccImagePath.resize((199,56))
RegisterAccButton = ImageTk.PhotoImage(RegisterAccImageResize)
RegisterAccPic = Button(createAccBg_label, bd=0   ,text="Button", image=RegisterAccButton,borderwidth=0,highlightthickness=0, bg='white', command=lambda: createfunction())
RegisterAccPic.place(x=124,y=450)

#back to login button
BackButton = Button(createAccBg_label, command=toLoginAcc)
BackButton.config(text='Back', bd =0, font=('Poppins', 14,'bold'), bg= 'white', fg='#4A4A4A', activeforeground='#4A4A4A', activebackground='white' )
BackButton.place(x=194,y=540)

#Cats Page
catsPage = tk.Canvas(window, width=1440, height=900, highlightthickness=0, background= "white", scrollregion=(300,0,1440,2000))
y_scroll = tk.Scrollbar(window, orient='vertical', command=catsPage.yview)
catsPage.config(yscrollcommand=y_scroll.set)


window.mainloop()


