"""Prove the C3 minimum, count all optimal unordered partitions, and verify a representative."""
import argparse,json,os,subprocess,sys
from collections import Counter
from pathlib import Path
from tempfile import TemporaryDirectory
from skeleton import enumerate_fixed
from count import realize
HERE=Path(__file__).resolve().parent

def main(previous):
    last=previous/'previous'
    older=last/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(older)
    sys.path[:0]=[str(previous/'eleven_order3'),str(last/'group'),str(older/'curve'),str(older/'bounds')]
    from fixed import fixed
    from generate import maps
    from verify import MINIMA,lower
    from prior_bounds import observation_file
    from cyclic11 import observations,class_cost
    bad,pair=observations()
    linear,translations,_=maps()
    gen=bytes(25*(i//5%5)+5*(i%5)+i//25 for i in range(125))
    eye=bytes(range(125))
    def compose(f,g):return bytes(f[i] for i in g)
    def conj(f,g):return compose(f,compose(g,bytes(f.index(i)for i in range(125))))
    cap=9996
    caps={s:(cap-lower(125-3*s,9))//3 for s in range(1,14) if 3*MINIMA[s]+lower(125-3*s,9)<=cap}
    assert caps=={8:442,9:624,10:807,11:989,12:1171,13:1354}
    assert {a for a in linear if a!=eye and compose(a,compose(a,a))==eye}=={conj(f,g) for f in linear for g in [gen,compose(gen,gen)]}
    with TemporaryDirectory()as tmp:
        w=Path(tmp);observation_file(w/'obs')
        fixed(w,[gen],bad,pair,class_cost)
        fixed_rows=[tuple(map(int,l.split())) for l in (w/'trifix0').read_text().splitlines()]
        tasks,nunions=enumerate_fixed(fixed_rows,gen,linear,translations,cap)
        (w/'tasks').write_text(''.join(' '.join(map(str,x))+'\n' for x in tasks))
        (w/'lin').write_text(''.join(' '.join(map(str,g))+'\n' for g in linear))
        (w/'g').write_text(' '.join(map(str,gen))+'\n')
        def run(name,*args):
            return subprocess.run([w/name,*[str(a)for a in args]],capture_output=True,text=True,check=True)
        for name in ('catalogue','orbits','short','triples'):
            subprocess.run(['c++','-O3','-std=c++20','-mpopcnt',HERE/(name+'.cpp'),'-o',w/name],check=True)
        run('catalogue',w/'obs',w/'seeds')
        inventory=run('orbits',w/'lin',w/'g',w/'seeds',0,w/'mobile')
        signatures=list(map(int,inventory.stderr.split()))
        short=[]
        for r in range(3):
            proc=run('short',w/'trifix0',w/'mobile',r,0,1,cap)
            assert not proc.stdout and proc.stderr.rstrip().endswith('found 0 best 9997')
            f=proc.stderr.split();short.append({'moving_orbits':r,'nodes':int(f[2]),'lookups':int(f[4])})
        result=run('triples',w/'mobile',w/'tasks',cap,0,1,len(tasks)).stdout.splitlines()
        assert result[-1]==f'end {len(tasks)} 9997'
        hits=[list(map(int,l.split()[1:]))for l in result[:-1]]
        assert len(hits)==2 and all(row[1]==cap for row in hits)
        assert len({row[0] for row in hits})==1
        known=tuple(sorted(tuple(sorted(r)) for r in json.loads((HERE/'groups.json').read_text())))
        tables=set();reconstructions=[]
        for j,_,a,b,c,*packets in hits:
            q,cost,*_,orbit=tasks[j]
            assert (a|b|c)==q
            receipt,ways=realize(fixed_rows,gen,q,cost,sorted(packets),pair,bad,class_cost)
            assert len(ways)==1 and ways.isdisjoint(tables)
            tables.update(ways);reconstructions.append(receipt)
        assert known in tables
        order3={gen,compose(gen,gen)}
        normalizer=sum(conj(compose(t,a),gen)in order3 for a in linear for t in translations)
        stab=sum({tuple(sorted(t[a[i]]for i in r))for r in known}==set(known) for a in linear for t in translations)
        number=orbit*len(tables);subgroups=12000//normalizer
        # The normalizer of the fixed union may permute the three mobile supports.
        # Count its images after fixing one union representative, before lifting to all unions.
        cycles=[];seen=set()
        for point in range(125):
            if point in seen:continue
            cycle={point,gen[point],gen[gen[point]]};cycles.append(cycle);seen|=cycle
        fixed_points=frozenset(i for j,cycle in enumerate(cycles) if q>>j&1 for i in cycle)
        rotations=[compose(t,a)for a in linear for t in translations]
        norm=[f for f in rotations if conj(f,gen) in order3]
        move=lambda f,r:tuple(sorted(tuple(sorted(f[p]for p in row))for row in r))
        images={move(f,known)for f in norm if {f[p] for p in fixed_points}==fixed_points}
        assert images==tables and number==40 and normalizer==120 and stab==3
        assert number*subgroups==12000//stab
        return {'minimum':cap,'fixed_supports':len(fixed_rows),'seed_counts':signatures[2:],
                'short_orbits':short,'three_fixed_unions':nunions,'canonical_unions':len(tasks),
                'single_winning_union_orbit_size':orbit,'reconstructions':reconstructions,
                'fixed_subgroup_optima':number,'conjugate_subgroups':subgroups,
                'stabilizer_order':stab,'normalizer_order':normalizer,'total_optima':number*subgroups}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--previous',type=Path,required=True)
    print(json.dumps(main(p.parse_args().previous.resolve()),indent=2,sort_keys=True))
