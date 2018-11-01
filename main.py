from tkinter import *
from selenium import webdriver
from stick_print import print_sticker
import re

url="your-url.com"
driver = webdriver.Chrome()  
driver.get(url)
root = Tk()
root.title("Satkar's amazing sticker printer")
def callBack():
    total = driver.find_element_by_xpath("//tr[@class='3']/td[@class='emph']/strong/span").text
    info=driver.find_elements_by_xpath("//div[@class='entry-edit']/fieldset/address")[1].text
    shipping_details =info.split('\n')
    orders = [[r.text,r.find_element_by_xpath("//table[@class='qty-table']/tbody/tr/td[2]").text] for r in driver.find_elements_by_xpath("//table[@class='data order-tables']/tbody//h5[@class='title']")]
    phone = re.search( r'(.*)T: [0-9]*', info, re.M|re.I).group()[3::]
    print_sticker(shipping_details[0],shipping_details[1],shipping_details[2],shipping_details[3],phone,total,orders)

root.geometry("300x100")
B = Button(root,padx="20",pady="20", text = "Print Bookworm Sticker", command = callBack)
B.place(x = 60,y =20)
var = StringVar()
label = Label( root, textvariable = var)

var.set("Log in and view the order. Then, click this print button.")
label.pack()
root.mainloop()