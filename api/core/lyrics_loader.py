def lyrics_loader(name: str) -> str:
    """
    Подгружает все тексты исполнителя 'name' в одной строке
    :param name: имя исполнителя
    :return: тексты песен исполнителя
    """
    with open(f"api/data/raw_data/{name}.txt", 'r', encoding='utf-8', newline='') as f:
        return f.read().replace("EmbedShare URLCopyEmbedCopy", "")
