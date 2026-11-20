#!/usr/bin/env python3
"""Stage446-B exact one-APPEND asymmetric two-source X6 equivalence, stdlib only."""
from collections import defaultdict
from itertools import combinations
import json

D = tuple((axis, sign) for axis in range(6) for sign in (1,-1))
A, B = (0,1), (0,-1)

def words(length, defects):
    for pos in combinations(range(1,length-1),defects):
        if all(b-a>1 for a,b in zip(pos,pos[1:])):
            yield tuple(B if i in pos else A for i in range(length))

def obs(p,q):
    def local(w):
        v=[0]*6; j={}
        for a in w: v[a[0]]+=a[1]
        for a,b in zip(w,w[1:]):
            name=f'{a[0]}{a[1]}:{b[0]}{b[1]}'
            j[name]=j.get(name,0)+1
        return tuple(v),tuple(sorted(j.items()))
    return (len(p),len(q),local(p),local(q),sum(x==y for x,y in zip(p,q)))

def dp(m,n,kp,kq,mismatch,forced):
    # All histories have A endpoints, internal nonadjacent Bs.
    state={(0,0,0,0,0):1}
    visits=0
    for i in range(1,n+1):
        new=defaultdict(int)
        for (ap,aq,d,prevp,prevq),w in state.items():
            for x in ((0,1) if 1<i<m else (0,)) if i<=m else (0,):
                if x and prevp: continue
                for y in (0,1) if 1<i<n else (0,):
                    if y and prevq: continue
                    if i==m+1 and y!=forced: continue
                    bp,bq=ap+x,aq+y
                    dd=d+(int(x!=y) if i<=m else 0)
                    if bp>kp or bq>kq or dd>mismatch: continue
                    new[(bp,bq,dd,x,y)]+=w
                    visits+=1
        state=new
    mass=sum(w for (ap,aq,d,_,_),w in state.items() if (ap,aq,d)==(kp,kq,mismatch))
    return mass,visits

def enumerate_fiber(m,n,kp,kq,mismatch):
    mass=[0,0]; examples={}; signatures=defaultdict(int); key_to_signature={}
    qwords=list(words(n,kq))
    for p in words(m,kp):
        for q in qwords:
            if sum(x!=y for x,y in zip(p,q))==mismatch:
                bit=int(q[m]==B)
                mass[bit]+=1
                examples.setdefault(bit,(p,q))
                signature=(obs(p,q),)+tuple(obs(p+(z,),q) for z in D)
                signatures[signature]+=1
                if bit in key_to_signature:
                    assert key_to_signature[bit]==signature
                else:
                    key_to_signature[bit]=signature
    assert len(signatures)==len(key_to_signature)
    return mass,examples,len(signatures)

def prove_example():
    p=tuple(B if i==2 else A for i in range(6))
    q1=tuple(B if i in (6,8) else A for i in range(10))
    q2=tuple(B if i in (2,4) else A for i in range(10))
    assert obs(p,q1)==obs(p,q2)
    assert q1[6]==B and q2[6]==A
    # A single P APPEND(B) distinguishes the K coordinate.
    after1=obs(p+(B,),q1)
    after2=obs(p+(B,),q2)
    assert after1[-1]==6 and after2[-1]==5
    return {'params': [6,10,1,2,1,0,0,1,0],
            'initial_common_observation':str(obs(p,q1)),
            'after_P_APPEND_B_K':[after1[-1],after2[-1]],
            'common_P':'AABAAA','Q1':'AAAAAABABA','Q2':'AABABAAAAA'}

def main():
    cases=0; nonempty=0; checked_histories=0; transitions=0
    supported_two=0; max_population=0; future_signatures_checked=0
    sample=[]
    for m in range(5,9):
        for n in range(m+1,m+6):
            for kp in range(0,min(3,m-2)+1):
                for kq in range(0,min(4,n-2)+1):
                    for mismatch in (1,):
                        direct,ex,n_signatures=enumerate_fiber(m,n,kp,kq,mismatch)
                        future_signatures_checked+=sum(direct)
                        row=[]
                        for bit in (0,1):
                            mass,steps=dp(m,n,kp,kq,mismatch,bit)
                            transitions+=steps
                            row.append(mass)
                        assert row==direct,(m,n,kp,kq,mismatch,row,direct)
                        cases+=1; nonempty+=int(sum(row)>0)
                        checked_histories+=sum(row)
                        supported_two+=int(all(v>0 for v in row))
                        max_population=max(max_population,sum(row))
                        if (m,n,kp,kq,mismatch)==(6,10,1,2,1):
                            sample=row
                        # Full current O is fiber-constant; full P-APPEND all directions
                        # equivalent iff the bit Q[m] agrees; cross-check representative pairs.
                        assert n_signatures==sum(int(v>0) for v in row)
                        if len(ex)==2:
                            (p0,q0),(p1,q1)=ex[0],ex[1]
                            assert obs(p0,q0)==obs(p1,q1)
                            assert any(obs(p0+(z,),q0)!=obs(p1+(z,),q1) for z in D)
                        if ex:
                            p0,q0=next(iter(ex.values()))
                            for zz in D:
                                actual=obs(p0+(zz,),q0)[-1]
                                expected=obs(p0,q0)[-1]+int(q0[m]==zz)
                                assert actual==expected
    assert sample[0]>0 and sample[1]>0
    print(json.dumps({'status':'STAGE446B_ONE_APPEND_POLYNOMIAL_SUPPORT_PASS',
     'tested_parameter_fibers':cases,'nonempty_fibers':nonempty,
     'raw_history_instances':checked_histories,'both_class_fibers':supported_two,
     'max_fiber_population':max_population,'dp_transitions':transitions,
     'witness':prove_example(),'sample_mass_by_Q_m_plus_1_A_B':sample,
     'append_alphabet_size':len(D),'complete_future_signatures_checked':future_signatures_checked},ensure_ascii=False,sort_keys=True))

if __name__=='__main__':main()
