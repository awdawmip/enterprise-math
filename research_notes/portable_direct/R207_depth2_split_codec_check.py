#!/usr/bin/env python3
"""R207 exact depth-two source-fibre split codec; pure Python, deterministic."""
import itertools
import json
import math
from hashlib import sha256

def N(k):
    return sum(math.perm(k, r) for r in range(k + 1))

def source_rank(source, k):
    r = len(source)
    if r > k or len(set(source)) != r or any(x < 0 or x >= k for x in source):
        raise ValueError("invalid source order")
    result = sum(math.perm(k, j) for j in range(r))
    available = list(range(k))
    for j, x in enumerate(source):
        idx = available.index(x)
        result += idx * math.perm(k - j - 1, r - j - 1)
        del available[idx]
    return result

def source_unrank(code, k):
    if not (0 <= code < N(k)):
        raise ValueError("source rank outside range")
    r = 0
    while code >= math.perm(k, r):
        code -= math.perm(k, r)
        r += 1
    available = list(range(k))
    result = []
    for j in range(r):
        stride = math.perm(k - j - 1, r - j - 1)
        idx, code = divmod(code, stride)
        result.append(available.pop(idx))
    return tuple(result)

def patterns(source):
    r = len(source)
    if r == 0:
        return ((-1, -1),)
    last = source[-1]
    if r == 1:
        return ((-1, -1), (-1, last), (last, -1), (last, last))
    prev = source[-2]
    return ((-1, -1), (-1, last), (last, -1), (last, last), (prev, last))

def fibre_size(r, m):
    return (1 + m + m * m) if r == 0 else (m + 4 * m * m if r == 1 else 5 * m * m)

def fibre_unrank(rank, source, m):
    r = len(source)
    if not (0 <= rank < fibre_size(r, m)):
        raise ValueError("fibre rank outside range")
    if r == 0:
        if rank == 0:
            return ()
        rank -= 1
        if rank < m:
            return ((rank, -1),)
        rank -= m
    elif r == 1:
        if rank < m:
            return ((rank, source[0]),)
        rank -= m
    tag, rem = divmod(rank, m * m)
    d0, d1 = divmod(rem, m)
    p0, p1 = patterns(source)[tag]
    return ((d0, p0), (d1, p1))

def fibre_rank(tail, source, m):
    r = len(source)
    length = len(tail)
    if length == 0 and r == 0:
        return 0
    if length == 1:
        (d, label), = tail
        if not (0 <= d < m):
            raise ValueError("direction")
        if r == 0 and label == -1:
            return 1 + d
        if r == 1 and label == source[0]:
            return d
        raise ValueError("invalid short tail")
    if length != 2:
        raise ValueError("bad depth-two tail")
    (d0, p0), (d1, p1) = tail
    if not (0 <= d0 < m and 0 <= d1 < m):
        raise ValueError("direction")
    try:
        tag = patterns(source).index((p0, p1))
    except ValueError as exc:
        raise ValueError("invalid provenance tail") from exc
    offset = (1 + m if r == 0 else m if r == 1 else 0)
    return offset + tag * m * m + d0 * m + d1

def ceil_log2(n):
    return (n - 1).bit_length()

def params(k, m):
    F = [fibre_size(r, m) for r in range(k+1)]
    total = sum(math.perm(k, r) * F[r] for r in range(k+1))
    closed = 1 + (k + 1) * m + (5 * N(k) - k - 4) * m * m
    assert total == closed
    bs, bf = ceil_log2(N(k)), ceil_log2(max(F))
    return dict(k=k,m=m,source_states=N(k),fibre_sizes=F,states=total,formula=closed,source_bits=bs,fibre_bits=bf,split_bits=bs+bf,optimal_bits=ceil_log2(total))

def encode(source,tail,k,m):
    b = params(k,m)["fibre_bits"]
    return (source_rank(source,k) << b) | fibre_rank(tail,source,m)

