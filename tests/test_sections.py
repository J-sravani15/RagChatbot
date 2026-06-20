import re


def build_sections(markdown_text):
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
    return sections


def test_build_sections():
    markdown = """
## Section 1
Hello World

## Section 2
StudentAI
"""
    sections = build_sections(markdown)
    assert len(sections) == 2


def test_build_sections_empty():
    assert build_sections("") == []


def test_build_sections_no_headings():
    result = build_sections("Just plain text\n\nNo headings here")
    assert len(result) == 1


def test_build_sections_with_content():
    markdown = """
## Title
Content line 1
Content line 2
"""
    sections = build_sections(markdown)
    assert len(sections) == 1
    assert sections[0]["title"] == "Title"
    assert "Content line 1" in sections[0]["content"]
