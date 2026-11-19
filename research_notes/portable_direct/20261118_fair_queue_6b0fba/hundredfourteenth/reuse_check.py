"""Public three-channel carrier and exact positive path/frequency calculations."""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import product
import json
from pathlib import Path
import runpy
import sys

TASK = 'research_tasks/RS-EULER-RR-20261012-06.md'
TASK_BLOB = '71d601468572fabcb62603aa85fe85214a059cf8'
ADAPTER = '868595349d4ed76eee8c8cd7376afa43e20e409d99e4c7c648b70fd966884621'
SOURCE = (0,0,0,1,0)


def trajectories(old, x, bits, echo, *, return_cores=False):
    z = x+(0,0)
    labels=[]
    for b in bits:
        start=z
        if b:
            for _ in range(2):
                z=old['primitive'](z,'U1',0)
        for op in ('H03','U2','C'):
            z=old['primitive'](z,op,0)
        labels.append(z[:5] if return_cores else z[0])
        if echo:
            for _ in range(2):
                z=old['primitive'](z,'C',0)
            for loop in ('U2','H03')+(('U1','U1') if b else ()):
                # U_i^{-1}=U_i^3 on the public core, H_{03}^{-1}=H_{03}.
                for _ in range(1 if loop=='H03' else 3):
                    z=old['primitive'](z,loop,0)
            assert z==start
    return tuple(labels)


def signs(labels, initial):
    return tuple(1 if (b-a)%3==1 else -1 for a,b in zip((initial,)+labels,labels))


def seeds(m,n,ring):
    k=min(m,n) if ring else n
    for b in product(range(2),repeat=k):
        yield tuple(b[i%k] for i in range(n))


def clean_counts(old,m,n,ring,echo):
    return Counter(trajectories(old,SOURCE,b,echo) for b in seeds(m,n,ring))


def noisy_counts(clean,q,n):
    states=clean.copy()
    for i in range(n):
        after=Counter()
        for z,w in states.items():
            for d,v in enumerate(q):
                if v:
                    y=z[:i]+((z[i]+d)%3,)+z[i+1:]
                    after[y]+=v*w
        states=after
    return states


def normlaw(law):
    z=sum(law.values())
    return {k:F(v,z) for k,v in law.items()}


def tv(p,q):
    return sum(abs(p.get(x,0)-q.get(x,0)) for x in p.keys()|q.keys())/2


def chi(p,q):
    assert p.keys()<=q.keys()
    return sum((p.get(z,0)-v)**2/v for z,v in q.items())


def transform(law,v):
    coeff=[0,0,0]
    for y,mass in law.items():coeff[sum(a*b for a,b in zip(y,v))%3]+=mass
    return coeff[0]-coeff[2],coeff[1]-coeff[2]


def times(x,y):
    a,b=x;c,d=y
    return (a*c-b*d,a*d+b*c-b*d)


def echo_rows(old,q,m,n):
    p=normlaw(noisy_counts(clean_counts(old,m,n,True,True),q,n))
    fresh=normlaw(noisy_counts(clean_counts(old,m,n,False,True),q,n))
    total=sum(q); levels=Counter(k%m for k in range(n))
    channels=[[F(q[(j-i)%3],total) for j in range(3)] for i in (1,2)]
    nu,mu=channels
    eta=sum((a-b)**2/(2*(a+b)) for a,b in zip(nu,mu) if a+b)
    expected=F(1)
    for count in levels.values():expected*=((1+eta)**count+(1-eta)**count)/2
    assert chi(p,fresh)==expected-1
    if n==m+1:assert tv(p,fresh)==F((max(q)-min(q))**2,2*total**2)
    # Archive the entire small-state positive output for one noisy fixture.
    if q==(4,1,1) and n==m+1 and m<=2:
        return dict(m=m,n=n,chi_square=str(expected-1),tv=str(tv(p,fresh)),
                    ring={' '.join(map(str,k)):str(v) for k,v in sorted(p.items())},
                    fresh={' '.join(map(str,k)):str(v) for k,v in sorted(fresh.items())})
    return None


