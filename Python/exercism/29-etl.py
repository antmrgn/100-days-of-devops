def transform(legacy_data):
    a = {}
    for key, val in legacy_data:
        for i in val:
            b = {key : i}
            a.update(b)
    return a

legacy_data = {1: ["A"]}
print(transform(legacy_data))
