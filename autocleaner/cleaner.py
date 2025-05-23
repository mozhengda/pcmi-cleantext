import os
import string
import pandas as pd
from .utils import load_rewrite_table 

def apply_rewrite(word, rewrite_table):
    """
    Clean and rewrite a single word using the rewrite_table.
    """
    word_clean = word.strip(string.punctuation).lower()
    return rewrite_table.get(word_clean, word)

def clean_text(text, rewrite_table, stats_counter=None):
    """
    Applies rewriting to a full text string using rewrite_table.
    Optionally tracks how many words were rewritten.
    """
    if not isinstance(text, str):
        return text

    tokens = text.split()
    cleaned_tokens = []

    for token in tokens:
        rewritten = apply_rewrite(token, rewrite_table)
        if stats_counter is not None and rewritten != token:
            stats_counter['rewritten'] += 1
        cleaned_tokens.append(rewritten)

    return ' '.join(cleaned_tokens)

def clean_column(df, columns_to_clean, rewrite_table):
    """
    Applies clean_text to specified DataFrame columns.
    Returns the cleaned DataFrame and prints stats.
    """
    stats = {'rewritten': 0}

    for col in columns_to_clean:
        df[col] = df[col].fillna('').apply(lambda text: clean_text(text, rewrite_table, stats))

    print(f"Total tokens rewritten across all columns: {stats['rewritten']}")
    return df

def clean_column_auto(df, columns_to_clean, table_path=None):
    """
    Automatically loads the rewrite table and cleans specified DataFrame columns.
    - If table_path is not provided, it will default to the rewrite_table.csv
      located in the same folder as this module (cleaner.py).
    - This makes it robust to be called from any working directory (e.g. notebooks, scripts).
    """
    if table_path is None:
        # This gets the absolute path to this file's directory
        base_dir = os.path.dirname(__file__)
        table_path = os.path.join(base_dir, 'rewrite_table.csv')
    
    rewrite_table = load_rewrite_table(table_path)
    return clean_column(df, columns_to_clean, rewrite_table)