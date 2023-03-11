def transform(legacy_data):
    a = {}
    for key in legacy_data:
        for i in key:
            b = {key : i}
            a.update(b)
    return a

legacy_data = {1: ["A"]}
print(transform(legacy_data))
