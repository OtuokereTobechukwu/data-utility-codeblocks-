# import libraries
import pandas as pd
from pathlib import Path

excel_file = Path.cwd()

all_dfs = pd.read_excel(excel_file, sheet_name=None)
#all_dfs.keys

concat_df = pd.concat(all_dfs, ignore_index=True)

