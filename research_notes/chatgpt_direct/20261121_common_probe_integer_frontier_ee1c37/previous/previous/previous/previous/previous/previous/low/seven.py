import subprocess

import geometry
from cyclic11 import observations,setbits
def seven(tmp):
    bad, obs = observations()
    actions=geometry.linear_actions()
    parents,centres=geometry.inventory(actions,bad,obs)
    (tmp/'parents').write_text(''.join(f'{p%2**64} {p>>64} {c}\n'for p,c in zip(parents,centres)))
    raw=subprocess.check_output([str(tmp/'seven_parents'),'7',str(tmp/'parents')],text=True)
    rows=[tuple(map(int,l.split()))for l in raw.splitlines() if l[0].isdigit()]
    key=geometry.normalize(parents,centres,actions)
    reps={key(r) for r in rows}
    print('parents',len(reps),flush=True)
    full=(1<<125)-1
    residuals=set()
    for ids in sorted(reps):
        candidates=[parents[i] for i in ids]
        def search(j,used,spent):
            if j==len(candidates):
                residuals.add((full^used,spent));return
            p=candidates[j]
            for i in [-1]+list(setbits(p)):
                m=p if i<0 else p^(1<<i)
                if used&m:continue
                # Omissions are charged by whether they remove the centre.
                c=1296 if i==-1 else 1104 if i==centres[ids[j]] else 1116
                search(j+1,used|m,spent+c)
        search(0,0,0)
    print('raw residuals',len(residuals),flush=True)
    normalized={}
    for m,c in residuals:
        normalized[m]=min(c,normalized.get(m,c))
    dest=tmp/'seven_spaces.txt'
    with dest.open('w')as f:
        for m,c in normalized.items():print(m%2**64,m>>64,c,file=f)
    print('normalized',len(normalized),flush=True)
    return len(reps),len(rows),len(residuals),len(normalized)
