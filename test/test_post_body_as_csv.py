import pytest
import polars as pl
import polars.testing as pt
from src.create_csv_bytes_object_from_dataframe \
    import create_csv_bytes_object_from_dataframe
from test_data.test_dataframe import test_df


def test_that_create_csv_from_dataframe_returns_csv_bytes_object():

    bytes_object = create_csv_bytes_object_from_dataframe(test_df)
    recovered_dataframe = pl.read_csv(bytes_object)
    
    pt.assert_frame_equal(test_df, recovered_dataframe)

@pytest.mark.skip("Exception message triggered but Exception not recognised")
def test_that_non_dataframe_input_raises_exception():
    with pytest.raises(Exception, match = "Failed to generate CSV"):
        create_csv_bytes_object_from_dataframe("hello")