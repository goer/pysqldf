# PySQLDF Package

This package provides a simple function `pysqldf` which allows executing SQL queries on pandas DataFrames using SQLite syntax.

# Installation

```bash
pip install pysqldf
```

# Usage

```python
import pandas as pd
from pysqldf import pysqldf

df = pd.DataFrame({
    'a': [1, 2, 3],
    'b': [4, 5, 6]
})

result = pysqldf('SELECT * FROM df WHERE a > 1',df)
print(result)
```

# Output

```
   a  b
0  2  5
1  3  6
```




