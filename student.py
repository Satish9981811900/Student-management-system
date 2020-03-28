from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class student:
	def __init__(self,root):
		self.root=root
		self.root.title("Student Management System")
		self.root.geometry("1350x700+0+0")
	
		title=Label(self.root,text="Student	Management System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd=5,relief=GROOVE)
		title.pack(side=TOP,fill=X)

		########     Variable     ######
		self.Roll_No_var=StringVar()
		self.Name_var=StringVar()
		self.Email_var=StringVar()
		self.Gender_var=StringVar()
		self.Contact_var=StringVar()
		self.DOB_var=StringVar()	

		self.search_by=StringVar()
		self.search_txt=StringVar()
#=============================================manage frame=========================================	
		Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="sky blue")
		Manage_Frame.place(x=10,y=80,width=450,height=600)
		
		m_title=Label(Manage_Frame,text="Manage Student",bg="sky blue",fg="white",font=("times new roman",30,"bold"))
		m_title.grid(row=0,columnspan=2,pady=20)		
######################################################	Roll number	
		
		m_roll=Label(Manage_Frame,text="Roll Number :",font=("times new roman",20,"bold"),bg="sky blue",fg="white",bd=2)
		m_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
		
		txt_roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=1,textvariable=self.Roll_No_var)
		txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")
############################################################################# name
		m_name=Label(Manage_Frame,text="Full Name :",font=("times new roman",20,"bold"),bg="sky blue",fg="white",bd=2)
		m_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")
		
		txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=1,textvariable=self.Name_var)
		txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
################################################################### Email
		m_email=Label(Manage_Frame,text="Email :",font=("times new roman",20,"bold"),bg="sky blue",fg="white",bd=2)
		m_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
		
		txt_email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=1,textvariable=self.Email_var)
		txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")
######################################################################### Gender
		m_gender=Label(Manage_Frame,text="Gender :",font=("times new roman",20,"bold"),bg="sky blue",fg="white",bd=2)
		m_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

		combo_gender=ttk.Combobox(Manage_Frame,width=19,font=("times new roman",15,"bold"),state="readonly",textvariable=self.Gender_var)
		combo_gender['values']=("Male","Female","other")
		combo_gender.grid(row=4,column=1,padx=20,pady=10,sticky="w")
	
#################################### contact
		m_contact=Label(Manage_Frame,text="Contact No.:",font=("times new roman",20,"bold"),bg="sky blue",fg="white",bd=2)
		m_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")
		
		txt_contact=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=1,textvariable=self.Contact_var)
		txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")
		####################################### DOB
		m_dob=Label(Manage_Frame,text="Date of Birth :",font=("times new roman",20,"bold"),bg="sky blue",fg="white",bd=2)
		m_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")
		
		txt_dob=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=1,textvariable=self.DOB_var)
		txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")
		######################################  ADdress
		m_address=Label(Manage_Frame,text="Address :",font=("times new roman",20,"bold"),bg="sky blue",fg="white",bd=2)
		m_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

		self.txt_address=Text(Manage_Frame,width=25,height=4)
		self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
#######t########  manage button ########################

		btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="sky blue")
		btn_Frame.place(x=10,y=530,width=420,height=50)




		add_btn=Button(btn_Frame,text="Add",width=8,command=self.add_students).grid(row=0,column=0,padx=5,pady=5)
		update_btn=Button(btn_Frame,text="Update",width=8,command=self.update_data).grid(row=0,column=1,padx=5,pady=5)
		delete_btn=Button(btn_Frame,text="Delete",width=8,command=self.delete_data).grid(row=0,column=2,padx=5,pady=5)
		clear_btn=Button(btn_Frame,text="Clear",width=8,command=self.clear).grid(row=0,column=3,padx=5,pady=5)	


