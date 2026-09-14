# plp-python-week7
# Assignment: Shopping List Manager

This assignment practices Python lists, indexes, `.append()`, `.remove()`, membership checking with `in`, loops, and list summaries.

## Files

* `list_warmup.py` - Demonstrates creating a list, accessing items by index, adding and removing items, and counting list items.
* `shopping_list.py` - Provides an interactive shopping list manager for adding, removing, showing, and finishing a shopping list.
* `list_report.py` - Prints a numbered shopping list, counts item names with more than four letters, and finds the longest item name.
* `screenshots/` - Contains screenshots showing the required program outputs.

## Why is it safer to check `in` before calling `.remove()`?

It is safer to check `in` first because `.remove()` causes an error if the item does not exist in the list. Checking whether the item is present allows the program to handle the situation safely and display a helpful message instead of crashing.
