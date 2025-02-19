#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import datetime
import re
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

def detect_encoding(file_path):
    """Определяет кодировку файла"""
    encodings = ['utf-8-sig', 'utf-8', 'cp1251']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                f.read()
            return encoding
        except UnicodeDecodeError:
            continue
    raise Exception('Не удалось определить кодировку файла')

def search_keyword(file_path, keyword):
    """
    Ищет строки с указанным ключевым словом и экспортирует их в XLSX
    
    Parameters:
    file_path (str): путь к исходному CSV файлу
    keyword (str): ключевое слово для поиска
    
    Returns:
    pandas.DataFrame: датафрейм с найденными строками
    """
    try:
        # Определяем кодировку файла
        encoding = detect_encoding(file_path)
        
        # Читаем CSV файл
        df = pd.read_csv(file_path, encoding=encoding, sep=';')
        
        # Приводим keyword к нижнему регистру
        keyword = keyword.lower()
        
        # Создаем маску для поиска
        mask = df['Запрос'].str.lower().str.contains(keyword, na=False)
        
        # Фильтруем датафрейм
        result_df = df[mask].copy()
        
        # Если найдены результаты
        if not result_df.empty:
            # Формируем имя файла с текущей датой и временем
            current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f'keyword_{keyword}_{current_time}.xlsx'
            
            # Сохраняем результаты в XLSX
            result_df.to_excel(output_file, index=False, engine='openpyxl')
            
            print(f'\nНайдено {len(result_df)} строк с ключевым словом "{keyword}"')
            print(f'Результаты сохранены в файл: {output_file}')
            print('\nПервые 5 строк результата:')
            print(result_df.head())
            
            return result_df
        else:
            print(f'\nСтроки с ключевым словом "{keyword}" не найдены')
            return None
            
    except Exception as e:
        print(f'Произошла ошибка: {str(e)}')
        return None

# Пример использования
if __name__ == "__main__":
    # Замените 'your_file.csv' на путь к вашему файлу
    file_path = 'import.csv'
    keyword = input('Введите ключевое слово для поиска: ')
    
    df = search_keyword(file_path, keyword)


# In[ ]:




