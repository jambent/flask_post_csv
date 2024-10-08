import pytest
import polars as pl
import polars.testing as pt
from create_csv_bytes_object_from_dataframe \
    import create_csv_bytes_object_from_dataframe


def test_that_create_csv_from_dataframe_returns_csv_bytes_object():

    data = {'name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
            'age': [20, 21, 22, 23]}
    df = pl.DataFrame(data)
    
    bytes_object = create_csv_bytes_object_from_dataframe(df)
    recovered_dataframe = pl.read_csv(bytes_object)
    
    pt.assert_frame_equal(df, recovered_dataframe)

def test_that_non_dataframe_input_raises_exception():
    with pytest.raises(Exception):
        create_csv_bytes_object_from_dataframe('hello')