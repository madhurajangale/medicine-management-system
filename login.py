from tkinter import *
import psycopg2

def signin():
    check_credentials()

def check_credentials():
    username = user.get()
    password = code.get()

    connection = None
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            user="postgres",
            password="7177",
            host="localhost",
            port="5432",
            database="register"
        )

        cursor = connection.cursor()

        # Query to check if the username and password match in the table
        check_query = "SELECT * FROM user_data WHERE username = %s AND password = %s"
        data = (username, password)

        cursor.execute(check_query, data)
        result = cursor.fetchone()

        if result:
            print("Login successful!")
        else:
            print("Incorrect username or password!")

    except Exception as error:
        print(f"Error: {error}")

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()

# Your existing code continues...


from tkinter import*
root = Tk()

root.title('login')
root.geometry('950x500+300+200')
root.configure(bg="#DCF2F1")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
   

img = PhotoImage(file='login3.png')
Label(root,image=img,bg='#DCF2F1').place(x=2,y=50)

frame=Frame(root,width=300,height=350,bg="#365486")
frame.place(x=620,y=70)

heading=Label(frame,text='Welcome!',fg="#DCF2F1",bg="#365486",font=('Microsoft yaHei UI Light',23,'bold'))
heading.place(x=36,y=20)

def on_enter(e):
    user.delete(0, 'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')
        

user=Entry(frame,width=25,fg="#DCF2F1",border=0,bg="#365486",font=('Microsoft yaHei UI Light',11))
user.place(x=45,y=90)
user.insert(0,'username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=200,height=2,bg="#DCF2F1").place(x=40,y=117)


def on_enter(e):
    code.delete(0, 'end')
    
def on_leave(e):
    name=code.get()
    if name=='':
       code.insert(0,'password')

code=Entry(frame,width=25,fg="#DCF2F1",border=0,bg="#365486",font=('Microsoft yaHei UI Light',11))
code.place(x=45,y=160)
code.insert(0,'password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=200,height=2,bg="#DCF2F1").place(x=40,y=187)

Button(frame,width=28,pady=7,text='Login',bg="#0F1035",fg="#DCF2F1",border=0,command=check_credentials).place(x=40,y=234)
label=Label(frame,text="Create a New Account",fg="#DCF2F1",bg="#365486",font=('Microsoft yaHei UI Light',10))
label.place(x=72,y=280)

login=Button(frame,width=6,text='Login',border=0,bg="#DCF2F1",cursor='hand2',fg="#0F1035",command=signin)

root.mainloop()
