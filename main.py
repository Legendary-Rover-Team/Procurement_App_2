import sys
import os
from fpdf import FPDF
import tkinter as tk
from  tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import date
from tkinter import scrolledtext
from pdf2docx import Converter

def popup_window():
    window = tk.Toplevel()

    label = tk.Label(window, text="Hello World!")
    label.pack(fill='x', padx=50, pady=5)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.pack(fill='x')
def CreatePDF():
    pdf = FPDF()
    pdf.set_left_margin(20)
    pdf.set_top_margin(20)
    pdf.set_right_margin(20)
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.add_font('timesnew', '', resource_path('times.ttf'), uni=True)
    pdf.add_font('timesnew', 'B', resource_path('timesbd.ttf'), uni=True)
    pdf.add_font('timesnew', 'I', resource_path('timesi.ttf'), uni=True)

    pdf.set_font('timesnew', 'B', 11)

    pdf.cell(120, 10, 'Studenckie Koło Naukowe Lotników', 0, 0, 'L')

    pdf.set_font('timesnew', '')

    pdf.cell(50, 10, entryData.get(), 0, 1, 'R')

    pdf.image(resource_path("logo_SKNL.svg"), w=30)
    pdf.ln(5)
    pdf.cell(10, 10, 'Opiekun: '+entryOpiekun.get(), 0, 1, 'L')
    pdf.cell(10, 10, 'Katedra: '+"Inżynierii Lotniczej i Kosmicznej", 0, 1, 'L')
    pdf.ln(5)

    pdf.set_font('timesnew', 'B', 14)
    pdf.cell(170, 10, 'Zamówienie publiczne', 0, 1, 'C')

    pdf.ln(2)

    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Specyfikacja produktu (opis): ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entrySpecs.get("1.0", tk.END))

    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Specyfikacja techniczna: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryTech.get("1.0", tk.END))

    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Nazwa oferty: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryNazwa1.get("1.0", tk.END))

    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Link: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryLink1.get("1.0", tk.END))

    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Cena: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryCena1.get())

    pdf.ln(10)
    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Zdjęcie: ')
    pdf.ln(10)
    pdf.set_font('timesnew', '', 11)
    pdf.image(file_path1, w=150)
    pdf.ln(10)



    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Nazwa kontroferty: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryNazwa2.get("1.0", tk.END))

    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Link: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryLink2.get("1.0", tk.END))

    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Cena: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryCena2.get())

    pdf.ln(10)
    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Zdjęcie: ')
    pdf.ln(10)
    pdf.set_font('timesnew', '', 11)
    pdf.image(file_path2, w=150)


    pdf.ln(20)
    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Ostateczny wybor oferty: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryWybor.get("1.0", tk.END))

    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Przeznaczone środki: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryPrzeznaczone.get())

    pdf.ln(10)
    pdf.set_font('timesnew', 'B', 11)
    pdf.write(10, 'Źródło finansowania: ')
    pdf.set_font('timesnew', '', 11)
    pdf.write(10, entryZrodloFin.get("1.0", tk.END))


    '''
    techniczne = ['Minimalna pojemność ogniw 2000mAh', 'Typ baterii wymagany do pracy z innymi komponentami 5/6S', 'Wtyczka zasilania XT60']

    for x in techniczne:
        pdf.cell(170, 10, '- '+x, 0, 1, 'L')

    class offers:
        name = 'aaa'
        link = 'abc.com'
        #TODO: photo
        price = 150.55
        quantity = 2

    offers_list = [offers()]

    for x in offers_list:

        pdf.cell(170, 10, 'Nazwa oferty: ' + x.name, 0, 1, 'L')
        pdf.cell(170, 10, 'link: ' + x.link, 0, 1, 'L')
        #TODO: photo here
        pdf.cell(170, 10, 'Cena: '+str(x.price) +', ilość: '+str(x.quantity)+' Suma: '+str(x.price*x.quantity)+'zł' , 0, 1, 'L')

        pdf.cell(170, 10, 'Ostateczny wybór oferty: ', 0, 1, 'L')
        pdf.multi_cell(170, 5, 'Porównując obie oferty wybrano wybrano ofertę pierwszego producenta, gdyż proponowany produkt posiada niższą cenę za asortyment o podobnych właściwościach. Ponadto są w pełni kompatybilne z silnikami które wymagają baterii 5s .', 0, 'L')

        pdf.cell(170, 10, 'Przeznaczone środki: 300zł ', 0, 1, 'L')
        pdf.cell(170, 10, 'Źródło finansowania: Środki rektorskie ', 0, 1, 'L')
    '''
    pdf.output( entryFileName.get() + '.pdf', 'F')

    pdf_file = entryFileName.get() + '.pdf'
    docx_file = entryFileName.get() + '.docx'

    # convert pdf to docx
    cv = Converter(pdf_file)
    cv.convert(docx_file)  # all pages by default
    cv.close()

