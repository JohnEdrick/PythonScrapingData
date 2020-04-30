from tkinter import *
import datetime
import requests
from bs4 import BeautifulSoup


class main:

    def __init__(self):
        self.res = requests.get('https://news.google.com/covid19/map?hl=en-PH&gl=PH&ceid=PH:en')
        soup = BeautifulSoup(self.res.text, 'html.parser')
        link = soup.select(".UvMayb")
        covid_list = []
        for a in link:
            covid_list.append(a.text.strip())
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S %D")

        # Window
        self.window = Tk()
        self.window.title("COVID-19 CORONAVIRUS PANDEMIC")
        self.window.geometry("360x230")
        # Title
        self.label_title = Label(self.window, text="Worldwide", font=("Arial", 20))
        self.label_title.place(x=100, y=18)

        # Label Total
        self.label_title = Label(self.window, text="Total:", font=("Arial", 15))
        self.label_title.place(x=60, y=60)
        self.label_title = Label(self.window, text=covid_list[0], font=("Arial", 15), fg="white", bg="red")
        self.label_title.place(x=180, y=60)

        # Label Recovered
        self.label_title = Label(self.window, text="Recovered:", font=("Arial", 15))
        self.label_title.place(x=60, y=90)
        self.label_title = Label(self.window, text=covid_list[1], font=("Arial", 15), fg="white", bg="green")
        self.label_title.place(x=180, y=90)

        # Label Deaths
        self.label_title = Label(self.window, text="Deaths:", font=("Arial", 15))
        self.label_title.place(x=60, y=120)
        self.label_title = Label(self.window, text=covid_list[2], font=("Arial", 15), fg="white", bg="black")
        self.label_title.place(x=180, y=120)

        # Label Time
        self.label_time = Label(self.window, text=f"As of: {current_time}     Source: news.google.com ",
                                font=("Arial", 11))
        self.label_time.place(x=0, y=210)

        # Quit Button
        self.button_quit = Button(self.window, text="Quit", command=self.window.quit)
        self.button_quit.place(x=290, y=165)
        self.window.mainloop()


if __name__ == '__main__':
    main()
