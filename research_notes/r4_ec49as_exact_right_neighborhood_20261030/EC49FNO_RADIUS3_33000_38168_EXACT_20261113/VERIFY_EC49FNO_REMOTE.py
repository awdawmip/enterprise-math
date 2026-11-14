#!/usr/bin/env python3
"""EC49FNO compact finite certificate check; Python 3 standard library only.
If frozen original BRC generator files are present in this directory, also
check all 72 words against that original lawful catalogue and signed-prefix map.
This reads historical exact output, not a substitute for independent re-solving.
"""
from pathlib import Path
from collections import Counter
import base64, hashlib, json, lzma

P = Path(__file__).resolve().parent
def decode(name, expected_sha):
    data = lzma.decompress(base64.b64decode((P / name).read_text().strip(), validate=True))
    assert hashlib.sha256(data).hexdigest() == expected_sha
    return data

raw = decode("EXACT_VECTOR_33000_38168.u8x4.xz.b64",
             "69f844ff0c8938b1a2f35b8eb753b0f41b4f37b17bb14e7b3d0eabf792852db2")
assert len(raw) == 5169 * 4
rows = [(33000 + j, *raw[4*j:4*j+4]) for j in range(5169)]
assert all(0 < cost < 256 and ways >= 1 and gap >= 1 and 2 <= roots <= 4
           for _, cost, ways, gap, roots in rows)
assert min(r[1] for r in rows) == 111
assert max(r[1] for r in rows) == 234
assert [r[0] for r in rows if r[1] == 111] == [33877, 33880, 34044]
assert Counter(r[3] for r in rows) == {1:3616,2:440,3:689,4:113,5:244,6:48,7:14,8:3,9:2}
assert Counter(r[2] for r in rows) == {1:2553,2:1665,3:310,4:341,5:53,6:5,7:3,8:228,9:6,10:1,12:4}
for index in (33877,33880,34044):
    assert rows[index-33000][1:4] == (111,2,1)
print("TAIL_VECTOR_PASS", len(rows), "minimum", 111, "maximum", 234)

words = json.loads(decode("MINIMA_COMPACT_ORIGINAL_WORDS.json.xz.b64",
                         "39fa36e8f769ebc768b2fca6dbbe8a11b00771e96686b6fe20f7e1851f14ca38"))
assert set(words) == {"33877","33880","34044"}
for index, record in words.items():
    assert len(record["keys"]) == 7 and len(set(record["keys"])) == 7
    assert len(record["words"]) == 24
    assert len({tuple(label) for label, word in record["words"]}) == 24
print("WITNESS_STRUCTURE_PASS", sum(len(w["words"]) for w in words.values()))

if (P / "EC49FGW_RADIUS5_SCREEN.py").is_file() and (P / "EC49FGJ_SEVEN_KEY_94_WITNESSES.json").is_file():
    from EC49FGW_RADIUS5_SCREEN import all_words, pref, raw_key, PIN
    assert PIN == "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"
    original = list(all_words())
    assert len(original) == 178850
    original_set = set(original)
    cache_keys = sorted({raw_key(word) for _, word in original})
    for index, record in words.items():
        chosen = record["words"]
        allowed = {cache_keys[k] for k in record["keys"]}
        prefixes = set()
        counts = Counter()
        for label, word in chosen:
            label = tuple(label)
            assert (label,word) in original_set and raw_key(word) in allowed
            ps = pref(word)
            prefixes.update(ps)
            counts[ps[0]] += 1
        assert len(prefixes) == 111 and len(counts) == 3
        print("ORIGINAL_NATIVE_WITNESS_PASS", index, "words", 24, "prefixes", 111)
else:
    print("SOURCE_LEGALITY_CHECK_REQUIRES_FROZEN_GENERATOR_FILES")
