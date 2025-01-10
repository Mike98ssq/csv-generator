import pandas as pd
import numpy as np

str_choi = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
def generate_data(num_rows, num_columns, data_types):

    data = {}
    
    for i in range(num_columns):
        col_type = data_types[i]

        if col_type == 'int':
            data[f'column_{i+1}'] = np.random.randint(0, 100, num_rows)
        elif col_type == 'float':
            data[f'column_{i+1}'] = np.random.rand(num_rows) * 100
        elif col_type == 'str':
            str_length = np.random.randint(1, 11)
            data[f'column_{i+1}'] = [''.join(np.random.choice(list(str_choi), size=str_length)) for _ in range(num_rows)]
        else:
            raise ValueError("Вводимые данные должны быть 'int', 'float' или 'str'.")

    return pd.DataFrame(data)

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f'Data сохранена как {filename}')

if __name__ == "__main__":
    num_rows = int(input("Введите количество строк: "))
    num_columns = int(input("Введите количество столбцов: "))
    
    data_types = []
    for i in range(num_columns):
        col_type = input(f"Введите тип данных для столбца {i+1} (int, float, str): ").strip().lower()
        data_types.append(col_type)
        
    df = generate_data(num_rows, num_columns, data_types)
    
    filename = input("Введите имя файла для сохранения (*.csv): ")
    save_to_csv(df, filename)