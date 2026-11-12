#!/usr/bin/env python3
"""Independent exact core-expansion census from 3- and 4-key optional support subsets."""
import itertools,collections,sys
from pathlib import Path
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'EC49FJD_RELEASE_B11_COMPLETE_20261111'))
from EC49FGW_RADIUS5_SCREEN import PIN,all_words,raw_key
assert PIN=='fc0f038e7bfd12c886b4d37f900bfb770c0f61ab'
labels=sorted({lab for lab,_ in all_words()});bit={lab:1<<i for i,lab in enumerate(labels)}
support=collections.defaultdict(int)
for lab,w in all_words():support[raw_key(w)]|=bit[lab]
forced=((2,1,1),(3,0,1))
other=sorted(set(support)-set(forced))
need=((1<<24)-1) & ~(support[forced[0]]|support[forced[1]])
a=[support[k]&need for k in other]
triples=[t for t in itertools.combinations(range(92),3) if a[t[0]]|a[t[1]]|a[t[2]]==need]
quads=[t for t in itertools.combinations(range(92),4) if a[t[0]]|a[t[1]]|a[t[2]]|a[t[3]]==need]
assert len(triples)==16 and len(quads)==2004
sup3={tuple(sorted((*t,*ext))) for t in triples for ext in itertools.combinations((i for i in range(92) if i not in t),2)}
sup4={tuple(sorted((*q,i))) for q in quads for i in range(92) if i not in q}
assert len(sup3)==58500 and len(sup4-sup3)==45030 and 108434-len(sup3|sup4)==4904
print('EC49FMC_INDEPENDENT_CORE_EXPANSION_PASS',len(sup3),len(sup4-sup3),4904)
