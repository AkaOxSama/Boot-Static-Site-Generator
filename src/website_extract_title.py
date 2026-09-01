

def extract_title(markdown: str) -> str:
    lines = [line for line in markdown.split("\n") if line != ""]
    if lines[0][:2] != "# ":
        raise ValueError("invalid markdown syntax, missing '# ' to extract a proper title")
    return lines[0][2:]
    
