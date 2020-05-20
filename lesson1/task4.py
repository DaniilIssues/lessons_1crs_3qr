array = ['разработка', 'администрирование', 'protocol', 'standard']
array_bytes = []
array_str = []
for i in array:
    array_bytes.append(i.encode('utf-8'))

for i in array_bytes:
    array_str.append(i.decode('utf-8'))

print(array_bytes)
print(array_str)
