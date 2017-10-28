from collections import Counter
from math import log2


B64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
HEX_CHARS = "1234567890abcdefABCDEF"

def shannon_entropy(input_data):
    '''
    Count entropy for given string input data.

    The method of using shannon entropy to detect high-entropy strings like
    RSA keys, secrets, and other fun treasures is was discussed in this post:
    http://blog.dkbza.org/2007/05/scanning-data-for-entropy-anomalies.html

    Shannon entropy code from this reddit post: https://redd.it/4fc896

    Args:
        input_data (str): string data to calculate entropy from.
    Returns: (float) entropy count
    '''
    return -sum(i/len(input_data) * log2(i/len(input_data)) \
            for i in Counter(input_data).values())


def find_suspicious_strings(word, charset, threshold=20):
    '''
    Iterate through each character of a word, and parse out long strings that
    contain only characters in the given `charset` (base64/hex).

    Args:
        word (str): string of characters
        charset (str): a string of characters that define your charset.
            It is recommended to use the provided `B64_CHARS` or
            `HEX_CHARS` charsets.
        threshold (int): threshold of characters to consider the given word a
            potential match. Defaults to 20.
    Returns: (list) of suspicious strings.
    '''
    char_match_count = 0
    matched_chars = ''
    strings = []

    for char in word:
        # If character exists in the given charset (base64/hex), concat the
        # character into `matched_chars`, and increment `char_match_count`.
        if char in charset:
            matched_chars += char
            char_match_count += 1
        else:
            # If current character does not exist in the given charset, we've
            # reached the end of a potential matched string.
            #
            # So we'll check if the matched character count  is greater than
            # our desired threshhold (20chars default).
            #
            # If it is not, we will drop this string.
            #
            # If the `character_match_count` is greater than the specified
            # threshhold, it's probably a match and we should keep it.
            if char_match_count > threshold:
                strings.append(matched_chars)

            matched_chars = ''
            char_match_count = 0

    # If the character match count is greater than the threshold, append it to
    # the strings array.
    if char_match_count > threshold:
        strings.append(matched_chars)

    return strings
