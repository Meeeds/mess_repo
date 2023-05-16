from bs4 import BeautifulSoup

assume_html = """
<html> <div class="contributors"> <span class="contributor" title="email: andrei01@yahoo.com">andreidev</span> <span class="contributor" title="email: cast@gmail.com">Frank</span> <span class="contributor" title="email: andrei1@github.com">andreidev</span> <span class="contributor" title="email: maryoer@users.inoreply.gthub.com">mary1</span> </div> </html>"""

soup = BeautifulSoup(assume_html, 'html.parser')

z = soup.find_all('span', {'class' : 'contributor'})
for element in z :
    print("element ", element, type(element), element.text)
print("---")
print(type(z))
print("------")

a = list(set(z))
for new_element in a :
    print("new_element ", new_element, type(new_element))
print("---")
print(type(a))
