from PyPDF2 import PdfFileWriter, PdfFileReader  #pip install pypdf2

pdf = 'a.pdf' #Enter The name of input file
dpdf = 'd.pdf' #Enter The name of output file

print('Finding password of pdf.....')

out = PdfFileWriter() 

file = PdfFileReader("a.pdf")

with open('password.txt') as f:
    pas = f.readlines()

with open('english.txt') as f:
    english = f.readlines()

password = pas + english

def pdfs():
    try:
        for idx in range(file.numPages): 
                page = file.getPage(idx) 
                out.addPage(page) 
            
        with open(dpdf, "wb") as f: 
            out.write(f) 
        print("File decrypted Successfully.")
        return True
    except:
        return False

if file.isEncrypted:
    for i in password:
        file.decrypt(i.replace('\n',''))
        try:
            if pdfs() == True:
                print('The password of file is',i)
                break
        except:
            pass
else: 
    print("File already decrypted.")