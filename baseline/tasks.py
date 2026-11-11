"""Baseline tasks: level-check exercises for lesson 4."""
from __future__ import annotations

import json


def count_selected(media_ids: list[str]) -> int:
    """Return the number of distinct media ids."""
    return len(set(media_ids))
    #מקבלת מערך ומחזירה ללא כפלויות


def group_by_gallery(media: list[dict]) -> dict[str, list[str]]:
    """Map gallery_id -> list of media ids in that gallery."""
    groups: dict[str, list[str]] = {}
    for item in media:
        groups.setdefault(item["gallery_id"], []).append(item["id"])
    return groups
    # מקבלת מערך של אובייקטים ומחזירה אובייקט שממפה gallery_id לרשימת media_ids


def total_price(prices_minor: list[int | None]) -> int:
    """Sum prices, ignoring None values."""
    return sum(p for p in prices_minor if p is not None)
    # מקבלת מערך של מספרים או None ומחזירה את הסכום של המספרים, מתעלמת מNone


def first_missing(required: list[str], present: list[str]) -> str | None:
    """Return the first item in required that is not in present, or None."""
    present_set = set(present)
    for item in required:
        if item not in present_set:
            return item
    return None
    # מקבלת שני מערכים ומחזירה את האיבר הראשון במערך הראשון שלא נמצא במערך השני, או None אם כולם נמצאים


def load_events(path) -> list[dict]:
    """Load a UTF-8 JSON file, keeping Hebrew text intact."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)
        # מקבלת נתיב לקובץ JSON ומחזירה מערך של אובייקטים, תוך שמירה על טקסט בעברית