"""Complete the two cost-8722 profiles which have ten minimum-cost 9-sets."""
from pathlib import Path
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor
import json
import subprocess
from replay import HERE, bank, maps, moved, LOW_MASK

def pair_orbits(rows,group,left,right):
    base=min(rows[left])
    assert {moved(base,g)for g in group}==set(rows[left])
    fixed=[g for g in group if moved(base,g)==base]
    allowed={y for y in rows[right]if not y&base}
    while allowed:
        b=min(allowed)
        eq={moved(b,g)for g in fixed}
        if left==right:
            eq|={moved(base,g)for g in group if moved(b,g)==base}
            stab=[g for g in group if moved(base,g)in(base,b) and moved(b,g)in(base,b)]
        else:
            stab=[g for g in fixed if moved(b,g)==b]
        assert eq<=allowed
        allowed-=eq
        yield (base,b),stab

def verify(work):
    lin,tr,_=maps()
    group=[bytes(t[i]for i in g)for g in lin for t in tr]
    rows=bank(work,lin,tr,8728)
    nine=rows[9,557]
    rfile=work/'rows'
    rfile.write_text('1\n9 557 '+str(len(nine))+'\n'+''.join(f'{m&LOW_MASK} {m>>64}\n'for m in nine))
    exe=work/'pure'
    subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(HERE/'pure.cpp'),'-o',str(exe)],check=True)
    results=[]
    for left,right,third in [((12,1104),(12,1104),(11,944)),((13,1296),(12,1104),(10,752))]:
        jobs=[]
        for (a,b),st in pair_orbits(rows,group,left,right):
            compatible={m for m in rows[third]if not m&(a|b)}
            while compatible:
                z=min(compatible)
                equiv={moved(z,g)for g in st}
                assert equiv<=compatible
                compatible-=equiv
                jobs.append((a,b,z))
        jf=work/'jobs'
        jf.write_text(''.join(' '.join(str(v)for m in j for v in (m&LOW_MASK,m>>64))+' 10\n'for j in jobs))
        def check(begin):
            stop=min(begin+1000,len(jobs))
            raw=subprocess.check_output([str(exe),str(rfile),str(jf),str(begin),str(stop)],text=True,stderr=subprocess.DEVNULL)
            res=[list(map(int,l.split()))for l in raw.splitlines()]
            assert [i for i,_,_ in res]==list(range(begin,stop)) and all(not ok for _,_,ok in res)
            return sum(n for _,n,_ in res)
        with ThreadPoolExecutor(max_workers=2)as pool:
            total=sum(pool.map(check,range(0,len(jobs),1000)))
        results.append({'anchor_costs':[left[1], right[1], third[1]],'triples':len(jobs),'nodes':total})
    return results
if __name__=='__main__':
    with TemporaryDirectory()as t:
        print(json.dumps(verify(Path(t)),indent=2,sort_keys=True))
