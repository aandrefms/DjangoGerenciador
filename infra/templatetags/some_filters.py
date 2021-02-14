from django import template
from PyPDF2 import PdfFileMerger, PdfFileReader
import uuid
import os
import shutil
from django.utils.functional import SimpleLazyObject
register = template.Library()


@register.filter(name='pdf')
def concat_pdf(value, id):
    merger = PdfFileMerger()
    for item in value:
        pdf_file = item.file.url
        pdf_file = "." + pdf_file
        merger.append(pdf_file)
    id = item.unique_documento_id
    try:
        shutil.rmtree(f"./static/upload/fullpdf/{item.processo.id}")
    except:
        pass
    path = f"./static/upload/fullpdf/{item.processo.id}"
    try:
        os.mkdir(path)
    except OSError:
        pass
    # id = uuid.uuid4()
    a = merger.write(f"./static/upload/fullpdf/{item.processo.id}/document-output{id}.pdf")
    return f"../../../../static/upload/fullpdf/{item.processo.id}/document-output{id}.pdf"





'''querydoc = Processo.objects.get(id=value)
filenames = querydoc.processo.all()
# filenames = querydoc.file.url
for filename in filenames:
    pdf_file = filename.file.url
    merger.append(pdf_file)'''
