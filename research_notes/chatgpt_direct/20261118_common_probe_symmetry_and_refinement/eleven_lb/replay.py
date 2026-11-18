"""Bound all legal eleven-label partitions by typed searches on projected parent unions."""
from pathlib import Path
from tempfile import TemporaryDirectory
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import argparse,json,subprocess,sys
HERE=Path(__file__).resolve().parent
def verify(base,previous,ceiling,jobs):
    sys.path[:0]=[str(base),str(previous/'previous/previous/previous/bounds'),str(previous/'parents')]
    from layout import cases
    from geometry import inventory,linear_actions
    from cyclic11 import observations
    from prior_bounds import observation_file,symmetries,expand
    from pairtypes import build
    plans=cases(ceiling);caps=defaultdict(int)
    for prices,_ in plans.values():
        for s,v in prices.items():caps[s]=max(caps[s],v)
    assert all(v<={9:650,10:900,11:1160,12:1560}[s]for s,v in caps.items())
    bad,menus=observations();parents,centers=inventory(linear_actions(),bad,menus)
    ranks={}
    for j,remaining in build(parents,centers):
        for i in remaining:ranks[i]=j
    bank=''.join(f'{m%(1<<64)} {m>>64}\n'for m in parents)+' '.join(str(ranks[i]) for i in range(1,250))+'\n'
    with TemporaryDirectory()as wd:
        work=Path(wd);(work/'parents').write_text(bank)
        for name,source in [('union',base/'union.cpp'),('census',HERE/'census.cpp'),('project',HERE/'project.cpp'),('quota',HERE/'quota.cpp')]:
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',source,'-o',work/name],check=True)
        observation_file(work/'obs')
        subprocess.run([work/'census',work/'obs',work/'seeds'],stdout=subprocess.DEVNULL,check=True)
        A,T=symmetries();seeds=defaultdict(list)
        for line in (work/'seeds').open():
            s,c,*row=map(int,line.split())
            if c>caps.get(s,0):continue
            m=sum(1<<j for j in row)
            if not any(m&p==m for p in parents):seeds[s,c].append((m,row))
        def keyfile(s,c):return work/f'proper{s}_{c}'
        for (s,c),rows in seeds.items():
            fam=set()
            for m,row in rows:
                if m not in fam:fam.update(expand([row],A,T))
            keyfile(s,c).write_text(''.join(f'{m%(1<<64)} {m>>64}\n' for m in sorted(fam)))
        frames={(len(req),125-sum(p)) for p,(_,req)in plans.items()}
        for k,t in sorted(frames):
            with (work/f'frame{k}_{t}').open('w')as out:subprocess.run([work/'union',str(k),str(t),'-1','all'],input=bank,text=True,stdout=out,check=True)
        def run(entry):
            P,(prices,dem)=entry
            eligible=lambda s:[keyfile(s,c) for ss,c in sorted(seeds)if ss==s and c<=prices[s]]
            k=len(dem);goal=125-sum(P);name=','.join(map(str,P));rest=work/f'rest{name}'
            with rest.open('w')as out:
                proc=subprocess.run([work/'project',work/'parents',work/f'frame{k}_{goal}',str(sum(P[:-1])),' '.join(map(str,dem)),*eligible(P[-1])],text=True,stdout=out,stderr=subprocess.PIPE,check=True)
            sizes=','.join(map(str,P[:-1]))
            opts=[f for s in sorted(set(P[:-1]))for f in eligible(s)]
            test=subprocess.run([work/'quota',rest,sizes,*opts],capture_output=True,text=True,check=True)
            if test.stdout:raise ValueError(('unresolved',name,test.stdout[:150]))
            checks=list(map(int,test.stderr.split()));assert checks[1]==0
            return name,{'parent_prefix_minima':dem,'price_caps':{str(k):v for k,v in sorted(prices.items())},'projection':list(map(int,proc.stderr.split())),'cover':checks}
        with ThreadPoolExecutor(jobs)as pool:stats=dict(pool.map(run,sorted(plans.items())))
    return {'budget':ceiling,'lower':ceiling+1,'cases':stats}
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',type=Path,required=True)
    p.add_argument('--base',type=Path,required=True)
    p.add_argument('--budget',type=int)
    p.add_argument('--jobs',type=int,default=4)
    a=p.parse_args();f=HERE/'result.json';expect=json.loads(f.read_text())if f.exists()else None
    budget=a.budget or expect['budget'];out=verify(a.base.resolve(),a.previous.resolve(),budget,a.jobs)
    if expect is not None and expect['budget']==budget:assert out==expect
    print(json.dumps(out,indent=2,sort_keys=True))
