import json
import re

import pymupdf4llm

pdf_path = "documents/sales.pdf"

markdown_text = pymupdf4llm.to_markdown(pdf_path)

sections = []

parts = re.split(r"\n##\s+", markdown_text)

for part in parts:
    part = part.strip()

    if not part:
        continue

    lines = part.split("\n", 1)

    title = lines[0]

    content = lines[1] if len(lines) > 1 else ""

    sections.append({"title": title, "content": content})

with open("sections.json", "w", encoding="utf-8") as f:
    json.dump(sections, f, indent=2, ensure_ascii=False)

print(f"Created {len(sections)} sections")
print()

print("First Section:")
print("-" * 50)
print(sections[0]["title"])
print("-" * 50)
print(sections[0]["content"][:500])
