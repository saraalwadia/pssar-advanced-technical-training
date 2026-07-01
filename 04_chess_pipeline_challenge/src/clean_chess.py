import pandas as pd

def clean_chess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean chess dataset and engineer features
    """

    # 2a - Parse time_increment
    df[['time_base', 'time_inc']] = df['time_increment'].str.split(
        '+', expand=True
    ).astype(int)

    # 2b - Add rating difference
    df['rating_diff'] = df['white_rating'] - df['black_rating']

    # 2c - Extract opening family
    df['opening_family'] = (
        df['opening_fullname']
        .str.split(':')
        .str[0]
        .str.strip()
    )

    # 2d - Drop high-null column
    df = df.drop(columns=['opening_response'])

    # 2e - Flag suspicious games
    df['is_suspicious'] = df['turns'] < 5

    return df