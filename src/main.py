from text import find_substring_by_regex

if __name__ == "__main__":
    TEXT = "20//23"
    DATE_PATTERN = r"[0-5][ ]{0,1}[0-9][/|1]{0,2}[ ]{0,1}[2-5][ ]{0,1}[0-9]"
    text_found = find_substring_by_regex(TEXT, DATE_PATTERN)
    print(text_found)
