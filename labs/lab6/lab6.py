import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

def get_page_content(url):
    """Отримуємо HTML-контент сторінки за URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Помилка при завантаженні сторінки: {e}")
        return None

def extract_text_and_tags(html):
    """Витягуємо текст з HTML та підраховуємо теги"""
    soup = BeautifulSoup(html, 'html.parser')

    # Витягуємо текст з тегів, що містять текст новини
    text = soup.get_text()

    # Підрахунок HTML тегів
    tags = [tag.name for tag in soup.find_all()]

    return text, tags

def count_word_frequency(text):
    """Підраховуємо частоту слів у тексті"""
    words = re.findall(r'\w+', text.lower())  # Вибираємо всі слова
    word_count = Counter(words)
    return word_count

def count_links_and_images(soup):
    """Підраховуємо кількість посилань та зображень"""
    links = soup.find_all('a')
    images = soup.find_all('img')

    return len(links), len(images)

def analyze_page(url):
    """Основна функція для аналізу сторінки"""
    html = get_page_content(url)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')
    text, tags = extract_text_and_tags(html)

    word_frequency = count_word_frequency(text)
    link_count, image_count = count_links_and_images(soup)

    # Виводимо результати
    print(f"Частота слів (топ 10): {word_frequency.most_common(10)}")
    print(f"Кількість HTML тегів: {len(tags)}")
    print(f"Кількість посилань: {link_count}")
    print(f"Кількість зображень: {image_count}")


url = 'https://tsn.ua/ukrayina'
analyze_page(url)
