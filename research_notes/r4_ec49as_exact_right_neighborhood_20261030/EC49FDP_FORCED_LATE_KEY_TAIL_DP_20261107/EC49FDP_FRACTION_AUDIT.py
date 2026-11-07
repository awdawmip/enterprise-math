#!/usr/bin/env python3
"""Independent exact rational nine-state observer audit of the EC49FDP DP witnesses.
Runs the sibling EC49FDP_TAIL_EXACT_DP.py; no imports from its rank-checking code.
Usage: python EC49FDP_FRACTION_AUDIT.py
"""
from fractions import Fraction
from collections import Counter
import EC49FDP_TAIL_EXACT_DP as tail

PR={'a':(-1,-1),'c':(1,2,-1,-2),'d':(2,1,-2,-1),
    'e':(3,1,1,-3),'f':(1,-1),'g':(2,-2)}
STATES=(('N',0),('N',1),('N',2),('A',0),('A',2),
        ('B',0),('B',1),('AB',0),('BA',0))
BUCKETS=('N','A','B','AB','BA')

def steps(w):
    return tuple(n for c in w for n in PR[c])

def observer(w):
    out=[]
    for name,prev in STATES:
        cur=name
        for t in steps(w):
            if prev==1 and t==2:
                if cur=='N':cur='A'
                elif cur=='B':cur='BA'
            elif prev==2 and t==1:
                if cur=='N':cur='B'
                elif cur=='A':cur='AB'
            prev=t
        out.append(BUCKETS.index(cur))
    return out

def rank_q(words):
    obs=[observer(w) for w in words]
    mat=[[Fraction(int(obs[j][i]==b)) for j in range(len(words))
          for b in range(5)] for i in range(9)]
    rank=0
    for j in range(len(mat[0])):
        pivot=next((i for i in range(rank,9) if mat[i][j]),None)
        if pivot is None:continue
        mat[rank],mat[pivot]=mat[pivot],mat[rank]
        v=mat[rank][j]
        mat[rank]=[a/v for a in mat[rank]]
        for i in range(rank+1,9):
            v=mat[i][j]
            if v:mat[i]=[a-v*b for a,b in zip(mat[i],mat[rank])]
        rank+=1
        if rank==9:break
    return rank

def main():
    for row in tail.main()['results']:
        key=tuple(row['key'])
        witness={int(sig):w for sig,w in row['witness'].items()}
        for h,sigs in [(8,(1,2,4,8)),(9,(16,32))]:
            words=[witness[s] for s in sigs]
            assert rank_q(words)==9,(key,h)
            for w in words:
                st=steps(w)
                assert len(w)==h
                assert tuple(st.count(i) for i in (1,2,3))==key
                assert tuple(st.count(i)-st.count(-i) for i in (1,2,3))==(2,0,0)
                assert len(st)==18+2*key[2]
        print(f"{key}: rank(H8)=rank(H9)=9; lower_bound={row['seed_plus_tail_lower_bound']}")
    print("ALL_16_EXACT_FRACTION_AUDITS_PASS")

if __name__=='__main__':main()
