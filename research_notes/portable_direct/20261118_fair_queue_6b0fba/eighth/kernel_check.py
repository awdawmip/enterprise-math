"""Exact endpoint-identification replay in the positive Weighted-BRC path algebra."""
import argparse
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import comb, isqrt, lcm
from pathlib import Path
import json
import sys

ANCHOR=12
BRC_SHA="4f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f"


def chart(j):
    v=[0]*6
    if j!=ANCHOR:
        v[j//2]=1
        if j%2: v[(j//2+1)%6]=1
    return tuple(v)


def edge(j,branch):
    if j==ANCHOR or branch=='reset': return ANCHOR
    return (j+{'forward':1,'backward':-1,'stay':0}[branch])%12


class Replay:
    def __init__(self,brc):
        self.brc=brc
        self.work=Counter()

    def trace(self,params,seed,depth):
        a,b,d=params
        ws={'forward':a,'backward':b,'stay':1-a-b-d,'reset':d}
        assert min(ws.values())>=0
        choices=[(label,self.brc.cwm_edge(weight)) for label,weight in ws.items() if weight]
        state={seed:self.brc.CWM_ONE}
        result=[state]
        for _ in range(depth):
            out={}
            for j,record in state.items():
                for label,weight in choices:
                    k=edge(j,label)
                    contrib=self.brc.cwm_propagate(record,weight)
                    out[k]=self.brc.cwm_recoalesce(out.get(k,self.brc.CWM_ZERO),contrib)
                    self.work['path_extension_and_merge']+=1
            assert sum(z.total for z in out.values())==1
            state=out;result.append(state)
        return result

    def marginal(self,state,axes=(0,)):
        out={}
        for j,record in state.items():
            key=tuple(chart(j)[a] for a in axes)
            out[key]=self.brc.cwm_recoalesce(out.get(key,self.brc.CWM_ZERO),record)
            self.work['readout_merge']+=1
        return {k:v.total for k,v in out.items()}

    def data(self,params,seed,h):
        return tuple(self.marginal(z).get((1,),F()) for z in self.trace(params,seed,h))

    def word_check(self,params,seed):
        a,b,d=params
        w={'forward':a,'backward':b,'stay':1-a-b-d,'reset':d}
        aggregate=self.trace(params,seed,3)[-1]; direct={}
        for word in product(w,repeat=3):
            j=seed; atom=self.brc.CWM_ONE
            for letter in word:
                atom=self.brc.cwm_propagate(atom,self.brc.cwm_edge(w[letter]));j=edge(j,letter)
            direct[j]=self.brc.cwm_recoalesce(direct.get(j,self.brc.CWM_ZERO),atom)
        assert direct==aggregate


def rsqrt(x):
    a,b=isqrt(x.numerator),isqrt(x.denominator)
    if F(a,b)**2!=x: raise ValueError("square root is not rational")
    return F(a,b)


def unordered(s):
    _,t,s2,s3=s
    q=t*t-s2
    z=6*t*q-2*(t**3-s3)
    # A rational root of D u^3+(3Dq)u-Dz has denominator dividing D.
    D=lcm((3*q).denominator,z.denominator)
    lo,hi=0,D
    while lo<hi:
        mid=(lo+hi)//2;v=F(mid,D)
        if v**3+3*q*v < z:lo=mid+1
        else:hi=mid
    u=F(lo,D)
    if u**3+3*q*u!=z:raise ValueError("outside the rational kernel image")
    gap=rsqrt(2*q-u*u)
    return (u+gap)/2,(u-gap)/2,1-t


def three(s1,s2,z1):
    return s1-z1,rsqrt(2*s1*z1-z1*z1-s2),1-s1


def strings(params):
    return list(map(str,params))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--json',type=Path)
    args=ap.parse_args()
    assert sha256((args.repo/'src/enterprise_math/brc_weighted.py').read_bytes()).hexdigest()==BRC_SHA
    sys.path.insert(0,str(args.repo/'src'))
    from enterprise_math import brc_weighted
    R=Replay(brc_weighted)
    assert len(set(map(chart,range(13))))==13
    assert {r for r in range(13) if chart(r)[0]}=={0,1,11}
    assert all(sum(abs(a-b) for a,b in zip(chart(j),chart(edge(j,'forward'))))==1 for j in range(12))
    grid=[];coll={}
    for ia,ib,id_ in product(range(5),repeat=3):
        if ia+ib+id_>4:continue
        pars=a,b,d=tuple(F(x,4) for x in (ia,ib,id_))
        out=R.trace(pars,0,3)
        s=tuple(R.marginal(z).get((1,),F()) for z in out)
        z1=R.data(pars,1,1)[1]
        assert unordered(s)==(max(a,b),min(a,b),d)
        assert three(s[1],s[2],z1)==pars
        joint=R.marginal(out[1],(0,1,5))
        assert joint.get((1,1,0),0)==a and joint.get((1,0,1),0)==b and joint.get((0,0,0),0)==d
        coll.setdefault(s,[]).append(pars)
        grid.append([strings(pars),strings(s),str(z1)])
    assert all(len(bag)==(1 if bag[0][0]==bag[0][1] else 2) for bag in coll.values())
    a,b,d=F(1,4),F(1,8),F(1,8)
    R.word_check((a,b,d),0)
    rows=[]
    for j in range(13):
        p=R.data((a,b,d),j,6);r=R.data((b,a,d),j,6)
        actual=next((t for t,(x,y) in enumerate(zip(p,r)) if x!=y),None)
        m=min(j,12-j)
        expected=None if j in (0,6,ANCHOR) else max(1,m-1)
        assert actual==expected
        rows.append([j,actual,strings(p),strings(r)])
    drops=[((F(1,8),F(1,4),F(1,8)),(F(1,4),F(1,8),F(1,8)),2),
           ((F(1,8),F(1,4),F(1,8)),(F(1,8),F(1,8),F(1,8)),1),
           ((F(1,8),F(0),F(3,8)),(F(3,16),F(1,4),F(5,16)),0)]
    for P,Q,i in drops:
        def feat(params):
            _,p1,p2=R.data(params,0,2)
            return (p1,p2,R.data(params,1,1)[1])
        v,w=feat(P),feat(Q)
        assert [j for j in range(3) if v[j]!=w[j]]==[i]
    noise=[]
    for e in (F(1,16),F(1,32),F(1,64)):
        t=F(1,2);P=(5*e,F(),1-t);Q=(4*e,3*e,1-t)
        x,y=R.data(P,0,14),R.data(Q,0,14)
        assert x[:3]==y[:3] and abs(x[3]-y[3])==184*e**3
        assert all(abs(x[n]-y[n])<=comb(n,3)*(7*e)**3*t**(n-3) for n in range(3,15))
        for j in (0,1):
            v=R.data((F(),F(),1-t),j,14);w=R.data((F(),e,1-t),j,14)
            assert all(abs(v[n]-w[n])<=comb(n,2)*e**2*t**(n-2) for n in range(2,15))
            if j==0:assert abs(v[2]-w[2])==e**2
        noise.append([str(e),strings(x),strings(y)])
    res=dict(brc_sha256=BRC_SHA,coordinates=[chart(j) for j in range(13)],
             grid_columns=['a,b,d','r0:x1 success at n=0..3','r1:x1 success at n=1'],grid=grid,
             grid_fibres=len(coll),swap_parameters=strings((a,b,d)),swap_rows=rows,
             single_seed_noise_probes=noise,work=dict(R.work))
    output=json.dumps(res,ensure_ascii=True,separators=(',',':'))+'\n'
    if args.json:args.json.write_text(output)
    print('grid',len(grid),'fibres',len(coll),'first swaps',[row[1] for row in rows],
          'work',R.work,'json_sha256',sha256(output.encode()).hexdigest())


if __name__=='__main__':main()
