## Step 1 - Extraction

**Done**
- `extract_pages(pdf_path)` in `src/extraction.py`, built on PyMuPDF.
- Returns a list of `(page_number, text)`, page numbers start at 1.
- Text is normalized with Unicode NFKC.

**Measured result**
- Tested on 1 database course PDF: 8 pages, 0 empty pages.
- Text length per page: from 84 to 451 characters.
- 7 pages out of 8 contain at least one image.
- `"fiddle" in text` on page 5: False before NFKC, True after.
- A first test on a non-database PDF (13 pages) showed the same header repeated on every page.

**What failed**
- Some pages contain images, so PyMuPDF cannot extract the text inside them.
- The footer (author, section title, date, page counter) is repeated on the pages I inspected (5 and 8).
- `if not text` does not detect pages that are almost empty: 0 empty pages does not mean there are no poor pages.
- The “fi” ligatures broke keyword search.
- Bullet points are extracted as a "§" character at the start of each bullet line, probably because the PDF uses a symbol font that is decoded incorrectly.

**Next step**
- Step 2: split pages into passages with metadata (course, file, page).

## Step 2 - Passages

**Done**
- `build_passages(pages, course, file)` in `src/passages.py`.
- One passage per page, as a dict with `course`, `file`, `page`, `text`.

**Measured result**
- 8 pages gave 8 passages, page numbers preserved.

**What failed**
- Nothing failed in this step.
- Known limit: passages still contain the repeated footer, and short pages (title only) are kept as they are. Both are left for a later, measured step.

**Next step**
- Gather all database course PDFs: 8 pages is too small for Recall@5 to mean anything (5 of 8 pages is already 62% by chance).