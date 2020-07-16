from tkinter import *
from tkinter import Label
from PIL import ImageTk, Image

from io import BytesIO
import requests
import tkinter.font as font


class News:
	def __init__(self):
		self.root =Tk()

		self.root.title("News Application")
		self.root.minsize(500, 600)
		self.root.maxsize(1540, 800)

		self.root.configure(background="#ceff0a")

		self.myFont = font.Font(family='Comic Sans MS', size=10, weight='bold')

		self.label = Label(self.root, text="Apnanews 24 * 7", bg="#ceff0a")
		self.label.configure(font=("Comic Sans MS", 30, "bold"))
		self.label.pack(pady=(50, 50))

		self.label1 = Label(self.root, text="Enter the topic", bg="#ceff0a")
		self.label1.configure(font=("Comic Sans MS", 15, "italic"))
		self.label1.pack(pady=(50, 20))


		self.topic = Entry(self.root)
		self.topic.pack(pady=(15, 10), ipadx=30, ipady=3)

		self.click = Button(self.root, text="Search", bg="#7d9c00", fg="white",command=lambda: self.fetch())
		self.click['font']=self.myFont
		self.click.pack(pady=(5, 10))

		self.root.mainloop()

	def fetch(self):
		# fetch the search
		term = self.topic.get()
		url = "https://newsapi.org/v2/everything?q={}&apiKey=1cdb329f317c4c2ab304ceda59bac177".format(term)
		# hit the api
		response = requests.get(url)
		self.response = response.json()
		#print(self.response)
		self.data=self.response['articles']
		self.extract()


	def extract(self, index=0):
		news = []
		news.append(self.data[index]['title'])
		news.append(self.data[index]['source']['name'])
		news.append(self.data[index]['description'])
		news.append(self.data[index]['urlToImage'])



		self.clear()
		self.display(news, index=index)


	def display(self,news,index):


		img_response = requests.get(news[3])
		img_data = img_response.content
		img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
		imglabel = Label(self.root, image=img)
		imglabel.image=img
		imglabel.pack(pady=(5,5), side='top')


		title = Label(self.root,text=news[0],fg="#9B59B6",bg="#ceff0a")
		title.pack(pady=(5,5),padx=(2, 2))

		source = Label(self.root, text=news[1], fg="black", bg="#ceff0a")
		source.pack(pady=(5,5),padx=(2, 2))


		desc = Label(self.root, text=news[2], fg="black", bg="#ceff0a")
		desc.pack(pady=(5,5),padx=(2, 2))


		frame=Frame(self.root)
		frame.pack()


		if index!=0:

			previous=Button(frame, text="Previous",fg="white",bg="#7d9c00", command=lambda: self.extract(index=index-1))
			previous['font']=self.myFont
			previous.pack(side="left")
		if index!=19:
			next=Button(frame, text="Next",fg="white",bg="#7d9c00", command=lambda: self.extract(index=index+1))
			next['font']=self.myFont
			next.pack(side="right")





	def clear(self):
		for i in self.root.pack_slaves():
			i.destroy()



obj=News()