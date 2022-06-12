import docx

docxFile = 'source/jds.docx'
doc = docx.Document(docxFile)
len = len(doc.paragraphs)
a_list = []
for i in range(len):
    if doc.paragraphs[i].text[0] >= '0' and doc.paragraphs[i].text[0] <= '9':
        # print(doc.paragraphs[i].text)
        a_list.append(i)

