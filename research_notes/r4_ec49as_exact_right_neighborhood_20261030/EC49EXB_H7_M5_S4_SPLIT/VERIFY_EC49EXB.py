#!/usr/bin/env python3
"""EC49EXB early-repeat exact enumeration; predecessor VERIFY_EC49ER.py required."""
from itertools import product,combinations
from collections import defaultdict,Counter
from VERIFY_EC49ER import OPS,BASE,path,poscount,displacement,signature,rational_rank,prefixes
import json

def verify():
    t4=frozenset(signature(w) for w in BASE)
    assert len(t4)==4
    ranks={str(k):sorted({rational_rank(comb) for comb in combinations(t4,k)}) for k in range(1,5)}
    assert ranks=={'1':[3],'2':[5],'3':[7],'4':[9]}
    P={};wordcounts={};short_tail={}
    for h in range(2,8):
        tbl=defaultdict(set); count=0;tails={}
        for tup in product(OPS,repeat=h):
            w=''.join(tup)
            if displacement(w)!=(2,0,0,0,0,0):continue
            count+=1
            p=poscount(w);s=signature(w)
            if s in t4:tbl[p].add(s)
            q=path(w);key=(p,q[:-2])
            assert key not in tails,(h,key,w,tails[key])
            tails[key]=w
        P[h]=tuple(sorted(p for p,sigs in tbl.items() if sigs==t4))
        wordcounts[h]=count;short_tail[h]=len(tails)
    assert [len(P[h]) for h in range(2,8)]==[1,3,7,13,22,34]
    assert [wordcounts[h] for h in range(2,8)]==[8,51,304,1770,10224,58947]
    base=P[2][0];counts=Counter();checked=0
    for ps in product(*(P[h] for h in range(3,8))):
        checked+=1;seq=(base,)+ps
        if len(set(seq))!=5:continue
        pair=[(i+2,j+2) for i in range(6) for j in range(i+1,6) if seq[i]==seq[j]]
        assert len(pair)==1
        counts[pair[0]]+=1
    expected={(3,4):9257,(4,5):6513,(4,6):1215,(5,6):4598,(5,7):1251,(6,7):3203}
    assert dict(counts)==expected
    early=sum(n for (i,j),n in counts.items() if j<7)
    late=sum(n for (i,j),n in counts.items() if j==7)
    assert (checked,early,late)==(204204,21583,4454)
    family={2:('ce','de','ec','ed'),3:('cec','ded','ecc','edd')}
    for h in range(4,8):
        family[h]=tuple(w+'f'*(h-4) for w in ('cefg','degf','ecfg','edgf'))
    allwords=[w for row in family.values() for w in row]
    assert len(prefixes(allwords))==80
    assert len({poscount(family[h][0]) for h in family})==5
    for h,words in family.items():
        assert len({poscount(w) for w in words})==1
        assert all(displacement(w)==(2,0,0,0,0,0) for w in words)
        assert {signature(w) for w in words}==t4
    return dict(unit='EC49EXB',status='PASS',returning_words=wordcounts,
                T4_subset_ranks=ranks,eligible_key_counts={h:len(P[h]) for h in P},
                schedules_examined=checked,M5_schedules=early+late,
                repeat_pair_counts={f'{i},{j}':n for (i,j),n in sorted(counts.items())},
                early_repeat=early,late_repeat=late,
                early_repeat_exact_optimum_E=80,attaining_words=family,
                late_repeat_global_optimum='OPEN',terminal_two_step_collisions=sum(wordcounts.values())-sum(short_tail.values()))
if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
