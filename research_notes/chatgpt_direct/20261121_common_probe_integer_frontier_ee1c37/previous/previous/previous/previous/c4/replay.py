"""Compute and classify all twelve-label optima under a cyclic symmetry of order four."""
from pathlib import Path
import argparse
import json
import os
from tempfile import TemporaryDirectory
import subprocess
import sys

HERE=Path(__file__).resolve().parent
def verify(previous):
    older=previous/'previous'
    ancient=older/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(ancient)
    sys.path[:0]=[str(older/'group'),str(ancient/'curve'),str(ancient/'bounds')]
    from generate import maps,observation_file
    from verify import lower
    items=[(i,(10148-lower(125-4*i,8))//4) for i in range(1,14)]
    assert [v for i,v in items if i>=8]==[465,645,829,1012,1192,1376]
    def subgroup(g):
        p=bytes(range(125));h=set()
        while p not in h:
            h.add(p);p=bytes(g[j]for j in p)
        return frozenset(h)
    linear,_,_=maps();remaining={subgroup(g)for g in linear};reps=[]
    while remaining:
        h=min(remaining,key=lambda h:(-len(h),sorted(h)))
        gen=min(g for g in h if subgroup(g)==h)
        images=set()
        for a in linear:
            inv=bytes(a.index(i)for i in range(125));images.add(subgroup(bytes(a[gen[j]]for j in inv)))
        reps.append((gen,len(images)));remaining-=images
    def run(args):
        return subprocess.run(list(map(str,args)),check=True,text=True,capture_output=True)
    with TemporaryDirectory()as tmp:
        w=Path(tmp)
        observation_file(w/'obs')
        source=(older/'low/class_enumeration.cpp').read_text()
        assert '1230,1350' in source
        (w/'enum.cpp').write_text(source.replace('1230,1350','1230,1376'))
        for name,path in [('enum',w/'enum.cpp'),('basis',HERE/'basis.cpp'),('short',previous/'twelve_order4/fixed4.cpp'),('packets',HERE/'packets.cpp'),('cover',HERE/'cover.cpp'),('direct',previous/'twelve_order4/fullpacket.cpp')]:
            run(['c++','-O3','-std=c++20','-mpopcnt',path,'-o',w/name])
        run([w/'enum',w/'obs',w/'seeds'])
        run([w/'basis',w/'seeds',w/'basis.txt'])
        basis_size=sum(1 for l in (w/'basis.txt').open())
        data=[]
        for i in range(2,8):
            g,n=reps[i];assert len(subgroup(g))==4
            (w/'g').write_text('4 '+' '.join(map(str,g))+'\n')
            (w/'short.txt').write_text(run([w/'short',w/'obs',w/'g','12','10148']).stdout)
            if i<6:
                b=run([w/'direct',w/'g',w/'basis.txt','500000000',w/'example',10148,w/'short.txt'])
                score,nodes=map(int,b.stdout.split())
                assert score==10149 and nodes<500000000
                data.append(dict(type=i,generator_images=[g[j]for j in (25,5,1)],linear_conjugates=n,cover_nodes=nodes))
                continue
            with (w/'bank').open('w')as f:
                subprocess.run([w/'packets',w/'g',w/'basis.txt','0','unused','10148',w/'short.txt'],stdout=f,check=True)
            result=run([w/'cover',w/'bank','10148'])
            first,last=result.stdout.splitlines()
            assert int(last.split()[1])==(10148 if i==7 else 10149)
            if i==7:
                assert not any(l.startswith(('SINGLE','SHORT')) for l in result.stderr.splitlines())
                hits=[tuple(map(int,l.split()[1:])) for l in result.stderr.splitlines() if l.startswith('PAIR ')]
                assert len(hits)==4
                from classify import classify
                counts_by_orbit,samples=classify(previous,g,w/'bank',hits)
                assert json.loads(json.dumps(samples))==json.loads((HERE/'representatives.json').read_text())
            counts=first.split()
            data.append(dict(type=i,generator_images=[g[j]for j in (25,5,1)],linear_conjugates=n,
                             fixed_support_configurations=list(map(int,counts[1:4])),
                             frame_nodes=int(counts[5]),complement_lookups=int(last.split()[2])))
        return dict(budget=10148,minimum=10148,basis_size=basis_size,cases=data,classification=counts_by_orbit)
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',required=True,type=Path)
    print(json.dumps(verify(p.parse_args().previous.resolve()),sort_keys=True,indent=2))
