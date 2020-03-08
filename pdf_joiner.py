from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
import argparse
'''
PDF joiner
'''

def merge_pdfs(paths, output):
     pdf_writer = PdfFileWriter()

     for path in paths:
         pdf_reader = PdfFileReader(path)
         for page in range(pdf_reader.getNumPages()):
             pdf_writer.addPage(pdf_reader.getPage(page))

     with open(output, "wb") as out:
         pdf_writer.write(out)

def user_input():
    files = glob.glob("*.pdf")
    print(files)
    file_dict = {key: files[key] for key in range(0,len(files))}
    print("the pdf files in your current directory are:")
    for key, value in file_dict.items():
        print(f"{key}: {value}")
    pdf_files_input = input("Using their corisponding number what files do you \
        whant to combine? (I.E 0,2): ")
    out_put_file_name = input("Enter the output flie name:")
    list_input = [int(i) for i in (pdf_files_input.split(","))]
    paths = []
    for key, value in file_dict.items():
        if key in list_input:
            paths.append(value)
        else:
            print("no it didnt work")
    
    return (paths, out_put_file_name)

if __name__ == "__main__":
     paths, output = user_input()
     merge_pdfs(paths, output)