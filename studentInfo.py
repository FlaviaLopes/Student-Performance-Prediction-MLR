import pandas as pd
pd.set_option('max_colwidth', 150)

def about():
    with open('student.txt', 'r') as f:
        about = f.read()
    about = about.split('\n')[1:36]
    del about[30:32]
    about = [' '.join(it.split(' ')[1:]) for it in about]

    data = {}
    [data.update( {it.split(' ')[0]: [' '.join(it.split(' ')[2:])]}) for it in about]
    data

    return pd.DataFrame(data=data)