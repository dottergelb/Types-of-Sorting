import asyncio
import random
import sys
import time
import tabulate
from pld.binvstavki import bin_vstavki_up, bin_vstavki_down
from pld.derevo import sort_up, sort_down
from pld.quicksort import quicksort_up, quicksort_down
from pld.sheiker import shaker_up, shaker_down
from pld.shell import shell_up, shell_down
from pld.viborka import vibor_up, vibor_down
from pld.vstavki import vstavki_up, vstavki_down

sys.setrecursionlimit(10000000)
elements_1 = [100, 1000, 10000]
elements_2 = [100, 1000, 10000, 100000, 1000000]
elements_3 = [1000, 10000, 100000, 1000000]
elements_4 = [100000, 1000000]
elements_5 = [1000, 10000, 100000, 1000000, 10000000]
elements_6 = [100, 1000]


def generate_list(elements):
    return [random.randint(1, 100000) for _ in range(elements)]


async def sorted(elements, lists, up, down, name):
    data = []
    for i in elements:
        start_time = time.time()

        list_sort = up(lists[i], i)
        end_time = time.time()
        sort_time = end_time - start_time

        start_time = time.time()
        list_sort = up(list_sort, i)
        end_time = time.time()
        voz_time = end_time - start_time

        start_time = time.time()
        down(list_sort, i)
        end_time = time.time()
        men_time = end_time - start_time
        data.append({
            'Название': f'{name}',
            'Количество элементов': i,
            'Сортировка': sort_time,
            'Возрастание': voz_time,
            'Убывание': men_time,
        })
    return data


async def start():
    lists = {
        100: generate_list(100),
        1000: generate_list(1000),
        10000: generate_list(10000),
        100000: generate_list(100000),
        1000000: generate_list(1000000),
        10000000: generate_list(10000000),
    }
    import datetime
    print(f'Время запуска: {datetime.datetime.now().time().strftime("%H:%M")}')
    start = time.time()
    tasks = []
    tasks.append(sorted(elements_5, lists, quicksort_up, quicksort_down, 'Быстрая сортировка'))
    tasks.append(sorted(elements_6, lists, sort_up, sort_down, 'Дерево'))
    tasks.append(sorted(elements_3, lists, shaker_up, shaker_down, 'Шейкер'))
    tasks.append(sorted(elements_3, lists, shell_up, shell_down, 'Шелл'))
    tasks.append(sorted(elements_1, lists, vibor_up, vibor_down, 'Выборка'))
    tasks.append(sorted(elements_1, lists, vstavki_up, vstavki_down, 'Вставки'))
    tasks.append(sorted(elements_2, lists, bin_vstavki_up, bin_vstavki_down, 'Бинарные вставки'))

    (quick_sort_results, tree_sort_results, sheiker_sort_results, shell_sort_results, choice_sort_results,
     vstavki_sort_results, binar_sort_results) = await asyncio.gather(*tasks)

    combined_result = []
    for results in (quick_sort_results, tree_sort_results, sheiker_sort_results, shell_sort_results,
                    choice_sort_results, vstavki_sort_results, binar_sort_results):
        combined_result.extend(results)
    end = time.time()
    headers = ["Количество", "Название", "Сортировка", "Возрастание", "Убывание"]
    print(tabulate.tabulate(combined_result, headers=dict(enumerate(headers)), tablefmt="pretty"))
    print(f'Общее время работы кода: {end - start}')


asyncio.run(start())
