# coding: utf8

from pathlib import Path
import re
import shutil

pat = '320х600'           # паттерн, который ищем в названиях файлов
replacement = '300х790'   # на что будем менять
extensions = ['dxf', 'cdw']                        # расширения файлов для переименования
exceptions = ['ЗРЭ-320х600-3 кронштейн NMRV063']   # исалючения, файлы, которые не нужно переименовывать


path = '.'                # путь к папке с файлами для переименования
path = Path(path)
pattern = re.compile(pat)

for file in path.glob('*'):
    if file.is_file() and file.suffix.lower()[1:] in extensions and file.stem not in exceptions:
        if pattern.findall(file.name):
            new_name = file.name.replace(pat, replacement)
            new_path = file.parent / new_name
            file.rename(new_path)

print('Готово')
