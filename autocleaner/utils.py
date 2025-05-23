import pandas as pd

def load_rewrite_table(filepath='autocleaner/rewrite_table.csv'):
    """
    Loads a rewrite_table from a CSV file.
    
    The CSV should have two columns:
        - original
        - rewrite

    Returns:
        A dictionary mapping original → rewrite
    """
    df = pd.read_csv(filepath)
    
    # Optional: Drop rows with missing values in either column
    df = df.dropna(subset=['original', 'rewrite'])

    # Convert to dictionary
    rewrite_dict = dict(zip(df['original'], df['rewrite']))
    
    print(f"✅ Loaded rewrite table with {len(rewrite_dict)} entries from {filepath}")
    return rewrite_dict