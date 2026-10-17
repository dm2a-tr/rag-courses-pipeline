



def build_passages(pages :list[tuple[int, str]], course : str,file: str) -> list[dict[str, str | int]]:
    """Return one passage per page, as a dict with keys course, file, page and text."""
    passages = []
    for number, text in pages:
        passage = {"course":course,"file":file,"page":number,"text":text}
        passages.append(passage)
    return passages