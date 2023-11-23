def build_bad_char_table(pattern):
    bad_char_table = {}
    pattern_length = len(pattern)

    for i in range(pattern_length - 1):
        bad_char_table[pattern[i]] = pattern_length - 1 - i

    return bad_char_table


def build_good_suffix_table(pattern):
    pattern_length = len(pattern)
    good_suffix_table = [0] * pattern_length
    suffix = [0] * pattern_length

    suffix[pattern_length - 1] = pattern_length
    j = pattern_length - 1

    for i in range(pattern_length - 2, -1, -1):
        if i > j and suffix[i + pattern_length - 1 - j] < i - j:
            suffix[i] = suffix[i + pattern_length - 1 - j]
        else:
            if i < j:
                j = i
            while j >= 0 and pattern[j] == pattern[j + pattern_length - 1 - i]:
                j -= 1
            suffix[i] = i - j

    for i in range(pattern_length - 1):
        good_suffix_table[i] = pattern_length

    for i in range(pattern_length - 1):
        good_suffix_table[pattern_length - 1 -
                          suffix[i]] = pattern_length - 1 - i

    return good_suffix_table


def boyer_moore_search(text, pattern):
    bad_char_table = build_bad_char_table(pattern)
    good_suffix_table = build_good_suffix_table(pattern)

    text_length = len(text)
    pattern_length = len(pattern)
    i = 0

    while i <= text_length - pattern_length:
        j = pattern_length - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            # Pattern found
            return i

        bad_char_shift = bad_char_table.get(text[i + j], pattern_length)
        good_suffix_shift = good_suffix_table[j]

        i += max(bad_char_shift, good_suffix_shift)

    # Pattern not found
    return -1


text = "This is the boyer moore algo."
pattern = "the"
result = boyer_moore_search(text, pattern)

if result != -1:
    print(f"Pattern found at index {result}")
else:
    print("Pattern not found in the text.")
