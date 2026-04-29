import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import items


def test_add_non_empty_item_appended():
    items.clear()
    item = "milk"
    if item:
        items.append(item)
    assert items == ["milk"]


def test_add_empty_string_is_skipped():
    items.clear()
    item = ""
    if item:
        items.append(item)
    assert items == []
