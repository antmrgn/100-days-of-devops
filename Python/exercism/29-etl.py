def transform(legacy_data):
    '''transform the legacy data format to the shiny new format'''
    a = {}
    for item in legacy_data.items():
        for i in item[1]:
            b = {i.lower(): item[0]}
            a.update(b)
    return a
