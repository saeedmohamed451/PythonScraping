#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyPdf import PdfFileWriter, PdfFileReader

# To create PDF documents.
from reportlab.pdfgen import canvas

# To create an image from a URL.
from reportlab.lib.utils import ImageReader
 
# Allow us to have exactly A4 sized PDF documents.
from reportlab.lib.pagesizes import A4
 
# Allow us to use inches.
from reportlab.lib.units import inch

import DocumentServices

def main():

# Aldi-TX_2017_09_06-1.pdf
# Aldi-TX_2017_09_13.pdf
# Aldi-TX_2017_09_27-1.pdf
# Aldi-CA_2017_10_04-1.pdf

    pdfCroppedFilename = "finalme/Aldi-TX_2017_10_04-1.pdf"
    pdfChoppedFilename = "finalme/Aldi-TX_2017_10_04-1_chopped.pdf"

    KROGER_PAGE_WIDTH = 974.99816
    # Only want to split the Insider In-store Catalog from Aldi
    # not the Weekly Ad Catalog.
    ALDI_PAGE_WIDTH = 1514.38059

    DocumentServices.chopPdf(pdfCroppedFilename, pdfChoppedFilename, ALDI_PAGE_WIDTH)

    DocumentServices.movePdf(pdfChoppedFilename, pdfCroppedFilename)

if __name__ == '__main__':
    main()




