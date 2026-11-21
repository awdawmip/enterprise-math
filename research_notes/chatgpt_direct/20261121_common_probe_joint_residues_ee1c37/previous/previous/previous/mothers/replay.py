"""Rebuild the coverage curve, exceptional-label exclusions and read lower bound."""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse,json,subprocess,sys
from costs import check as check_costs

HERE=Path(__file__).resolve().parent
def readints(path):
    return tuple(map(int,path.read_text().strip().split()))

def run(previous):
    native=previous/'previous/previous/previous/bounds'
    sys.path[:0]=[str(native),str(previous/'parents')]
    from geometry import linear_actions,inventory
    from cyclic11 import observations,class_cost
    from prior_bounds import observation_file,expand,symmetries
    from pairtypes import build
    bad,menus=observations()
    parents,centers=inventory(linear_actions(),bad,menus)
    ranks={}
    for j,remaining in build(parents,centers):
        for i in remaining:ranks[i]=j
    assert len(ranks)==249
    bank=''.join(f'{m%(1<<64)} {m>>64}\n' for m in parents)
    bank+=' '.join(str(ranks[i]) for i in range(1,250))+'\n'
    expected=HERE/'result.json'
    with TemporaryDirectory() as folder:
        tmp=Path(folder)
        (tmp/'parents').write_text(bank)
        for name in ('union','census','embed','color','three','five','ten'):
            subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/(name+'.cpp'),'-o',tmp/name],check=True)
        def call(parts,inp=None):
            return subprocess.check_output([str(x) for x in parts],text=True,input=inp)
        observation_file(tmp/'observations')
        call([tmp/'census',tmp/'observations',tmp/'seeds'])
        embed=call([tmp/'embed',tmp/'parents',tmp/'seeds'])
        minima={}
        for line in embed.splitlines():
            s,v,j=map(int,line.split())
            key=s,s==j
            minima[key]=min(minima.get(key,10**8),v)
        assert sorted((s,b,v) for (s,b),v in minima.items())==[
            (8,False,419),(8,True,460),(9,False,557),(9,True,608),
            (10,False,744),(10,True,768),(11,False,1008),(11,True,936),
            (12,False,1244),(12,True,1104),(13,True,1296)]
        A,T=symmetries();seeds=defaultdict(list);large=set()
        for line in (tmp/'seeds').open():
            s,c,*row=map(int,line.split())
            if not(s==10 and c<=787 or s==11 and c<=1051 or s==12):continue
            mask=sum(1<<i for i in row)
            if any(mask&p==mask for p in parents):
                if s==12:large.add(c)
                continue
            seeds[s,c].append(row)
        assert large=={1104,1116}
        for key,rows in seeds.items():
            family=expand(rows,A,T)
            f=tmp/('rows%d_%d'%key)
            f.write_text(''.join(f'{mask%(1<<64)} {mask>>64}\n'for mask in sorted(family)))
        def setfiles(size):
            return [tmp/('rows%d_%d'%k) for k in sorted(seeds) if k[0]==size]
        curve={};curve_checks={}
        for k,maximum in [(6,78),(7,85),(8,96),(9,102),(10,112),(11,119),(12,121)]:
            witness=call([tmp/'union',k,maximum,-1],bank).splitlines()
            indices=list(map(int,witness[0].split()))
            mask=0
            for i in indices:mask|=parents[i]
            assert len(set(indices))==k and mask.bit_count()==maximum
            if k>6:
                upper=list(map(int,call([tmp/'union',k,maximum+1,-1],bank).split()))
                assert upper[:3]==[k,maximum+1,0]
                curve_checks[str(k)]=sum(upper[3:])
            curve[str(k)]=maximum
        w=json.loads((HERE/'twelve.json').read_text());rows=w['rows']
        assert sorted(sum(rows,[]))==list(range(125)) and len(rows)==12
        assert all(all(parents[i]>>x&1 for x in row)for i,row in zip(w['parents'],rows))
        last=sum(1<<x for x in rows[-1])
        assert len(rows[-1])==6 and not any(last&p==last for p in parents)
        assert all(not(bad[a][b]>>c&1)for r in rows for a,b,c in combinations(r,3))
        witness_cost=sum(class_cost(r,menus)for r in rows)
        def families(k,m):
            file=tmp/f'family{k}_{m}'
            with file.open('w')as ff:subprocess.run([tmp/'union',str(k),str(m),'-1','all'],text=True,input=bank,stdout=ff,check=True)
            return file
        def color(k,c,m):
            rows=call([tmp/'color',k,c,tmp/'observations',tmp/'parents',families(k,m)])
            answer=list(map(int,rows.split()));assert len(answer)==2
            return answer
        exclusions={'9,2':color(9,2,101),'8,3,small':color(8,3,92),'7,4':color(7,4,84)}
        text=call([tmp/'three',tmp/'observations',tmp/'parents',families(8,89),*setfiles(12)])
        data=list(map(int,text.split()));assert len(data)==6 and data[-1]==0
        exclusions['8,3,large']=data
        with (tmp/'residuals').open('w')as ff:
            p=subprocess.run([tmp/'five',tmp/'parents',families(6,74),*setfiles(11)],stdout=ff,stderr=subprocess.PIPE,check=True,text=True)
        exclusions['six_parent_hall']=list(map(int,p.stderr.split()))
        q=subprocess.run([tmp/'ten',tmp/'residuals','4',*setfiles(10)],capture_output=True,check=True,text=True)
        assert not q.stdout
        exclusions['four_ten_rows']=list(map(int,q.stderr.split()))
        assert exclusions['four_ten_rows'][1]==0
        out={'curve':curve,'curve_upper_search_visits':curve_checks,'exclusions':exclusions,
             'one_exception_twelve':{'size':6,'reads':witness_cost},'cost':check_costs(minima)}
        if expected.exists():assert out==json.loads(expected.read_text())
        return out
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--previous',type=Path,required=True,help='Full extracted previous release with its previous/ dependency tree')
    print(json.dumps(run(p.parse_args().previous.resolve()),sort_keys=True,indent=2))
