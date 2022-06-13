import docx
from answer import answer
from check import a_list, doc_text

dict = {}
id = 0
subject_list = a_list
i = 0
tmp_str = ''
for i, text in enumerate(doc_text):
    if i in subject_list:
        dict[id] = {'tm': '', 'xs': '', 'an': answer[id]}
        dict[id]['tm'] = text
        id += 1
        tmp_str = ''
    else:
        tmp_str += text
        if i + 1 not in subject_list:
            tmp_str += '\n'
        else:
            dict[id - 1]['xs'] = tmp_str
dict[id - 1]['xs'] = tmp_str
