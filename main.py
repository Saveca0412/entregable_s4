import pandas as pd
import requests

def coon_pool_to_google_spreadsheets(sheet_id):
    return f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&id={sheet_id}&gid=135007174'

sheet_id = '1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU'
url = coon_pool_to_google_spreadsheets(sheet_id=sheet_id)
df = pd.read_csv(url)
