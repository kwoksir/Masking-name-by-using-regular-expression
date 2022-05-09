# Masking Name by Using Regular Expression


## Procedures
1. Import the libraries
2. Open the Excel file
3. Masking by using regular expression
4. Save and close the file

## Step 1: Import the libraries
```python
import openpyxl
import re
```
## Step 2: Open the Excel file
```python
wb = openpyxl.load_workbook('demo.xlsx')
sheet = wb.worksheets[0]
```
## Step 3: Masking by using regular expression
```python
for i in range(sheet.max_row):
    sheet.cell(row=i+1, column=2).value = re.sub(r'[a-z]', '*', sheet.cell(row=i+1,column=1).value)
```
## Step 4: Save and close the file
```python
wb.save("demo.xlsx") 
print('Done')
```