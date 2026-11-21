"""Classify all relabelings preserving the pairwise minimum-read counts on 125 histories."""
from collections import Counter
import json
import sys
from pathlib import Path
from generate import BASE,maps
sys.path.insert(0,str(BASE/'bounds'))
from cyclic11 import observations

def verify():
    bad,menus=observations()
    weights=[[x.bit_count() for x in row]for row in menus]
    linear,translations,_=maps()
    for g in linear+translations:
        assert all(weights[g[i]][g[j]]==weights[i][j]for i in range(125)for j in range(i))
    histogram=Counter(weights[0][1:])
    search_nodes=0;images=[]
    def enumerate_maps(partial,blocks):
        nonlocal search_nodes
        search_nodes+=1
        if not blocks:
            images.append(bytes(partial[i]for i in range(125)))
            return
        # Refinement by the edge colour to a new matched pair; singleton cells are forced.
        source,target=min(blocks,key=lambda p:len(p[0]))
        x=source[0]
        for y in target:
            rest=[];valid=True
            for a,b in blocks:
                sa={};sb={}
                for i in a:
                    if i!=x:sa.setdefault(weights[x][i],[]).append(i)
                for i in b:
                    if i!=y:sb.setdefault(weights[y][i],[]).append(i)
                if sa.keys()!=sb.keys()or any(len(sa[k])!=len(sb[k])for k in sa):
                    valid=False;break
                rest.extend((v,sb[k])for k,v in sa.items())
            if valid:
                partial[x]=y;enumerate_maps(partial,rest);del partial[x]
    initial=[[i for i in range(1,125)if weights[0][i]==k]for k in sorted(histogram)]
    enumerate_maps({0:0},[(v,v)for v in initial])
    assert set(images)==set(linear),len(images)
    return {'pair_histogram_from_zero':sorted((2*k,n) for k,n in histogram.items()),'origin_isometries':len(images),'full_isometries':125*len(images),'nodes':search_nodes}
if __name__=='__main__':print(json.dumps(verify(),sort_keys=True))
