# Mahdi Sabbouri
# 11/15
# bots.py

"""bots.py"""

import threading
import time

def bot_clerk(items):
    """Bot_clerk"""
    cart = []
    lock = threading.Lock()

    robot_fetcher_lists = {1: [], 2: [], 3: []}

    for i, item in enumerate(items):
        robot_fetcher_lists[(i % 3) + 1].append(item)

    threads = []
    for i in range(1, 4):
        thread = threading.Thread(target=bot_fetcher, args=(robot_fetcher_lists[i], cart, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return cart

def bot_fetcher(items, cart, lock):
    """bot_fetcher"""
    inventory = {
        "101": ["Notebook Paper", 2],
        "102": ["Pencils", 2],
        "103": ["Pens", 6],
        "104": ["Graph Paper", 1],
        "105": ["Paper Clips", 1],
        "106": ["Staples", 4],
        "107": ["Stapler", 7],
        "108": ["3 Ring Binder", 1],
        "109": ["Printer Paper", 1],
        "110": ["Notepad", 1]
    }

    for item in items:
        item_number = item
        item_description = inventory[item][0]
        seconds = inventory[item][1]

        time.sleep(seconds)

        with lock:
            cart.append([item_number, item_description])
