"""Replay this increment against the immutable previous shared-probe directory."""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from profiles import get, make_profiles, mn

HERE = Path(__file__).resolve().parent
DEFAULT = next((a/'round2/delivery' for a in HERE.parents if (a/'round2/delivery/bounds').is_dir()), HERE.parent/'previous')

def run(old, limits):
    sys.path.insert(0, str(old / 'bounds'))
    import prior_bounds as bank
    from cores import write_all
    # All thirteen-point classes have price 1296, so no other prices arise at that size.
    record_caps = (0,0,0,0,0,0,0,0,550,740,880,1090,1230,1350)
    with tempfile.TemporaryDirectory() as directory:
        tmp = Path(directory)
        for name in ('core_completions','class_enumeration','typed_cover','seven_parents'):
            subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',str(HERE/(name+'.cpp')),'-o',str(tmp/name)],check=True)
        bank.observation_file(tmp/'obs')
        from seven_cert import verify as verify_seven
        seven=verify_seven(tmp)
        print("seven-parent exclusion",seven,flush=True)
        orbits = write_all(tmp)
        strata = {}
        for (k,cap,maximum) in [(6,31250,6),(5,11300,2),(4,10980,1)]:
            output = subprocess.check_output([str(tmp/'core_completions'),str(k),'11',str(cap),str(maximum),str(tmp/'obs'),str(tmp/f'cores{k}.txt')],text=True)
            found = [list(map(int,row.split())) for row in output.splitlines()]
            assert all(len(row)==4 and row[3]==0 for row in found)
            strata[k] = dict(orbits=orbits[k],branches=len(found),nodes=sum(v[2]for v in found),
                              budget=cap,max_centres=maximum)
        print('core completions',strata,flush=True)
        minima = subprocess.check_output([str(tmp/'class_enumeration'),str(tmp/'obs'),str(tmp/'seeds')],text=True)
        assert {int(a):int(c) for a,_,c,*_ in (l.split() for l in minima.splitlines())} == {s:mn[s]for s in range(2,14)}
        caps = {k:get(k,budget) for k,budget in limits.items()}
        assert all(s>=8 and (s==13 or cap<=record_caps[s]) for d in caps.values() for s,cap in d.items())
        with (tmp/'filter').open('w')as f:
            for line in (tmp/'seeds').open():
                s,c,_=line.split(' ',2)
                if int(c)<=max(d.get(int(s),0)for d in caps.values()):f.write(line)
        families=bank.families(tmp/'filter',tmp/'db')
        keys=sorted(families)
        assert all(c in (1104,1116) for s,c in keys if s==12)
        results={}
        for k,cap in limits.items():
            previous = {11:10962,12:9825}[k]
            rows=make_profiles(k,cap,previous,mn,keys)
            keep=[]
            for cost,counts in rows:
                ncores = sum(count for (s,c),count in zip(keys,counts) if s==13 or (s,c)==(12,1104))
                if k==11 and ncores>=4 and cap<=10980:continue
                if k==11 and sum(count for (s,c),count in zip(keys,counts) if s==13 or (s==12 and c in (1104,1116)))>=7:continue
                keep.append((cost,counts))
            body=''.join(' '.join(map(str,[cost,*counts]))+'\n'for cost,counts in keep)
            output=subprocess.check_output([str(tmp/'typed_cover'),str(tmp/'db'),str(tmp)],text=True,input=body)
            tested=[list(map(int,l.split())) for l in output.splitlines()]
            assert all(found==0 for _,_,found in tested)
            assert [v for v,_,_ in tested]==[v for v,_ in keep]
            results[k]=dict(budget=cap,bound=cap+1,profiles=len(keep),nodes=sum(x[1] for x in tested))
            print(k,results[k],flush=True)
    return {'strata':strata,'bounds':results,'seven':seven}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--prior',type=Path,default=DEFAULT)
    p.add_argument('--budgets',nargs=2,type=int,default=[10979,9833])
    a=p.parse_args()
    result=json.loads(json.dumps(run(a.prior.resolve(),dict(zip((11,12),a.budgets)))))
    reference=json.loads((HERE/'result.json').read_text())
    if a.budgets == [reference['bounds'][k]['budget'] for k in ('11','12')]:
        for section in ('bounds','strata'):
            for key,spec in reference[section].items():
                assert all(result[section][key][field] == expected for field,expected in spec.items())
        assert all(result['seven'][field]==expected for field,expected in reference['seven'].items())
        print(json.dumps(reference,sort_keys=True))
    else:
        print(json.dumps(result,sort_keys=True))
