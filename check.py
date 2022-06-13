import docx

docxFile = 'source/jds.docx'
doc = docx.Document(docxFile)
doc_text = []
a_list = []
for i in doc.paragraphs:
    if len(i.text) == 0:
        continue
    doc_text.extend(i.text.split('\n'))

for i, text in enumerate(doc_text):
    if '0' <= text[0] <= '9':
        a_list.append(i)