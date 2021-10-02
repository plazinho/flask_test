def artist_count():
    with open("api/data/artist_names.txt", 'r', encoding="utf-8") as file:
        return len(file.read().strip().split('\n'))
