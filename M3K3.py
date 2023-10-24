random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# filter
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

# map
def map_int_to_units(value):
    ratusan = value // 100
    sisa = value % 100
    puluhan = sisa // 10
    satuan = sisa % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

int_mapped = list(map(map_int_to_units, int_values))

print("Data Float :", float_values)
print("Data Int :")
for item in int_mapped:
    print(item)
print("Data String :", [s.lower() for s in string_values])
