"""Recreate cheap one-read classes and all prime-order symmetries of the native cost model."""
from collections import defaultdict
from functools import cache
from itertools import permutations,product
from pathlib import Path
import json,os,subprocess,sys,tempfile

HERE=Path(__file__).resolve().parent
BASE=Path(os.environ.get('NATIVE_PROBE_PREVIOUS',str(HERE.parent/'previous')))
if not BASE.is_dir():
    BASE=next((p/'round2/delivery' for p in HERE.parents if (p/'round2/delivery/curve').is_dir()),BASE)
sys.path.insert(0,str(BASE/'curve'))
sys.path.insert(0,str(BASE/'bounds'))
from verify import lower, MINIMA
from prior_bounds import observation_file

def maps():
    points=list(product(range(5),repeat=3))
    def ix(p):return 25*(p[0]%5)+5*(p[1]%5)+p[2]%5
    lin=[bytes(ix([c*s[i]*p[pm[i]] for i in range(3)])for p in points)
         for c,pm,s in product([1,2],permutations(range(3)),product([1,-1],repeat=3))]
    trans=[bytes(ix(tuple(x+y for x,y in zip(p,v)))for p in points) for v in points]
    def comp(f,g):return bytes(f[i]for i in g)
    def inverse(f):return bytes(f.index(i)for i in range(125))
    eye=bytes(range(125));group={comp(t,a) for t in trans for a in lin}
    assert len(group)==12000
    inv={a:inverse(a)for a in lin}
    buckets=[]
    for prime in (2,3,5):
        canon={}
        for f in lin+trans[1:]:
            powers=[f]
            while powers[-1]!=eye:powers.append(comp(f,powers[-1]))
            if len(powers)!=prime:continue
            options={comp(a,comp(g,inv[a]))for a in lin for g in powers[:-1]}
            r=min(options);canon[r]=len(options)
        for r,l in sorted(canon.items()):buckets.append((prime,r,l))
    return lin,trans,buckets

def bank(work,lin,trans,upper):
    observation_file(work/'observations')
    exe=work/'enum'
    subprocess.run(['c++','-O3','-std=c++17','-mpopcnt',str(BASE/'curve/class_minima.cpp'),'-o',str(exe)],check=True)
    subprocess.run([str(exe),str(work/'observations'),str(work/'seeds')],stdout=subprocess.DEVNULL,check=True)
    seeds=defaultdict(set)
    limits={9:587,10:780,11:965,12:1140,13:1350}
    assert all(MINIMA[s]+lower(125-s,12)>upper for s in range(1,9))
    assert all(limits[s]+1+lower(125-s,12)>upper for s in limits)
    for line in (work/'seeds').read_text().splitlines():
        s,c,*row=map(int,line.split())
        if s in limits and c+lower(125-s,12)<=upper:seeds[s,c].add(tuple(row))
    shift=[[1<<i for i in t]for t in trans]
    out={}
    for key,rows in sorted(seeds.items()):
        rots={tuple(sorted(a[i]for i in row))for a in lin for row in rows}
        out[key]=sorted({sum(t[i]for i in r)for t in shift for r in rots})
    return out

def profiles(types,upper):
    @cache
    def dp(n,k,first,budget):
        if not k:return [()] if n==0 else []
        out=[]
        for j in range(first,len(types)):
            s,c=types[j]
            if s>n or c+lower(n-s,k-1)>budget:continue
            out.extend((j,)+tail for tail in dp(n-s,k-1,j,budget-c))
        return out
    rows=dp(125,13,0,upper)
    return sorted((sum(types[i][1]for i in row),[row.count(i)for i in range(len(types))])for row in rows)

def main(work):
    lin,trans,gs=maps()
    rows=bank(work,lin,trans,8728)
    types=list(rows)
    (work/'bank').write_text(str(len(types))+'\n'+''.join(f'{s} {c} {len(arr)}\n'+''.join(f'{m%(1<<64)} {m>>64}\n'for m in arr)for(s,c),arr in rows.items()))
    ps=profiles(types,8728)
    (work/'profiles').write_text(''.join(' '.join(map(str,[c,*cnt]))+'\n'for c,cnt in ps))
    (work/'maps').write_text(''.join(' '.join(map(str,[p,*r]))+'\n'for p,r,_ in gs))
    print([(p,sum(i==v for i,v in enumerate(r)),l)for p,r,l in gs],len(ps),flush=True)
if __name__=='__main__':
    main(Path(sys.argv[1]))
