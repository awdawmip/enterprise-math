"""Exact twelve-label V4 minimum, and classification of every equality case."""
import argparse,json,os,sys,subprocess
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor
from optimal import classify

HERE=Path(__file__).resolve().parent
CAP=10672

def composition(a,b):
    return bytes(a[i]for i in b)

def representatives(L):
    ident=bytes(range(125))
    inv={a:bytes(a.index(i)for i in range(125))for a in L}
    involutions=[a for a in L if a!=ident and composition(a,a)==ident]
    remaining={frozenset((ident,a,b,composition(a,b))) for a,b in combinations(involutions,2)
               if composition(a,b)==composition(b,a)}
    assert len(remaining)==25
    groups=[]
    while remaining:
        group=min(remaining,key=lambda h:sorted(h))
        elems=sorted(group-{ident})
        G=[ident,elems[0],elems[1],composition(elems[0],elems[1])]
        orbit={frozenset(composition(t,composition(s,inv[t]))for s in G)for t in L}
        remaining-=orbit
        groups.append((G,len(orbit)))
    return groups

def orbit_permutations(G,L,T):
    index={};history=[]
    for j in range(125):
        if j not in index:
            o=sorted({a[j]for a in G});index.update({x:len(history)for x in o});history.append(o)
    permutations=set()
    for a in L:
        v=bytes(a.index(j)for j in range(125))
        if {composition(a,composition(h,v))for h in G}!=set(G):continue
        for t in T:
            if any(h[t[0]]!=t[0]for h in G):continue
            g=composition(t,a);permutations.add(tuple(index[g[o[0]]]for o in history))
    return sorted(permutations)

def verify(previous,jobs):
    r4=previous/'previous';r3=r4/'previous';r2=r3/'previous'
    os.environ['NATIVE_PROBE_PREVIOUS']=str(r2)
    sys.path[:0]=[str(r4/'eleven_klein'),str(r3/'group'),str(r2/'bounds')]
    from fixed import build
    from generate import maps,observation_file
    from cyclic11 import observations,class_cost
    bad,pair=observations();L,T,_=maps();groups=representatives(L)
    with TemporaryDirectory() as d:
        w=Path(d);observation_file(w/'observations')
        def run(cmd,output=None):
            args=list(map(str,cmd))
            if output is None:
                return subprocess.run(args,text=True,check=True,capture_output=True).stdout
            with output.open('w')as f:
                subprocess.run(args,text=True,check=True,stdout=f,stderr=subprocess.DEVNULL)
        def compile(source,name):
            run(['c++','-O3','-mpopcnt','-std=c++20',source,'-o',w/name])
        def write(name,rows):
            (w/name).write_text(''.join(' '.join(map(str,l))+'\n'for l in rows))
        write('v4all',[[p for h in G for p in h]for G,_ in groups])
        build(w,bad,pair,class_cost)
        source=(r3/'low/class_enumeration.cpp').read_text()
        assert '1230,1350' in source
        (w/'seeds.cpp').write_text(source.replace('1230,1350','1230,1376'))
        source=(r4/'eleven_klein/pairs.cpp').read_text()
        assert 'if(s>=8)'in source and 'if(c<=caps[s])'in source
        (w/'pairs.cpp').write_text(source.replace('if(s>=8)','if(s>0)').replace('if(c<=caps[s])','if(c<=31250)'))
        for f,n in [(w/'seeds.cpp','seed'),(previous/'c4/basis.cpp','basis'),(w/'pairs.cpp','pairs'),(HERE/'four.cpp','four'),(HERE/'search.cpp','search')]:
            compile(f,n)
        run([w/'seed',w/'observations',w/'seeds'])
        run([w/'basis',w/'seeds',w/'basisdata'])
        def solve(i,case):
            G,num=case
            perms=orbit_permutations(G,L,T)
            write('norm'+str(i),perms)
            for h in (1,2,3):run([w/'pairs',w/'observations',w/'v4all',i,h],w/f'pbank{i}.{h}')
            run([w/'four',w/'v4all',w/'basisdata',i],w/f'qbank{i}')
            out=run([w/'search',w,i,CAP])
            r=[]
            for line in out.splitlines():
                if not line[0].isdigit():continue
                _,k,relaxed,rows,nodes,scans,leaves,best=map(int,line.split())
                r.append(dict(quads=k,shape_lower=relaxed,short_rows=rows,visited=nodes,completions=leaves,
                              minimum_if_within_budget=(None if best==CAP+1 else best)))
            return dict(basis_images=[[a[j]for j in (25,5,1)]for a in G[1:]],linear_conjugates=num,
                        normalization_permutations=len(perms),cases=r)
        with ThreadPoolExecutor(max_workers=jobs)as ex:
            data=list(ex.map(lambda arg:solve(*arg),enumerate(groups)))
        assert [min([c['minimum_if_within_budget'] for c in r['cases'] if c['minimum_if_within_budget'] is not None]or [CAP+1])
                for r in data]==[CAP+1,10632,CAP+1,CAP+1,CAP+1,10672,CAP+1]
        assert all((c['minimum_if_within_budget']or CAP+1)>10632 for c in data[1]['cases'][1:])
        frames=[]
        for line in run([w/'search',w,1,10632,'enumerate_fixed_and_paired']).splitlines():
            if not line.startswith('FRAME '):continue
            values=list(map(int,line.split()[1:]));assert values[0]==10632
            frames.append([tuple(values[j:j+3])for j in range(1,len(values),3)])
        eq=classify(groups[1][0],L,T,frames,bad,pair,class_cost)
        assert eq['support_frames']==eq['fixed_subgroup_tables']==8 and eq['types']==[dict(normalizer_orbit=8,stabilizer_order=4,affine_orbit=3000)]
        return dict(labels=12,budget=CAP,minimum=10632,types=data,classification=eq)
if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--previous',type=Path,required=True)
    parser.add_argument('--jobs',type=int,default=2)
    opts=parser.parse_args()
    print(json.dumps(verify(opts.previous.resolve(),opts.jobs),sort_keys=True,indent=2))
