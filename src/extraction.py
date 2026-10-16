import sys
import pymupdf
import unicodedata
from pathlib import Path


def extract_pages(pdf_path: str) -> list[tuple[int, str]]:
    """Return (page_number, text) for each page, start at 1."""
    path = Path(pdf_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")
    pages = []
    with pymupdf.open(path) as doc:
        for page_number, page in enumerate(doc, start=1):
            text = unicodedata.normalize("NFKC", page.get_text()).strip()
            pages.append((page_number, text))
    return pages


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/extraction.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    pages = extract_pages(pdf_path)
    print(len(pages), "pages")

    count_empty = 0
    for number, text in pages:
        print(number, len(text))
        if not text:
            count_empty += 1
    print(f"empty pages: {count_empty}")
    
    