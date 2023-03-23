from fpdf import FPDF 
 
pdf = FPDF() 

pdf.set_top_margin(20)

pdf.add_page() 

pdf.set_font("Times", size = 15) 

f = open("wasteco.txt", "r") 
MyList = []
PageNumber = 0

for x in f:
    if (PageNumber < CurrentPageNumber):
        PageNumber = PageNumber + 1
        pdf.image(r'C:\Users\ngo\Downloads\logo.png', x = 0, y = 0, w = 75, h = 20.5)
    MyList = x.split()
    CurrentPageNumber = pdf.page_no()
    pdf.multi_cell(190, 10, txt = x)
    for i in MyList:
        if (i == "*-*"):
            pdf.add_page()
    

pdf.output("BeeMovie.pdf") 

