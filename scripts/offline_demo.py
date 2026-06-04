"""Offline locality inference demo for the archived Twitter prototype.

The live scraper/API code is intentionally not exercised here because it needs
credentials and depends on old Twitter/X markup. This keeps the normalization
idea demoable with fixed sample profile locations.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CITY_ALIASES = {
    "atl": "Atlanta",
    "atlanta": "Atlanta",
    "new york": "New York",
    "nyc": "New York",
    "san francisco": "San Francisco",
    "sf": "San Francisco",
    "knoxville": "Knoxville",
    "nashville": "Nashville",
}
SAMPLE_LOCATIONS = [
    "ATL",
    "Atlanta, GA",
    "nyc",
    "New York, NY",
    "San Francisco Bay Area",
    "SF",
    "Knoxville, TN",
    "",
    "Nashville / Knoxville",
    "Greater Atlanta Area",
]


def normalize(location: str) -> str | None:
    text = re.sub(r"[^a-zA-Z ]+", " ", location).lower()
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return None
    for alias, city in CITY_ALIASES.items():
        if re.search(rf"\b{re.escape(alias)}\b", text):
            return city
    return None


def main() -> None:
    counts = Counter(filter(None, (normalize(location) for location in SAMPLE_LOCATIONS)))
    top_city, top_count = counts.most_common(1)[0]
    lines = [
        "# Twitter Locality Offline Demo",
        "",
        f"Sample profile locations: {len(SAMPLE_LOCATIONS)}",
        f"Normalized locations: {sum(counts.values())}",
        f"Most common inferred city: {top_city} ({top_count})",
        "",
        "Counts:",
    ]
    for city, count in counts.most_common():
        lines.append(f"- {city}: {count}")

    output = "\n".join(lines) + "\n"
    output_path = ROOT / "outputs" / "offline_demo_summary.md"
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text(output, encoding="utf-8")
    print(output)


if __name__ == "__main__":
    main()
