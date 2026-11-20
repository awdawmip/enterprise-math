"""Continue the complete typed exact-cover exclusion, retaining every work item."""
import argparse
import hashlib
import json
import struct
import subprocess
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from queue import Empty, Queue
from threading import Lock
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent

def tag(counts):
    return '_'.join('-'.join(map(str, (s,c,n))) for (s,c),n in sorted(counts.items()))

def run(previous, work, jobs, first, last, cost, core_counts, engine, profile=None):
    third = previous/'previous/previous/previous/previous'
    fourth = previous/'previous/previous/previous'
    sys.path[:0] = [str(third/'low'),str(third/'previous/bounds')]
    from prior_bounds import observation_file, symmetries
    from cores import orbits
    from profiles import get, make_profiles, mn
    assert 9855 <= first <= last <= 9870
    assert set(core_counts).issubset({0,1,2,4})
    caps = get(12,last)
    ceilings={8:550,9:740,10:880,11:1090,12:1230,13:1350}
    assert all(s in ceilings and (s==13 or cap<=ceilings[s]) for s,cap in caps.items())
    work.mkdir(parents=True,exist_ok=True)
    if not (work/'obs').exists(): observation_file(work/'obs')
    full=(1<<125)-1
    (work/'cores0.txt').write_text(f'{full%(1<<64)} {full>>64}\n')
    for k in sorted(set(core_counts)-{0}):
        target=work/f'cores{k}.txt'
        if not target.exists():
            fixed,seen,reps=orbits(k)
            assert fixed==seen and len(reps)=={1:1,2:6,4:61}[k]
            with target.open('w') as f:
                for rows,centres in reps:
                    remaining=full^sum(rows)
                    print(remaining%(1<<64),remaining>>64,*centres,file=f)
    executable='front' if engine=='baseline' else 'front_orbits'
    for name,source in [('census',third/'low/class_enumeration.cpp'),
                        ('anchor',fourth/'lower/anchor.cpp'),
                        ('anchor_two',fourth/'lower/anchor_two.cpp'),
                        ('genprof',HERE/'genprof.cpp'),(executable,HERE/(executable+'.cpp'))]:
        exe=work/name
        if not exe.exists() or exe.stat().st_mtime<source.stat().st_mtime:
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',source,'-o',exe],check=True)
    if not (work/'seeds').exists():
        with (work/'census.log').open('w') as out:
            subprocess.run([work/'census',work/'obs',work/'seeds'],stdout=out,check=True)
    seen=set()
    with (work/'seeds').open() as f:
        for line in f:
            s,c=map(int,line.split(' ',2)[:2])
            if c<=caps.get(s,0):seen.add((s,c))
    keys=sorted(seen)
    cases={}
    for value,counts in make_profiles(12,last,first,mn,keys):
        row={key:n for key,n in zip(keys,counts) if n}
        h=row.get((13,1296),0)
        k=row.get((12,1104),0)+h
        p=row.get((12,1116),0)
        if k not in core_counts or k+p>=7:continue
        a=min(p,2 if k<=1 else 1)
        cases[tag(row)]=(value,row,k,h,a)
    digest=hashlib.sha256(('\n'.join(sorted(cases))+'\n').encode()).hexdigest()
    if profile is not None:assert profile in cases
    used=sorted({(12,1116)}.union(*(set(row) for _,row,*_ in cases.values())))
    manifest={'first_cost':first,'last_cost':last,'profile_digest':digest,'core_counts':core_counts,
              'profiles_by_cost':dict(sorted(Counter(v[0] for v in cases.values()).items())),
              'types':used,'caps':caps}
    (work/'manifest.json').write_text(json.dumps(manifest,sort_keys=True,indent=2)+'\n')
    print(json.dumps(manifest,sort_keys=True),flush=True)
    with (work/'seeds').open() as source,(work/'needed').open('w') as out:
        for line in source:
            if tuple(map(int,line.split(' ',2)[:2])) in used:out.write(line)
    (work/'caps').write_text(' '.join(str(caps.get(i,0)) for i in range(14))+'\n')
    (work/'linear').write_text(''.join(' '.join(map(str,row))+'\n' for row in symmetries()[0]))
    if not (work/'bank').exists():
        stats=subprocess.check_output([work/'genprof',work/'linear',work/'needed',work/'caps',work/'bank'],text=True)
        (work/'bank.log').write_text(stats)
    stats=(work/'bank.log').read_text()
    assert [tuple(map(int,l.split()[:2])) for l in stats.splitlines()]==used
    punctures=[]
    with (work/'bank').open('rb') as f:
        for buf in iter(lambda:f.read(24*32768),b''):
            for lo,hi,c,s in struct.iter_unpack('<QQII',buf):
                if (s%256,c)==(12,1116):punctures.append((lo,hi,int(s>=256)))
    assert len(punctures)==3000
    (work/'punct').write_text('1\n12 1116 3000\n'+''.join(f'{lo} {hi} {r}\n' for lo,hi,r in sorted(punctures)))
    for k,h,a in sorted({(k,h,a) for _,_,k,h,a in cases.values() if a}):
        pg='anchor_two' if a==2 else 'anchor'
        dest=work/(('pair' if a==2 else 'anchored')+f'{k}_{h}')
        if not dest.exists():
            args=[work/pg,str(k),str(h),str(a),work/'punct',work/f'cores{k}.txt']
            if a==2:args.append('2')
            with dest.open('w') as out:subprocess.run(args,stdout=out,check=True)
            assert dest.stat().st_size>0
    log=work/'completed.jsonl'
    done={}
    if log.exists():
        for line in log.read_text().splitlines():
            obj=json.loads(line)
            assert obj['tag'] in cases and obj['found']==0
            assert obj['cost']==cases[obj['tag']][0]
            assert obj['tag'] not in done
            done[obj['tag']]=obj
    q=Queue()
    for key,(value,row,*_) in sorted(cases.items(),key=lambda item:(item[1][0],item[0])):
        if key not in done and (cost is None or value==cost) and (profile is None or key==profile):q.put((key,value,[row.get(t,0) for t in used]))
    lock=Lock()
    def worker(worker_id):
        with subprocess.Popen([work/executable,work/'bank',work,work],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True) as proc:
            while True:
                try:key,value,vec=q.get_nowait()
                except Empty:break
                (work/f'running{worker_id}.json').write_text(json.dumps({'tag':key,'cost':value,'started':time.time()})+'\n')
                start=time.monotonic()
                proc.stdin.write(' '.join(map(str,[value,*vec]))+'\n');proc.stdin.flush()
                words=list(map(int,proc.stdout.readline().split()))
                assert len(words)==5 and words[0]==value,words
                obj=dict(zip(('cost','geometric_nodes','leaf_nodes','search_nodes','found'),words))
                obj.update(tag=key,seconds=time.monotonic()-start,engine=engine)
                assert obj['found']==0,obj
                with lock:
                    with log.open('a') as out:out.write(json.dumps(obj,sort_keys=True)+'\n');out.flush()
                    done[key]=obj
                    if len(done)%20==0:print(json.dumps({'completed':len(done),'pending':q.qsize(),'last':obj}),flush=True)
            proc.stdin.close();assert proc.wait()==0
            (work/f'running{worker_id}.json').unlink(missing_ok=True)
    with ThreadPoolExecutor(max_workers=jobs) as pool:
        list(pool.map(worker,range(min(jobs,q.qsize()))))
    tallies=Counter(obj['cost'] for obj in done.values())
    finished=[v for v in range(first,last+1) if tallies[v]==manifest['profiles_by_cost'].get(v,0)]
    ans={'profile_digest':digest,'profiles_completed':len(done),'completed_by_cost':dict(sorted(tallies.items())),
         'fully_excluded_costs':finished,'all_excluded':len(done)==len(cases),
         'search_nodes':sum(o['search_nodes'] for o in done.values()),
         'geometric_nodes':sum(o['geometric_nodes'] for o in done.values())}
    if profile is not None:
        assert profile in done
        ans['verified_profile']=done[profile]
    (work/'result.json').write_text(json.dumps(ans,sort_keys=True,indent=2)+'\n')
    print(json.dumps(ans,sort_keys=True,indent=2),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',type=Path,required=True)
    p.add_argument('--work',type=Path,help='explicit persistent work directory; completed items are reused only here')
    p.add_argument('--jobs',type=int,default=2)
    p.add_argument('--first',type=int,default=9855)
    p.add_argument('--last',type=int,default=9860)
    p.add_argument('--cost',type=int)
    p.add_argument('--cores',type=str,default='0,1,2')
    p.add_argument('--engine',choices=['baseline','orbits'],default='baseline')
    p.add_argument('--profile',help='verify only this exact size/cost/count profile')
    a=p.parse_args()
    if a.work is None:
        with TemporaryDirectory() as d:
            run(a.previous.resolve(),Path(d),a.jobs,a.first,a.last,a.cost,list(map(int,a.cores.split(','))),a.engine,a.profile)
    else:
        run(a.previous.resolve(),a.work.resolve(),a.jobs,a.first,a.last,a.cost,list(map(int,a.cores.split(','))),a.engine,a.profile)
