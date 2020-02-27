from bs4 import BeautifulSoup

with open('books.xml', 'r', encoding='utf-8') as books_file:
    books_xml = books_file.read()

print(books_file)

# xml 모듈을 사용하여 분석, lxml 라이브러리 설치 필요!
soup = BeautifulSoup(books_xml, 'lxml')

for book_info in soup.find_all('author'):
    print(book_info)
    print(book_info.get_text())
