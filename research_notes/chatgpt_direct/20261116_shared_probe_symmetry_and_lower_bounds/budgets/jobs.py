"""Anchor pairs of rare 12/13 point classes before an unrestricted residual search."""
from pathlib import Path
from collections import Counter
import sys
from itertools import permutations,product
g=Path(__file__).resolve().parent.parent/'group'
sys.path.insert(0,str(g))
from generate import maps
from single_orbit import bits

def prepare(work,limit,basename='other',fixed_profiles=None):
 with (work/'bank').open()as f:
    nt=int(next(f));rows={}
    for _ in range(nt):
        s,c,n=map(int,next(f).split());rows[c]=[(lo|hi<<64)for lo,hi in (map(int,next(f).split())for _ in range(n))]
 profiles=[list(map(int,l.split()))for l in (work/'profiles').read_text().splitlines()]
 lin,tr,_=maps()
 actions=[bytes(t[i]for i in a)for a in lin for t in tr]
 def moved(m,g):return sum(1<<g[i]for i in bits(m))
 bytype={};jobs=[]
 for pid,(cost,*cnt) in enumerate(profiles):
    if cost>limit or (fixed_profiles is not None and pid not in fixed_profiles):continue
    keys=list(rows);m={p:n for p,n in zip(keys,cnt) if n}
    anchors=sorted([p for p,n in m.items()if p>=1104 for _ in range(n)],key=lambda p:len(rows[p]))
    if len(anchors)!=2:continue
    a,b=anchors
    if fixed_profiles is None and a==b==1104 and cost not in (8714,8716):continue
    if tuple(anchors) not in bytype:
        first=rows[a][0];mus={moved(first,g)for g in actions}
        assert mus==set(rows[a]),(a,len(mus))
        stab=[g for g in actions if moved(first,g)==first]
        others={v for v in rows[b]if not(v&first)}
        reps=[]
        while others:
            second=min(others);orb={moved(second,g)for g in stab}
            if a==b:orb|={moved(first,g)for g in actions if moved(second,g)==first}
            assert orb<=others
            others-=orb;reps.append((first,second))
        bytype[tuple(anchors)]=reps
    m[a]-=1;m[b]-=1
    for f,s in bytype[tuple(anchors)]:
        arr=[pid,cost,f%(1<<64),f>>64,s%(1<<64),s>>64,*[m.get(k,0)for k in keys]]
        jobs.append(arr)
 (work/basename).write_text(''.join(' '.join(map(str,j))+'\n'for j in jobs))
 return len(jobs)
if __name__=='__main__':print(prepare(Path(sys.argv[1]),int(sys.argv[2])))
