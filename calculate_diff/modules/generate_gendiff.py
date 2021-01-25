import json


def generate_string_diff(dict1, dict2, key):
    result = []
    if dict1.get(key, object) == object:
        result.append('  + {0}: {1}'.format(key, dict2.get(key)))
    elif dict2.get(key, object) == object:
        result.append('  - {0}: {1}'.format(key, dict1.get(key)))
    elif dict1.get(key) == dict2.get(key):
        result.append('    {0}: {1}'.format(key, dict1.get(key)))
    else:
        result.append('  - {0}: {1}'.format(key, dict1.get(key)))
        result.append('  + {0}: {1}'.format(key, dict2.get(key)))
    return result


def union_keys(dictionary1, dictionary2):
    return set(dictionary1.keys()).union(set(dictionary2.keys()))


def generate_diff(first_file, second_file):
    dictionary1 = json.load(open(first_file))
    dictionary2 = json.load(open(second_file))
    all_keys = union_keys(dictionary1, dictionary2)
    result = ['{']
    for key in all_keys:
        result.extend(generate_string_diff(dictionary1, dictionary2, key))
    result.append('}')
    return '\n'.join(result)

