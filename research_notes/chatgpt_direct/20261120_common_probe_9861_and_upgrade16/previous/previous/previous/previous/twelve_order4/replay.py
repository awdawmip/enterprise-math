"""Rebuild cheap four-class orbits and bounded covers, with a complete original census."""
from pathlib import Path
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor
import argparse,json,subprocess,sys
HERE=Path(__file__).resolve().parent
def run(older,groupdir,previous,ids):
    sys.path[:0]=[str(older/'bounds'),str(older/'curve'),str(groupdir)]
    from prior_bounds import observation_file
    from generate import maps
    from verify import lower
    assert [((10130-lower(125-4*s,8))//4)for s in range(8,14)]==[461,641,824,1008,1188,1371]
    linear,_,_=maps()
    def subgroup(g):
        e=bytes(range(125));o={e};a=g
        while a!=e:o.add(a);a=bytes(g[i]for i in a)
        return frozenset(o)
    groups={subgroup(g)for g in linear};reps=[]
    while groups:
        a=min(groups,key=lambda a:(-len(a),sorted(a)));gen=min(g for g in a if subgroup(g)==a);orb=set()
        for g in linear:
            inv=bytes(g.index(i)for i in range(125));orb.add(subgroup(bytes(g[gen[i]]for i in inv)))
        groups-=orb;reps.append((gen,len(a),len(orb)))
    assert [o for g,o,n in reps[2:8]]==[4]*6
    with TemporaryDirectory()as temp:
        w=Path(temp)
        observation_file(w/'obs')
        src=(previous/'low/class_enumeration.cpp').read_text().replace('880,1090,1230,1350','880,1090,1230,1371')
        assert '1230,1371' in src
        (w/'enum.cpp').write_text(src)
        for label,file in [('enum',w/'enum.cpp'),('basis',HERE/'seedbank.cpp'),('short',HERE/'fixed4.cpp'),('cover',HERE/'fullpacket.cpp')]:
            subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(file),'-o',str(w/label)],check=True)
        def proc(args):return subprocess.run([str(a)for a in args],capture_output=True,text=True,check=True)
        proc([w/'enum',w/'obs',w/'seeds']); cc=proc([w/'basis',w/'seeds',w/'classes'])
        counts=[list(map(int,l.split()))for l in cc.stdout.splitlines()];assert sum(n for c,s,seeds,n in counts)==46696
        def get(i):
            g,order,con= reps[i];p=w/f'g{i}';p.write_text('4 '+' '.join(map(str,g))+'\n')
            sr=proc([w/'short',w/'obs',p,'12','10130']);q=w/f'short{i}';q.write_text(sr.stdout)
            result=proc([w/'cover',p,w/'classes','500000000',w/f'hit{i}',10130,q])
            b,n=map(int,result.stdout.split());assert b==10131 and n<500000000
            return {'index':i,'generator_basis_images':[g[j] for j in (25,5,1)],'linear_conjugates':con,
                    'short_support_counts':[list(map(int,l.split()[1:]))for l in sr.stderr.splitlines()if l.startswith('bank ')],
                    'admissible_packet_counts':{s.split(':')[0]:int(s.split(':')[1]) for s in result.stderr.split()},
                    'nodes':n}
        with ThreadPoolExecutor(max_workers=2)as pool:out=list(pool.map(get,ids))
    return {'cap':10130,'four_orbit_translation_representatives':46696,'types':out}
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for n in ['older','group','previous']:p.add_argument('--'+n,type=Path,required=True)
    p.add_argument('--types',type=int,nargs='+',default=[2,3,4,5])
    a=p.parse_args();print(json.dumps(run(a.older.resolve(),a.group.resolve(),a.previous.resolve(),a.types),sort_keys=True,indent=2))
