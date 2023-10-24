data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def extract_integers(text):
    return list(filter(str.isdigit, text.split()))

result = [extract_integers(entry) for entry in data]

for item in result:
    print(item)
