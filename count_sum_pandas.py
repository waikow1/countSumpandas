from pandas import DataFrame


def count_sum (arg: DataFrame) -> DataFrame:
    result = arg.groupby('Товар', as_index = False)['Количество'].sum()
    return result
