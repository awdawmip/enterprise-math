"""Recompute the eleven-label bound directly from the native common menu."""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,os,subprocess,sys
from profiles import cases,pr
HERE=Path(__file__).resolve().parent
def verify(previous, budget, jobs, native=False, envelope=None):
    sixth=previous.resolve()
    fifth=sixth/'previous'
    third=fifth/'previous/previous'
    second=third/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(second)
    sys.path[:0]=[str(sixth/'mothers'),str(fifth/'parents'),str(third/'group'),str(second/'bounds')]
    from costs import partitions
    from geometry import inventory,linear_actions
    from cyclic11 import observations
    from generate import maps
    from pairtypes import build
    from prior_bounds import observation_file
    configs=list(cases(budget,partitions))
    total_profiles=len(configs)
    requested={p for p,e,f in configs}
    def spec(t):return ','.join(map(str,t))
    if envelope:
        assert set(envelope)=={spec(p)for p in requested}
        assert all(budget<=c<=11300 for c in envelope.values())
        all_configs={c:list(cases(c,partitions))for c in set(envelope.values())}
        configs=[]
        for p in sorted(requested):
            variants=[(e,f) for pp,e,f in all_configs[envelope[spec(p)]] if pp==p]
            threshold=tuple(map(min,zip(*(e for e,f in variants))))
            configs.append((p,threshold,min(f for e,f in variants)))
    caps=[0]*14
    for proper,inside,minimum in configs:
        assert max(proper)>=11 and sum(inside[:2])>13
        limit=envelope[spec(proper)] if envelope else budget
        possible_extra=limit-minimum-sum(pr[s]for s in proper)
        for s in proper:caps[s]=max(caps[s],pr[s]+possible_extra)
        # Every unassigned proper class has some point outside all parents.
        coverage=[0,13,26,39,52,65,78,85]
        assert min(proper)>coverage[len(inside)]-(125-sum(proper))
    if native and envelope:
        # In the geometric certificate all 8..10 point rows are generated
        # locally by the native solver. Only the two larger banks are read.
        caps[8:11]=[0,0,0]
    legal,menus=observations()
    parents,centers=inventory(linear_actions(),legal,menus)
    rank={i:j for j,items in build(parents,centers)for i in items}
    stream=''.join(f'{m%2**64} {m>>64}\n'for m in parents)+' '.join(str(rank[i])for i in range(1,250))+'\n'
    lin,tr,_=maps()
    with TemporaryDirectory() as temp:
        w=Path(temp)
        (w/'parents').write_text(stream)
        affine=[bytes(t[i]for i in g)for g in lin for t in tr];assert len(set(affine))==12000
        (w/'maps').write_bytes(b''.join(affine))
        observation_file(w/'obs')
        def compiler(n):
            src=sixth/'mothers/union.cpp' if n=='union' else HERE/('native.cpp' if n=='solve' and native else n+'.cpp')
            subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',src,'-o',w/n],check=True)
        with ThreadPoolExecutor(jobs)as pool:list(pool.map(compiler,['census','bank','frame','solve','union']))
        subprocess.run([w/'census',w/'obs',w/'seeds',*map(str,caps[8:13])],stdout=subprocess.DEVNULL,check=True)
        scan=subprocess.run([w/'bank',w/'parents',w/'maps',w/'seeds',w/'B',' '.join(map(str,caps))],capture_output=True,text=True,check=True)
        indexed={str(s):[n,rows]for s,n,rows in [map(int,l.split())for l in scan.stderr.splitlines()]}
        keys=sorted({(len(e),125-sum(p))for p,e,f in configs})
        def frame(pair):
            k,total=pair
            assert total>13*(k-1)
            raw=w/f'raw{k}_{total}';fn=w/f'frame{k}_{total}'
            with raw.open('w')as o:subprocess.run([w/'union',str(k),str(total),'-1','all'],input=stream,text=True,stdout=o,check=True)
            with raw.open()as i,fn.open('w')as o:
                q=subprocess.run([w/'frame',w/'parents',w/'maps',str(k)],stdin=i,stdout=o,stderr=subprocess.PIPE,text=True,check=True)
            raw.unlink()
            return f'{k},{total}',list(map(int,q.stderr.split()))
        with ThreadPoolExecutor(jobs)as pool:frames=dict(pool.map(frame,keys))
        def search(item):
            p,e,minimum=item;k,total=len(e),125-sum(p);limit=envelope[spec(p)] if envelope else budget
            r=subprocess.run([w/'solve',w/'obs',w/'parents',w/'B',w/f'frame{k}_{total}',spec(p),spec(e),str(minimum),str(limit),'0',str(frames[f'{k},{total}'][1])],capture_output=True,text=True,check=True)
            stat=list(map(int,r.stderr.split()))
            assert stat[0]==frames[f'{k},{total}'][1] and len(stat)==5
            assert not r.stdout and stat[-1]==0, (p,e,r.stdout)
            if envelope:assert stat[3]==0
            return (spec(p) if envelope else spec(p)+'__'+spec(e)),stat
        configs.sort(key=lambda v:(v[0],v[1]))
        with ThreadPoolExecutor(jobs)as pool:data=dict(pool.map(search,configs))
    if envelope:
        return dict(budget=budget,checked_budgets=envelope,profiles=total_profiles,groups=len(requested),cases=data,search_nodes=sum(a[1]for a in data.values()))
    return dict(budget=budget,proper_price_caps=caps[8:13],anchored_orbit_inventory=indexed,
                canonical_parent_families=frames,profiles=len(configs),cases=data,
                search_nodes=sum(a[1]for a in data.values()),terminal_assignments=sum(a[3]for a in data.values()))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',type=Path,required=True);p.add_argument('--jobs',type=int,default=3)
    p.add_argument('--budget',type=int);p.add_argument('--native',action='store_true')
    a=p.parse_args();f=HERE/'result.json';old=json.loads(f.read_text())if f.exists()else None
    budget=a.budget if a.budget is not None else old['budget']
    r=verify(a.previous,budget,a.jobs,a.native)
    if old and old['budget']==budget:assert r==old
    print(json.dumps(r,sort_keys=True,indent=2))
