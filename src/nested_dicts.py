def flat_dict(dictionary: dict, path=None) -> list:
    if path is None:
        path = []

    result = []

    for key, value in dictionary.items():
        new_path = path + [key]

        if isinstance(value, dict):
            if all(not isinstance(v, dict) for v in value.values()):
                result.append([new_path, list(value.values())])
            else:
                result.extend(flat_dict(value, new_path))

    return result