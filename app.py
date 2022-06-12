
import PySimpleGUI as sg
import random
from subject import dict

count = 0
acc = 0
sg.theme('GreenMono')
while True:
    i = random.randint(0,248)
    layout = [
        [sg.Text(dict[i]['tm'], size=(64, 2), font=20, text_color='Black', auto_size_text=True)],
        [sg.Text(dict[i]['xs'], size=(64, 5), font=20, text_color='navy')],
        [sg.Button(' A ', key="A", font=20), sg.Button(' B ', key="B", font=20),sg.Button(' C ', key="C", font=20),sg.Button(' D ', key="D", font=20),],
        [sg.Text("正确率:%d/%d"%(acc,count) , size=(64, 1), font=30, text_color='black')],
        [sg.Button('退出', key="exit", font=20), ],
    ]
    window = sg.Window('近代史题库', layout, default_element_size=(24, 2), auto_size_text=True)
    event, values = window.read()
    window.close()
    if event=='exit':
        break
    answer = dict[i]['an']
    if event!=answer:
        str = '正确答案是: %s '%(answer)
        layout_ = [
            [sg.Text(dict[i]['tm'], size=(64, 2), font=20, text_color='Black', auto_size_text=True)],
            [sg.Text(dict[i]['xs'], size=(64, 5), font=20, text_color='navy')],
            [sg.Text(str , size=(64,2),font=20,text_color='red')],
            [sg.Button('下一题', key="continue", font=20), ],
            [sg.Button('退出', key="exit", font=20), ],
        ]
        window = sg.Window('近代史题库', layout_, default_element_size=(24, 2), auto_size_text=True)
        event, values = window.read()
        window.close()
        if event == 'exit':
            break

    else:
        acc+=1
    count+=1



