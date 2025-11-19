import tkinter as tk
from tkinter import messagebox
import mysql.connector

# ------------------ Database Setup ------------------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          # change to your MySQL username
        password="yourpassword",  # change to your MySQL password
        database="login_db"       # database name
    )
    cursor = conn.cursor()
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(50) PRIMARY KEY,
            password VARCHAR(50) NOT NULL
        )
    """)
    # Insert default user if not exists
    cursor.execute("SELECT * FROM users WHERE username=%s", ("admin",))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", ("admin", "1234"))
        conn.commit()
except mysql.connector.Error as e:
    messagebox.showerror("Database Error", str(e))
finally:
    conn.close()

# ------------------ GUI Setup ------------------
root = tk.Tk()
root.title("Login Application")    
root.geometry("400x250")

tk.Label(root, text="Username:", font=("Times New Roman", 14)).grid(row=0, column=0, padx=10, pady=15)
entry_user = tk.Entry(root, font=("Times New Roman", 12))
entry_user.grid(row=0, column=1, padx=10, pady=15)

tk.Label(root, text="Password:", font=("Times New Roman", 14)).grid(row=1, column=0, padx=10, pady=15)
entry_pass = tk.Entry(root, font=("Times New Roman", 12), show="*")
entry_pass.grid(row=1, column=1, padx=10, pady=15)

msg_label = tk.Label(root, text="", font=("Times New Roman", 12))
msg_label.grid(row=3, column=0, columnspan=2, pady=10)

# ------------------ Login Logic ------------------
attempts = 2

def user_submitted():
    global attempts
    username = entry_user.get()
    password = entry_pass.get()

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root", 
            password="yourpassword",
            database="login_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", str(e))
        return
    finally:
        conn.close()

    if result:
        msg_label.config(text="Login Successful!", fg="green")
        entry_user.config(state="disabled")
        entry_pass.config(state="disabled")
    else:
        attempts -= 1
        if attempts > 0:
            msg_label.config(text=f"Invalid Credentials! {attempts} attempts left.", fg="red")
        else:
            msg_label.config(text="No attempts left! Login blocked.", fg="red")
            submit_btn.config(state="disabled")

# Submit button
submit_btn = tk.Button(root, text="Submit", font=("Times New Roman", 12), command=user_submitted)
submit_btn.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
