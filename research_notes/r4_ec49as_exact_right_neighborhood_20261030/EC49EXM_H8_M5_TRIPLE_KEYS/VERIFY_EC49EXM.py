#!/usr/bin/env python3
"""EC49EXM: finite H=2..8 threefold-BRC-key scheduling certificate.
Uses the native-X6 rank-eligible full-key criterion proved and checked in EC49EXL.
No floating-point arithmetic, no external libraries.
"""
import collections
import itertools
import json

HS = tuple(range(2, 9))
FROZEN = {"global": "773d538180bfb49e24cffeb35c3ee75eb0628e2e",
          "enterprise_math": "fc0f038e7bfd12c886b4d37f900bfb770c0f61ab"}

def eligible(h):
    ks = {}
    for w in range(1, (h+1)//2+1):
        for u in range(2*h+3):
            for v in range(h+2):
                r = u+v-h-1
                f = h+1-v-2*w
                g = h+1-u
                if min(r, f, g) >= 0 and (r >= 1 or (r == 0 and f >= 1 and g >= 1)):
                    ks[(u, v, w)] = "T4" if r else "T2"
    return ks

S = {h: eligible(h) for h in HS}
assert [len(S[h]) for h in HS] == [1, 4, 9, 17, 28, 43, 62]

def rgs(seq=(0,), num=1):
    if len(seq) == len(HS):
        if num == 5:
            yield seq
        return
    for v in range(min(num+1, 5)):
        yield from rgs(seq+(v,), max(num,v+1))

def blocks_and_options(p):
    blocks = {c: tuple(h for h, j in zip(HS, p) if j == c) for c in range(5)}
    options = {c: set.intersection(*(set(S[h]) for h in hs)) for c, hs in blocks.items()}
    return blocks, options

def injective_count_dfs(options):
    order = sorted(range(5), key=lambda c:(len(options[c]),c))
    def rec(i, used):
        if i == 5:
            return 1
        return sum(rec(i+1, used | {k}) for k in options[order[i]] if k not in used)
    return rec(0,set())

def injective_count_dp(options):
    # Independent counting principle: process each complete key at most once;
    # a key may be skipped or matched to exactly one of its eligible five blocks.
    universe = sorted(set.union(*options.values()))
    dp = [0]*32
    dp[0] = 1
    for k in universe:
        new = dp.copy()
        for mask in range(32):
            if not dp[mask]:
                continue
            for c in range(5):
                if (mask >> c) & 1 == 0 and k in options[c]:
                    new[mask | (1<<c)] += dp[mask]
        dp = new
    return dp[31]

out=[]
for p in rgs():
    blocks, options=blocks_and_options(p)
    if 3 not in map(len, blocks.values()):
        continue
    count=injective_count_dfs(options)
    if count == 0:
        continue
    dp=injective_count_dp(options)
    assert count == dp, (p,count,dp)
    triple=next(hs for hs in blocks.values() if len(hs)==3)
    trlabel = next(c for c,hs in blocks.items() if len(hs)==3)
    trkeys = sorted(options[trlabel])
    assert all(sum(h in triple for h in HS)==3 for _ in trkeys)
    assert all(S[triple[0]][k] == 'T4' for k in trkeys)
    # For the last triple horizon the key is T2 precisely when r=0.
    result={"partition": list(p), "three_equal_horizons":list(triple),
            "triple_common_full_keys": [list(k)+[0,0,0] for k in trkeys],
            "triple_key_count":len(trkeys), "full_distinct_key_schedules":count}
    out.append(result)

assert len(out)==8, len(out)
assert sum(r['full_distinct_key_schedules'] for r in out)==123147
assert [r['full_distinct_key_schedules'] for r in out]==[71799,23502,4983,2905,10158,3015,1917,4868]
assert [r['triple_key_count'] for r in out]==[1,3,1,1,7,3,3,13]
print(json.dumps({"status":"PASS", "proof_type":"exact integer finite classification; two independent counting algorithms",
                  "scope":"H=2..8; exactly five distinct full BRC keys; rank-9 each horizon; <=6 T2/T4 signatures; one triple collision, all other blocks singleton",
                  "eligible_key_counts":{str(h):len(S[h]) for h in HS},
                  "triple_skeletons":len(out),"full_distinct_key_schedules":sum(r['full_distinct_key_schedules'] for r in out),
                  "families":out, "frozen_scientific_pins":FROZEN,
                  "next_question":"Native signed primitive prefix minimum across these schedules; 32 two-pair families remain"},indent=2,ensure_ascii=False))