def main(repo,adapter):
    def blob(b):
        return sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
    assert sha256(adapter.read_bytes()).hexdigest()==ADAPTER
    old=runpy.run_path(str(adapter))
    pins={TASK:TASK_BLOB,**old['PINS']}
    for file,digest in pins.items():assert blob((repo/file).read_bytes())==digest,file
    sys.path.insert(0,str(repo/'src'))
    from enterprise_math import brc_weighted as brc
    cores=0
    for x in product(range(3),range(2),range(8),range(4),range(2)):
        c=signs(trajectories(old,x,(0,0,0),False),x[0])
        for bits in product(range(2),repeat=3):
            got=signs(trajectories(old,x,bits,False),x[0]);par=1
            for d,ci,bi in zip(got,c,bits):
                par*=(-1)**bi
                assert d==ci*par
            trajectories(old,x,bits,True)
            cores+=1
    straight=[]; echoes=[]; tests=0
    for m in range(1,5):
        n=m+1
        base=signs(trajectories(old,SOURCE,(0,)*n,False),SOURCE[0])
        marked=({2} if m==1 else {1,m,n})
        factor=1
        for i in marked:factor*=base[i-1]
        for q in [(1,0,0),(1,1,1),(4,1,1),(4,2,1)]:
            total=sum(q)
            p=normlaw(noisy_counts(clean_counts(old,m,n,True,False),q,n))
            fresh=normlaw(noisy_counts(clean_counts(old,m,n,False,False),q,n))
            diff={y:p.get(y,0)-fresh.get(y,0) for y in p.keys()|fresh.keys()}
            for nn in range(1,m+1):
                assert clean_counts(old,m,nn,True,False)==clean_counts(old,m,nn,False,False)
            if total==3*min(q):
                assert tv(p,fresh)==0
            else:
                assert tv(p,fresh)>0
            qhat={v:transform({(j,):F(x,total) for j,x in enumerate(q)},(v,)) for v in range(3)}
            delta2=(qhat[1][0]**2-qhat[1][0]*qhat[1][1]+qhat[1][1]**2)
            best=0
            for word in product(range(3),repeat=n):
                x,y=transform(diff,word)
                form=(F(factor),F(0)); tail=0
                for j in range(n,0,-1):
                    v=word[j-1]
                    tail=(tail+v)%3
                    g=([(0,0),(F(1,2),1),(F(-1,2),-1)][tail] if j in marked
                       else ((1,0) if tail==0 else (F(-1,2),0)))
                    form=times(times(form,g),qhat[v])
                assert form==(x,y)
                best=max(best,x*x-x*y+y*y)
                tests+=1
            if m>=3:
                assert best==F(27,64)*max(delta2/F(4**(m-2)),delta2**3)
            if q==(4,1,1):
                straight.append(dict(m=m,n=n,first_tv=str(tv(p,fresh)),max_char_gap_squared=str(best),
                    clean_first_tv=str(tv(normlaw(clean_counts(old,m,n,True,False)),
                                           normlaw(clean_counts(old,m,n,False,False)))),
                    ring={''.join(map(str,k)):str(v) for k,v in sorted(p.items())} if m<=2 else None,
                    fresh={''.join(map(str,k)):str(v) for k,v in sorted(fresh.items())} if m<=2 else None))
            saved=echo_rows(old,q,m,n)
            if saved:echoes.append(saved)
            if m<=2:echo_rows(old,q,m,n+2)
    # Real E contacts for every path at m=1,2 rather than direct convolution.
    checks=0
    for m,ring,echo,sheet in product((1,2),(False,True),(False,True),(0,1)):
        n=m+1;q=(4,1,1); acc={};bits_all=list(seeds(m,n,ring))
        for bits in bits_all:
            source=trajectories(old,SOURCE,bits,echo,return_cores=True)
            for shifts in product(range(3),repeat=n):
                mass=brc.CWM_ONE
                for _ in range(min(m,n) if ring else n):
                    mass=brc.cwm_propagate(mass,brc.cwm_edge(F(1,2)))
                answer=[]
                for core,d in zip(source,shifts):
                    mass=brc.cwm_propagate(mass,brc.cwm_edge(F(q[d],sum(q))))
                    z=core+(0,d)
                    for op in old['instructions'](z,'E',sheet):
                        z=old['primitive'](z,op,sheet)
                        mass=brc.cwm_propagate(mass,brc.CWM_ONE)
                    answer.append(z[-1])
                key=tuple(answer)
                acc[key]=brc.cwm_recoalesce(acc.get(key,brc.CWM_ZERO),mass)
                checks+=1
        target=normlaw(noisy_counts(clean_counts(old,m,n,ring,echo),q,n))
        assert {x:z.total for x,z in acc.items()}==target
    return dict(task='RS-EULER-RR-20261012-06',public_blobs=pins,public_adapter_sha256=ADAPTER,
                exact_source_words_all_384_initial_cores=cores,exact_base_field_character_comparisons=tests,
                complete_positive_recorded_paths_both_receiver_sheets=checks,
                calibration_noise_in_saved_tables='(4,1,1)/6',straight=straight,
                controlled_replay=echoes)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path.cwd())
    parser.add_argument('--adapter',type=Path,default=Path(__file__).resolve().parent.parent/'hundredninth'/'feedback_check.py')
    args=parser.parse_args()
    print(json.dumps(main(args.repo,args.adapter),sort_keys=True,indent=2))
