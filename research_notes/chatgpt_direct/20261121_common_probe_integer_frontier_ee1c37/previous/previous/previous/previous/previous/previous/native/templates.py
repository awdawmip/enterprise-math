"""Reconstruct the symmetric optimum from four seeds, and check the two-action cost balance."""
from itertools import product
from pathlib import Path
import json,os,sys

HERE=Path(__file__).resolve().parent
BASE=Path(os.environ.get('NATIVE_PROBE_PREVIOUS',str(HERE.parent/'previous')))
if not BASE.is_dir():BASE=next(p/'round2/delivery'for p in HERE.parents if (p/'round2/delivery/curve').is_dir())
sys.path.insert(0,str(BASE/'bounds'))
from cyclic11 import observations,class_cost
points=list(product(range(5),repeat=3))
def turn(i):
    x,y,z=points[i]
    return (2*z%5)*25+(2*y%5)*5+(2*x%5)
def ix(p):return 25*(p[0]%5)+5*(p[1]%5)+p[2]%5

def verify():
    groups=json.loads((BASE/'curve/open_witnesses.json').read_text())['13']['groups']
    bad,mask=observations()
    T=tuple(turn(i)for i in range(125));q=lambda g:tuple(sorted(T[i]for i in g))
    groups={tuple(sorted(g)) for g in groups}
    remaining=set(groups);seeds=[];total=0
    while remaining:
        h=min(remaining,key=lambda g:(-len(g),g))
        orbit=[h];u=q(h)
        while u!=h:orbit.append(u);u=q(u)
        assert set(orbit)<=remaining;remaining-=set(orbit)
        price=class_cost(list(h),mask);assert all(class_cost(list(x),mask)==price for x in orbit)
        seeds.append({'size':len(h),'cost':price,'orbit_length':len(orbit),'seed':list(h)})
        total+=price*len(orbit)
    assert total==8728 and sorted(e['orbit_length']for e in seeds)==[1,4,4,4]
    # A public menu is specified in old-history coordinates by the three unordered
    # edges {start_i,start_i+d}; T swaps d=1 and d=3 while renaming the starts.
    all_menus={d:set() for d in (1,3)}
    for d in all_menus:
        for p in points:
            edges=tuple(frozenset((x,(x+d)%5))for x in p)
            all_menus[d].add(edges)
    for d,e in [(1,3),(3,1)]:
        rotated={tuple(frozenset(2*x%5 for x in m[j])for j in (2,1,0))for m in all_menus[d]}
        assert rotated==all_menus[e]
    joint=json.loads((BASE/'native/m13.json').read_text())['joint']
    assert joint['by_maps']=={'doubling doubling doubling':{'0':11261,'1':4364},'identity identity identity':{'0':11261,'1':4364}}
    return {'seeds':seeds,'one_read':total,'zero_reads':31250-total,'reads_per_action':4364}
if __name__=='__main__':print(json.dumps(verify(),sort_keys=True,indent=2))
