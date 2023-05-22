import gspread
from oauth2client.service_account import ServiceAccountCredentials


def read_links():
    gc = gspread.service_account("parser-buff163-dcf844ba7756.json")
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1x2CtS3ISIUM_9EWmYurR3iM9xlFV_B9a669NPjW-UvA/edit#gid=0').sheet1
    i = 0
    links = []
    while True:
        i += 1
        v = sheet.cell(i, 1).value
        if v is not None:
            links.append(v)
        else:
            return links