#=============================================Detail frame=========================================	
		Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="sky blue")
		Detail_Frame.place(x=480,y=80,width=800,height=600)

		search=Label(Detail_Frame,text="Search By",bg="sky blue",fg="white",font=("times new roman",20,"bold"))
		search.grid(row=0,column=0,pady=20)

		combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",15,"bold"),state="readonly",textvariable=self.search_by)
		combo_search['values']=("roll_no","name","contact")
		combo_search.grid(row=0,column=1,padx=13,pady=10,sticky="w")

		txt_search=Entry(Detail_Frame,font=("times new roman",15,"bold"),bd=1,textvariable=self.search_txt)
		txt_search.grid(row=0,column=2,pady=10,padx=25,sticky="w")
	
		search_btn=Button(Detail_Frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=5,pady=10)
		show_btn=Button(Detail_Frame,text="Show All",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

		Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="white")
		Table_Frame.place(x=4,y=70,width=785,height=520)
	
		scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)	
		self.student_table=ttk.Treeview(Table_Frame,columns=("Roll No.","Name","Email","Gender","Contact","D.O.B","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)
		scroll_x.config(command=self.student_table.xview)
		scroll_y.config(command=self.student_table.yview)
##############################
		self.student_table.heading("Roll No.",text="Roll No.")
		self.student_table.heading("Name",text="Name")
		self.student_table.heading("Email",text="Email")
		self.student_table.heading("Gender",text="Gender")
		self.student_table.heading("Contact",text="Contact")
		self.student_table.heading("D.O.B",text="D.O.B")
		self.student_table.heading("Address",text="Address")
		self.student_table['show']='headings'
	
		self.student_table.column("Roll No.",width=100)
		self.student_table.column("Name",width=100)
		self.student_table.column("Email",width=100)
		self.student_table.column("Gender",width=100)
		self.student_table.column("Contact",width=100)
		self.student_table.column("D.O.B",width=100)
		self.student_table.column("Address",width=150)
		self.student_table.pack(fill=BOTH,expand=1)
		self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
		self.fetch_data()
##################################	

	def add_students(self):
		if self.Roll_No_var.get()=="" or self.Name_var.get()=="":
			messagebox.showerror("Error","Roll Number is required !")
		else:
			con=pymysql.connect(host="localhost",user="root",password="",database="sms")
			cur=con.cursor()
			cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
													self.Roll_No_var.get(),
													self.Name_var.get(),
													self.Email_var.get(),
													self.Gender_var.get(),
													self.Contact_var.get(),
													self.DOB_var.get(),
													self.txt_address.get('1.0',END)			
													))
			con.commit()
			self.fetch_data()
			self.clear()
			con.close()
			#messagebox.showinfo("success","values are inserted")
	def fetch_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="sms")
		cur=con.cursor()
		cur.execute("select *from students")
		rows=cur.fetchall()
		if len(rows):
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert('',END,values=row)
			con.commit()
		con.close()
	def clear(self):
		self.Roll_No_var.set(" ")
		self.Name_var.set("")
		self.Email_var.set("")
		self.Gender_var.set("")
		self.Contact_var.set("")
		self.DOB_var.set("")
		self.txt_address.delete('1.0',END)
	def get_cursor(self,ev):
		cursor_row=self.student_table.focus()
		contents=self.student_table.item(cursor_row)
		row=contents['values']
		self.Roll_No_var.set(row[0])
		self.Name_var.set(row[1])
		self.Email_var.set(row[2])
		self.Gender_var.set(row[3])
		self.Contact_var.set(row[4])
		self.DOB_var.set(row[5])
		self.txt_address.delete('1.0',END)
		self.txt_address.insert(END,row[6])
	def update_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="sms")
		cur=con.cursor()
		cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
												
												self.Name_var.get(),
												self.Email_var.get(),
												self.Gender_var.get(),
												self.Contact_var.get(),
												self.DOB_var.get(),
												self.txt_address.get('1.0',END),
												self.Roll_No_var.get()		
												))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()
	def delete_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="sms")
		cur=con.cursor()
		cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
		con.commit()
		con.close()
		self.fetch_data()
		self.clear()
	def search_data(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="sms")
		cur=con.cursor()
		cur.execute("select *from students where " +str(self.search_by.get())+ "=" "'"+str(self.search_txt.get())+"'")
		rows=cur.fetchall()
		if len(rows)!=0:
			self.student_table.delete(*self.student_table.get_children())
			for row in rows:
				self.student_table.insert('',END,values=row)
			con.commit()
		con.close()
	'''def roll(self):
		con=pymysql.connect(host="localhost",user="root",password="",database="sms")
		cur=con.cursor()
		cur.execute("select roll_no from students ")
		rows=cur.fetchall()
		if self.Roll_No_var.get() in rows:
			messagebox.showerror("Error","this roll number is already inserted")'''

		

	
###############        Functions  #########################
root = Tk()
ob=student(root)
root.mainloop()
 
