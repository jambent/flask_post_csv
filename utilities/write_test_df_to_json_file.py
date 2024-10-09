import polars as pl

test_df = pl.DataFrame({"id": [101, 102, 103, 104, 105],
                        "name": ["James", "Dan", "Lisa", "Yvonne", "Ken"],
                        "age": [22, 25, 23, 28, 32], })


if __name__ == "__main__":
    test_df.write_json("test_data/test_df_json.json")
