with open('tmp.py', encoding='utf-8') as fd:
    content = fd.read()
with open('newtmp.py', 'w', encoding='utf-8') as fd:
    fd.write(content)

