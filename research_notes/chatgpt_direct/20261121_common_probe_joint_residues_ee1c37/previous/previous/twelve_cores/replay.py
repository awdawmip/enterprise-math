"""Certify all placements of a specified number of central punctures or their full parents."""
import argparse,json,subprocess,sys,os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from tempfile import TemporaryDirectory
HERE=Path(__file__).resolve().parent

def placements(cores,k):
    seen=set();frames=[]
    for index,line in enumerate(cores.read_text().splitlines()):
        lo,hi,*centres=map(int,line.split());free=(hi<<64)|lo
        for choice in range(1<<k):
            inserted=sum(1<<v for j,v in enumerate(centres)if choice>>j&1)
            if inserted&~free:continue
            entry=free^inserted,choice.bit_count()
            if entry in seen:continue
            seen.add(entry);frames.append((free^inserted,1104*k+192*choice.bit_count()))
    return frames

def verify(previous,jobs,scope_filter=None):
    r3=previous/'previous/previous/previous';r2=r3/'previous'
    sys.path[:0]=[str(r3/'low'),str(r2/'curve'),str(r2/'bounds')]
    from prior_bounds import observation_file, symmetries
    from cores import write_all
    from verify import lower,MINIMA
    archive=json.loads((HERE/'weights.json').read_text())
    output={}
    with TemporaryDirectory() as name:
        d=Path(name);observation_file(d/'obs');write_all(d)
        for program in ['rows','cover']:
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/(program+'.cpp'),'-o',d/program],check=True)
        for scope,weight_list in archive.items():
            if scope_filter is not None and scope!=scope_filter: continue
            k,budget=map(int,scope.split('/'));labels=12-k
            frames=placements(d/f'cores{k}.txt',k)
            assert len(frames)==len(weight_list)
            if k==3:
                # The previous census is complete through these ceilings. Every legal
                # size-13 set is a full mother of cost 1,296 (previous geometry proof).
                ceilings=[0]*8+[550,740,880,1090,1230,1350]
                maxima=[0]*14
                for mask,spent0 in frames:
                    for size in range(1,14):
                        cap=budget-spent0-lower(mask.bit_count()-size,labels-1)
                        if cap>=MINIMA[size]:
                            assert size>=8 and (size==13 or cap<=ceilings[size])
                            maxima[size]=max(maxima[size],cap)
                (d/'caps').write_text(' '.join(map(str,maxima))+'\n')
                (d/'linear').write_text(''.join(' '.join(map(str,r))+'\n' for r in symmetries()[0]))
                for pg,src in [('census',r3/'low/class_enumeration.cpp'),('global',HERE/'global.cpp'),('filter',HERE/'filter.cpp')]:
                    subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',src,'-o',d/pg],check=True)
                subprocess.run([d/'census',d/'obs',d/'seeds'],stdout=subprocess.DEVNULL,check=True)
                subprocess.run([d/'global',d/'linear',d/'seeds',d/'caps',d/'global.bin'],stdout=subprocess.DEVNULL,check=True)
            def run(i):
                m,spent=frames[i];left=budget-spent
                rowcap=[left-lower(m.bit_count()-s,labels-1)for s in range(14)]
                least=next((s for s in range(1,14)if rowcap[s]>=MINIMA[s]),14)
                if least==14:
                    assert weight_list[i] is None
                    return 'size'
                inp=d/f'i{i}';wf=d/f'w{i}';data=d/f'd{i}'
                inp.write_text(' '.join(map(str,[m%2**64,m>>64,least,13,*rowcap[least:]]))+'\n')
                if k==3:
                    subprocess.run([d/'filter',d/'global.bin',inp,data,'1'],check=True)
                else:
                    subprocess.run([d/'rows',d/'obs',inp,data],check=True)
                if not data.stat().st_size:
                    assert weight_list[i] is None
                    return 'empty'
                assert len(weight_list[i])==126
                wf.write_text(' '.join(map(str,weight_list[i]))+'\n')
                raw=subprocess.check_output([d/'cover',data,wf,inp,str(left),str(labels)],text=True).strip()
                data.unlink()
                a=list(map(int,raw.split()));assert len(a)==5 and a[-1]==0
                return a
            with ThreadPoolExecutor(jobs)as pool:
                cases=list(pool.map(run,range(len(frames))))
            rows=[r for r in cases if isinstance(r,list)]
            output[scope]=dict(branches=len(cases),legal_candidates=sum(r[1]for r in rows),
                 weighted_candidates=sum(r[2]for r in rows),cover_nodes=sum(r[3]for r in rows),cases=cases)
    return output

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True);p.add_argument('--jobs',type=int,default=4);p.add_argument('--scope',choices=('3/9860','5/9995'));a=p.parse_args()
    result=verify(a.previous.resolve(),a.jobs,a.scope)
    expected=json.loads((HERE/"result.json").read_text())
    assert result==({a.scope:expected[a.scope]} if a.scope else expected)
    print(json.dumps(result,indent=2,sort_keys=True))
