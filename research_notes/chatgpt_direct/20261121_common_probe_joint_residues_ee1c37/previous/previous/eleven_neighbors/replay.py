"""Can changing five old classes take an optimal eleven-label table off its optimal plateau?"""
from concurrent.futures import ThreadPoolExecutor
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,os,subprocess,sys
HERE=Path(__file__).resolve().parent
def run(sixth,k,jobs):
    fifth=sixth/'previous';fourth=fifth/'previous';third=fourth/'previous';second=third/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(second);sys.path[:0]=[str(third/'group'),str(second/'bounds')]
    from generate import maps
    from cyclic11 import observations,class_cost
    from prior_bounds import observation_file
    _,menus=observations()
    reps=json.loads((fourth/'eleven_six_counts/groups.json').read_text())+[json.loads((fifth/'eleven_equal/groups.json').read_text())]
    linear,trans,_=maps();affine=[bytes(t[y]for y in g) for g in linear for t in trans]
    out=[]
    with TemporaryDirectory()as tmp:
        w=Path(tmp);observation_file(w/'menus')
        subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/'cover.cpp','-o',w/'cover'],check=True)
        for i,old in enumerate(reps):
            code={tuple(sorted(r)):j for j,r in enumerate(old)}
            stab=[]
            for g in affine:
                action=[code.get(tuple(sorted(g[x]for x in r)))for r in old]
                if None not in action:stab.append(action)
            price=[class_cost(r,menus)for r in old];assert sum(price)==11292
            opts=[]
            for t in combinations(range(11),k):
                if t!=min(tuple(sorted(g[j]for j in t))for g in stab):continue
                rows=[sum(1<<x for x in old[j])for j in t];m=sum(rows)
                opts.append([m%2**64,m>>64,k,11292-sum(price[j]for j in t),*[b for h in rows for b in (h%2**64,h>>64)]])
            (w/'regions').write_text(''.join(' '.join(map(str,r))+'\n'for r in opts))
            def search(first):
                raw=subprocess.check_output([w/'cover',w/'menus',w/'regions',str(first),str(min(len(opts),first+5)),'31250'],text=True)
                return [list(map(int,l.split()))for l in raw.splitlines()]
            with ThreadPoolExecutor(jobs)as pool:hits=[r for rs in pool.map(search,range(0,len(opts),5))for r in rs]
            assert [r[0]for r in hits]==list(range(len(opts)))
            assert all(len(r)==3 and r[2]==0 for r in hits)
            out.append(dict(stabilizer_order=len(stab),regions=len(opts),nodes=sum(r[1]for r in hits)))
    return dict(changed_old_classes=k,source_cost=11292,ceiling=31250,distinct_more_expensive_partitions=0,by_orbit=out)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);p.add_argument('--jobs',type=int,default=3)
    a=p.parse_args();old=json.loads((HERE/'result.json').read_text())
    result=run(a.previous.resolve(),old['changed_old_classes'],a.jobs);assert old==result
    print(json.dumps(result,indent=2,sort_keys=True))
