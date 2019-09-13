from pprint import pprint
from itertools import chain


# Ignore command which contains words
ignore = ['ipv6', 'sh run',
          'Current configuration', 'Building configuration',
          'aqm-register-fnf',
          'clock timezone',
          'vlan internal allocation', 'banner motd']


def clean_config(config):
    """
    Delete ! sign and lines with commands in ignore list.
    config - file of configuration.
    Return config as a list
    """
    with open(config) as cfg:
        clean_cfg = [line.rstrip() for line in cfg
                     if not '!' in line[:3]
                        and line.rstrip()
                        and not ignore_command(line, ignore)]
    return clean_cfg


def ignore_command(command, ignore):
    """
    Checks command if it contains words from ignore list.
    command - string, command to check,
    ignore - list of words.
    Return True if command contains word from ignore list, False otherwise.
    """

    return any(word in command for word in ignore)


def all_children_flat(section, level):
    """
    Function checks if all children in ALL sections is in same level.
    * section_dict - dictionary with sections.
    * level - integer, current level of depth.
    Returns True if all children in all sections is in the same level, False otherwise.
    """
    result = []
    for child in section:
        try:
            is_alpha = child[(level+1):][0].isalpha()
            result.append(is_alpha)
        except IndexError:
            print(child)
    return all(result)


def takewhile_partition(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    x = ''
    items_iterator = iter(iterable)
    items_before = []

    for x in items_iterator:
        if predicate(x):
            items_before.append(x)
        else:
            break
    return items_before, chain([x], items_iterator)


def parse_cfg_to_sections(config, level=0):
    """
    Функция парсит конфигурацию и возвращает словарь.
    Рекурсивно парсит каждую секцию в которой не все команды на одном уровне
    """
    config_dict = {}

    while True:
        try:
            line = next(config)
        except StopIteration:
            break
        try:
            if line[level].isalnum():
                section = line
                section_content, config = takewhile_partition(
                    lambda line: not line[level].isalpha(), config)
                if not all_children_flat(section_content, level):
                    section_content = parse_cfg_to_sections(iter(section_content), level+1)
                config_dict[section] = section_content
        except IndexError:
            break

    return config_dict


def parse_config(filename):
    """
    Функция ожидает имя файла и возвращает конфигурацию в виде словаря
    """
    cleaned_config = iter(clean_config(filename))
    return parse_cfg_to_sections(cleaned_config)


if __name__ == "__main__":
    result = parse_config('example_cfg.txt')
    pprint(result, width=160)

