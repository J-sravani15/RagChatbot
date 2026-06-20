import pymupdf4llm

pdf_path = "documents/sales.pdf"

try:
    text = pymupdf4llm.to_markdown(pdf_path)

    print("=" * 50)
    print(text[:2000])
    print("=" * 50)

except (FileNotFoundError, ValueError) as e:
    print("Error:", e)
