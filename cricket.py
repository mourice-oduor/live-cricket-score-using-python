from tkinter import *
import time
import requests
import json


cricket=Tk()
cricket.title("My Live Cricket Scores")

cricket.geometry("600x200")


match_data=requests.get('http://cricapi.com/api/cricketScore?unique_id=1201947&apikey=q5eB6MBPQkSKlbrXmzqL40oYUoT2')
json_data=match_data.json()

def times():
	current_score=json_data['stat']
	score.configure(text="current score :  "+current_score)
	score.after(200,times)
	

score=Label(cricket,font=("time",15,"bold"),fg="red", bg="blue")
score.grid(row=2,column=2,pady=25,padx=100)
times()

live=Label(cricket,text="LIVE CRICKET SCORES",font=("italics 24 bold"),fg="green")
live.grid(row=0,column=2)


cricket.mainloop()
