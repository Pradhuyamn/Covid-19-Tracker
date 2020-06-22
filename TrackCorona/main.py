import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
import threading

def get_html_data(url):
    data = requests.get(url)
    return data

def get_corona_detail_of_india():
    url="https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text,"html.parser")
    info_div = bs.find("div", class_="site-stats-count").find_all("li")
    all_details = ""
    for block in info_div:
        count = block.find("strong").get_text()
        text = block.find("span").get_text()
        all_details=all_details+text+" : "+count+"\n"
        if text == "Migrated":
            return all_details


#function used to reload the data from website
def refresh():
    newdata = get_corona_detail_of_india()
    print("Refreshing....")
    mainLabel['text'] = newdata



#Function for Notification
def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID-19",
            message=get_corona_detail_of_india(),
            timeout=10,
            # app_icon='icon.ico'
        )
        time.sleep(30)



#Creating GUI:
root = tk.Tk()
root.geometry("900x800")
root.title("Track Corona - INDIA")
root.configure(background='white')
f = ("poppins", 25, "bold")
#Adding Images to GUI
#banner = tk.PhotoImage(file="download.png")
#bannerLabel = tk.Label(root, image=banner)
#bannerLabel.pack()
mainLabel = tk.Label(root, text=get_corona_detail_of_india(), font=f)
mainLabel.pack()

#Create a new Thread
th1 = threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

reBtn = tk.Button(root, text="REFRESH", font=f, relief='solid', command=refresh)
reBtn.pack()
root.mainloop()









