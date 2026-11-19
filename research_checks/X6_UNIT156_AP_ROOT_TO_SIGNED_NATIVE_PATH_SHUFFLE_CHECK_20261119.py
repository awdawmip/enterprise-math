#!/usr/bin/env python3
"""Independent exact A_p root-word vs standard-axis native-word census."""
from functools import lru_cache
from itertools import product
from math import comb, factorial, prod
import json

def require(condition, reason):
    if not condition:
        raise ArithmeticError(reason)

@lru_cache(None)
def a_root_words(positive, negative):
    if not any(positive):
        return 1
    return sum(
        a_root_words(tuple(v-(j==i) for j,v in enumerate(positive)),
                     tuple(v-(j==k) for j,v in enumerate(negative)))
        for i,a in enumerate(positive) if a
        for k,b in enumerate(negative) if b
    )

@lru_cache(None)
def native_words(magnitudes):
    if not any(magnitudes):
        return 1
    return sum(
        native_words(tuple(v-(j==i) for j,v in enumerate(magnitudes)))
        for i,a in enumerate(magnitudes) if a
    )

def census(p, bound=2):
    seen=0
    maximum_m=0
    for x in product(range(-bound,bound+1),repeat=p+1):
        if sum(x)!=0:
            continue
        pos=tuple(v for v in x if v>0)
        neg=tuple(-v for v in x if v<0)
        m=sum(pos)
        require(m==sum(neg), "zero sum positive/negative discrepancy")
        r=a_root_words(pos,neg)
        n=native_words(tuple(abs(v) for v in x))
        den=prod(factorial(v) for v in pos+neg)
        require(r*den==factorial(m)**2, "A_p root multinomial identity")
        require(n*den==factorial(2*m), "signed native multinomial identity")
        require(n==comb(2*m,m)*r, "interleaving lift identity")
        seen+=1
        maximum_m=max(maximum_m,m)
    return {"p":p,"states":seen,"max_m":maximum_m}

def main():
    blocks=[census(p) for p in range(1,5)]
    require([x["states"] for x in blocks]==[5,19,85,381],"census counts")
    return {"schema":"X6_UNIT156_AP_ROOT_NATIVE_SHUFFLE_CENSUS_V1",
            "frozen_source_commit":"fd2bcff10ca6e147348b6c1236027fc0d2877df3",
            "frozen_geometry_blob":"a1a8dc4d1ca53fde2ca00d9b944c1b8aa346a152",
            "frozen_ap_geometry_blob":"825ee26c918a4d7007e280aeaa1d7b750cd46aba",
            "frozen_geometry_test_blob":"e1a8988169f12d4294e29446fb1a8558c412c77b",
            "frozen_ap_test_blob":"304ff8e769f93fa0e96a03c1ffe89960ea5dd622",
            "blocks":blocks,"states_total":sum(x["states"] for x in blocks),
            "witness":{"x":[2,2,-2,-2],"m":4,"root_paths":36,"native_paths":2520,"shuffle_ratio":70},
            "all_checked":True,"original_historical_test_executed":False,
            "original_R063_executed":False}

if __name__=="__main__":
    print(json.dumps(main(),sort_keys=True,separators=(",",":")))
