import pandas as pd
import requests
import pymongo


def request_marketplace_names(marketplace_ids):
    marketplaces = {}
    marketplace_names = []
    for _, mid in marketplace_ids.items():
        # for performance, try to skip doing the same http request
        if mid in marketplaces:
            marketplace_names.append(marketplaces[mid])
        else:
            url = f"https://stores.robinrover.io/api/{mid}"
            response_json = requests.request("GET", url).json()

            marketplaces[mid] = response_json["name"]
            marketplace_names.append(response_json["name"])

    return pd.Series(marketplace_names)


def main():
    # Read csv
    df_products = pd.read_csv("productAttributes.csv", sep=';')

    # Retrieve marketplace names and assign in df
    df_products["marketplaceName"] = request_marketplace_names(
        df_products["marketplace"])

    # Rename columns
    columnRenames = {
        "category.name": "categoryName",
        "category.code": "categoryCode",
        "brand.name": "brandName",
        "marketplace": "marketplaceId",
    }

    df_products.rename(columns=columnRenames, inplace=True)

    # Convert into dict to insert into mongodb
    dict_products = df_products.to_dict("records")

    # MongoDB insertion
    # Create client with default credentials
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    db = myclient["robin"]
    collection = db["testPythonDB"]

    collection.insert_many(dict_products)


if __name__ == "__main__":
    main()
