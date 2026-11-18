#!/usr/bin/env python3
"""Exact 2-port rank-one WBRC grid realizability, constructive certificate."""
from fractions import Fraction as F
from itertools import product
import json


def lows(K,M):
    return [F(0)]+[F(K,M-h+1) for h in range(1,M+1)]


def diag_intervals(K,M):
    l=lows(K,M)
    return [(F(1) if h==0 else l[h],F(K,M-h) if h<M else None) for h in range(M+1)]


def feasible(K,M,ha,hd,hb,hc):
    ua=diag_intervals(K,M)[ha][1]
    ud=diag_intervals(K,M)[hd][1]
    if ua is None or ud is None: return True
    off=lows(K,M)
    return off[hb]*off[hc] < ua*ud-max(ua,ud)


def witness(K,M,ha,hd,hb,hc):
    assert feasible(K,M,ha,hd,hb,hc)
    dia=diag_intervals(K,M)
    la,ua=dia[ha]; ld,ud=dia[hd]
    lo=lows(K,M)
    b,c=lo[hb],lo[hc]
    if ua is not None and ud is not None:
        gap=ua*ud-max(ua,ud)-b*c
        assert gap>0
        eps=min((ua-la)/2,(ud-ld)/2,gap/(2*(ua+ud+1)))
        a,d=ua-eps,ud-eps
    else:
        a=la if ua is None else (la+ua)/2
        d=ld if ud is None else (ld+ud)/2
        if ua is None: a=max(a,F(K),d+1)
        if ud is None: d=max(d,F(K),a+1)
        while a*d-max(a,d)<=b*c:
            if ua is None: a+=1
            else: d+=1
    delta=a*d-b*c
    assert delta>max(a,d)
    W=(1-d/delta,b/delta,c/delta,1-a/delta)
    assert min(W)>=0
    return (a,b,c,d),W


def bin_of(s,K,M):
    return sum(j*s>=K for j in range(1,M+1))


def main():
    samples={}
    for K,M in [(2,1),(3,2),(4,3),(5,4),(5,2),(7,3)]:
        arr=range(M+1)
        total=0
        table=[]
        witnesses=0
        excluded=0
        for ha in arr:
            row=[]
            for hd in arr:
                n=0
                for hb,hc in product(arr,repeat=2):
                    if feasible(K,M,ha,hd,hb,hc):
                        S,W=witness(K,M,ha,hd,hb,hc)
                        a,b,c,d=S
                        assert tuple(bin_of(s,K,M) for s in (a,d,b,c))==(ha,hd,hb,hc)
                        p,q,r,t=W
                        assert p<1 and t<1 and (1-p)*(1-t)-q*r>0
                        n+=1
                        witnesses+=1
                    else: excluded+=1
                row.append(n);total+=n
            table.append(row)
        assert witnesses+excluded==(M+1)**4
        samples[f'K{K}_M{M}']={"classes":total,"excluded":excluded,"bit_cost":(total-1).bit_length(),"table_diagonal_bins":table,"realized_witnesses":witnesses}
    assert samples['K4_M3']['classes']==190
    out={"status":"PASS","scope":"Exact rational 2-port W>=0,rho(W)<1 under all ordered rank-one grid guards","formula":"sum_{i,j=0}^M count_{a,b=0}^M [L_a L_b < U_i U_j - max(U_i,U_j)], U_M=infinity; infinite diagonal upper counts all","finite_grid_examples":samples,"exact_4_3_classes":190,"exact_4_3_impossible":66,"optimal_fixed_width_bits_4_3":8}
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
    return out
if __name__=='__main__':main()
