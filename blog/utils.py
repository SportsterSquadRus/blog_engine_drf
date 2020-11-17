def banned_tags_check(tags_list):
    with open('blog/banned_words.txt', encoding='utf8') as file:
        STOP_LIST = file.read().split(', ')
    clean_tags = []
    for tag in tags_list:
        if tag not in STOP_LIST:
            clean_tags.append(tag)
    return clean_tags