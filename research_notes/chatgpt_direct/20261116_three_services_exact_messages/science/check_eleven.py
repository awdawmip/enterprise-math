"""Verify the eleven-label code against all public conditions, and the ten-label lower bound."""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT/'next_repair/triple'))
from packing import no_ten

P = list(product(range(5), repeat=3))


def translate(i, v, scale=1):
    x,y,z = ((a + scale*b) % 5 for a,b in zip(P[i],v))
    return 25*x+5*y+z


def check():
    data=json.loads((HERE/'strict_eleven.json').read_text())
    labels=data['table']
    assert len(labels)==125 and set(labels)==set(range(11))
    blocks=[frozenset(i for i,c in enumerate(labels) if c==j) for j in range(11)]
    assert sorted(map(len,blocks))==[10]*6+[13]*5
    for j in range(5):
        assert blocks[j]=={translate(i,data['direction'],j) for i in data['orbit_seed']}
    bad=set()
    counts=Counter()
    per_class=[0]*11
    for scale in (1,2):
        for edge in P:
            groups=defaultdict(list)
            for i,row in enumerate(P):
                updated=tuple(v*scale % 5 for v in row)
                inside=tuple(j for j,(x,s) in enumerate(zip(updated,edge)) if x==s or x==(s+1)%5)
                out=tuple(updated[j]==edge[j] for j in inside)
                groups[inside].append((i,out))
            for inside,members in groups.items():
                for (i,x),(j,y),(k,z) in combinations(members,3):
                    if len({x,y,z})==3:bad.add((i,j,k))
                by_class=defaultdict(list)
                for i,x in members:by_class[labels[i]].append(x)
                for b,answers in by_class.items():
                    poss=set(answers)
                    assert 1<=len(poss)<=2
                    if len(poss)==2:
                        u,v=poss
                        k=next(j for j in range(len(inside)) if u[j]!=v[j])
                        for ans in answers:
                            assert [w for w in poss if w[k]==ans[k]]==[ans]
                        per_class[b]+=len(answers)
                    counts[len(poss)-1]+=len(answers)
    assert len(bad)==47000 and counts=={0:19958,1:11292}
    assert all(len({labels[i] for i in t})>=2 for t in bad)
    sym=[]
    for t in P:
        translated={frozenset(translate(i,t) for i in block) for block in blocks}
        if translated==set(blocks):sym.append(t)
    assert sym==[(0,0,0)]
    return dict(sizes=list(map(len,blocks)),public_conditions=250,histogram=dict(counts),
                reads_by_message=per_class,forbidden_triples=len(bad),
                full_partition_translation_stabilizer=sym,lower_bound=no_ten(sorted(bad)))


if __name__=='__main__':
    print(json.dumps(check(),indent=2,sort_keys=True))
