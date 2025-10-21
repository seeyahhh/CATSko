import mysql.connector
from mysql.connector import Error
import customtkinter as ctk
from tkinter import *
from customtkinter import *
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk


#Create connection
def connect_db():
    conn = mysql.connector.connect(host='localhost', user='root', password='Admincatsko123',
                                   database='catsko')
def add_applicants_to_db(name, dob, temp_addr, town, zip_code, s_name,
    living_arr, home_type, know_pet, rent_type,
    landlord_name, rent_type1, landlord_name1, landlord_phone):

    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.callproc("insert_applicant", [
                name, dob, temp_addr, town, zip_code, email,
                h_phone, c_phone, m_addr, s_name,
                living_arr, home_type, know_pet, rent_type,
                landlord_name, rent_type1, landlord_name1, landlord_phone])
            conn.commit()
            messagebox.showinfo("Success", "Applicant added successfully.")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to insert applicant: {e}")
        finally:
            cursor.close()
            conn.close()


def test():
    print(addName.get())


def addtoDB(parent_window):
    addWin = ctk.CTkToplevel(parent_window, fg_color="#800000")  # Use CTkToplevel for customtkinter consistency
    addWin_width, addWin_height = 977, 749
    addWin.title("Add Applicant")

    # Calculate position to center the window on screen
    screen_width = parent_window.winfo_screenwidth()
    screen_height = parent_window.winfo_screenheight()
    x = (screen_width - addWin_width) // 2
    y = (screen_height - addWin_height) // 2

    addWin.geometry(f"{addWin_width}x{addWin_height}+{x}+{y}")
    addWin.transient(parent_window)
    addWin.grab_set()

    addCanvas = tk.Canvas(addWin, width=addWin_width, height=addWin_height, background="white",
                         scrollregion=(0, 0, 977, 1000))  # , scrollregion=(300,0,1440,2000)
    y_scroll = tk.Scrollbar(addCanvas, orient='vertical', command=addCanvas.yview)
    addCanvas.config(yscrollcommand=y_scroll.set)
    addCanvas.pack(side="left", fill="both", expand=True)

    # scrollbar
    y_scroll = tk.Scrollbar(addCanvas, orient='vertical', command=addCanvas.yview)
    y_scroll.pack(side='right', fill='y')

    addCanvas.bind_all("<MouseWheel>", lambda event: _on_mousewheel(event, addCanvas))

    #Add Applicants Widgets
    global addName, addDOB, addAddress, addTown, addZip,addSName, addLA, addHome, addDOKP, addRent
    global addLName, addRent1, addLName1, addLPhone
    global addApplicantImageFinal

    #Applicant Name
    addCanvas.create_text(130, 40, text="Applicant Name:", font=("Poppins", 16, "bold"),
                               fill="Black")
    addName = ctk.CTkEntry(addCanvas, width=649, height=25,fg_color="light gray", text_color="black")
    addCanvas.create_window(215, 30, anchor="nw", window=addName)

    #Date of Birth
    addCanvas.create_text(112, 70, text="Date of Birth:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addDOB = ctk.CTkEntry(addCanvas, width=682, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(180, 60, anchor="nw", window=addDOB)

    #Address
    addCanvas.create_text(92, 100, text="Address:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addAddress = ctk.CTkEntry(addCanvas, width=723, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(140, 90, anchor="nw", window=addAddress)

    #Town
    addCanvas.create_text(76, 130, text="Town:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addTown = ctk.CTkEntry(addCanvas, width=753, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(110, 120, anchor="nw", window=addTown)

    #Zip Code
    addCanvas.create_text(96, 160, text="Zip Code:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addZip = ctk.CTkEntry(addCanvas, width=715, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(147, 150, anchor="nw", window=addZip)

    #Spouse Name
    addCanvas.create_text(120, 220, text="Spouse Name:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addSName = ctk.CTkEntry(addCanvas, width=662, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(198, 210, anchor="nw", window=addSName)

    #Living Arrangement
    addCanvas.create_text(150, 250, text="Living Arrangement:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addLA = ctk.CTkEntry(addCanvas, width=603, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(258, 240, anchor="nw", window=addLA)

    #Home Type
    addCanvas.create_text(108, 280, text="Home Type:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addHome = ctk.CTkEntry(addCanvas, width=685, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(175, 270, anchor="nw", window=addHome)

    #Does Owner know pet
    addCanvas.create_text(161, 310, text="Does Owner know pet:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addDOKP = ctk.CTkEntry(addCanvas, width=580, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(278, 300, anchor="nw", window=addDOKP)

    #Rent Type
    addCanvas.create_text(102, 340, text="Rent Type:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addRent = ctk.CTkEntry(addCanvas, width=696, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(162, 330, anchor="nw", window=addRent)

    #Landlord Name
    addCanvas.create_text(128, 370, text="Landlord Name:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addLName = ctk.CTkEntry(addCanvas, width=647, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(212, 360, anchor="nw", window=addLName)

    #Rent Type
    addCanvas.create_text(102, 400, text="Rent Type:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addRent1 = ctk.CTkEntry(addCanvas, width=696, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(162, 390, anchor="nw", window=addRent1)

    #Landlord Name
    addCanvas.create_text(128, 430, text="Landlord Name:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addLName1 = ctk.CTkEntry(addCanvas, width=647, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(212, 420, anchor="nw", window=addLName1)

    #Landlord Phone
    addCanvas.create_text(132, 460, text="Landlord Phone:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addLPhone = ctk.CTkEntry(addCanvas, width=638, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(219, 450, anchor="nw", window=addLPhone)

    #Veterinarian Name
    addCanvas.create_text(143, 520, text="Veterinarian Name:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addVet = ctk.CTkEntry(addCanvas, width=616, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(242, 510, anchor="nw", window=addVet)

    #Allergies
    addCanvas.create_text(96, 550, text="Allergies:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addAllergies = ctk.CTkEntry(addCanvas, width=710, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(148, 540, anchor="nw", window=addAllergies)

    #Shelter History
    addCanvas.create_text(126, 580, text="Shelter History:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addSH = ctk.CTkEntry(addCanvas, width=650, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(208, 570, anchor="nw", window=addSH)

    #Indoor/Outdoor
    addCanvas.create_text(131, 610, text="Indoor/Outdoor:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addIO = ctk.CTkEntry(addCanvas, width=645, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(215, 600, anchor="nw", window=addIO)

    #Declaw
    addCanvas.create_text(89, 640, text="Declaw:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addDeclaw = ctk.CTkEntry(addCanvas, width=725, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(134, 630, anchor="nw", window=addDeclaw)

    #Child Count
    addCanvas.create_text(112, 670, text="Child Count:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addChild = ctk.CTkEntry(addCanvas, width=678, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(180, 660, anchor="nw", window=addChild)

    # Child Age
    addCanvas.create_text(102, 700, text="Child Age:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addAge = ctk.CTkEntry(addCanvas, width=701, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(158, 690, anchor="nw", window=addAge)

    #Email
    addCanvas.create_text(83, 760, text="Email:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addEmail = ctk.CTkEntry(addCanvas, width=739, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(120, 750, anchor="nw", window=addEmail)

    #Hotline No.
    addCanvas.create_text(110, 790, text="Hotline No.:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addHotline = ctk.CTkEntry(addCanvas, width=686, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(172, 780, anchor="nw", window=addHotline)

    #Cellphone No.
    addCanvas.create_text(125, 820, text="Cellphone No.:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addHotline = ctk.CTkEntry(addCanvas, width=656, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(203, 810, anchor="nw", window=addHotline)

    #Mail Address
    addCanvas.create_text(122, 850, text="Mail Address:", font=("Poppins", 16, "bold"),
                          fill="Black")
    addMail = ctk.CTkEntry(addCanvas, width=664, height=25, fg_color="light gray", text_color="black")
    addCanvas.create_window(194, 840, anchor="nw", window=addMail)

    addApplicantImagePath = Image.open("Applicants/Add.png")
    addApplicantImageResize = addApplicantImagePath.resize((126, 51))
    addApplicantImageFinal = ImageTk.PhotoImage(addApplicantImageResize)
    addApplicantButton = addCanvas.create_image(790, 950, image=addApplicantImageFinal)
    addCanvas.tag_bind(addApplicantButton, "<Button-1>", on_add_applicant_click)

def on_add_applicant_click(event=None):
    add_applicants_to_db(
        addName.get(),
        addDOB.get(),
        addAddress.get(),
        addTown.get(),
        addZip.get(),
        addSName.get(),
        addLA.get(),
        addHome.get(),
        addDOKP.get(),
        addRent.get(),
        addLName.get(),
        addRent1.get(),
        addLName1.get(),
        addLPhone.get()
    )

def _on_mousewheel(event, canvas):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
