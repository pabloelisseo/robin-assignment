import pymongo
import pandas as pd


def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017")
    db = myclient["robin"]
    collection = db["testPythonDB"]

    # Retrieve all Documents
    df_products = pd.DataFrame(list(collection.find({})))

    df_products.groupby("brand").name.count().plot.bar(ylim=0)


if __name__ == "__main__":
    main()
