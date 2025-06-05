import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    le = LabelEncoder()
    for col in ['crop', 'Variety', 'state', 'Unit', 'Recommended Zone']:
        df[col] = le.fit_transform(df[col])
    df['Season'] = pd.to_datetime(df['Season'], errors='coerce').dt.dayofyear.fillna(0)
    return df