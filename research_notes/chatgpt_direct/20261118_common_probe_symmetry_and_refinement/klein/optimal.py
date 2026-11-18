"""Expand all minimal pairs above the eight winning supports and classify their tables."""
from itertools import product
from collections import Counter
from functools import cache
from pathlib import Path

def classify(G,L,T,frames,bad,pair,class_cost):
    history=[];used=set()
    for i in range(125):
        if i in used:continue
        orb=tuple(sorted({g[i]for g in G}));history.append(orb);used.update(orb)
    @cache
    def choices(r,q,cost):
        support=[orb for h,orb in enumerate(history)if q>>h&1]
        pts=set().union(*support)
        if r==1:
            row=tuple(sorted(pts));assert cost==class_cost(row,pair)
            return [(row,)]
        assert r==2;out=set()
        for h in G[1:]:
            families=[]
            for orb in support:
                cos=sorted({tuple(sorted({j,h[j]}))for j in orb})
                if len(cos)!=2:break
                families.append(cos)
            else:
                families[0]=families[0][:1]
                for obj in product(*families):
                    row=tuple(sorted(sum(obj,())))
                    if any(bad[a][b]>>c&1 for i,a in enumerate(row)for j,b in enumerate(row[:i])for c in row[:j]):continue
                    if 2*class_cost(row,pair)!=cost:continue
                    other=tuple(sorted(pts.difference(row)))
                    assert any(tuple(sorted(s[k]for k in row))==other for s in G)
                    out.add(tuple(sorted((row,other))))
        assert out
        return sorted(out)
    tables=set();counts=[]
    for frame in frames:
        picks=[choices(*r)for r in frame]
        counts.append(sorted(len(K)for K in picks))
        for obj in product(*picks):tables.add(tuple(sorted(sum(obj,()))))
    def mov(g,table):return tuple(sorted(tuple(sorted(g[k]for k in row))for row in table))
    group=[bytes(t[k]for k in a)for a in L for t in T]
    normalizes=[g for g in group if {bytes(g[k]for k in a)for a in G}=={bytes(a[k]for k in g)for a in G}]
    assert len(group)==12000
    left=tables.copy();types=[]
    while left:
        t=min(left);orb={mov(a,t)for a in normalizes};assert orb<=left;left-=orb
        stab=[g for g in group if mov(g,t)==t]
        types.append(dict(normalizer_orbit=len(orb),stabilizer_order=len(stab),affine_orbit=len(group)//len(stab)))
    return dict(support_frames=len(frames),fixed_subgroup_tables=len(tables),normalizer=len(normalizes),
                affine_subgroups=len(group)//len(normalizes),types=types,per_frame_choices=counts)
