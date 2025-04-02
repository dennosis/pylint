"""Este módulo fornece um funções para manipulação de textos."""

import re


def find_substring_by_regex(text, pattern):
    """Busca a substring mais longa que corresponde ao padrão no texto.

    Args:
        text (str): O texto no qual a pesquisa será realizada.
        pattern (str): A expressão regular usada para encontrar a substring.

    Returns:
        str | None: A substring mais longa encontrada ou
        None se nenhuma correspondência for encontrada.
    """
    texts_found = re.findall(pattern, text)
    text_match = None

    if len(texts_found) > 0:
        texts_found_lens = [len(text_found) for text_found in texts_found]
        max_len = max(texts_found_lens)
        idxs_max_len = [
            i for i, text_len in enumerate(texts_found_lens) if text_len == max_len
        ]
        text_match = texts_found[idxs_max_len[0]]

    return text_match
