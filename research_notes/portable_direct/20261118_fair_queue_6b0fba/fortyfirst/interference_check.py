"""Exact integer checks for the frozen three-port signed-CWM bridge. Python 3.10+."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import importlib.util
from itertools import combinations, product
import json
from math import gcd, isqrt
from pathlib import Path

PINS={
    "REPORT.zh-CN.md":"08dd1b08a05d6991d3051cabc3f80071d61d97fa9be7b32449ce9fb5fca491e3",
    "THEOREMS.md":"58e24ea97366716c4155f513539306c8695206a49d720e8820b8ac632c01e204",
    "SUMMARY.json":"779bb73f6d69cfe705d69c9c350003d792fd5e9ca2f73773f8c3af9a1be1bea2",
    "MANIFEST.json":"d0a9c959957a1ada95fe09de15e608a9c41a25aab62973b42ad36872381bcd03",
    "SOURCE_BINDINGS.json":"b3df98d16c57d70544205ac7a1f5dbd8d0f23ab88f2a3c7c936e95347b3042e3",
    "run.py":"7765142879b0798998fbe3253da4fc751a0162d9b81206b4a584d0c0e336889b",
    "collision.py":"5ccfde3031cdc0c6c73690d55d6527605769fb1850c7a63900348992bbde1cd2",
}
PORTS=range(3)
def coef(p,j):
    return -1 if p==j else 2

def packed(mapping):
    return sorted([*key,value] for key,value in mapping.items() if value)

def digest(mapping):
    return sha256(json.dumps(packed(mapping),separators=(',',':')).encode()).hexdigest()

def bind(root):
    pins={**PINS,**json.loads((root/'SOURCE_BINDINGS.json').read_text())['files']}
    parent_manifest='inherited/MANIFEST.json'
    if not (root/parent_manifest).exists():
        del pins[parent_manifest]  # The primary archive intentionally references this parent-only item.
    for name,code in pins.items():
        assert sha256((root/name).read_bytes()).hexdigest()==code, name
    manifest=json.loads((root/'MANIFEST.json').read_text())
    source_checks=0
    for row in manifest['files']:
        data=(root/row['path']).read_bytes()
        assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256']
        source_checks+=1
    s=importlib.util.spec_from_file_location('frozen_record',root/'run.py')
    src=importlib.util.module_from_spec(s)
    s.loader.exec_module(src)
    return src,{'registered_hashes':len(PINS),'inherited_hashes':len(pins)-len(PINS),'manifest_entries':source_checks,'parent_manifest_in_primary':(root/parent_manifest).exists()}

class Ops:
    def __init__(self,n,horizon,src=None,a=2):
        self.n=n
        self.actual=src.old.Arithmetic(limit=2500000) if src else None
        self.count=Counter()
        # Identical scalar inputs are memoized only on the instrumented source run.
        if src:
            self.add0=lru_cache(None)(self.actual.add)
            self.mul0=lru_cache(None)(self.actual.mul)
            assert a==2
            self.work=src.old.Modular(self.actual,n,horizon)
            self.f,self.inv=self.work.f,self.work.fi
        else:
            self.f=[a%n]
            self.inv=[pow(a,-1,n)]
            for _ in range(1,horizon):
                self.f.append(self.f[-1]**2%n)
                self.inv.append(self.inv[-1]**2%n)
    def add(self,a,b):
        return self.add0(a,b) if self.actual else a+b
    def mul(self,a,b):
        return self.mul0(a,b) if self.actual else a*b
    @lru_cache(None)
    def wp(self,w,u):
        return self.work.mul(w,u) if self.actual else w*u%self.n
    @lru_cache(None)
    def step(self,t,x,h,p):
        if self.actual:
            z=self.actual.walk.address((x,h,t-x-h,0,0,0),p,1)
            assert z[2]==t+1-z[0]-z[1] and z[3:]==(0,0,0)
            return z[:2]
        return x+(p==0),h+(p==1)
    def stats(self):
        return self.actual.stats() if self.actual else {}

def wave_update(state,t,o):
    out={}
    for (x,h,p,w),value in state.items():
        for r in PORTS:
            nx,nh=o.step(t,x,h,r)
            nw=o.wp(w,o.f[t]) if r==1 else w
            key=(nx,nh,r,nw)
            out[key]=o.add(out.get(key,0),o.mul(value,coef(r,p)))
    return {k:v for k,v in out.items() if v}

def wave_hist(st,o):
    out={}
    for (x,h,p,_),v in st.items():
        key=(x,h,p)
        out[key]=o.add(out.get(key,0),o.mul(v,v))
    return out

def fresh_update(state,t,o):
    out={}
    for (h,x,y,p,j),v in state.items():
        for r,s in ((0,0),(0,2),(2,0),(2,2),(1,1)):
            nx,nh=o.step(t,x,h,r)
            ny,mh=o.step(t,y,h,s)
            assert nh==mh
            key=(nh,nx,ny,r,s)
            k=o.mul(coef(r,p),coef(s,j))
            out[key]=o.add(out.get(key,0),o.mul(v,k))
    return {k:v for k,v in out.items() if v}

def fresh_hist(st):
    return {(x,h,p):v for (h,x,y,p,s),v in st.items() if p==s and x==y}

def diagnostics(whole,fresh,t):
    delta={k:whole.get(k,0)-fresh.get(k,0) for k in set(whole)|set(fresh)}
    assert sum(delta.values())==0 and sum(fresh.values())==sum(whole.values())==9**t
    assert all(v%(64 if t-x-h else 32)==0 for (x,h,p),v in delta.items())
    return delta

def describe(delta,t):
    return {'Q':9**t,'l1_numerator':sum(map(abs,delta.values())),
            'nonzero_full_keys':sum(v!=0 for v in delta.values()),'signed_delta_sha256':digest(delta),
            'event_z2_zero':sum(v for (x,h,p),v in delta.items() if x+h==t),
            'event_port1':sum(v for (x,h,p),v in delta.items() if p==1)}

def exact_sequence(n,ts,source=None,a=2,reference=None):
    T=max(ts)
    o=Ops(n,T,source,a)
    wave={(0,0,0,1):1}
    fresh={(0,0,0,0,0):1}
    out={}
    moves=[0,0]
    peaks=[1,1]
    for t in range(T):
        moves[0]+=3*len(wave)
        moves[1]+=5*len(fresh)
        wave=wave_update(wave,t,o)
        fresh=fresh_update(fresh,t,o)
        peaks=[max(peaks[0],len(wave)),max(peaks[1],len(fresh))]
        if t+1 in ts:
            W=wave_hist(wave,o)
            F=fresh_hist(fresh)
            if reference:
                assert W==reference[n,t+1][0] and F==reference[n,t+1][1]
            delta=diagnostics(W,F,t+1)
            out[t+1]=(W,F,dict(describe(delta,t+1),nonzero_state_peaks=peaks[:],attempted_updates=moves[:]))
    return out,o.stats()

def direct_pair(n,T,source=None,a=2):
    o=Ops(n,T,source,a)
    state={(0,0,0,0,0,0,1,False):1}
    moves=0
    for t in range(T):
        out={}
        for (x,h,y,k,p,j,u,d),v in state.items():
            for r,s in product(PORTS,repeat=2):
                nx,nh=o.step(t,x,h,r)
                ny,nk=o.step(t,y,k,s)
                # Terminal equal addresses require both paths able to bridge each coordinate gap.
                remaining=T-t-1
                if max(abs(nx-ny),abs(nh-nk),abs(nx+nh-ny-nk))>remaining:continue
                if not remaining and r!=s:continue
                moves+=1
                mismatch=(r==1)!=(s==1)
                rel=o.wp(u,o.f[t] if s==1 else o.inv[t]) if mismatch else u
                key=(nx,nh,ny,nk,r,s,rel,d or mismatch)
                weight=o.mul(coef(r,p),coef(s,j))
                out[key]=o.add(out.get(key,0),o.mul(v,weight))
        state={k:v for k,v in out.items() if v}
    delta={}
    for (x,h,y,k,p,j,u,d),v in state.items():
        if x==y and h==k and p==j and u==1 and d:delta[x,h,p]=v
    return delta,moves,o.stats()

def band_interval(A,B,eps,iterations=24):
    # A,B are the two squared projected norms, lower/upper are outward rationals.
    c=(1+A+B-eps*eps)/2
    if not eps and A+B==1:return A,A
    if A+B==0 or c<=0:return Fraction(0),Fraction(1)
    peak=A/(A+B)
    def feasible(p):
        z=A*p
        w=B*(1-p)
        v=c*c-z-w
        return v<=0 or 4*z*w>=v*v
    assert feasible(peak)
    ends=[]
    for exterior in (Fraction(0),Fraction(1)):
        if feasible(exterior):
            ends.append(exterior)
            continue
        inner=peak
        for _ in range(iterations):
            test=(exterior+inner)/2
            if feasible(test):inner=test
            else:exterior=test
        ends.append(exterior)
    return tuple(ends)

def paid_interval_check(A,B,eps,lo,hi,o):
    # All quantities below are integer pairs; no square-root or materialized rational division.
    def pair(x):
        return x.numerator,x.denominator
    def plus(x,y):
        return o.add(o.mul(x[0],y[1]),o.mul(y[0],x[1])),o.mul(x[1],y[1])
    def times(x,y):
        return o.mul(x[0],y[0]),o.mul(x[1],y[1])
    def minus(x,y):
        return plus(x,(-y[0],y[1]))
    def sign(x):return (x[0]>0)-(x[0]<0)
    u,v,e=map(pair,(A,B,eps))
    rr=plus(u,v)
    c=times(minus(plus((1,1),rr),times(e,e)),(1,2))
    if eps==0:
        assert sign(minus(rr,(1,1)))==0 and sign(minus(pair(lo),u))==sign(minus(pair(hi),u))==0
        return
    for end,left in ((lo,True),(hi,False)):
        if (left and end==0) or (not left and end==1):continue
        t=pair(end)
        side=sign(minus(times(t,rr),u))
        assert side<=0 if left else side>=0
        a=times(u,t)
        b=times(v,minus((1,1),t))
        rem=minus(minus(times(c,c),a),b)
        assert sign(c)>0 and sign(rem)>=0
        assert sign(minus(times(rem,rem),times((4,1),times(a,b))))>=0


def crop(n,T,keep,truth,fresh,o,bits=24,event=lambda x,h,p:p==1):
    state={(0,0,0,1):1}
    eps=Fraction(0)
    moved=sorted_count=0
    discarded=[]
    for t in range(T):
        moved+=len(state)*3
        state=wave_update(state,t,o)
        if len(state)>keep:
            items=sorted(state.items(),key=lambda z:(-abs(z[1]),z[0]))
            sorted_count+=len(items)
            drop=0
            for _,v in items[keep:]:drop=o.add(drop,o.mul(v,v))
            state=dict(items[:keep])
        else:drop=0
        discarded.append(drop)
        d=9**(t+1)
        scaled=drop<<(2*bits)
        u=isqrt(scaled//d)
        u+=int(o.mul(o.mul(u,u),d)<scaled)
        assert o.mul(o.mul(u,u),d)>=scaled and (not u or o.mul(o.mul(u-1,u-1),d)<scaled)
        eps+=Fraction(u,1<<bits)
    estimates=wave_hist(state,o)
    Q=1
    for _ in range(T):Q=o.mul(Q,9)
    mass=[0,0]
    for key,v in estimates.items():
        idx=int(event(*key))
        mass[idx]=o.add(mass[idx],v)
    A,B=Fraction(mass[1],Q),Fraction(mass[0],Q)
    f=0
    for key,v in fresh.items():
        if event(*key):f=o.add(f,v)
    actual=None if truth is None else sum(v for k,v in truth.items() if event(*k))
    lo,hi=band_interval(A,B,eps)
    if o.actual:paid_interval_check(A,B,eps,lo,hi,o)
    assert actual is None or lo*Q<=actual<=hi*Q
    floor=lambda x:x.numerator//x.denominator
    ceil=lambda x:-floor(-x)
    bounds=[32*ceil((lo*Q-f)/32),32*floor((hi*Q-f)/32)]
    return {'max_live':keep,'candidate_updates':moved,'sorted_candidates':sorted_count,'discarded_squares':discarded,
            'epsilon_upper':str(eps),'A_sq':str(A),'B_sq':str(B),'delta_numerator_bounds':bounds,
            'trivial_probability_interval':(lo==0 and hi==1),'true_delta':None if actual is None else actual-f}

def low_switch(n,a,t,bits):
    group=Counter()
    records=Counter()
    limit=1<<bits
    expansions=0
    for switches in range(min(t,bits-3)+1):
        signed=(-1)**(t-switches)*(1<<switches)
        for steps in combinations(range(t),switches):
            for turns in product((1,2),repeat=switches):
                p=x=h=wexp=index=0
                for j in range(t):
                    if index<switches and j==steps[index]:
                        p=(p+turns[index])%3
                        index+=1
                    x+=p==0
                    h+=p==1
                    if p==1:wexp|=1<<j
                b=(x,h,p)
                group[b,pow(a,wexp,n)]+=signed
                records[b,wexp]+=signed
                expansions+=1
    values=Counter()
    for (b,_),v in group.items():values[b]+=v*v
    for (b,_),v in records.items():values[b]-=v*v
    return {b:v%limit for b,v in values.items() if v%limit},expansions

def face_only(n,ts,src=None):
    o=Ops(n,max(ts),src)
    st={(0,0,1):1}
    result={}
    moves=0
    peak=1
    for t in range(max(ts)):
        nxt={}
        for (h,p,w),v in st.items():
            for j in (0,1):
                moves+=1
                _,newh=o.step(t,t-h,h,j)
                key=newh,j,(o.wp(w,o.f[t]) if j else w)
                nxt[key]=o.add(nxt.get(key,0),o.mul(v,coef(j,p)))
        st={k:v for k,v in nxt.items() if v}
        peak=max(peak,len(st))
        if t+1 in ts:
            total=0
            for v in st.values():total=o.add(total,o.mul(v,v))
            # Counts of unrestricted-weight binary spatial paths producing the fresh diagonal.
            formal=1
            for _ in range(t+1):formal=o.mul(formal,5)
            result[t+1]={'delta':o.add(total,o.mul(-1,formal)),'Q':9**(t+1),'peak_work_wave':peak,'attempted_updates':moves}
    return result,o.stats()

def frozen_laws(root):
    old=json.loads((root/'inherited/INPUTS.json').read_text())
    R=json.loads((root/'runs/density/results.json').read_text())['result']['frames']
    result={}
    for n,t in product((21,35,77),(4,6)):
        W={(key[0][0],key[0][1],key[1]):item['mass'] for item in old['moduli'][str(n)]['truth'][str(t)]['items']
           if (key:=item['key']) and item['mass']}
        F={(z[0],z[1],p):v for ((z,p),v) in R[str(t)]['diag'] if v}
        result[n,t]=W,F
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,required=True,help='unpacked frozen heartbeat_record_quotient directory')
    parser.add_argument('--query',type=int,nargs=2,metavar=('N','T'),help='query one finite terminal box')
    parser.add_argument('--a',type=int,default=2)
    parser.add_argument('--box',type=int,nargs=8,metavar=('X0','X1','H0','H1','Z0','Z1','P0','P1'),
                        help='four half-open ranges on axis 0,1,2 and named port')
    parser.add_argument('--capacity',type=int,help='use only capped wave plus exact fresh law')
    parser.add_argument('--backend',choices=['integer','source'],default='integer',help='backend for --query')
    args=parser.parse_args()
    src,pins=bind(args.source)
    if args.query:
        n,T=args.query
        if n<2 or T<0 or gcd(args.a,n)!=1 or args.box is None or (args.capacity is not None and args.capacity<1):
            parser.error('query needs N>=2, T>=0, a a unit, a box, and a positive optional capacity')
        if args.backend=='source' and (args.a!=2 or n<=2 or n%2==0):
            parser.error('frozen source Modular supports only a=2 and odd N>2')
        bounds=args.box
        if any(l>h for l,h in zip(bounds[::2],bounds[1::2])):parser.error('reversed box endpoints')
        def event(x,h,p):
            return all(lo<=v<hi for v,lo,hi in zip((x,h,T-x-h,p),bounds[::2],bounds[1::2]))
        o=Ops(n,T,src if args.backend=='source' else None,args.a)
        R={(0,0,0,0,0):1}
        density_work=0
        for t in range(T):
            density_work+=5*len(R)
            R=fresh_update(R,t,o)
        F=fresh_hist(R)
        base=0
        for key,v in F.items():
            if event(*key):base=o.add(base,v)
        result={'N':n,'a':args.a,'T':T,'Q':9**T,'box':bounds,'fresh_mass_numerator':base,
                'fresh_updates':density_work,'backend':args.backend}
        if args.capacity is not None:
            result['certificate']=crop(n,T,args.capacity,None,F,o,event=event)
        else:
            W={(0,0,0,1):1}
            moves=0
            for t in range(T):
                moves+=3*len(W)
                W=wave_update(W,t,o)
            target=0
            for key,v in wave_hist(W,o).items():
                if event(*key):target=o.add(target,v)
            result.update({'true_mass_numerator':target,'delta_numerator':o.add(target,-base),'wave_updates':moves})
        result['source_execution_cost']=o.stats()
        print(json.dumps(result,indent=2,sort_keys=True))
        return
    if args.box is not None or args.capacity is not None:parser.error('box/capacity require --query')
    fixed=frozen_laws(args.source)
    out={'source':pins,'bound_signed_cwm':{},'full_integer':{},'direct_relative_pair':{},'face_event':{},'low_switch':{},'cropping':{}}
    for n in (21,35,77):
        wired,stats=exact_sequence(n,(4,6),src,reference=fixed)
        out['bound_signed_cwm'][n]={'Q_and_deltas':{t:r[2] for t,r in wired.items()},'actual_cost':stats}
        waves,_=exact_sequence(n,(4,6,8,12,20,32))
        out['full_integer'][n]={t:r[2] for t,r in waves.items()}
        for t in (4,6):
            D,moves,_=direct_pair(n,t)
            assert digest(D)==waves[t][2]['signed_delta_sha256']
            out['direct_relative_pair'][f'{n},{t}']={'attempted_after_terminal_cone':moves,'signed_delta_sha256':digest(D)}
        f,_=face_only(n,(6,12,20,32,64,128))
        assert all(f[t]['delta']==waves[t][2]['event_z2_zero'] for t in (6,12,20,32))
        out['face_event'][n]=f
        for t in (6,12,20):
            D,expanded=low_switch(n,2,t,6)
            exact=diagnostics(*waves[t][:2],t)
            assert D=={k:v%64 for k,v in exact.items() if v%64}
            out['low_switch'][f'{n},{t}']={'spatial_words':expanded,'nonzero_mod64':len(D),'sha256':digest(D)}
        budgets=(12,32,128,384,800,1200)
        out['cropping'][n]=[crop(n,12,K,*waves[12][:2],Ops(n,12)) for K in budgets]
        low,high=-9**12,9**12
        for row in out['cropping'][n]:
            u,v=row['delta_numerator_bounds']
            low,high=max(u,low),min(v,high)
            row['intersection_to_date']=[low,high]
    # Direct CWM trials additionally test the relative adapter, event face and sparse truncation.
    D,updates,stats=direct_pair(21,6,src)
    assert digest(D)==out['full_integer'][21][6]['signed_delta_sha256']
    out['bound_relative_pair']={'N':21,'T':6,'kept_updates':updates,'stats':stats}
    f,stats=face_only(21,(6,10,14),src)
    assert f[6]['delta']==out['face_event'][21][6]['delta']
    out['bound_face']={'N':21,'rows':f,'stats':stats}
    c=Ops(21,6,src)
    out['bound_crop']={'N':21,'T':6,'rows':[crop(21,6,K,*fixed[21,6],c) for K in (4,16,40,200)],'stats':c.stats()}
    allzero,_=exact_sequence(3,(3,),a=1)
    D=diagnostics(*allzero[3][:2],3)
    assert D[2,1,0]==32
    out['sharp_singleton']={'N':3,'a':1,'T':3,'z':[2,1,0,0,0,0],'port':0,'delta':32}
    one,_=exact_sequence(21,(5,))
    sharper=diagnostics(*one[5][:2],5)
    assert sharper[3,2,1]==32 and sharper[1,1,2]==576
    out['sharp_a2_same_family']={'N':21,'a':2,'T':5,'z3_p_delta':[[[3,2,0],1,32],[[1,1,3],2,576]]}
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
