import pandas as pd
import re
from nltk.corpus import stopwords
import nltk

# Скачиваем стоп-слова
nltk.download('stopwords', quiet=True)

def detect_encoding(file_path):
    encodings_to_try = ['utf-8', 'cp1251']
    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                f.read()
            return encoding
        except UnicodeDecodeError:
            continue
    raise Exception('Не удалось определить кодировку файла')

def clean_text(text):
    if pd.isna(text):
        return None
    
    # Получаем список стоп-слов
    stop_words = set(stopwords.words('russian'))
    
    # Паттерн для удаления специальных символов
    patterns = r'[A-Za-z0-9!#$%&\'()*+,\./:;<=>?@\[\]^_`{|}~—"\-]+'
    
    # Очищаем текст
    text = re.sub(patterns, ' ', str(text).lower())
    
    # Разбиваем на слова и фильтруем стоп-слова
    words = [word.strip() for word in text.split() if word.strip() and word.strip() not in stop_words]
    
    return words if words else None

try:
    # Читаем файл
    file_encoding = detect_encoding('import.csv')
    df = pd.read_csv('import.csv', sep=';', encoding=file_encoding)
    
    # Создаем словарь для хранения статистики
    word_stats = {}
    
    # Обрабатываем каждую строку
    for index, row in df.iterrows():
        words = clean_text(row['Запрос'])
        if not words:
            continue
            
        for word in words:
            if word not in word_stats:
                word_stats[word] = {
                    'count': 0,
                    'frequency_sum': 0,
                    'positions': []
                }
            
            word_stats[word]['count'] += 1
            word_stats[word]['frequency_sum'] += row['Точная частотность']
            word_stats[word]['positions'].append(row['Позиция'])
    
    # Преобразуем статистику в DataFrame
    result_data = []
    for word, stats in word_stats.items():
        result_data.append({
            'Слово': word,
            'Количество': stats['count'],
            'Суммарная частотность': stats['frequency_sum'],
            'Средняя позиция': sum(stats['positions']) / len(stats['positions'])
        })
    
    result_df = pd.DataFrame(result_data)
    result_df = result_df.sort_values('Количество', ascending=False)
    
    # Сохраняем результаты
    output_filename = 'result.xlsx'
    result_df.to_excel(output_filename, index=False)
    
    print("Топ 10 слов по количеству (после удаления стоп-слов):")
    print(result_df.head(10)[['Слово', 'Количество', 'Суммарная частотность', 'Средняя позиция']])
    
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
    # Выводим первые несколько строк файла для диагностики
    with open('import.csv', 'r', encoding=file_encoding) as f:
        print("\nПервые 5 строк файла:")
        for i, line in enumerate(f):
            if i < 5:
                print(line.strip())
