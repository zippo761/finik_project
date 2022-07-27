from prepare_data import *

# name of file
path_of_file = r'КС/КС2-1.xlsx'
# number of columns in xlsx file that will use
number_of_columns = [2, 3, 8, 6]

# товары с ценами по которым закупили

price_ks = spoil_items_for_search(path_of_file, number_of_columns)

df_price_test = pd.read_excel('price_for_test.xlsx')
















"""pdf_document = "ФССЦ.pdf"
doc = fitz.open(pdf_document)
from thefuzz import process
from thefuzz import fuzz

count = 0

with open('1_text.txt', 'r') as file:
    text = file.read()

    text = text.replace('\n', ' ')

    pattern = re.compile('(?<=\d\d\.\d\.\d\d\.\d\d-\d\d\d\d).+?(?=\d\d\.\d\.\d\d)')

    r = pattern.findall(text, re.M)

    print(len(r))

    for el in r:
        result = fuzz.WRatio('Керамогранит 600х600', el)

        if result >= 90:
            print(el, '===>', result)"""
