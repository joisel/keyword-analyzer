# keyword-analyzer
Инструмент для глубокого анализа семантического ядра, который помогает анализировать и группировать ключевые слова из выгрузки keys.so.

# Возможности
- Подсчёт частоты встречаемости слов в поисковых запросах
- Расчёт суммарной частотности для каждого слова
- Вычисление средней позиции для каждого слова в выдаче
- Поддержка стоп-слов русского языка
- Детальный поиск по конкретным ключевым словам

# Установка и запуск
## Требования
Python 3.7+
pandas
nltk
openpyxl

# Установка зависимостей

Необходимо установить Python 3.7

## Установка библиотек
pip install pandas nltk openpyxl

# Использование
Анализ ключевых слов
1. Поместите файл import.csv (выгрузка из keys.so) в папку со скриптом
2. Запустите файл keyword-analyzer.py

На выходе получите файл result.xlsx со следующими данными:
- Список всех слов из запросов
- Количество повторений каждого слова
- Суммарная частотность по каждому слову
- Средняя позиция в выдаче

# Поиск по ключевым словам
Для детального анализа конкретных слов:

1. Запустите searcher.py
2. Введите интересующее слово из таблицы result.xlsx
3. Получите Excel-файл с полной выборкой всех запросов, содержащих искомое слово

# Структура выходных данных
## keywords_analysis.xlsx
- Слово
- Количество упоминаний
- Суммарная частотность
- Средняя позиция

## keyword_[слово]_[дата].xlsx
Полная информация по запросам с искомым словом:

- Текст запроса
- Позиция
- Частотность
- Дополнительные метрики из keys.so
  
# Примечания

- Анализ нечувствителен к регистру
- Автоматически определяется кодировка входного файла
- Учитываются только значимые слова (исключаются стоп-слова)
- Результаты поиска сохраняются с временной меткой для удобства сравнения
