import pyttsx3
import PyPDF2
book = open('html.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

voiceassistant = pyttsx3.init()
for num in range(17, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    voiceassistant.say(text)
    voiceassistant.runAndWait()