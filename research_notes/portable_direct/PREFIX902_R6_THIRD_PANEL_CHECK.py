#!/usr/bin/env python3
"""PREFIX-902 third-panel exact census (Python stdlib).
Build the byte-pinned PREFIX900_R6_64ROW_FF_COMPLETE.cpp with:
  g++ -O3 -std=c++17 PREFIX900_R6_64ROW_FF_COMPLETE.cpp -o prefix900
Run: python3 PREFIX902_R6_THIRD_PANEL_CHECK.py ./prefix900 > recomputed.json
Exact input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d
Original C++ Git blob: 175aabe087718cc48ecc8e2f7492cef6731fc5ca
"""
import json, math, subprocess, sys

N = 2**32
T = 33*N
Q = range(262145, 524288, 2)
S = {262147, 280001, 300001, 320003, 340007, 360007,
     380003, 400009, 420001, 440003, 460001, 480007,
     500383, 510007, 520001, 524285}
U = S | set(range(400011,400522,2)) | set(range(480011,480522,2))
U |= {q for q in Q if any(((1<<h)-1)%q==0 or ((1<<h)+1)%q==0
                         for h in range(1,32))}
assert len(U) == 552
P0 = [510001+194*j for j in range(64)]
P1 = [510003+194*j for j in range(64)]
P2 = [510005+194*j for j in range(64)]
A = P0+P1
P = A+P2
assert len(set(P))==len(P)==192 and not (set(P)&U)

def old(a,b):
    return (a*b<T or a in U or b in U or
            (a//math.gcd(a,b))*b<N or
            33*((N+a-1)//a)>b or 33*((N+b-1)//b)>a)

def check_witness(a,b,w):
    x,y,i,j=(w[t] for t in ('x','y','i','j'))
    assert 0<=x<N and 0<=y<N and 0<=i<32 and 0<=j<32
    assert (x,i)!=(y,j)
    assert x%a==y%a and (x^(1<<i))%b==(y^(1<<j))%b

def run(exe):
    rows=[]
    names=('old_four_family','zf_new','anchored_ff_new',
           'general_ff_new','unresolved')
    for a in P2:
        r=json.loads(subprocess.check_output([exe,str(a)], text=True))
        assert r['q1']==a and r['q_count']==131072
        assert sum(r[n] for n in names)==131072
        assert r['unresolved']==0
        assert r['old_four_family']==sum(old(a,b) for b in Q)
        assert len(r['general_witnesses'])==r['general_ff_new']
        for w in r['general_witnesses']+r['anchored_examples']:
            check_witness(a,w['q2'],w)
        rows.append(r)
    totals={name:sum(r[name] for r in rows) for name in names}
    assert list(totals.values())==[505972,3482710,4399503,423,0]
    ea=sum(old(a,b) for a in A for b in A)
    eba=sum(old(a,b) for a in P2 for b in A)
    eb=sum(old(a,b) for a in P2 for b in P2)
    assert (ea,eba,eb)==(182,59,64)
    delta=2*(64*len(Q)-totals[names[0]]-(64*128-eba))-(64*64-eb)
    final=7599130064+delta
    assert delta==15744974 and final==7614875038
    assert final==7567620214+2*(192*len(Q)-507393-506797-totals[names[0]])-(192**2-(ea+2*eba+eb))
    return {'schema':'PREFIX902_R6_THIRD_PANEL_RECOMPUTED_V1',
            'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
            'counts':totals,
            'old_E_in_old_128_square':ea,
            'old_E_in_new_to_old_64x128':eba,
            'old_E_in_new_64_square':eb,
            'old_E_in_192_square':ea+2*eba+eb,
            'net_new_distinct_ordered_pairs':delta,
            'certified_union':final,
            'remaining_outside_this_union':len(Q)**2-final,
            'rows':[[r['q1']]+[r[n] for n in names] for r in rows]}

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('usage: script compiled_prefix900_executable')
    print(json.dumps(run(sys.argv[1]),indent=2))
