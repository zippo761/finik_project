import pandas as pd


def load_data(name_of_file: str, array_columns: list):
    """
    This function load data from xlsx into DataFrame and separate
    :param name_of_file: string, like: 'КС2-1.xlsx'
    :param array_columns: list of columns those will use, like: [2, 3, 8, 6]
    :return: DataFrame with separated columns
    """
    data_frame = pd.read_excel(name_of_file, usecols=array_columns, engine='openpyxl')
    # take columns that will use
    data_frame = data_frame[data_frame['Обоснование'].str.contains('ТЦ_', regex=False, na=False)]
    return data_frame


def pull_data_into_dict(data_frame: pd.DataFrame):
    """
    This function take data from DataFrame and make dict with params that we are need
    :param data_frame: pd.DataFrame
    :return:
    """
    params_dict = {}
    for item in data_frame.iloc:
        params_dict[item[1]] = item[2], item[3]

    return params_dict


def clear_dict(params):
    """
    This function convert params in dict like
    was: '100 30,50'
    will be: '10030.50' for make math operators
    :param params is dict
    :return: params_dict is dict after convert
    """
    params_items = params
    items = {
        key: (round(float(''.join(value[1].replace(',', '.').split()))*1.2, 4),
              value[0]) for key, value in params_items.items()
                   }
    return items


def spoil_items_for_search(path, number_of_columns):
    df = load_data(path, number_of_columns)
    dict_with_params = pull_data_into_dict(df)
    dict_with_params = clear_dict(dict_with_params)
    return dict_with_params


if __name__ == '__main__':
    # name of file
    path_of_file = r'КС/КС2-1.xlsx'
    # number of columns in xlsx file that will use
    number_of_columns = [2, 3, 6, 8]

    print(spoil_items_for_search(path_of_file, number_of_columns))

