"""Rebuild involution orbits and verify the twelve-label read threshold."""
import argparse
from collections import Counter
from functools import cache
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory

HERE=Path(__file__).resolve().parent
BUDGET=9996
IMP=1000000
GENERAL=(0,0,12,36,72,120,201,292,419,557,744,936,1104,1296)

def actions(linear):
    identity=bytes(range(125))
    def comp(a,b):return bytes(a[x] for x in b)
    inv={a:bytes(a.index(i) for i in identity) for a in linear}
    rest={g for g in linear if g!=identity and comp(g,g)==identity}
    output=[]
    while rest:
        g=min(rest)
        conjugates={comp(l,comp(g,inv[l])) for l in linear}
        rest-=conjugates
        output.append((g,len(conjugates),[h for h in linear if comp(g,h)==comp(h,g)]))
    return output

def basic_bounds(fixed,pair,fix,budget=BUDGET):
    @cache
    def low(n,h,f,b):
        if min(n,h,f,b)<0 or h>n or n>13*(f+2*b):return IMP
        if f:return min(c+low(n-s,h-d,f-1,b) for (s,d),c in fixed.items())
        if b:return min(2*c+low(n-2*s,h,0,b-1) for s,c in pair.items())
        return 0 if n==h==0 else IMP
    values=[]
    ceilings=[0]*14
    for b in range(7):
        f=12-2*b
        root=low(125,fix,f,b)
        values.append(root if root<IMP else None)
        if b and root<=budget:
            for s,c in pair.items():
                mx=(budget-low(125-2*s,fix,f,b-1))//2
                if mx>=c:ceilings[s]=max(ceilings[s],mx)
    return values,ceilings

def profiles(fixed,pair,b):
    types=[(1,s,h,c) for (s,h),c in sorted(fixed.items())]
    types.extend((2,s,0,2*c) for s,c in sorted(pair.items()))
    @cache
    def low(j,n,h,f,b):
        if min(n,h,f,b)<0 or n>13*(f+2*b) or h>n:return IMP
        if j==len(types):return 0 if (n,h,f,b)==(0,0,0,0) else IMP
        r,s,d,c=types[j]
        return min(low(j+1,n,h,f,b),c+low(j,n-r*s,h-d,f-(r==1),b-(r==2)))
    def generate(j,n,h,f,b,left):
        if low(j,n,h,f,b)>left:return
        if not f+b:
            yield []
            return
        r,s,d,c=types[j]
        yield from generate(j+1,n,h,f,b,left)
        for indices in generate(j,n-r*s,h-d,f-(r==1),b-(r==2),left-c):
            yield [100*r+s]+indices
    return list(generate(0,125,1,12-2*b,b,BUDGET))

