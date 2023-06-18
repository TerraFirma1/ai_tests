import json
import docx2txt


def read_file(name, path):
    res = docx2txt.process(name, path)
    return res


content = read_file('Edward_Royce_v2.docx', './')

print(content)


