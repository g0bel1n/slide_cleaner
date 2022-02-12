import numpy as np
from tqdm import tqdm
from pdf2image import convert_from_path
from PyPDF2 import PdfFileReader, PdfFileWriter

def cut(filename):
    pages = convert_from_path(filename)
    differentiated_pages=[]
    for i in tqdm(range(1,len(pages))):
        differentiated_pages.append([np.count_nonzero(np.asarray(pages[i])-np.asarray(pages[i-1])),i])

    idx_to_save = [page[1]-1 for page in differentiated_pages if page[0]>60000] + [len(pages)-1]

    pdf = PdfFileReader(filename)

    pdfWriter = PdfFileWriter()

    for idx in idx_to_save:
        pdfWriter.addPage(pdf.getPage(idx))

    with open('{0}_cleaned.pdf'.format(filename), 'wb') as f:
        pdfWriter.write(f)
        f.close()