#!/usr/bin/env python3
"""Typed rotation excursions, primitive reductions, directed clocks, and return counts."""
import argparse
from collections import Counter, defaultdict
from hashlib import sha1
from itertools import combinations, product
import json
from math import factorial, gcd, prod
from pathlib import Path
import runpy

ZERO = (0,) * 6
LETTERS = tuple(v for i in range(1,7) for v in (i,-i))
SOURCE = "experiments/x6_rotation_path_dagger_jet_20260909/check_rotation_path_dagger_jet.py"
BLOB = "51a567303d2d6da37c82dda418b82c5d90a1e4a9"


def step(x, v):
    i = abs(v)-1
    return x[:i]+(x[i]+(1 if v>0 else -1),)+x[i+1:]


def end(x, word):
    for v in word:
        x = step(x,v)
    return x


def reverse(word):
    return tuple(-v for v in reversed(word))


def unit(x):
    return sum(map(abs,x))==1


def pieces(start,word,belongs):
    begin = cur = start
    at = 0
    out = []
    for j,v in enumerate(word,1):
        cur = step(cur,v)
        if belongs(cur):
            out.append((begin,word[at:j],cur))
            begin,at = cur,j
    assert at==len(word)
    return out


def invert(p):
    x,w,y = p
    return y,reverse(w),x


def reduced(seq,inv):
    out = []
    for s in seq:
        if out and out[-1]==inv(s):
            out.pop()
        else:
            out.append(s)
    return tuple(out)


def normal(x,w,lease):
    if lease=="primitive":
        return reduced(w,lambda v:-v)
    return reduced(pieces(x,w,unit if lease=="unit" else lambda z:z==ZERO),invert)


def compare_source(repo):
    filename = repo/SOURCE
    data = filename.read_bytes()
    oid = sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    assert oid==BLOB
    origin = runpy.run_path(str(filename))
    count = 0
    for r in range(6):
        a,b = origin["ORBIT"][r],origin["ORBIT"][(r+1)%6]
        for outer in (False,True):
            lifted = tuple((axis+1)*sign for vec in origin["edge_steps"](a,b,outer)
                           for axis,sign in [origin["step_letter"](vec)])
            x,y = tuple(a)+(0,)*3,tuple(b)+(0,)*3
            assert end(x,lifted)==y and len(pieces(x,lifted,unit))==1
            assert reverse(lifted)==tuple((axis+1)*sign for vec in
                  origin["reverse_steps"](origin["edge_steps"](a,b,outer))
                  for axis,sign in [origin["step_letter"](vec)])
            count+=1
    return {"blob":oid,"signed_lifts_checked":count}


def typed_tests():
    x = step(ZERO,1)
    counts = {}
    for size in (0,2,4):
        legal = 0
        for w in product(LETTERS,repeat=size):
            y = end(x,w)
            if not unit(y):
                continue
            p = normal(x,w,"unit")
            assert normal(y,reverse(w),"unit")==tuple(invert(e) for e in reversed(p))
            assert not normal(x,w+reverse(w),"unit")
            # Insert a whole, self-reverse rotation arrow and its reverse at the tip.
            tip = (6,-6)
            assert normal(x,w+tip+reverse(tip),"unit")==p
            legal+=1
        counts[str(size)] = legal
    spike = (1,-1)
    assert normal(ZERO,spike,"origin") and not normal(ZERO,spike,"primitive")
    assert not normal(ZERO,spike*2,"origin")
    assert len({normal(ZERO,(v,-v),"origin") for v in LETTERS})==12
    inner,outer = (-1,-2),(-2,-1)
    square = inner+reverse(outer)
    for k in range(1,20):
        assert len(normal(x,square*k,"unit"))==2*k
        assert len(normal(x,square*k,"primitive"))==4*k
    return {"legal_paths_from_e1_by_grade":counts,"single_spike_order":2,
            "shortest_positive_rot_grade":2,"inner_reverse_outer_square":square,
            "tested_square_powers":19}


def clocks():
    # These are actual two-step arrows from 0 to 0 or e_i to -e_j, j != i.
    probes = [(ZERO,(i,-i)) for i in range(1,7)]
    probes += [(step(ZERO,i),(-i,-j)) for i,j in combinations(range(1,7),2)]
    for x,w in probes:
        y=end(x,w)
        assert x==y or unit(x) and unit(y)
    out = {}
    for m in range(2,9):
        accepted = 0
        for ss in product(range(m),repeat=6):
            # The full signed weight of w w^dagger groups by axis into the defects ss.
            observed = all(sum(ss[abs(v)-1] for v in w)%m==0 for _,w in probes)
            predicted = len(set(ss))==1 and 2*ss[0]%m==0
            assert observed==predicted
            accepted+=observed
        assert accepted==gcd(m,2)
        out[str(m)] = {"defect_tuples_checked":m**6,"admissible_defects":accepted,
                       "rotation_weightings":accepted*m**6,"primitive_weightings":m**6}
    return out


def compositions(n,k):
    if k==1:
        yield (n,)
        return
    for i in range(n+1):
        for z in compositions(n-i,k-1):
            yield (i,)+z


def return_counts(bound):
    total = [0]*(2*bound+1)
    for k in range(bound+1):
        total[2*k]=sum(factorial(2*k)//prod(factorial(i)**2 for i in ns)
                       for ns in compositions(k,6))
    first = [0]*len(total)
    survival = [1]
    for n in range(1,len(total)):
        first[n]=total[n]-sum(first[j]*total[n-j] for j in range(1,n))
        survival.append(12*survival[-1]-first[n])
    counts = {}
    for k in range(1,bound+1):
        nonpal = first[2*k]-survival[k]
        assert nonpal>=0 and nonpal%2==0
        counts[str(2*k)] = {"all_returns":total[2*k],"first_returns":first[2*k],
                              "order_two_letters":survival[k],"inverse_pairs":nonpal//2}
        if k<=3:
            # Independently list both halves sharing a midpoint with no internal visit to 0.
            halves=defaultdict(list)
            for p in product(LETTERS,repeat=k):
                x=ZERO
                for v in p:
                    x=step(x,v)
                    if x==ZERO:
                        break
                else:
                    halves[x].append(p)
            words = {p+reverse(q) for group in halves.values() for p in group for q in group}
            assert len(words)==first[2*k]
            assert sum(w==reverse(w) for w in words)==survival[k]
            assert all(reverse(w) in words for w in words)
    return counts


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--repo",type=Path,required=True,help="checkout containing the frozen checker")
    p.add_argument("--json",type=Path)
    args=p.parse_args()
    evidence={"frozen":compare_source(args.repo),"rotation_paths":typed_tests(),
              "directed_clock":clocks(),"origin_by_grade":return_counts(8)}
    s=json.dumps(evidence,ensure_ascii=False,indent=2)+"\n"
    if args.json:
        args.json.write_text(s)
    else:
        print(s,end="")


if __name__=="__main__":
    main()
