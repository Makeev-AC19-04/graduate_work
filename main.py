import PySimpleGUI as sg
import pandas as pd

def LoadData(path):
    imported_data = []
    if path == 0:
        sg.popup_ok("Файл не выбран")
    else:
        if path[-3::] == 'csv':
            try:
                imported_data = pd.read_csv(path)
            except:
                sg.popup_ok("Ошибка открытия файла")
            else:
                if not any(i.isalpha() for i in imported_data.columns[0]):
                    imported_data = pd.read_csv(path, header=None)
                print(imported_data.head())
                print(imported_data.columns)
        else:
            try:
                imported_data = pd.read_excel(path)
            except:
                sg.popup_ok("Ошибка открытия файла")
            else:
                if not any(i.isalpha() for i in imported_data.columns[0]):
                    imported_data = pd.read_excel(path, header=None)
                print(imported_data.head())
                print(imported_data.columns)
    return imported_data

def ShowTable(data): #Функция создания окна с таблицей
    layout = [[sg.Table(values=data.values, 
                        headings=[str(i) for i in data.columns],
                        max_col_width=5,
                        vertical_scroll_only=False)],
                [sg.Button("Закрыть")]]
    window = sg.Window("Second Window", layout, modal=True, size=(600,400), resizable=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Закрыть" or event == sg.WIN_CLOSED:
            break


loadLayout = [  [sg.Text('Выберите файл с данными')],
            [sg.Input(key="-IN-"), sg.FileBrowse(key="-IN-", file_types=(("CSV файл", "*.csv"), ("XLS(X) файл", "*.xls, *.xlsx")))],
            [sg.Button("Загрузить"), sg.Button("Показать данные")]]

mainWindow = sg.Window('Загрузка файла', loadLayout, resizable=True) #Создать главное окно

imported_data=[]
while True: #Цикл главного окна
    event, values = mainWindow.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == 'Загрузить':
        imported_data = LoadData(str(values["-IN-"]))
    elif event == "Показать данные" and len(imported_data)!=0:
        ShowTable(imported_data) #Создать окно показа таблицы с данными

mainWindow.close()