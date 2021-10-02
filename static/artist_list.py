def artist_list():
    with open("api/data/artist_names.txt", 'r', encoding="utf-8") as file:
        return '\n'.join(sorted(file.read().strip().split('\n'))).replace('_', '/')
