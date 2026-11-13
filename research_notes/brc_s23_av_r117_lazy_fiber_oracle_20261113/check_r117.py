"""R117: exact feasibility oracle for unseen fractional-threshold time."""
from fractions import Fraction as Q
from random import Random
import json

L0, R0 = Q(0), Q(1)
OFFSET = Q(1,4)

def floor(q): return q.numerator // q.denominator

def m(t, x):
    v = t*x + OFFSET
    v -= floor(v)
    return Q(0) <= v < Q(1,2)

def cuts(t):
    if t == 0: return set()
    l, h = min(OFFSET, t + OFFSET), max(OFFSET, t + OFFSET)
    out = set()
    for phi in (Q(0), Q(1,2)):
        for k in range(floor(l)-2, floor(h)+4):
            x = (k + phi - OFFSET)/t
            if 0 < x < 1: out.add(x)
    return out

def raw_cells(ts):
    p = sorted({L0,R0}.union(*(cuts(t) for t in ts)))
    result = []
    for a,b in zip(p,p[1:]):
        result.append((a,a,True))
        result.append((a,b,False))
    result.append((p[-1],p[-1],True))
    return result

def bits(ts,x): return tuple(int(m(t,x)) for t in ts)

def witness_on_cell(a,b,single,t,new_bit):
    if single:
        return a if m(t,a) == bool(new_bit) else None
    if t == 0:
        return (a+b)/2 if m(t,a) == bool(new_bit) else None
    q0, q1 = t*a+OFFSET, t*b+OFFSET
    l,h=min(q0,q1),max(q0,q1)
    shift = Q(0) if new_bit else Q(1,2)
    L = l - (shift + Q(1,2))
    H = h - shift
    k=floor(L)+1
    if not k < H: return None
    lo=max(l,k+shift)
    hi=min(h,k+shift+Q(1,2))
    assert lo < hi
    q=(lo+hi)/2
    x=(q-OFFSET)/t
    assert a < x < b and m(t,x)==bool(new_bit)
    return x

def oracle(ts,new_t):
    cs=raw_cells(ts)
    found={}
    queries=0
    for a,b,single in cs:
        old_sig=bits(ts,a if single else (a+b)/2)
        for new_bit in (0,1):
            w=witness_on_cell(a,b,single,new_t,new_bit)
            queries+=1
            if w is not None:
                assert 0<=w<=1 and bits(ts,w)==old_sig and int(m(new_t,w))==new_bit
                found.setdefault((old_sig,new_bit),w)
    return found, len(cs),queries

def brute(ts,new_t):
    xs=raw_cells(tuple(ts)+(new_t,))
    return {(bits(ts,a if single else (a+b)/2),int(m(new_t,a if single else (a+b)/2))) for a,b,single in xs},len(xs)

def run():
    rng=Random(1172026)
    test_cases=0
    oracle_calls=0
    checked_witnesses=0
    brute_atoms=0
    old_atoms=0
    worst_witness_bits=0
    for _ in range(150):
        ts=tuple(sorted(rng.sample(range(-5,6),rng.randint(0,5))))
        new_t=rng.choice([t for t in range(-17,18) if t not in ts])
        f,n,q=oracle(ts,new_t)
        exact,na=brute(ts,new_t)
        assert set(f)==exact,(ts,new_t,set(f)^exact)
        for (s,b),w in f.items():
            assert bits(ts,w)==s and int(m(new_t,w))==b
            worst_witness_bits=max(worst_witness_bits,w.numerator.bit_length(),w.denominator.bit_length())
        test_cases+=1;oracle_calls+=q;checked_witnesses+=len(f);brute_atoms+=na;old_atoms+=n
    huge_values=(10**30+39,-(10**30+39),10**80+7,-(10**80+7))
    huge=[]
    for new_t in huge_values:
        f,n,q=oracle((-3,7),new_t)
        assert len(f)==8, (new_t,len(f),f)
        huge.append({"time":str(new_t),"old_raw_atoms":n,"queries":q,"new_signatures":len(f),"max_witness_bits":max(max(w.numerator.bit_length(),w.denominator.bit_length()) for w in f.values())})
        for (s,b),w in f.items():
            assert bits((-3,7),w)==s and int(m(new_t,w))==b
    return {"status":"R117_PASS","random_seed":1172026,"random_cases":test_cases,"oracle_cell_bit_queries":oracle_calls,"random_checked_witnesses":checked_witnesses,"brute_new_atoms_total":brute_atoms,"oracle_old_atoms_total":old_atoms,"max_random_witness_bits":worst_witness_bits,"huge_cases":huge,"fractions":"exact","old_times_provenance":"complete signatures and exact cells","model":"single half-open fractional threshold"}

if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,ensure_ascii=False))
