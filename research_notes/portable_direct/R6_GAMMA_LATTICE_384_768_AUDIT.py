#!/usr/bin/env python3
"""PREFIX-750A-R6: original-768-fine-grid geometric audit of published
Gamma auxiliary certificate coordinates. Pure finite integer geometry.
The source records (with exact Git blob OIDs) appear in the companion report.
Does not certify the inherited Gamma inequality or historical 712 union.
"""
from fractions import Fraction

PAIR_STRINGS = {
    "sibling": """7-45 7-46 8-46 15-46 16-46 7-47 8-47 9-47 10-47 15-47 16-47 17-47 18-47 20-47 7-48 8-48 9-48 10-48 11-48 20-48 21-48 8-49 9-49 10-49 11-49 12-49 13-49 18-49 19-49 20-49 21-49 22-49 23-49 8-50 9-50 10-50 11-50 12-50 13-50 14-50 15-50 16-50 17-50 18-50 19-50 20-50 21-50 22-50 23-50 24-50 10-51 11-51 12-51 13-51 14-51 15-51 16-51 17-51 18-51 19-51 20-51 21-51 22-51 23-51 24-51 25-51 11-52 12-52 13-52 14-52 15-52 16-52 17-52 18-52 19-52 20-52 21-52 22-52 23-52 24-52 25-52 26-52 27-52 28-52 29-52 30-52 11-53 12-53 13-53 14-53 15-53 16-53 17-53 18-53 19-53 20-53 12-54 13-54 14-54 15-54 16-54 17-54 18-54 19-54 20-54 13-55 14-55 15-55 16-55 17-55 18-55 19-55 12-56 13-56 14-56 15-56 16-56 17-56 18-56 19-56 13-57 14-57 15-57 16-57 17-57 18-57 19-57 14-58 15-58 16-58 17-58 18-58 19-58 14-59 15-59 16-59 17-59 18-59 19-59 20-59 21-59 15-60 16-60 17-60 18-60 19-60 20-60 21-60 22-60 15-61 16-61 17-61 18-61 19-61 20-61 21-61 22-61 15-62 16-62 17-62 18-62 19-62 20-62 21-62 22-62 15-63 16-63 17-63 18-63 19-63 20-63 21-63 22-63 15-64 16-64 17-64 18-64 19-64 20-64 21-64 22-64 15-65 16-65 17-65 18-65 19-65 20-65 21-65 22-65 15-66 16-66 17-66 18-66 19-66 20-66 21-66 22-66""",
    "741": """20-40 21-40 22-40 23-40 24-40 25-40 20-41 21-41 22-41 23-41 24-41 25-41 26-41 27-41 28-41 20-42 21-42 22-42 23-42 24-42 25-42 26-42 27-42 28-42 29-42 20-43 21-43 22-43 23-43 24-43 25-43 26-43 27-43 28-43 29-43 20-44 21-44 22-44 23-44 24-44 25-44 26-44 27-44 28-44 29-44 20-45 21-45 22-45 23-45 24-45 25-45 26-45 27-45 28-45 29-45 20-46 21-46 22-46 23-46 24-46 25-46 26-46 27-46 28-46 29-46 21-47 22-47 23-47 24-47 25-47 26-47 27-47 28-47 29-47 22-48 23-48 24-48 25-48 26-48 27-48 28-48 29-48 24-49 25-49 26-49 27-49 28-49 29-49 25-50 26-50 27-50 28-50 29-50 26-51 27-51 28-51 29-51""",
    "742": """17-40 18-40 19-40 17-41 18-41 19-41 17-42 18-42 19-42 17-43 18-43 19-43 17-44 18-44 19-44 17-45 18-45 19-45""",
    "743": """14-40 15-40 16-40 14-41 15-41 16-41 14-42 15-42 16-42 14-43 15-43 16-43 15-44 16-44 19-46""",
    "744": """13-44 14-44 14-45 15-45 16-45 17-46 18-46 19-47""",
    "745": """4-40 5-40 6-40 7-40 8-40 9-40 10-40 11-40 12-40 13-40 4-41 5-41 6-41 7-41 8-41 9-41 10-41 11-41 12-41 13-41 4-42 5-42 6-42 7-42 8-42 9-42 10-42 11-42 12-42 13-42 7-43 8-43 9-43 10-43 11-43 12-43 13-43 8-44 9-44 10-44 11-44 12-44 8-45 9-45 10-45 11-45 12-45 13-45 9-46 10-46 11-46 12-46 13-46 14-46 11-47 12-47 13-47 14-47 12-48 13-48 14-48 15-48 16-48 17-48 18-48 19-48 14-49 15-49 16-49 17-49""",
    "750": """11-52""",
}

def normalized_pairs(text):
    pairs = set()
    for part in text.split():
        i, j = map(int, part.split("-"))
        assert 0 <= i < j < 192, (i, j)
        pairs.add((i, j))
    return pairs

def expand_to_original_768_fine(pairs):
    # D=[0,1/2]^2; original PREFIX712 fine cell side=1/768.
    # Later R_ij=[i/384,(i+1)/384] x [j/384,(j+1)/384].
    result = set()
    for i,j in pairs:
        for a in (0,1):
            for b in (0,1):
                result.add((2*i+a,2*j+b))
                result.add((2*j+b,2*i+a))
    return result

P = {name: normalized_pairs(t) for name,t in PAIR_STRINGS.items()}
F = {name: expand_to_original_768_fine(pairs) for name,pairs in P.items()}
previous = set().union(*(P[name] for name in ("741","742","743","744","745")))
previous_fine = set().union(*(F[name] for name in ("741","742","743","744","745")))
assert len(P["sibling"]) == 197 and len(F["sibling"]) == 1576
assert len(P["745"]) == 70 and len(F["745"]) == 560
assert len(P["750"]) == 1 and len(F["750"]) == 8
assert not P["sibling"].intersection(previous)
assert not F["sibling"].intersection(previous_fine)
assert F["750"].issubset(F["sibling"])
assert len(F["sibling"] | F["745"]) == 2136
assert Fraction(len(F["sibling"]), 384*384) == Fraction(197,18432)
print("PASS sibling 197 upper /384 boxes = 394 reflected /384 boxes = 1576 original /768 fine boxes")
print("PASS PREFIX745 70 upper /384 boxes = 560 original /768 fine boxes")
print("PASS sibling vs PREFIX741..745 fine-grid intersection = 0")
print("PASS sibling + PREFIX745 = 2136 distinct /768 fine boxes")
print("PASS PREFIX750 contribution beyond sibling = 0 original fine boxes")
print("CHECK NOT PERFORMED: historic PREFIX712-745 full /768-mask union and analytic Gamma proof replay")
