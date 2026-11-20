"""Reduce anchored subsets of the cost-8728 witness using its affine stabilizer."""
from itertools import combinations
from pathlib import Path
import json,sys
from generate import maps,BASE
from single_orbit import bits

def prepare(work,k):
    groups = json.loads((BASE/'curve/open_witnesses.json').read_text())['13']['groups']
    rows = [sum(1<<i for i in g)for g in groups]
    lin,tr,_ = maps()
    st=[]
    for l in lin:
        rots=[[l[i]for i in g]for g in groups]
        for t in tr:
            result=[sum(1<<t[i]for i in r)for r in rots]
            if set(result)==set(rows):st.append([rows.index(m)for m in result])
    assert len(st)==4
    kinds={}
    with (work/'bank').open()as f:
        for j in range(int(next(f))):
            s,c,n=map(int,next(f).split())
            for _ in range(n):
                lo,hi=map(int,next(f).split());mask=lo|hi<<64
                if mask in rows:kinds[rows.index(mask)]=j
    assert len(kinds)==13
    keys=set(combinations(range(13),k))
    with (work/f'neighbor{k}').open('w')as f:
        while keys:
            members=min(keys)
            keys-= {tuple(sorted(p[i]for i in members))for p in st}
            pts=[rows[i]for i in members];u=sum(pts)
            print(0,u%(1<<64),u>>64,*[v for m in pts for v in (m%(1<<64),m>>64)],*[kinds[i]for i in members],file=f)
if __name__=='__main__':prepare(Path(sys.argv[1]),int(sys.argv[2]))
