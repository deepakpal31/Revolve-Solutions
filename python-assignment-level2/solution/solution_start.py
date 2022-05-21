import argparse
import pandas as pd


def get_params() -> dict:
    parser = argparse.ArgumentParser(description='DataTest')
    parser.add_argument('--customers_location',  required=False, default="/home/deepak/Downloads/python-assignment-level2-6ed53b4e828af18bc24b1770a3a3e3e70706e785/input_datastarter/customers.csv")

    parser.add_argument('--products_location', required=False, default="/home/deepak/Downloads/python-assignment-level2-6ed53b4e828af18bc24b1770a3a3e3e70706e785/input_datastarter/products.csv")
    parser.add_argument('--transactions_location', required=False, default="/home/deepak/Downloads/python-assignment-level2-6ed53b4e828af18bc24b1770a3a3e3e70706e785/input_datastarter/transactions/")
    parser.add_argument('--output_location', required=False, default="/home/deepak/Downloads/python-assignment-level2-6ed53b4e828af18bc24b1770a3a3e3e70706e785/output_data/")
    # parser.add_argument('--aex','-x', required=False, default="arun")
    return vars(parser.parse_args())
    




def main():
    params = get_params()
    # print(params)
    # print(params['aex'])
    df1 = pd.read_csv(params['customers_location'])
    # print(df.head())
    df2 = pd.read_csv(params['products_location'])
    df3 = pd.read_csv(params['transactions_location'])

    print(df1.head(10))
    print(df2.head(10))
    print(df3.head(10))




    


if __name__ == "__main__":
    main()
