import io


def create_csv_bytes_object_from_dataframe(dataframe):
        """
        Converts a DataFrame to a CSV BytesIO object 

        Args:
            dataframe: target DataFrame to be converted to CSV BytesIO object
        Returns:
            buffer: CSV BytesIO object with read pointer set to start of data
            Raises:
                Exception if CSV BytesIO object canot be generated from DataFrame
        """
        try:

            buffer = io.BytesIO()
            dataframe.write_csv(buffer)
            buffer.seek(0)

            return buffer
        

        except Exception as e:
             print(f'Failed to generate CSV BytesIO object from DataFrame: {e}') 
