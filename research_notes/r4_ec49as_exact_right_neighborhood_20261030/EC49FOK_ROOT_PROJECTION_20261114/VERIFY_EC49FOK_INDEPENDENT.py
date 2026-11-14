#!/usr/bin/env python3
"""Independent native prefix-trie DP verification of FOK hidden-root-profile cases.
Usage: python VERIFY_EC49FOK_INDEPENDENT.py master_and_radius3_cases.txt
No C++ root cost table or C++ result file is imported.
"""
from pathlib import Path
import hashlib
import itertools
import sys

ROOTS=(3,5,6,7)
IDS=(32315,32308,32324)
EXPECTED_SHA='cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e'
INF=10**9

def parse(path):
    raw=Path(path).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==EXPECTED_SHA
    it=iter(raw.decode().split())
    assert tuple(int(next(it)) for _ in range(3))==(94,178850,38169)
    words=[]
    for k in range(94):
        n=int(next(it));part=[]
        for j in range(n):
            label=int(next(it));code=next(it)
            part.append((label,int(code[:2],16),tuple(bytes.fromhex(code[2:]))))
        words.append(part)
    cases={}
    for case in range(38169):
        keys=tuple(int(next(it)) for _ in range(7))
        if case in IDS: cases[case]=keys
    try: next(it); raise AssertionError('trailing source')
    except StopIteration: pass
    return words,cases

def table(words, keys, root):
    terms=[(l,code) for k in keys for l,r,code in words[k] if r==root]
    labels=sorted({l for l,_ in terms}); ix={l:j for j,l in enumerate(labels)}
    children=[{}];terminal=[0]
    for l,code in terms:
        u=0
        for letter in code:
            if letter not in children[u]:
                children[u][letter]=len(children); children.append({}); terminal.append(0)
            u=children[u][letter]
        terminal[u]|=1<<ix[l]
    def visit(u):
        states={0:0}
        if terminal[u]:states[terminal[u]]=0
        for child in children[u].values():
            other=visit(child);merged={}
            for a,ca in states.items():
                for b,cb in other.items():
                    m=a|b;v=ca+cb
                    if v<merged.get(m,INF):merged[m]=v
            states=merged
        return {m:c+(m!=0) for m,c in states.items()}
    exact=visit(0);f=[INF]*(1<<len(labels))
    for m,c in exact.items():f[m]=c
    for j in range(len(labels)):
        for m in range(len(f)):
            if not(m>>j&1):f[m]=min(f[m],f[m|1<<j])
    return labels,ix,f

def domain(profile):
    return {l:tuple(r for r in ROOTS if l in profile[r][1]) for l in range(24)}

def projections(d,profile):
    result={}
    for r in ROOTS:
        labels,idx,f=profile[r]
        must=[l for l in labels if len(d[l])==1]
        opt=[l for l in labels if len(d[l])>1]
        base=sum(1<<idx[l] for l in must)
        result[r]=[base|sum(1<<idx[l] for l in chosen)
                   for length in range(len(opt)+1)
                   for chosen in itertools.combinations(opt,length)]
    return result

def complete_map(d,p):
    observed={}
    options=[d[l] for l in range(24)]
    for assignments in itertools.product(*options):
        masks={r:0 for r in ROOTS}
        for l,r in enumerate(assignments):masks[r]|=1<<l
        cost=0
        for r in ROOTS:
            labels,ix,f=p[r]
            local=sum(1<<ix[l] for l in labels if masks[r]>>l&1)
            cost+=f[local]
        observed[tuple(masks[r] for r in ROOTS)]=cost
    return observed

def main(path):
    words,cases=parse(path)
    profiles={k:{r:table(words,cases[k],r) for r in ROOTS} for k in IDS}
    domains={k:domain(profiles[k]) for k in IDS}
    base=32315
    for target,expected_whole in ((32308,443),(32324,10)):
        assert domains[base]==domains[target]
        ps=projections(domains[base],profiles[base])
        assert [len(ps[r]) for r in ROOTS]==[16,8,16,128]
        total=0;visible=0
        for r in ROOTS:
            la,ia,a=profiles[base][r];lb,ib,b=profiles[target][r]
            assert la==lb
            total+=sum(x!=y for x,y in zip(a,b))
            visible+=sum(a[i]!=b[i] for i in ps[r])
        assert total==expected_whole and visible==0,(target,total,visible)
        maps_a=complete_map(domains[base],profiles[base]);maps_b=complete_map(domains[target],profiles[target])
        assert maps_a==maps_b and len(maps_a)==648
        print(f'INDEPENDENT_PASS 32315->{target}: full_root_dp_changes={total}, projected_changes=0, projected_masks=168, complete_assignments=648, exact_cost_maps_equal=1')
    print('EC49FOK_INDEPENDENT_EXACT_PASS')

if __name__=='__main__':main(sys.argv[1])
