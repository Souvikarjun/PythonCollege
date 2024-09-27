import Addition

attributes = dir(Addition)

for item in attributes:
    if not item.startswith('__'):
        print(item)