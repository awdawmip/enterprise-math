"""Exact finite checks for reconstruction from all unoriented circular windows."""
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb
from pathlib import Path
import argparse
import importlib.util
import json


def windows(w, length):
    full = w*((len(w)+length-1)//len(w)+1)
    return [full[i:i+length] for i in range(len(w))]


def canon(w):
    return min(windows(w,len(w))+windows(w[::-1],len(w)))


def deck(w, length, reverse=True):
    reads = windows(w,length)
    return tuple(sorted(min(s,s[::-1]) if reverse else s for s in reads))


def bracelets(k):
    reps = Counter()
    for i in range(2**k):
        reps[canon(format(i, f"0{k}b"))] += 1
    unresolved = set(reps)
    labelled, half, uniform = Counter(),Counter(),Counter()
    two_cases = 0
    for t in range(1,k//2+1):
        bags = defaultdict(list)
        for w in reps:
            if w not in unresolved:
                continue
            bags[deck(w,2*t-1)].append(w)
        # For odd lengths the central subwindow reads give the previous deck.
        for bucket in bags.values():
            if len(bucket)==1:
                w = bucket[0]
                unresolved.remove(w)
                uniform[t] += 1
                labelled[t] += reps[w]
                if w.count("1")==k//2:
                    half[t] += reps[w]
        if t > 1:
            for w in reps:
                h = 2*t-2
                if len(set(deck(w,h)))==k:
                    two_cases += 1
                    assert w not in unresolved
    assert not unresolved and sum(labelled.values())==2**k
    assert sum(half.values())==comb(k,k//2)
    return {"k":k,"bracelets":len(reps),"round_placement_counts":dict(labelled),
            "round_half_weight_counts":dict(half),"round_bracelet_counts":dict(uniform),
            "distinct_unoriented_overlap_sufficiency_checks":two_cases}


def moment(h,n):
    length = h+n-1
    all_counts = [Counter(w[i:i+h] for i in range(n))
                  for bits in product("01",repeat=length) for w in ["".join(bits)]]
    histogram = Counter()
    for left in all_counts:
        for right in all_counts:
            histogram[sum(c*right[w] for w,c in left.items())] += 1
    total = 2**(2*length)
    mu = Fraction(n*n,2**h)
    assert sum(k*v for k,v in histogram.items()) == mu*total
    var = sum((k-mu)**2*v for k,v in histogram.items())/total
    formula = n*n*(Fraction(1,2**h)-Fraction(1,2**(2*h)))
    for d in range(1,min(n,h)):
        formula += 2*(n-d)**2*(Fraction(1,2**(h+d))-Fraction(1,2**(2*h)))
    assert var == formula and var <= 3*mu
    return [h,n,str(mu),str(var),histogram[0],total]


def swap_example(equal_nodes):
    for i in range(500):
        s = list(format(int.from_bytes(sha256(str(i).encode()).digest()[:4],"big"),"032b"))
        if equal_nodes:
            s[8:12] = s[:4]
        s[16:20],s[24:28] = s[:4],s[8:12]
        w = "".join(s)
        if (w[:4]==w[8:12]) != equal_nodes:
            continue
        arcs = [w[i:i+8] for i in (0,8,16,24)]
        v = "".join(arcs[j] for j in (0,3,2,1))
        assert deck(w,5,False)==deck(v,5,False)
        if canon(w)!=canon(v):
            return {"input":w,"alternative":v,"starts":[0,8,16,24],
                    "junction_words":[w[:4],w[8:12]],"length":5}
    raise AssertionError("no witness")


def overlap_counts():
    rows=[]
    for h in range(1,8):
        for d in range(h+1):
            # All comparisons are within this single interval of length h+d.
            equal=reverse=0
            for bits in product((0,1),repeat=h+d):
                a,b=bits[:h],bits[d:]
                equal += a==b
                reverse += a==b[::-1]
            assert reverse==2**(h+d-(h+d)//2)
            assert equal==2**d if d else equal==2**h
            rows.append([h,d,equal,reverse])
    return {"verified_pairs":len(rows),"table_sha256":sha256(json.dumps(rows).encode()).hexdigest()}


def native_rounds(word, module, tmax):
    k = len(word)
    edges = [(i,(i+1)%k) for i in range(k)]
    n=k
    for i,bit in enumerate(word):
        if bit=="1":
            edges.extend([(i,n),(n,n+1),(n+1,n+2),(n+2,n)])
            n+=3
    adj=module.adj_from_edges(n,edges)
    profiles,_,(legend,layers,colors),_ = module.stable_packet(adj)
    assert all(sum(row)==1 and row[(k if i<k else 3)-3]==1
               for i,row in enumerate(profiles))
    counts=Counter(colors)
    ans={}
    for t in range(len(layers),-1,-1):
        if t<=tmax:
            ans[t]=(legend,layers[:t],tuple(sorted(counts.items())))
        if t:
            parent=Counter()
            for color,value in counts.items():
                parent[layers[t-1][color][0]]+=value
            counts=parent
    return ans


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",type=Path,help="optionally also replay the pinned Q22 graph kernel")
    opt=ap.parse_args()
    twins=[swap_example(False),swap_example(True)]
    for pair in twins:
        u,v=pair["input"],pair["alternative"]
        t=next(t for t in range(1,len(u)//2+1) if deck(u,2*t-1)!=deck(v,2*t-1))
        pair["first_different_round"]=t
    if opt.source:
        assert sha256(opt.source.read_bytes()).hexdigest()=="e0c6ce8d79fa4e725c89d0f7132c67d01ed48d47933a53c8f1aea45c3213fb14"
        spec=importlib.util.spec_from_file_location("q22_random",opt.source)
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for pair in twins:
            t=pair["first_different_round"]
            a,b=(native_rounds(pair[key],module,t) for key in ("input","alternative"))
            assert all(a[i]==b[i] for i in range(t)) and a[t]!=b[t]
    records=[bracelets(k) for k in range(4,16)]
    moments=[moment(h,n) for h in range(1,5) for n in range(1,5)]
    print(json.dumps({"model":"indexed circular binary words; includes constant words in finite checks",
                      "bracelets":records,"two_region_variances_h_n_mean_var_no_match_total":moments,
                      "overlap":overlap_counts(),
                      "directed_deck_twins":twins},
                     ensure_ascii=False,sort_keys=True,indent=2))


if __name__=="__main__":
    main()
