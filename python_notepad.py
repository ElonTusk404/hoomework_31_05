#Программа открывает текстовый файл и пользователь может прочесть файл или же добавить новые данные:
while True:
    print('Для выхода из программы введите \'q\'')
    input_file = input('Введите название файла, для редактирования: ')
    print('Введите режим работы с файлом:read/write')
    mode = input()
    if input_file == 'q':
        break
    if mode == 'q':
        break
    if mode == 'write':
        with open(input_file, 'a') as file:
            while True:
                text = input('Введите текст. Для выхода введите \'q\'): ')
                if text == 'q':
                    break
                file.write(text + '\n')
    if mode == 'read':
        try:
            with open(input_file) as file:
                print(file.read())
        except FileNotFoundError:
            print(f"Файл под названием: {input_file} не найден.")


