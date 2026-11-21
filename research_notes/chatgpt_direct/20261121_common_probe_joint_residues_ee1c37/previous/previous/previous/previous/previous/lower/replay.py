"""Check the incremental universal lower bounds, starting from the archived single-class model."""
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,subprocess,sys
HERE=Path(__file__).resolve().parent
ROOT=next((p for p in HERE.parents if (p/'round2/delivery/bounds').exists()),None)
def verify(native,last,jobs,reference):
    sys.path[:0]=[str(last/'low'),str(native/'bounds')]
    import prior_bounds
    from profiles import make_profiles,get,mn
    from cores import write_all
    lower={11:10981,12:9836}
    with TemporaryDirectory()as dest:
        tmp=Path(dest);prior_bounds.observation_file(tmp/'obs');write_all(tmp);print('core orbit representatives ready',flush=True)
        def build(name,src):
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',str(src),'-o',str(tmp/name)],check=True)
        for name,src in [('regions',HERE/'regions.cpp'),('anchor',HERE/'anchor.cpp'),
                         ('anchored',HERE/'anchored.cpp'),('anchor_two',HERE/'anchor_two.cpp'),('anchored_two',HERE/'anchored_two.cpp'),('cover',HERE/'cover.cpp'),
                         ('census',last/'low/class_enumeration.cpp')]:build(name,src)
        geometry={}
        for s,sp in reference['strata'].items():
            k,labels=s.split('/');cap,maxcentres=sp['budget'],sp['max_full']
            out=subprocess.check_output([str(tmp/'regions'),k,labels,str(cap),str(maxcentres),str(tmp/'obs'),str(tmp/f'cores{k}.txt')],text=True)
            vals=[tuple(map(int,line.split()))for line in out.splitlines()]
            assert not any(v[3]for v in vals)
            geometry[s]=dict(budget=cap,max_full=maxcentres,branches=len(vals),nodes=sum(r[2]for r in vals));print('stratum',s,geometry[s],flush=True)
        subprocess.run([str(tmp/'census'),str(tmp/'obs'),str(tmp/'seeds')],stdout=subprocess.DEVNULL,check=True)
        limits={i:get(i,reference['bounds'][str(i)]['bound']-1) for i in lower}
        caps={8:550,9:740,10:880,11:1090,12:1230,13:1350}
        assert all(s in caps and (s==13 or v<=caps[s])for d in limits.values()for s,v in d.items())
        maxima={s:max(d.get(s,0)for d in limits.values())for s in caps}
        needed=set()
        for line in (tmp/'seeds').open():
            s,c,_=line.split(' ',2);s,c=int(s),int(c)
            if c<=maxima.get(s,0):needed.add((s,c))
        keys=sorted(needed);profiles={};types=set()
        for k,lo in lower.items():
            cap=reference['bounds'][str(k)]['bound']-1
            cases=[]
            for v,counts in make_profiles(k,cap,lo,mn,keys):
                d={t:n for t,n in zip(keys,counts)if n}
                big=d.get((13,1296),0);core=big+d.get((12,1104),0);punct=d.get((12,1116),0)
                if k==11 and big==2 and v<10986:continue
                if core+punct>=7:continue
                if k==11 and core>=4:continue
                if k==12 and core>=reference['twelve_core_cutoff']:continue
                cases.append((v,d,core,big,punct));types|=set(d)
            profiles[k]=cases;print('generated',k,len(cases),'profiles',flush=True)
        with (tmp/'filter').open('w')as f:
            for line in (tmp/'seeds').open():
                s,c,_=line.split(' ',2)
                if (int(s),int(c)) in types:f.write(line)
        fam=prior_bounds.families(tmp/'filter',tmp/'bank');keys=sorted(fam)
        anchorfiles={}
        def fixed_file(n,h,number):
            if (n,h,number) not in anchorfiles:
                name=tmp/f'anchored{n}_{h}_{number}'
                program='anchor_two' if number==2 else 'anchor'
                cmd=[str(tmp/program),str(n),str(h),str(number),str(tmp/'bank'),str(tmp/f'cores{n}.txt')]
                if number==2:cmd.append('2')
                with name.open('w')as out:subprocess.run(cmd,stdout=out,check=True)
                assert name.stat().st_size
                anchorfiles[n,h,number]=name
            return anchorfiles[n,h,number]
        results={}
        for k,cases in profiles.items():
            buckets=defaultdict(list)
            for i,(v,d,core,big,punct) in enumerate(cases):
                ext=2 if core in (0,1) and punct>=3 else int(core in (1,2,3) and punct>=2)
                arr=[d.get(key,0)for key in keys]
                row=[i,v,*arr] if ext else [v,*arr]
                exe=[str(tmp/('anchored_two' if ext==2 else 'anchored')),str(tmp/'bank'),str(tmp),str(fixed_file(core,big,ext))] if ext else [str(tmp/'cover'),str(tmp/'bank'),str(tmp)]
                buckets[tuple(exe)].append((v,row))
            def run(job):
                exe,rows=job
                raw=subprocess.check_output(exe,input=''.join(' '.join(map(str,row))+'\n'for _,row in rows),text=True)
                out=[list(map(int,l.split()))for l in raw.splitlines()]
                assert len(rows)==len(out)
                assert all(ok==0 and v==test[0]for (*_,v,n,ok),test in zip(out,rows))
                return len(rows)
            blocks=[(exe,arr[i:i+4])for exe,arr in buckets.items()for i in range(0,len(arr),4)]
            with ThreadPoolExecutor(max_workers=jobs)as pool:tested=sum(pool.map(run,blocks))
            results[str(k)]=dict(bound=reference['bounds'][str(k)]['bound'],profiles=tested);print('checked',k,tested,flush=True)
    return dict(strata=geometry,bounds=results,twelve_core_cutoff=reference['twelve_core_cutoff'])
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--native',type=Path,default=(ROOT/'round2/delivery')if ROOT else HERE.parent/'previous/previous')
    p.add_argument('--last',type=Path,default=(ROOT/'round3/delivery')if ROOT else HERE.parent/'previous')
    p.add_argument('--jobs',type=int,default=4)
    a=p.parse_args()
    ref=json.loads((HERE/'result.json').read_text())
    tested=verify(a.native.resolve(),a.last.resolve(),a.jobs,ref)
    assert tested==ref
    print(json.dumps(tested,sort_keys=True))
