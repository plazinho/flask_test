def update_artist_names(name):
    with open(f"../../api/data/artist_names.txt", "a") as f:
        f.write(f"{name}\n")