def submit():
    CreatePDF()

def upload_photo1():
    global file_path1
    file_path1= filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path1:
        image = Image.open(file_path1)
        # Calculate new dimensions while maintaining aspect ratio
        width, height = image.size
        max_size = 200
        if width > height:
            new_width = max_size
            new_height = int(max_size * height / width)
        else:
            new_height = max_size
            new_width = int(max_size * width / height)
        image = image.resize((new_width, new_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        photo_label1.config(image=photo)
        photo_label1.image = photo

def upload_photo2():
    global file_path2
    file_path2 = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_path2:
        image = Image.open(file_path2)
        # Calculate new dimensions while maintaining aspect ratio
        width, height = image.size
        max_size = 200
        if width > height:
            new_width = max_size
            new_height = int(max_size * height / width)
        else:
            new_height = max_size
            new_width = int(max_size * width / height)
        image = image.resize((new_width, new_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        photo_label2.config(image=photo)
        photo_label2.image = photo

'''
def add_text_input():
    new_entry = tk.Entry(root,width=80)

    new_entry.pack()
    new_entry.grid(column=1, row=3, padx=5, pady=5)
    entry_array.append(new_entry)

def remove_text_input():
    if entry_array:
        entry_array[-1].destroy()
        entry_array.pop()
'''

# Create the main window
root = tk.Tk()
root.title("LEGENDARY Procurement App v2")


# Prevent the widgets from resizing the window
root.pack_propagate(False)

######


# Step 3: Create a Frame for Grid Layout
frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

# Step 4: Create a Canvas and Scrollbar
canvas = tk.Canvas(frame)
scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Step 5: Create a Frame for Scrollable Content
content_frame = tk.Frame(canvas)

# Step 6: Configure the Canvas and Scrollable Content Frame
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))



#####


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


logo = Image.open(resource_path("logo_legendary.png"))
logo.resize((60, 60), Image.LANCZOS)

logo_label = tk.Label(content_frame)
photoLogo = ImageTk.PhotoImage(logo)
logo_label.config(image=photoLogo)
logo_label.image = logo

logo_label.grid(column=1, row=0, sticky=tk.E, pady=5, padx=5)


label1 = tk.Label(content_frame, text="Data:")
label1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
entryData = tk.Entry(content_frame, width=30)
entryData.grid(column=1, row=0, padx=5, sticky=tk.W, pady=5)
entryData.insert(0, "Rzeszów, dnia "+date.today().strftime("%d.%m.20%yr."))


label2 = tk.Label(content_frame, text="Opiekun:")
label2.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
entryOpiekun = tk.Entry(content_frame)
entryOpiekun.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
entryOpiekun.insert(0, "dr. inż. Tomasz Lis")


label3 = tk.Label(content_frame, text="Specyfikacja produktu:")
label3.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
entrySpecs = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=70, height=5)
entrySpecs.grid(column=1, row=2, pady=10, padx=10, sticky=tk.W)

label4 = tk.Label(content_frame, text="Specyfikacja techniczna:")
label4.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
entryTech = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=70, height=5)
entryTech.grid(column=1, row=3, pady=10, padx=10, sticky=tk.W)


#entry_array = []
#add_button = tk.Button(content_frame, text="+", command=add_text_input)
#add_button.grid(column=0, row=3, sticky=tk.N, padx=5, pady=35)

