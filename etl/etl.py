from collections import defaultdict
def transform(legacy_data):
    data=defaultdict()
    for key in legacy_data.keys():
        for value in legacy_data[key]:
            data[value.lower()]=key
    return data
