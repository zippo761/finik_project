import re

from thefuzz import fuzz
from prepare_data import *


def comparison_price(ks_price, db_price, index=False):
    """Make comparison between two price"""
    if index:
        db_price *= index
        result_percent = abs((ks_price-db_price)/db_price*100)
        result_price = abs(ks_price - db_price)
    else:
        result_percent = abs((ks_price-db_price)/db_price*100)
        result_price = abs(ks_price - db_price)

    return (True if result_percent > 15 else False, result_price, round(result_percent))


def make_comparison(price_ks, df_price):
    """Make comparison"""

    df = pd.DataFrame(columns=[
        'Наименование',
        'Закупочная цена',
        'Цена в загруженной базе',
        'Разница в цене',
        'Разница в процентах',
        'В пределах диапазона'
    ])

    for name_item_ks, price_index_ks in price_ks.items():

        flag = False

        for name_price_db in df_price.iloc:

            result = fuzz.ratio(name_item_ks, name_price_db[0])

            if result >= 95:

                #print(name_item_ks, '////', name_price_db[0], '===>', result)

                result_comparison = comparison_price(price_index_ks[0], name_price_db[1])

                #print(result_comparison, name_price_db[1])

                to_df = {
                    'Наименование': name_item_ks,
                    'Закупочная цена': price_index_ks[0],
                    'Цена в загруженной базе': name_price_db[1],
                    'Разница в цене': result_comparison[1],
                    'Разница в процентах': f"{result_comparison[2]} %",
                    'В пределах диапазона': 'Нет' if result_comparison[0] else 'Да'
                }

                df = df.append(to_df, ignore_index=True)

                flag = True

                break

        if flag:
            continue

        to_df = {
            'Наименование': name_item_ks,
            'Закупочная цена': price_index_ks[0],
            'Цена в загруженной базе': 'Не найден',
            'Разница в цене': 'Не найден',
            'Разница в процентах': 'Не найден ',
            'В пределах диапазона': 'Не найден'
        }

        df = df.append(to_df, ignore_index=True)

    df.to_excel('Результат сравнения цен КС2-3.xlsx', index=False)


if __name__ == '__main__':

    # name of file
    path_of_file = r'КС/КС2-3.xlsx'
    # number of columns in xlsx file that will use
    number_of_columns = [2, 3, 6, 8]

    # товары с ценами по которым закупили
    price_ks = spoil_items_for_search(path_of_file, number_of_columns)

    df_price_test = pd.read_excel('price_for_test.xlsx')
    print(df_price_test)

    make_comparison(price_ks, df_price_test)




