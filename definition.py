"""
Python Definition to copy and paste in other python codes

List:
    writeText
"""

def writeText(file_name, article_text):
    with open(file_name, "w") as text_file: 
        text_file.write(article_text)