import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox


#Create connection
def connect_db():
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='Admincatsko123',
            database='catsko'
        )
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

#Search base on App ID
def display_single_record(app_id, result_frame):
    import tkinter as tk
    if not app_id:
        messagebox.showwarning("Input Error", "Please enter an App ID.")
        return

    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                SELECT App_ID, App_Name, DOB, Temp_Address, Town, Zip, Email,
                       H_Phone, C_Phone, M_Address, S_Name, Living_Arr,
                       Home_Type, Know_Pet, Rent_Type, Landlord_Name,
                       Landlord_Phone, Vet_Name, Allergies, Shel_History,
                       In_Out, Declaw, Child_Count, Child_Age
                FROM applicant
                WHERE App_ID = %s
            """
            cursor.execute(query, (app_id,))
            record = cursor.fetchone()

            # Clear previous widgets
            for widget in result_frame.winfo_children():
                widget.destroy()

            if record:
                card = tk.Frame(result_frame, bg="#F8F8F8", bd=1, relief="solid")
                card.pack(pady=10, padx=10, fill="x")

                # Header
                header = tk.Frame(card, bg="#D9D9D9", height=30)
                header.pack(fill="x")
                tk.Label(header, text=f"{record[0]:>03}", font=("Arial", 10, "bold"), bg="#D9D9D9").pack(side="left", padx=10)
                tk.Label(header, text=record[1], font=("Arial", 10, "bold"), bg="#D9D9D9").pack(side="left", padx=5)

                # Body
                body = tk.Frame(card, bg="#F8F8F8")
                body.pack(fill="both", expand=True, padx=10, pady=5)

                def add_label(frame, label, value, row, col):
                    tk.Label(frame, text=f"{label}:", font=("Arial", 10, "bold"), bg="#F8F8F8").grid(row=row, column=col*2, sticky="w", padx=5, pady=2)
                    tk.Label(frame, text=value or "N/A", font=("Arial", 10), bg="#F8F8F8").grid(row=row, column=col*2+1, sticky="w", padx=5, pady=2)

                labels = [
                    ("Applicant Name", record[1]),
                    ("Date of Birth", record[2]),
                    ("Address", record[3]),
                    ("Town", record[4]),
                    ("Zip Code", record[5]),
                    ("Spouse Name", record[10]),
                    ("Living Arrangement", record[11]),
                    ("Home Type", record[12]),
                    ("Does Owner know pet", record[13]),
                    ("Rent Type", record[14]),
                    ("Landlord Name", record[15]),
                    ("Landlord Phone", record[16]),
                ]

                for i, (label, value) in enumerate(labels):
                    add_label(body, label, value, i // 2, i % 2)
            else:
                messagebox.showinfo("Not Found", "No record found for this App ID.")

        except Error as e:
            messagebox.showerror("Database Error", f"Error accessing database: {str(e)}")
        finally:
            conn.close()


def display_all_records(result_frame):
    #import tkinter as tk
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                SELECT App_ID, App_Name, DOB, Temp_Address, Town, Zip, Email,
                       H_Phone, C_Phone, M_Address, S_Name, Living_Arr,
                       Home_Type, Know_Pet, Rent_Type, Landlord_Name,
                       Landlord_Phone, Vet_Name, Allergies, Shel_History,
                       In_Out, Declaw, Child_Count, Child_Age
                FROM applicant
            """
            cursor.execute(query)
            results = cursor.fetchall()

            # Clear previous display
            for widget in result_frame.winfo_children():
                widget.destroy()

            y = 0  # Y-position tracker

            for record in results:
                card = tk.Frame(result_frame, bg="#F8F8F8", bd=1, relief="solid")
                card.grid(row=y, column=0, pady=10, padx=5, sticky="ew")

                # Header
                header = tk.Frame(card, bg="#D9D9D9", height=30)
                header.pack(fill="x")
                tk.Label(header, text=f"{record[0]:>03}", font=("Arial", 10, "bold"), bg="#D9D9D9").pack(side="left", padx=10)
                tk.Label(header, text=record[1], font=("Arial", 10, "bold"), bg="#D9D9D9").pack(side="left", padx=5)

                # Body
                body = tk.Frame(card, bg="#F8F8F8")
                body.pack(fill="both", expand=True, padx=10, pady=5)

                def add_label(frame, label, value, row, col):
                    tk.Label(frame, text=f"{label}:", font=("Arial", 10, "bold"), bg="#F8F8F8").grid(row=row, column=col*2, sticky="w", padx=5, pady=2)
                    tk.Label(frame, text=value or "N/A", font=("Arial", 10), bg="#F8F8F8").grid(row=row, column=col*2+1, sticky="w", padx=5, pady=2)

                labels = [
                    ("Applicant Name", record[1]),
                    ("Date of Birth", record[2]),
                    ("Address", record[3]),
                    ("Town", record[4]),
                    ("Zip Code", record[5]),
                    ("Spouse Name", record[10]),
                    ("Living Arrangement", record[11]),
                    ("Home Type", record[12]),
                    ("Does Owner know pet", record[13]),
                    ("Rent Type", record[14]),
                    ("Landlord Name", record[15]),
                    ("Landlord Phone", record[16]),
                ]

                for i, (label, value) in enumerate(labels):
                    add_label(body, label, value, i // 2, i % 2)

                y += 1

        except Error as e:
            messagebox.showerror("Database Error", f"Error accessing database: {str(e)}")
        finally:
            conn.close()
