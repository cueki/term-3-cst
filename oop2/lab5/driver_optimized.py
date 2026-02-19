"""
I use str.translate (very underutilized if I do say so myself) to make a lookup table so that translate() is O(n).

Then open the file in binary (for obvious reasons). Then do said translate() to process the whole file in a single call.

The real optimization begins when I split()[::-1] to reverse the input order, such that the first occurrence in the original order is kept,
then call lower() on the same giant string to create keys for a dict(zip(keys, values)).

Due to how dicts work, this mapping of lowercase keys to original case values cause the duplicated keys to automatically get overwritten, its basically a set.

I then handle the case where split() after translate() drops any tokens that become empty strings after punctuation removal by adding an empty string.

Then I simply build the list with the dict values. The print call is also using unpacking to do it all in a single operation.
"""


_PUNCT_TABLE = str.maketrans("", "", ",*;.:([])")
with open("House of Usher.txt", mode="rb") as _f:
    _content = _f.read().decode("utf-8")
_translated = _content.translate(_PUNCT_TABLE)
_seen = dict(zip(_translated.lower().split()[::-1], _translated.split()[::-1]))
_seen[""] = ""
different_words = list(_seen.values())
print(f"List of different words (Count: {len(different_words)})", "-" * 50, *different_words, "-" * 50, sep="\n")
