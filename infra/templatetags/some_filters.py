from django import template
from PyPDF2 import PdfFileMerger, PdfFileReader
import uuid
import os
from django.utils.functional import SimpleLazyObject
register = template.Library()

@register.filter(name='pdf')
def concat_pdf(value, id):
    merger = PdfFileMerger()
    for item in value:
        pdf_file = item.file.url
        pdf_file = "." + pdf_file
        merger.append(pdf_file)
        id = item.file.id
    # id = uuid.uuid4()
    a = merger.write(f"./static/upload/fullpdf/document-output{id}.pdf")
    return f"../../../../static/upload/fullpdf/document-output{id}.pdf"


def delete_pdf(id):
    try:
        os.remove(f"./static/upload/fullpdf/document-output{id}.pdf")
    except:
        pass



def call_functions(value, pk):
    id = uuid.uuid4()
    return concat_pdf(value, id)




'''querydoc = Processo.objects.get(id=value)
filenames = querydoc.processo.all()
# filenames = querydoc.file.url
for filename in filenames:
    pdf_file = filename.file.url
    merger.append(pdf_file)'''
