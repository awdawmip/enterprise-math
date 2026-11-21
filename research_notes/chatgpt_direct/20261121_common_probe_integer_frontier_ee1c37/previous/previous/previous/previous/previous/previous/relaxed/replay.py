"""Check profiles 8712 and 8715 by anchoring a pair of cores and one 747-cost class."""
from pathlib import Path
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor
import argparse,json,sys,subprocess
HERE=Path(__file__).resolve().parent

def check(older,groupdir,costs,workers):
    sys.path[:0]=[str(older/"curve"),str(older/"bounds"),str(groupdir)]
    import generate
    generate.BASE=older
    linear,trans,_=generate.maps()
    group=[bytes(t[i]for i in l)for t in trans for l in linear]
    def members(m):
        while m:
            b=m&-m;yield b.bit_length()-1;m-=b
    def moved(m,g):return sum(1<<g[i]for i in members(m))
    low=(1<<64)-1
    with TemporaryDirectory() as tmp:
        work=Path(tmp)
        rows=generate.bank(work,linear,trans,8728)
        profiles={t:[] for t in costs}
        keys=list(rows)
        for t,q in generate.profiles(keys,8728):
            if t in profiles:
                profiles[t].append({keys[i]:n for i,n in enumerate(q) if n})
        expected={8712:{(9,557):9,(10,744):1,(10,747):1,(12,1104):2},8715:{(9,557):9,(10,747):2,(12,1104):2}}
        assert all(profiles[t]==[expected[t]] for t in costs)
        with (work/'rows').open('w') as stream:
            for s,c in sorted(rows):
                if c not in (557,744,747):continue
                v=sorted(rows[s,c]);print(s,c,len(v),file=stream)
                for r in v:print(r&low,r>>64,0,file=stream)
        population=set(rows[12,1104]);first=min(population)
        assert {moved(first,g)for g in group}==population
        stabilizer=[g for g in group if moved(first,g)==first]
        remaining={r for r in population if not r&first}
        pairs=[]
        while remaining:
            b=min(remaining)
            equiv={moved(b,g)for g in stabilizer}
            equiv.update(moved(first,g)for g in group if moved(b,g)==first)
            assert equiv<=remaining
            remaining-=equiv;pairs.append((first,b))
        assert len(pairs)==6
        def prepare(pair,idx):
            u,v=pair
            st=[g for g in group if {moved(u,g),moved(v,g)}=={u,v}]
            available={r for r in rows[10,747] if not r&(u|v)}
            sets=[]
            while available:
                rep=min(available);orb={moved(rep,g)for g in st}
                assert orb<=available
                available-=orb;sets.append((rep,len(orb)))
            with (work/f'anchors{idx}').open('w')as stream:
                for x,n in sets:print(*[q for r in (u,v,x)for q in (r&low,r>>64)],n,file=stream)
            return len(sets)
        anchor_sizes=[prepare(pair,i)for i,pair in enumerate(pairs)]
        exe=work/'complete'
        subprocess.run(['c++','-std=c++17','-O3','-mpopcnt',str(HERE/'complete.cpp'),'-o',str(exe)],check=True)
        assert anchor_sizes==[787,424,416,1735,516,19]
        def task(job):
            i,t=job;out=subprocess.check_output([str(exe),str(work/'rows'),str(work/f'anchors{i}'),'1','0',str((t-8709)//3)],cwd=work,text=True)
            data=[list(map(int,l.split()))for l in out.splitlines()]
            assert len(data)==anchor_sizes[i] and [r[0]for r in data]==list(range(len(data))) and not any(r[1]for r in data)
            return (i,t,len(data),sum(r[2]for r in data))
        with ThreadPoolExecutor(max_workers=workers)as pool: output=list(pool.map(task,[(i,t)for t in costs for i in range(6)]))
    return {str(t):[{'special_anchors':n,'nodes':nodes}for i,tt,n,nodes in output if tt==t]for t in costs}
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--older',type=Path,required=True)
    p.add_argument('--group',type=Path,default=HERE.parent/'group')
    p.add_argument('--costs',type=int,nargs='+',choices=[8712,8715],default=[int(k) for k in json.loads((HERE/"result.json").read_text())])
    p.add_argument('--jobs',type=int,default=2)
    a=p.parse_args()
    print(json.dumps(check(a.older.resolve(),a.group.resolve(),a.costs,a.jobs),indent=2))
