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

def clean_column_auto(df, columns_to_clean, table_path='autocleaner/rewrite_table.csv'):
    """
    Automatically loads the rewrite table and cleans specified DataFrame columns.
    Use this when you don't want to manually load rewrite_table.
    """
    rewrite_table = load_rewrite_table(table_path)
    return clean_column(df, columns_to_clean, rewrite_table)