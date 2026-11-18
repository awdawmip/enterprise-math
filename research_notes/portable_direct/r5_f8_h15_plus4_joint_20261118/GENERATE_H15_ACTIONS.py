#!/usr/bin/env python3
"""Regenerate R5 H15 support masks from frozen SHA256-pinned table."""
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
SHA="50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b"
H=(18,24,82,34,17,0,1,2,3,144,208,255,50,66,4)
U=58182461585441404127941754880
A=(214,215,216,223,296)
def max_support(values,tau):
    by={}
    for i,c in enumerate(values): by[c]=by.get(c,0)|(1<<i)
    supports={sum(m for c,m in by.items() if lo<=c<=lo+tau) for lo in by}
    return tuple(sorted(s for s in supports if not any(t!=s and (t&s)==s for t in supports)))
def main():
    raw=(HERE/"EXACT_R5_ALL_101_BUDGETS.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA
    table=json.loads(raw)["counts_and_cohorts"]
    rows=[f"{len(H)} {len(A)}"]
    for k in A:
        v=[int(table[str(k)]["counts"][h]) for h in H]
        s=max_support(v,U-1)
        rows.append(f"{k} {len(s)} "+" ".join(map(str,s)))
    text="\n".join(rows)+"\n"
    assert text==(HERE/"ACTIONS_H15_PLUS_4.txt").read_text()
    assert hashlib.sha256(text.encode()).hexdigest()=="58c07dc117a8d62da8b0f2e31c4eef9f4b22a3e14ea39bc555898c4521874a8a"
    print("PASS_R5_H15_PLUS4_FIVE_QUERY_MAXIMAL_SUPPORTS")
if __name__=="__main__":main()
