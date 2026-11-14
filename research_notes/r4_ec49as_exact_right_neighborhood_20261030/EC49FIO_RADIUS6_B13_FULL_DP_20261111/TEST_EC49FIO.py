#!/usr/bin/env python3
"""Independent literal six-label prefix union oracle for the exact tree-DP principle."""
import collections,itertools,json,random,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'EC49FGW_RADIUS5_EXACT_SCREENS_20261110'))
from EC49FGW_RADIUS5_SCREEN import W,raw_key,validate_profile

def literal(words,background):
    return min(len(set().union(*(set(w[:i] for i in range(1,len(w)+1))-background for w in chosen)))
               for chosen in itertools.product(*words))
def independent_trie(words,background):
    root={}
    for j,group in enumerate(words):
        for w in group:
            node=root
            for c in w:node=node.setdefault(c,{})
            node.setdefault('_leaf',set()).add(j)
    goal=(1<<len(words))-1
    def solve(node,path):
        d={0:0}
        terminal=sum(1<<j for j in node.get('_leaf',()))
        sub=terminal
        while sub:
            d[sub]=0
            sub=(sub-1)&terminal
        for c,child in node.items():
            if c=='_leaf':continue
            g=solve(child,path+c)
            edge=0 if path+c in background else 1
            old=dict(d);new=dict(old)
            for a,ca in old.items():
                for b,cb in g.items():
                    if b:
                        s=a|b
                        new[s]=min(new.get(s,10**9),ca+cb+edge)
            d=new
        return d
    return solve(root,'')[goal]
def main():
    rng=random.Random(20261111)
    for trial in range(160):
        groups=[[''.join(rng.choices('ab12xy',k=rng.randint(2,6))) for _ in range(rng.randint(2,3))]
                for j in range(6)]
        possible={w[:i] for group in groups for w in group for i in range(1,len(w)+1)}
        background={p for p in possible if rng.random()<.32}
        assert literal(groups,background)==independent_trie(groups,background),trial
    for witness in W['profiles']:
        rows,paths=validate_profile(witness)
        prefix_support=collections.defaultdict(int);key_support=collections.defaultdict(int)
        for j,(row,path) in enumerate(zip(rows,paths)):
            key_support[raw_key(row['word'])]|=1<<j
            for e in path:prefix_support[e]|=1<<j
        qs=[tuple(map(int,line.split())) for line in
            (HERE/('QS_'+witness['profile_id']+'_13.txt')).read_text().splitlines()]
        assert len(qs)==len(set(qs))==2498
        for q in qs:
            mask=sum(1<<i for i in q)
            assert all((s&mask)!=s for s in key_support.values())
            fixed={e for e,s in prefix_support.items() if s&~mask}
            removed=set().union(*(paths[j] for j in q))-fixed
            assert len(fixed)==80 and len(removed)==14 and len(fixed|removed)==94
    print(json.dumps({'toy_oracle_checks':160,'native_Q_each':2498,'witness_upperbound':94,'status':'PASS'}))
if __name__=='__main__':main()
