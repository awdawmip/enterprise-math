#!/usr/bin/env python3
"""R139B extremal word: exact one-division test and independent rational-atom check.
Requires check_r139.py in the same directory. No floating-point arithmetic.
"""
from fractions import Fraction
import json
from check_r139 import cells, feasible


def strict_word(t, K, m):
    return tuple(int(((K+i)*t) % 1 < t % 1) for i in range(m))


def chronological_words(K, m):
    L=K-1
    split=sorted({Fraction(a,n) for n in range(max(1,L), L+m+1)
                  for a in range(n+1)})
    return {strict_word((a+b)/2,K,m) for a,b in zip(split,split[1:])}


def main():
    count=0
    independent=0
    rows=[]
    for m in range(4,41):
        target=(1,)+(0,)*(m-2)+(1,)
        target_comp=tuple(1-v for v in target)
        gaps=[g for g in cells(m) if g[-1]==target]
        assert len(gaps)==2,(m,'expected two Farey gap representations',len(gaps))
        K_bad=(m-2)*((m-1)//2)
        for K in list(range(2,(m-1)**2+4))+[10**80+137,10**80+7]:
            L=K-1
            q,r=divmod(L,m)
            predicted=2*q+r>=m-2
            actual=any(feasible(g,K) for g in gaps)
            assert predicted==actual,(m,K,predicted,actual)
            count+=1
        assert not any(feasible(g,K_bad) for g in gaps)
        assert all(any(feasible(g,K) for g in gaps)
                   for K in range(K_bad+1,(m-1)**2+4))
        rows.append(dict(m=m,last_missing_K=K_bad,eventual_K=K_bad+1,
                         gap_representations=len(gaps)))
        if m<=8:
            for K in range(2,40):
                L=K-1
                q,r=divmod(L,m)
                predicted=2*q+r>=m-2
                present=chronological_words(K,m)
                assert (target in present)==predicted,(m,K,'target')
                assert (target_comp in present)==predicted,(m,K,'complement')
                independent+=2
    out={'marker':'R139B_EXTREMAL_WORD_TEST_PASS',
         'arithmetic':'Python exact integers and fractions.Fraction',
         'frozen_source_pin':'43ec6098b1330ae86d0a7863be336c5d97f6ef34',
         'm_range':[4,40],
         'exact_quotient_vs_gap_comparisons':count,
         'independent_chronological_original_strict_comparisons':independent,
         'rows':rows,'formal_verification':'NOT_PERFORMED',
         'independent_mathematical_review':'NOT_REVIEWED'}
    print(out['marker'])
    print('quotient_vs_gap_comparisons',count)
    print('independent_chronological_comparisons',independent)
    with open('verification_r139b.json','w',encoding='utf-8') as f:
        json.dump(out,f,indent=2,ensure_ascii=False)
if __name__=='__main__':main()
