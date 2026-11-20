"""Stage496-B: exact bit accounting and successor-oracle comparisons.
Extends the mathematical Stage495-B algorithm and independently recomputes each candidate.
Native letters A..L encode +/-E1..+/-E6, with positive unit BRC branch multiplicity.
"""
from collections import Counter
from fractions import Fraction
from math import factorial
import time,json

D='ABCDEFGHIJKL'

def support(m,s,t):
    return sorted({s,t}|{a for (a,b),v in m.items() if v}|{b for (a,b),v in m.items() if v})
def outdeg(m):
    c=Counter()
    for (a,b),v in m.items():
        if v:c[a]+=v
    return c

def reduced_lap(m,verts,t):
    vv=[v for v in verts if v!=t]
    L=[[sum(q for (a,b),q in m.items() if a==u and b!=u) if u==v else -m.get((u,v),0) for v in vv] for u in vv]
    return vv,L

def bareiss(A):
    n=len(A)
    if not n:return 1
    q=[list(row) for row in A];last=1;sgn=1
    for k in range(n-1):
        if q[k][k]==0:
            j=next((j for j in range(k+1,n) if q[j][k]!=0),None)
            if j is None:return 0
            q[j],q[k]=q[k],q[j];sgn=-sgn
        pivot=q[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=q[i][j]*pivot-q[i][k]*q[k][j]
                assert num%last==0
                q[i][j]=num//last
            q[i][k]=0
        last=pivot
    return sgn*q[-1][-1]

def count(m,s,t):
    n=sum(m.values())
    if not n:return int(s==t)
    vv=support(m,s,t);oo=outdeg(m);ii=Counter()
    for (a,b),q in m.items():
        if q:ii[b]+=q
    if any(oo[v]-ii[v]!=(v==s)-(v==t) for v in vv):return 0
    if any(v!=t and oo[v]==0 for v in vv):return 0
    tau=bareiss(reduced_lap(m,vv,t)[1])
    if tau<=0:return 0
    num=tau*factorial(oo[t]);den=1
    for v in vv:
        if v!=t:num*=factorial(oo[v]-1)
    for q in m.values():den*=factorial(q)
    assert num%den==0
    return num//den

def solve(A,b):
    n=len(A);q=[[Fraction(x) for x in row]+[Fraction(bi)] for row,bi in zip(A,b)]
    for k in range(n):
        z=next((j for j in range(k,n) if q[j][k]),None)
        assert z is not None
        q[z],q[k]=q[k],q[z]
        p=q[k][k];q[k]=[v/p for v in q[k]]
        for i in range(n):
            if i!=k:
                p=q[i][k]
                if p:q[i]=[a-p*b for a,b in zip(q[i],q[k])]
    return [row[-1] for row in q]

def remove(m,a,b):
    n=m.copy();assert n[(a,b)]>0;n[(a,b)]-=1
    if not n[(a,b)]:del n[(a,b)]
    return n

def fast_blocks(m,s,t):
    N=count(m,s,t)
    if not N:return {}
    vv=support(m,s,t);oo=outdeg(m);idx,L=reduced_lap(m,vv,t)
    tau=bareiss(L);pos={a:j for j,a in enumerate(idx)}
    y=solve(L,[int(v==s) for v in idx]) if s!=t else []
    ys=y[pos[s]] if s!=t else Fraction(0)
    ans={}
    for b in sorted({b for (a,b),q in m.items() if a==s and q}):
        nxt=remove(m,s,b)
        if support(nxt,b,t)!=vv:
            v=count(nxt,b,t)
        else:
            tau2=Fraction(tau)
            if s!=t and b!=s:
                tau2=tau*(1-ys+(y[pos[b]] if b!=t else 0))
            assert tau2.denominator==1
            den=oo[s] if s==t else oo[s]-1
            assert den>0
            r=Fraction(N*m[(s,b)]*int(tau2),den*tau)
            assert r.denominator==1
            v=int(r)
        if v:ans[b]=v
    assert sum(ans.values())==N
    return ans

def slow_blocks(m,s,t):
    return {b:v for b in sorted({b for (a,b),q in m.items() if a==s and q}) if (v:=count(remove(m,s,b),b,t))}

def full_example():
    # Heterogeneous balanced inventory: 144 positive directed types,
    # extra 120 copies of one loop, 37 of another, 13 of a third,
    # and an asymmetric-in-label but balanced 22+22 two-cycle.
    m=Counter({(a,b):1 for a in D for b in D})
    m['A','A']+=120;m['B','B']+=37;m['C','C']+=13
    m['A','D']+=22;m['D','A']+=22
    return m

def main():
    t0=time.perf_counter();m=full_example();n=sum(m.values());s=t='A';N=count(m,s,t)
    vv,L=reduced_lap(m,support(m,s,t),t);tau=bareiss(L)
    assert N>0 and sum(m.values())==358
    # theoretical bounds: tau <= product of nonroot outgoing degrees;
    # N <= 12^n; stronger edge-multiset permutations also available.
    from math import prod
    tau_upper=prod(outdeg(m)[v] for v in vv)
    assert 0<tau<=tau_upper and 0<N<=12**n
    measured=[];cur=m.copy();rank=N//2;history=s
    # Rank-guided valid prefix: compare all exact successor blocks by independent recount.
    for j in range(18):
        a=time.perf_counter();fb=fast_blocks(cur,s,t);fast=time.perf_counter()-a
        a=time.perf_counter();sb=slow_blocks(cur,s,t);slow=time.perf_counter()-a
        assert fb==sb
        measured.append({'step':j,'s':s,'positive_out':len(fb),'fast_ms':round(fast*1000,4),'slow_ms':round(slow*1000,4)})
        for b,v in fb.items():
            if rank<v:break
            rank-=v
        else:raise AssertionError('bad rank')
        cur=remove(cur,s,b);s=b;history+=b
    assert len(history)==19
    # Random-prefix state remained viable, so it can be ranked by original value-word oracle.
    assert count(cur,s,t)>0
    population_digits=len(str(N))
    serialized_rank=(N//2).to_bytes((N.bit_length()+7)//8,'big')
    assert int.from_bytes(serialized_rank,'big')==N//2
    # Consumed distinct type multiplicities, input bit accounting in canonical fixed-type order.
    input_bits=sum((m.get((a,b),0)).bit_length() for a in D for b in D)
    t1=time.perf_counter()
    record={
      'stage':'496-B','signed_native_X6_directions':12,'active_edge_types':len(m),
      'total_edges':n,'max_multiplicity':max(m.values()),'population_decimal_digits':population_digits,
      'population_bits':N.bit_length(),'rank_payload_bytes':len(serialized_rank),
      'raw_multiplicity_bits_no_delimiters':input_bits,'L_reduced_dimension':len(L),
      'tree_det_bits':tau.bit_length(),'tree_upper_bound_bits':tau_upper.bit_length(),
      'theorem_det_bound':True,'theorem_population_bound':True,
      'head_to_head_layers':len(measured),'fast_total_ms':round(sum(v['fast_ms'] for v in measured),3),
      'slow_total_ms':round(sum(v['slow_ms'] for v in measured),3),
      'timing_detail':measured,'elapsed_s':round(t1-t0,3),'assertions':'PASSED'}
    print(json.dumps(record,ensure_ascii=False,sort_keys=True))

if __name__=='__main__':main()
