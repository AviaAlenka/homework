import os
import time

directory = "."
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath =os.path.join(directory, file)
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(file)
    print(f'Обнаружен файл: {file}, Путь: "{filepath}", Размер: {filesize} байт, '
          f'Время изменения: {formatted_time}, Родительская директория: "{parent_dir}"')
  break # Поставила, чтобы не вскрывались вложенные папки. Только файлы в корне.