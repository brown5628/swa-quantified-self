# %%
from pathlib import Path
import re
from datetime import datetime

def infer_date_from_filename(filename: str):
    filename_string = Path(filename).stem
    match = re.search(r'\d{4}-\d{2}-\d{2}', filename_string)
    inferred_date = datetime.strptime(match.group(), '%Y-%m-%d').date()
    inferred_date = inferred_date.strftime('%Y-%m-%d')
    return inferred_date