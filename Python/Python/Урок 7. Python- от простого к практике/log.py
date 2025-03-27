def log_info(info):
    with open('log.txt', 'a', encoding='utf-8') as f:
        if len(info.split()) == 1:
            f.write(f'экспорт - {info}' + '\n')
        else:
            f.write(f'импорт - {info}' + '\n')