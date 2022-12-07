import re

ext_lang_map = {
    "py": "python",
    "java": "java",
    "js": "javascript",
    "cpp": "cpp",
    "cxx": "cpp",
    "hpp": "cpp",
}


def highlight_multiline_code_md(md_text: str, language_str: str) -> str:
    """
    Highlight markdown-embedded code blocks.
    """
    out = ""
    in_code_block = False
    for line in md_text.split("\n"):
        if not in_code_block and re.search("^```(.*)$", line):
            in_code_block = True
            if line.strip() == "```":
                line = f"```{language_str}"
        elif in_code_block and line.strip() == "```":
            in_code_block = False

        out += line + "\n"

    return out
