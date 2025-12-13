import pandas as pd

def describe_data(clean_data):
    """
    Docstring for describe_data
    
    :param clean_data: Description
    """

    if not isinstance(clean_data, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")    
    if clean_data.empty:
        raise ValueError("Dataframe must contain observations.")
    
    describe_stats = clean_data.describe()
    nunique_stats = pd.DataFrame(clean_data.nunique())

    info_data = []
    for col in clean_data.columns:
        info_data.append({
            'Column': col,
            'Type': str(clean_data[col].dtype),
            'Non-Null Count': clean_data[col].notna().sum(),
            'Null Count': clean_data[col].isna().sum()
        })
    info_stats =pd.DataFrame(info_data)

    return [describe_stats, nunique_stats, info_stats]