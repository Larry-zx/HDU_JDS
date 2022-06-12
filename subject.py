import docx
from answer import answer
from check import  a_list
docxFile = 'source/jds.docx'
doc = docx.Document(docxFile)
len = len(doc.paragraphs)
dict = {}
id = 0
subject_list = a_list
i = 0
tmp_str = ''
for i in range(len):
    if i in subject_list:
        dict[id] = {'tm':'','xs':'','an':answer[id]}
        dict[id]['tm'] = doc.paragraphs[i].text
        id += 1
        tmp_str = ''
    else:
        tmp_str += doc.paragraphs[i].text
        if i+1 not in subject_list:
            tmp_str += '\n'
        else:
            dict[id-1]['xs'] = tmp_str
dict[id-1]['xs']=tmp_str