from bs4 import BeautifulSoup

with open('US08621662-20140107.XML', 'r', encoding='utf8') as patent_xml:
    xml = patent_xml.read()

# xml 모듈을 사용하여 분석, lxml 라이브러리 설치 필요!
soup = BeautifulSoup(xml, 'lxml')

invention_title_tag = soup.find('invention-title')
print(invention_title_tag.get_text())

publication_reference_tag = soup.find('publication-reference')
p_document_id_tag = publication_reference_tag.find('document-id')
p_country = p_document_id_tag.find('country').get_text()
p_doc_number = p_document_id_tag.find('doc-number').get_text()
p_kind = p_document_id_tag.find('kind').get_text()
p_date = p_document_id_tag.find('date').get_text()

print(p_doc_number, p_kind, p_date)

application_reference_tag = soup.find('application-reference')
a_document_id_tag = publication_reference_tag.find('document-id')
a_country = p_document_id_tag.find('country').get_text()
a_doc_number = p_document_id_tag.find('doc-number').get_text()
a_kind = p_document_id_tag.find('kind').get_text()
a_date = p_document_id_tag.find('date').get_text()

print(a_country, a_doc_number, a_date)