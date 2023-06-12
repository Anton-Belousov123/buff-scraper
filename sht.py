import gspread


def read_links():
    gc = gspread.service_account("parser-buff163-dcf844ba7756.json")
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1x2CtS3ISIUM_9EWmYurR3iM9xlFV_B9a669NPjW-UvA/edit#gid=0').sheet1
    return sheet.col_values(1)
