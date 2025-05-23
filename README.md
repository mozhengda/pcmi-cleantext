# pcmi-cleantext

`pcmi-cleantext` is a simple text cleaner for automotive repair data.  
It uses a custom rewrite table to replace common abbreviations with standardized terms.

## Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/mozhengda/pcmi-cleantext.git
cd pcmi-cleantext
pip install -e .
```

## Example usage

```python
from autocleaner.cleaner import clean_column_auto
import pandas as pd

df = pd.DataFrame({
    "sComplaint": ["C/S VEH INOP"],
    "sCause": ["diag dtc in ecm"]
})

df_cleaned = clean_column_auto(df, ['sComplaint', 'sCause'])
print(df_cleaned)
```

## File structure

```
pcmi-cleantext/
├── autocleaner/
│   ├── cleaner.py
│   ├── utils.py
│   ├── rewrite_table.csv
│   └── __init__.py
├── setup.py
├── pyproject.toml
└── README.md
```

## License

MIT
