"""Certify R_11 >= 11328 under the single-axis reflection, using native menus."""
from argparse import ArgumentParser
from collections import Counter
from functools import cache
from itertools import combinations_with_replacement
from pathlib import Path
from tempfile import TemporaryDirectory
import json,subprocess,sys
HERE=Path(__file__).resolve().parent
CAP=11327
def run(older):
    sys.path.insert(0,str(older/'bounds'))
    from prior_bounds import observation_file
    def proc(cmd,cwd):return subprocess.run(list(map(str,cmd)),cwd=cwd,text=True,capture_output=True,check=True)
    with TemporaryDirectory()as tmp:
        w=Path(tmp);observation_file(w/'menus')
        for name in ['fixed','paired','five','seven']:
            proc(['c++','-O3','-std=c++20','-mpopcnt',HERE/(name+'.cpp'),'-o',w/name],w)
        fix=proc([w/'fixed',w/'menus',w/'fixed.rows'],w)
        fixed={(s,h):(n,c)for s,h,n,c in (map(int,l.split())for l in fix.stdout.splitlines())}
        expected_fixed=sum(n for n,c in fixed.values())+1
        assert int(fix.stderr)==expected_fixed==1442676
        pair=proc([w/'paired',w/'menus',w/'paired.rows'],w)
        pairmeta=[list(map(int,l.split()))for l in pair.stdout.splitlines()]
        assert pairmeta[0][0]==sum(v[2]for v in pairmeta[1:])==7852445
        prices={s:c for s,c,n in pairmeta[1:]}
        assert max(prices)==11
        @cache
        def lower(f,b,n,p):
            if min(f,b,n,p)<0 or n>13*f+22*b or p>10*f:return 10**8
            if f==b==0:return 0 if n==p==0 else 10**8
            if f:return min(c+lower(f-1,b,n-s,p-h) for (s,h),(_,c)in fixed.items())
            return min(2*c+lower(0,b-1,n-2*s,p) for s,c in prices.items())
        possible=[f for f in [1,3,5,7,9,11]if lower(f,(11-f)//2,125,25)<=CAP]
        assert possible==[5,7]
        caps={}
        for f in possible:
            b=(11-f)//2
            left={(s,h):CAP-lower(f-1,b,125-s,25-h) for (s,h),(_,c) in fixed.items()
                  if c+lower(f-1,b,125-s,25-h)<=CAP}
            right={s:(CAP-lower(f,b-1,125-2*s,25))//2 for s,c in prices.items()
                   if 2*c+lower(f,b-1,125-2*s,25)<=CAP}
            caps[f]=(left,right)
        assert caps[5]==({(9,5):719,(11,5):1165,(13,5):1501},{8:503,9:671,10:894,11:1062})
        assert caps[7]==({(8,0):671,(9,1):863,(10,2):1031,(11,3):1199,(12,4):1367,(13,5):1535},{11:1091})
        seedlines=[l.split()for l in (w/'paired.rows').read_text().splitlines()]
        (w/'root11rows').write_text(''.join(' '.join(l[1:])+'\n' for l in seedlines if int(l[0])==11))
        proc([sys.executable,'-B',HERE/'expand.py'],w)
        five=proc([w/'five',w/'fixed.rows',w/'paired.rows'],w)
        seven=proc([w/'seven',w/'fixed.rows',w/'all11',w/'first11'],w)
        assert 'HIT' not in five.stderr and 'hit' not in seven.stderr
        assert not (w/'reflection_winner.txt').exists() and not (w/'k7winner.txt').exists()
        f5=[list(map(int,l.split()))for l in five.stdout.splitlines()]
        f7=[list(map(int,l.split()))for l in seven.stdout.splitlines()]
        fst=[]
        for ff in combinations_with_replacement(sorted(caps[5][0]),5):
            for pp in combinations_with_replacement(sorted(caps[5][1]),3):
                total=sum(s for s,h in ff)+2*sum(pp)
                minimum=sum(fixed[a][1]for a in ff)+2*sum(prices[s]for s in pp)
                if total==125 and minimum<=CAP:fst.append((ff,pp))
        assert len(f5)==len(fst)==9 and len(f7)==2
        assert all(a[-1]==0 for a in f5+f7)
        return {'budget':CAP,'minimum_at_least':CAP+1,'fixed_class_nodes':expected_fixed,
                'pair_seed_nodes':pairmeta[0][0],'pair_minima':pairmeta[1:],
                'fixed_counts_possible':possible,'five_fixed_shape_profiles':len(fst),
                'five_skeletons':[r[1]for r in f5],'seven_anchors_and_nodes':[r[1:3]for r in f7],
                'seven_pool_counts':list(map(int,seven.stderr.split())),'feasible':False}
if __name__=='__main__':
    parser=ArgumentParser();parser.add_argument('--older',type=Path,required=True)
    a=parser.parse_args();print(json.dumps(run(a.older.resolve()),sort_keys=True,indent=2))
