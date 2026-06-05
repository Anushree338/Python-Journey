#write a program to fill in letter templete with name and date

letter = '''Dear <|NAME|>,
You are selected 
<|DATE|>'''
print(letter.replace("<|NAME|>","harry").replace("<|DATE|>","20/06/2024"))