def banned_tags_check(tag):
    with open('blog/banned_words.txt', encoding='utf8') as file:
        STOP_LIST = file.read().split(', ')
    if tag not in STOP_LIST:
        return True