def find_key(name: str, website: dict, depth=0):
    result = None
    if name in website:
        return website[name]
    if depth > 0:
        for i in website:
            result = find_key(name, website[i], depth - 1)
    return result


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
name_in = input("Введите искомый ключ: ")
depth_bool = input("Хотите ввести максимальную глубину? Y/N:")
if depth_bool.lower() == "y":
    depth_in = int(input("Введите максимальную глубину: "))
    answer = find_key(name_in, site, depth_in)
    if answer is None:
        print("Ключ не найден")
    else:
        print("Значение ключа:", answer)
else:
    answer = find_key(name_in, site)
    if answer is None:
        print("Ключ не найден")
    else:
        print("Значение ключа:", answer)
