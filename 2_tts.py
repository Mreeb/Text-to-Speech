from gtts import gTTS  # FOR GOOGLE TEXT TO SPEECH RECOGNITION
import os
import PyPDF2 as reader  # PYTHON PDF READER LIBRARY

bookName = "sample.pdf"

try:
    os.mkdir(bookName.split('.')[0])  # FOR MAKING A NEW DIRECTORY
except:
    pass

with open(bookName, "rb") as file:
    pdf = reader.PdfFileReader(file)
    print("PDF Contains {} Pages.\n".format(pdf.numPages))  # FINDING TOTAL NUMBER OF PAGES
    os.chdir(bookName.split(".")[0])
    for page_no in range(pdf.numPages):  # ITERATING THROUGH PAGES
        page = pdf.getPage(page_no)
        text = page.extractText()  # EXTRACTING TEXT FROM PAGE
        tts = gTTS(text=text, lang='en', tld='co.uk', slow=False)  # TEXT TO SPEECH
        audio_file = f"{str(page_no)}.mp3"  # SAVING AUDIO FILE
        tts.save(audio_file)
    p = input("Enter The page no you want to listen to : ")
    audio_ = f"{str(p)}.mp3"
    os.system(audio_)  # READING AUDIO FILE