#remove_button = tk.Button(content_frame, text="-", command=remove_text_input)
#remove_button.grid(column=0, row=3, sticky=tk.S, padx=5, pady=5)


upload_button1 = tk.Button(content_frame, text="Upload Photo 1", command=upload_photo1)
upload_button1.grid(column=0, row=4, pady=5, padx=5)

label4_1 = tk.Label(content_frame, text="Na zdjęciu musi być widoczna nazwa sklepu i cena. Warto dodać również zdjęcie z kosztami przesyłki")
label4_1.grid(column=1, row=4, sticky=tk.W, padx=5, pady=5)


# Create a label to display the uploaded photos in two columns
photo_label1 = tk.Label(content_frame)
photo_label1.grid(column=1, row=4, pady=5, padx=5)


label5 = tk.Label(content_frame, text="Nazwa oferty (1):")
label5.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)
entryNazwa1 = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=70, height=1)
entryNazwa1.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

label6 = tk.Label(content_frame, text="Link (1):")
label6.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
entryLink1 = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=70, height=1)
entryLink1.grid(column=1, row=7, sticky=tk.W, padx=5, pady=5)

label7 = tk.Label(content_frame, text="Cena(1)[zł]:")
label7.grid(column=0, row=11, sticky=tk.W, padx=5, pady=5)
entryCena1 = tk.Entry(content_frame, width=10)
entryCena1.grid(column=1, row=11, sticky=tk.N, padx=5, pady=5)

CzyBruttoProdukt1 = tk.StringVar

Brutto1ComboBox = ttk.Combobox(content_frame, width=27, textvariable=CzyBruttoProdukt1)
Brutto1ComboBox['values'] = ('Brutto', 'Netto')
Brutto1ComboBox.grid(column=1,row=11, sticky=tk.E, padx=5, pady=5)
Brutto1ComboBox.current(0)

label7 = tk.Label(content_frame, text="Koszt dostawy(1)[zł]:")
label7.grid(column=0, row=12, sticky=tk.W, padx=5, pady=5)
entryCenaDostawy1 = tk.Entry(content_frame, width=10)
entryCenaDostawy1.grid(column=1, row=12, sticky=tk.N, padx=5, pady=5)

CzyBruttoDostawa1 = tk.StringVar

BruttoDostawa1ComboBox = ttk.Combobox(content_frame, width=27, textvariable=CzyBruttoDostawa1)
BruttoDostawa1ComboBox['values'] = ('Brutto', 'Netto')
BruttoDostawa1ComboBox.grid(column=1,row=12, sticky=tk.E, padx=5, pady=5)
BruttoDostawa1ComboBox.current(0)



labelVAT = tk.Label(content_frame, text="VAT[%]:")
labelVAT.grid(column=0, row=17, sticky=tk.W, padx=5, pady=5)
entryVAT = tk.Entry(content_frame, width=10)
entryVAT.grid(column=1, row=17, sticky=tk.N, padx=5, pady=5)

upload_button2 = tk.Button(content_frame, text="Upload Photo 2", command=upload_photo2)
upload_button2.grid(column=0, row=19, pady=5, padx=5)

photo_label2 = tk.Label(content_frame)
photo_label2.grid(column=1, row=19, pady=5, padx=5)


label8 = tk.Label(content_frame, text="Nazwa oferty (2):")
label8.grid(column=0, row=22, sticky=tk.W, padx=5, pady=5)
entryNazwa2 = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=70, height=1)
entryNazwa2.grid(column=1, row=22, sticky=tk.W, padx=5, pady=5)

label9 = tk.Label(content_frame, text="Link (2):")
label9.grid(column=0, row=25, sticky=tk.W, padx=5, pady=5)
entryLink2 = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=70, height=1)
entryLink2.grid(column=1, row=25, sticky=tk.W, padx=5, pady=5)

label10 = tk.Label(content_frame, text="Cena(2)[zł]:")
label10.grid(column=0, row=28, sticky=tk.W, padx=5, pady=5)
entryCena2 = tk.Entry(content_frame, width=10)
entryCena2.grid(column=1, row=28, sticky=tk.N, padx=5, pady=5)

CzyBruttoProdukt2 = tk.StringVar

