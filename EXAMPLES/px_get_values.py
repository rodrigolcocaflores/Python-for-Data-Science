#!/usr/bin/env python
import openpyxl as px

def main():
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb.active  # <.>
    headers = next(ws.values)   # <.>
    for row in ws.values:  # <.>
        print(row[:5])   # <.>


if __name__ == '__main__':
    main()
