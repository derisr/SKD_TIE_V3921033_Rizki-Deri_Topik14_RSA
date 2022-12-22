from PyPDF2 import PdfWriter, PdfReader
  
# buat objek pdf writer
out = PdfWriter()
  
# buka file pdf asli 
file = PdfReader("pdf_asli.pdf")
  
# identifikasi total halaman file
num = file.numPages
  
#program membaca setiap halaman file sesuai halaman yg diidentifikasi 
for page in file.pages:
    # tambahkan halaman ke objek pdf writer
    out.add_page(page)
  
  
# membuat password file enkripsi 
password = "rizkideri"
  
# mengenkripsi tiap halaman 
out.encrypt(password)
  
# buka file enkripsi "pdf_hasil_encrypt.pdf"
with open("pdf_hasil_encrypt.pdf", "wb") as f:
    
    # simpan pdf 
    out.write(f)