def replay(root,complete,work):
    sys.path[:0]=[str(root/'group'),str(root/'previous'/'bounds')]
    from generate import maps
    from prior_bounds import observation_file
    linear,_,_=maps()
    def run(*args):return subprocess.run(list(map(str,args)),text=True,check=True,capture_output=True)
    def lines(src):return [list(map(int,l.split())) for l in src.splitlines()]
    for name in ['fixed','axis_min','seeds','cover','bank','sig','geom','fastgeo']:
        run('c++','-O3','-std=c++20','-mpopcnt',HERE/(name+'.cpp'),'-o',work/name)
    observation_file(work/'obs')
    native=lines(run(work/'seeds',work/'obs',work/'cheap').stdout)
    assert all(row[2]==GENERAL[row[0]] for row in native)
    assert [row[0] for row in native]==list(range(2,14))
    (work/'linear').write_text(''.join(' '.join(map(str,l))+'\n' for l in linear))
    result={}
    for i,(g,conjugates,cent) in enumerate(actions(linear)):
        gx=work/'map'
        gx.write_text(''.join(' '.join(map(str,l))+'\n' for l in [g]+cent))
        fixrows=work/'fx';pairs=work/'pairs'
        data=lines(run(work/'fixed',work/'obs',fixrows,gx).stdout)
        fixed={(s,h):c for s,h,n,c in data}
        pair=dict(enumerate(GENERAL));del pair[0]
        if i==0:
            special=lines(run(work/'axis_min',work/'obs',work/'axis_seeds').stdout)
            pair={s:c for s,c,n in special[1:]}
        nfix=sum(t==p for p,t in enumerate(g))
        bounds,caps=basic_bounds(fixed,pair,nfix)
        result[i]={'linear_conjugates':conjugates,'basis_images':[g[x] for x in (25,5,1)],
                   'fixed_histories':nfix,'shape_bounds_by_pair_count':bounds}
        if i==3:
            with fixrows.open() as rows:
                costs=[int(line.split()[2]) for line in rows]
            assert len(costs)==27487 and all(c%2==0 for c in costs)
            result[i]['fixed_classes_with_even_cost']=len(costs)
        if all(v is None or v>BUDGET for v in bounds):continue
        assert all(c<=v for c,v in zip(caps,[0]*8+[476,656,836,1023,1203,1383]))
        capfile=work/'caps'
        capfile.write_text(' '.join(map(str,caps))+'\n')
        run(work/'bank',work/'linear',work/'cheap',gx,pairs,capfile)
        result[i]['paired_class_cost_ceilings']={s:c for s,c in enumerate(caps) if c}
        if i in [0,1]:
            cover_budget=BUDGET+1
            new_bounds,new_caps=basic_bounds(fixed,pair,nfix,cover_budget)
            assert new_bounds==bounds and new_caps==caps
            result[i]['cover_budget']=cover_budget
            branches={}
            for b,v in enumerate(bounds):
                if v is None or v>cover_budget:continue
                proc=run(work/'cover',gx,fixrows,pairs,b,cover_budget,work/'w',0,100000)
                rows=lines(proc.stdout)
                assert rows and all(row[0]==j and row[1:3]==[cover_budget,0] for j,row in enumerate(rows))
                assert not (work/'w').stat().st_size
                branches[b]=len(rows)
            result[i]['emptied_anchor_counts']=branches
        elif i==3:
            sig=work/'signatures'
            sig.write_text(run(work/'sig',gx,fixrows,pairs).stdout)
            branches={}
            for b in range(6 if complete else 5):
                shapes=profiles(fixed,pair,b)
                pf=work/'profiles';pm=work/'geometry';w=work/'w'
                pf.write_text(''.join(' '.join(map(str,[len(z)]+z))+'\n' for z in shapes))
                gl=lines(run(work/'geom',sig,pf,HERE/f'geo{b}',pm,BUDGET).stdout)
                assert len(gl)==len(shapes) and all(row[0]==k for k,row in enumerate(gl))
                total=sum(row[2] for row in gl)
                if total:
                    with (work/'coverlog').open('w') as f:
                        subprocess.run(list(map(str,[work/'fastgeo',gx,fixrows,pairs,pm,BUDGET,w,0,total,sig])),stdout=f,check=True)
                    with (work/'coverlog').open() as f:
                        n=0
                        for n,line in enumerate(f,1):
                            j,rem,won,nodes,lookups=map(int,line.split())
                            assert (j,rem,won)==(n-1,BUDGET,0)
                        assert n==total
                    assert not w.stat().st_size
                branches[b]={'size_profiles':len(shapes),'geometric_profiles':total}
            result[i]['empty_branches']=branches
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--last',type=Path,required=True,help='Round-three evidence directory containing group/ and previous/.')
    ap.add_argument('--through-four-pairs',action='store_true',help='shorter central-reflection check, omitting five pairs')
    ap.add_argument('--work',type=Path,help='optional persistent empty working folder')
    args=ap.parse_args()
    with TemporaryDirectory() as tmp:
        work=args.work or Path(tmp);work.mkdir(parents=True,exist_ok=True)
        print(json.dumps(replay(args.last.resolve(),not args.through_four_pairs,work.resolve()),ensure_ascii=False,sort_keys=True,indent=2))