def decode(code,k,m):
    b = params(k,m)["fibre_bits"]
    s = source_unrank(code >> b,k)
    return (s,fibre_unrank(code & ((1<<b)-1),s,m))

def order_prod(s,t):
    tset=set(t)
    return tuple(x for x in s if x not in tset) + tuple(t)

def product(a,b):
    s,t=a; s2,t2=b
    return order_prod(s,s2),(t + t2)[-2:]

def observe(history):
    src=()
    for d,p in history:
        if p>=0:
            src=order_prod(src,(p,))
    return (src,tuple(history[-2:]))

def witness(source,tail):
    seen={p for _,p in tail if p>=0}
    prefix=tuple((0,p) for p in source if p not in seen)
    return prefix+tail

def check_model(k,m,full=False):
    p=params(k,m)
    all_sources=[s for r in range(k+1) for s in itertools.permutations(range(k),r)]
    assert len(all_sources)==p["source_states"]
    sranks=set(source_rank(s,k) for s in all_sources)
    assert sranks == set(range(p["source_states"]))
    for i in range(p["source_states"]):
        assert source_rank(source_unrank(i,k),k)==i
    check_count=0
    code_count=0
    dig=sha256()
    for s in all_sources:
        idx=source_rank(s,k)
        assert source_unrank(idx,k)==s
        for f in range(fibre_size(len(s),m)):
            t=fibre_unrank(f,s,m)
            assert fibre_rank(t,s,m)==f
            code=(idx<<p["fibre_bits"])|f
            idx2, f2=divmod(code,1<<p["fibre_bits"])
            assert idx2==idx and f2==f
            if full or (f % max(1,m*m//4) == 0):
                assert observe(witness(s,t))==(s,t)
                check_count+=1
            dig.update(code.to_bytes((p["split_bits"]+7)//8 or 1,"big"))
            code_count+=1
    assert code_count==p["states"]
    p["exhaustive_codec_checks"]=code_count
    p["history_witness_checks"]=check_count
    p["ordered_code_digest_sha256"]=dig.hexdigest()
    pool=[]
    for s in all_sources:
        for f in range(fibre_size(len(s),m)):
            if p["states"]<=5000 or ((source_rank(s,k)*7369+f*131)%997==0):
                pool.append((s,fibre_unrank(f,s,m)))
    checks=0
    for j,a in enumerate(pool):
        b=pool[(j*31+7)%len(pool)]
        expected=observe(witness(*a)+witness(*b))
        direct=product(a,b)
        assert direct==expected,(a,b,direct,expected)
        code=encode(*direct,k,m)
        assert decode(code,k,m)==direct
        checks+=1
    p["composition_checks"]=checks
    return p

def main():
    models=[]
    for k in range(5):
        for m in range(1,5):
            models.append(check_model(k,m))
    x6=check_model(6,12,full=True)
    total_check=sum(x["exhaustive_codec_checks"] for x in models)+x6["exhaustive_codec_checks"]
    result={
        "status":"PASS",
        "scientific_input_pin":"awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34",
        "model":"R200 independent paired direction/source observer, L=2",
        "finite_field_claim":"none; bijective combinatorial state code",
        "finite_models_checked":len(models),
        "total_exhaustive_codec_checks":total_check,
        "total_composition_checks":sum(x["composition_checks"] for x in models)+x6["composition_checks"],
        "x6":x6,
        "small_models":models,
        "scope":"Exhaustive rank/unrank of every valid joint state for listed finite models. History representatives all tested in X6; product checked on finite deterministic pair subsets, mathematically proved by quotient law. Bit count exact, time complexity analysis symbolic; no runtime speed claim."
    }
    with open("R207_verification.json","w") as f:
        json.dump(result,f,indent=2,ensure_ascii=False,sort_keys=True)
        f.write("\n")
    print(json.dumps({k:v for k,v in result.items() if k!="small_models"},ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
