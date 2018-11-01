from fpdf import Template
from datetime import date
import os,time
def print_sticker(book_name, address1,address2,country,phone,total,books):

  if(len(address1)>25):
    address1=address1[0:23]+".."
  elements = [
    { 'name': 'bg', 'type': 'I', 'x1': 0, 'y1': 0, 'x2': 100, 'y2': 150, 'font': None, 'size': 0.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': 'logo', 'priority': 1, },
  { 'name': 'name', 'type': 'T', 'x1': 5, 'y1': 27, 'x2': 90, 'y2': 33, 'font': 'helvetica', 'size': 13.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'address1', 'type': 'T', 'x1': 20, 'y1': 33, 'x2': 90, 'y2': 40, 'font': 'helvetica', 'size': 8.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'address2', 'type': 'T', 'x1': 20, 'y1': 38, 'x2': 90, 'y2': 45, 'font': 'helvetica', 'size': 8.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'city', 'type': 'T', 'x1': 20, 'y1': 43, 'x2': 90, 'y2': 50, 'font': 'helvetica', 'size': 8.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'phone', 'type': 'T', 'x1': 17, 'y1': 48, 'x2': 90, 'y2': 55, 'font': 'helvetica', 'size': 8.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
  {'name': 'addresstext', 'type': 'T', 'x1': 5, 'y1': 33, 'x2': 0, 'y2': 40, 'font': 'helvetica', 'size': 8.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'phonetext', 'type': 'T', 'x1': 5, 'y1': 48, 'x2': 0, 'y2': 55, 'font': 'helvetica', 'size': 8.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
  { 'name': 'date', 'type': 'T', 'x1': 66, 'y1': 8, 'x2': 0, 'y2': 0, 'font': 'helvetica', 'size': 11.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
  { 'name': 'totaltext', 'type': 'T', 'x1': 63, 'y1': 23, 'x2': 0, 'y2': 0, 'font': 'helvetica', 'size': 9.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
  { 'name': 'total', 'type': 'T', 'x1': 75, 'y1': 23, 'x2': 0, 'y2': 0, 'font': 'helvetica', 'size': 9.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
    { 'name': 'booktext', 'type': 'T', 'x1': 63, 'y1': 40, 'x2': 0, 'y2': 0, 'font': 'helvetica', 'size': 10.0, 'bold': 1, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text': '', 'priority': 2, },
  ]
  initial_margin = 50
  for book in books:
      name= book[0]
      if(len(name)>22):
        name=name[0:20]+".."
      name = "("+str(book[1])+") "+ name
      elements.append({ 'name': 'books'+str(initial_margin), 'type': 'T', 'x1': 60, 'y1': initial_margin, 'x2': 0, 'y2': 0, 'font': 'helvetica', 'size': 8.0, 'bold': 0, 'italic': 0, 'underline': 0, 'foreground': 0, 'background': 0, 'align': 'I', 'text':name, 'priority': 2, })
      initial_margin+=10
  f = Template(format=(100, 150), elements=elements)
  f.add_page()

  f["bg"] = "./bg.jpg"
  f["name"]=book_name
  f['address1']=address1
  f['address2']=address2
  f['city']=country
  f['phone']=phone
  f['date']=str(date.today())
  f['total']=total
  #static texts
  f['addresstext']="ADDRESS:"
  f['phonetext']="PHONE:"
  f['booktext']="BOOK/S"
  f['totaltext']="TOTAL:"
  filename = 'latest-print'+".pdf"
  f.render(filename)
  os.startfile(filename, "print")