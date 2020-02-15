
with open('Scr.png', 'rb') as rf:
    with open('Scr_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