Brutto2ComboBox = ttk.Combobox(content_frame, width=27, textvariable=CzyBruttoProdukt2)
Brutto2ComboBox['values'] = ('Brutto', 'Netto')
Brutto2ComboBox.grid(column=1,row=28, sticky=tk.E, padx=5, pady=5)
Brutto2ComboBox.current(0)

label7 = tk.Label(content_frame, text="Koszt dostawy(2)[zł]:")
label7.grid(column=0, row=30, sticky=tk.W, padx=5, pady=5)
entryCenaDostawy2 = tk.Entry(content_frame, width=10)
entryCenaDostawy2.grid(column=1, row=30, sticky=tk.N, padx=5, pady=5)

CzyBruttoDostawa2 = tk.StringVar

BruttoDostawa2ComboBox = ttk.Combobox(content_frame, width=27, textvariable=CzyBruttoDostawa2)
BruttoDostawa2ComboBox['values'] = ('Brutto', 'Netto')
BruttoDostawa2ComboBox.grid(column=1,row=30, sticky=tk.E, padx=5, pady=5)
BruttoDostawa2ComboBox.current(0)


label11 = tk.Label(content_frame, text="Wybór oferty:")
label11.grid(column=0, row=31, sticky=tk.W, padx=5, pady=5)
entryWybor = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=70, height=5)
entryWybor.grid(column=1, row=31, sticky=tk.W, padx=5, pady=5)
entryWybor.insert(tk.INSERT, "Ze względu na korzystniejszą ofertę cenową lub dostępność wygrała oferta")

label12 = tk.Label(content_frame, text="Przeznaczone środki:")
label12.grid(column=0, row=34, sticky=tk.W, padx=5, pady=5)
entryPrzeznaczone = tk.Entry(content_frame, width=10)
entryPrzeznaczone.grid(column=1, row=34, sticky=tk.W, padx=5, pady=5)

label12_1 = tk.Label(content_frame, text="Tutaj wpisujemy przeznaczone środki na zamówienie (suma z wybranej oferty + sensowny naddatek \n"
                                           " (zazwyczaj 20-30% np. wyszło 109,35 to dajemy 140, bo inflacja, zmiany cen itd.)")
label12_1.grid(column=1, row=35, sticky=tk.W, padx=5, pady=5)

label13 = tk.Label(content_frame, text="Źródło finansowania:")
label13.grid(column=0, row=37, sticky=tk.W, padx=5, pady=5)
entryZrodloFin = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, width=70, height=1)
entryZrodloFin.grid(column=1, row=37, sticky=tk.W, padx=5, pady=5)

label14 = tk.Label(content_frame, text="Nazwa pliku (.pdf / .docx):")
label14.grid(column=0, row=40, sticky=tk.W, padx=5, pady=5)
entryFileName = tk.Entry(content_frame, width=50)
entryFileName.grid(column=1, row=40, padx=5, sticky=tk.W, pady=5)


submit_button = tk.Button(content_frame, text="Stwórz pliki .pdf oraz .docx", command=submit)
submit_button.grid(sticky=tk.W, column=1, row=44, padx=5, pady=5)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Step 9: Pack Widgets onto the Window
canvas.create_window((0, 0), window=content_frame, anchor="nw")
canvas.grid(row=0, column=0, sticky="nsew")
scrollbar.grid(row=0, column=1, sticky="ns")



# Step 10: Bind the Canvas to Mousewheel Events
def _on_mousewheel(event):
   canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)


# Configure minimum and maximum window size
root.minsize(800, 600)
root.maxsize(1920, 1080)

win = tk.Toplevel(root)
win.wm_title("Uwaga!")

l = tk.Label(win, text="Aplikacja działa tylko dla pojedyńczych zamówień.\n"
                       "Nie pozwala złożyć zamówienia na kilka przedmiotów z jednego sklepu naraz.\n"
                        "Opiekunem programu jest Krystian Sołtys, w sprawie poprawek zapraszam do kontaktu\n"
                        "na Messenger / Discord.")
l.pack(fill="x")

b = tk.Button(win, text="OK", command=win.destroy)
b.pack(fill="x")


win.attributes('-topmost',True)
# Start the GUI event loop
root.mainloop()

