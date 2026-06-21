from manual_sections import build_sections


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
