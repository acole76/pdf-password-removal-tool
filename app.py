from pypdf import PdfWriter, PdfReader
import argparse

def main():
    parser = argparse.ArgumentParser(description="PDF Password Removal Tool")
    parser.add_argument("--infile", "-i", action="append", required=True, help="Full path to a password protected pdf")
    parser.add_argument("--password", "-p", required=True, help="Known password of the pdf")

    args = parser.parse_args()
    password = args.password

    for file in args.infile:
        outfile = file.replace(".pdf", "-decrypt.pdf")

        writer = PdfWriter()
        pdf = PdfReader(file)
        pdf.decrypt(password)
        for page in pdf.pages:
            writer.add_page(page)
        
        with open(outfile, "wb") as f:
            writer.write(f)

if(__name__ == "__main__"):
    main()