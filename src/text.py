import re


def find_substring_by_regex(text, pattern, all_match=False):
    texts_found = re.findall(pattern, text)
    text_match = None
    if all_match:
        text_match = [text_found for text_found in texts_found if len(text_found) > 0]
    else:
        if len(texts_found) > 0:
            texts_found_lens = [len(text_found) for text_found in texts_found]
            max_len = max(texts_found_lens)
            idxs_max_len = [
                i for i, text_len in enumerate(texts_found_lens) if text_len == max_len
            ]
            text_match = texts_found[idxs_max_len[0]]

    return text_match


def find_substring_with_space(text, find_text, limit_spaces=1, all_match=False):
    spaces = f"[ ]{{0,{limit_spaces}}}"
    pattern = spaces.join([f"[{char}]{{1}}" for char in list(find_text)])
    return find_substring_by_regex(text, pattern, all_match)


def find_substring_by_text_list(text, find_text_list):
    idx_found = None
    text_found = None
    for idx, text_l in enumerate(find_text_list):
        if text == text_l or text.find(text_l) > -1:
            idx_found = idx
            text_found = text_l
            break
    return idx_found, text_found


def find_substring_with_space_by_text_list(text, find_text_list, limit_spaces=1):
    idx_found = None
    text_found = None
    for idx, text_l in enumerate(find_text_list):
        text_found = find_substring_with_space(text, text_l, limit_spaces)
        if text_found is not None:
            idx_found = idx
            break
    return idx_found, text_found


def replace_or_include_values_in_list_by_index(tagert_list, idx_list, new_values):
    if new_values is None or len(new_values) == 0:
        tagert_list_copied = tagert_list.copy()
        del tagert_list_copied[idx_list]
        final_list = tagert_list_copied
    else:
        final_list = tagert_list[:idx_list] + new_values + tagert_list[idx_list + 1 :]
    return final_list


def remove_sub_text_from_list(text_list, text_list_remove):
    new_text_list = text_list
    if len(text_list_remove) > 0:
        new_text_list = []
        for idx_t, text in enumerate(text_list):
            if idx_t in text_list_remove:
                text_remove = text_list_remove[idx_t]
                for text_splited in text.split(text_remove):
                    if len(text_splited.replace(" ", "")) > 0:
                        new_text_list.append(text_splited)
            else:
                new_text_list.append(text)
    return new_text_list


def ratio_text_list_a_in_text_list_b(list_a, list_b):
    a_in_b = []
    for text_a in list_a:
        a_in_b.append(text_a in list_b)

    return sum(a_in_b) / len(a_in_b)


def extract_substring_from_circular_text_by_regex(text, pattern, text_union=" "):
    residual_text = text
    found_text = None

    found_texts = re.findall(pattern, text, flags=re.DOTALL)

    if len(found_texts) > 0:
        found_text = found_texts[0]
        start_index = text.find(found_text)
        end_index = start_index + len(found_text)

        if start_index == 0:
            residual_text = text[end_index:]
        elif end_index == len(text):
            residual_text = text[:start_index]
        else:
            text_p1 = text[:start_index]
            text_p2 = text[end_index:]
            residual_text = text_p2 + text_union + text_p1
    else:

        concatenated_text = text + text_union + text
        found_texts = re.findall(pattern, concatenated_text, flags=re.DOTALL)
        if len(found_texts) > 0:
            found_text = found_texts[0]
            start_index = concatenated_text.find(found_text)
            end_index = (start_index + len(found_text) - len(text_union)) % len(text)
            residual_text = text[end_index:start_index]

    return found_text, residual_text
