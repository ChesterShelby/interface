def query(params):
    return '&'.join(sorted(f'{k}={v}' for k, v in params.items()))


print(query({'course': 'python', 'lesson': 2, 'challenge': 17}))
