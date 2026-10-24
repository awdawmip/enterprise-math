#!/usr/bin/env python3
"""R260 exact six-axis BRC affine-source verifier.

This is a source-law-faithful independently implemented typed BRC subcarrier.
It is NOT a claim that the original enterprise_math package was imported.
Source contracts: brc_transport.py Affine.then/EffectHistogram.then,
brc_control_port.py ControlPacket.from_edges/then.
Positive branch weight=1; source selector occurrences retained until DFA update.
Formal edge depth is not physical heartbeat time; q and r are nonspatial.
"""
from collections import Counter
from dataclasses import dataclass
from itertools import product
import json

EDGE={0:{0:(2,-1,-1),1:(2,1,-1)},
      1:{0:(0,-1,-1),1:(0,1,-1)},
      2:{0:(1,1,1),1:(2,1,-1)}}
DFA={0:{0:1,1:0},1:{0:2,1:0},2:{0:2,1:2}}

@dataclass(frozen=True)
class Affine6:
    diag:tuple
    shift:tuple
    def __post_init__(self):
        assert len(self.diag)==len(self.shift)==6
        assert all(t in (-1,1) for t in self.diag)
        assert all(type(t)==int for t in self.shift)
    @classmethod
    def identity(cls): return cls((1,)*6,(0,)*6)
    def then(self,later):
        # Native BRC Affine.then: (B,c) o (A,b) = (BA,Bb+c).
        return Affine6(
          tuple(later.diag[i]*self.diag[i] for i in range(6)),
          tuple(later.diag[i]*self.shift[i]+later.shift[i] for i in range(6)))
    @property
    def pair(self):
        assert self.diag[0]==self.diag[1] and self.diag[2:]==(1,1,1,1)
        assert self.shift[1:]==(0,0,0,0,0)
        return self.diag[0],self.shift[0]

def action(e,b): return Affine6((e,e,1,1,1,1),(b,0,0,0,0,0))
def step(q,r,e,a):
    q1,eta,b=EDGE[q][a]
    return q1,DFA[r][a],e.then(action(eta,b))
def word(w,q=0,r=0):
    e=Affine6.identity()
    for c in w:q,r,e=step(q,r,e,int(c))
    return (q,r,e)
def fib(n):
    x,y=0,1
    for _ in range(n):x,y=y,x+y
    return x
def fibre_min(hist):
    rows={}
    for (q,r,e),n in hist.items():rows.setdefault((q,e),[0,0,0])[r]+=n
    return max((min(t) for t in rows.values()),default=0)
def no00_end1_effects(L):
    hist=Counter({(0,1,Affine6.identity()):1})
    for _ in range(L):
        new=Counter()
        for (q,last,e),n in hist.items():
            for a in (0,1):
                if a==last==0:continue
                q1,eta,b=EDGE[q][a]
                new[(q1,a,e.then(action(eta,b)))]+=n
        hist=new
    group=Counter()
    for (q,last,e),n in hist.items():
        if last==1:group[e]+=n
    return group

BASE={7:('1110101','1011010','0000000'),
      8:('11110101','10111010','00011010'),
      9:('101101011','010101010','000000011')}
S='1101';P='101'
SIX=('10110111','10111011','10111101',
     '11011011','11011101','11101101')

def main():
    for q in (0,1,2):
        q1,r1,e=word(S,q)
        assert (q1,r1,e.pair)==(0,0,(1,-2))
    for length,words in BASE.items():
        v=[word(w) for w in words]
        assert all(len(w)==length for w in words)
        assert [r for q,r,e in v]==[0,1,2]
        assert len({(q,e) for q,r,e in v})==1
        assert v[0][0]==2 and v[0][2].pair[0]==-1
    q,r,e=word(P)
    assert (q,r,e.pair)==(0,0,(1,-1))
    for w in SIX:
        assert len(w)==8 and '00' not in w and w.endswith('1')
        assert word(w)[2].pair==(1,-4)
        q,r,e=word(w+S)
        assert (q,r,e.pair)==(0,0,(1,-6))
    assert len(set(SIX))==6

    cur=Counter({(0,0,Affine6.identity()):1})
    Ms={}
    for m in range(129):
        assert sum(cur.values())==2**m
        Ms[m]=fibre_min(cur)
        if m>=1:assert Ms[m]<=fib(m)
        if m<=10:
            raw=Counter(word(''.join(bits)) for bits in product('01',repeat=m))
            assert raw==cur
        if m<128:
            nxt=Counter()
            for (q,r,e),count in cur.items():
                for a in (0,1):nxt[step(q,r,e,a)]+=count
            cur=nxt
    assert [i for i,v in Ms.items() if v>0][0]==7

    regular={}
    Ls=(8,11,14,17,20,23,29,32,50)
    checks=0
    for L in Ls:
        h=no00_end1_effects(L)
        assert sum(h.values())==fib(L+1)
        assert len(h)<=2*(L+1)
        lb=(fib(L+1)+2*(L+1)-1)//(2*(L+1))
        a,nmax=max(h.items(),key=lambda p:p[1])
        assert nmax>=lb
        regular[str(L)]={'F_L_plus_1':str(fib(L+1)),
                         'distinct_effect_atoms':len(h),
                         'pigeonhole_lower':lb,
                         'max_effect_fibre':str(nmax),
                         'one_max_effect':list(a.pair),
                         'reset_block_length':L+4}
        if L==8:assert nmax==6
        if L==11:assert nmax==21
        if L==50:assert nmax==671125852
        if L<=32:
            assert (L+4)%3==0
            for m in range(7,129):
                j=next(j for j in (7,8,9) if m>=j and (m-j)%3==0)
                K=(m-j)//(L+4)
                assert Ms[m]>=nmax**K
                checks+=1
    assert checks==976

    samples=0
    for K in (0,1,2,4,8,13):
        pfx=''.join(SIX[0]+S for _ in range(K))
        for ix in range(K):
            alternate=''.join((SIX[5] if n==ix else SIX[0])+S for n in range(K))
            assert word(alternate)==word(pfx)
            samples+=1
        for j,words in BASE.items():
            t=[word(pfx+w) for w in words]
            assert [r for q,r,e in t]==[0,1,2]
            assert len({(q,e) for q,r,e in t})==1
            samples+=3
    assert samples==82

    out={
     'schema':'EM_R260_BRC_FIBONACCI_FIBRE_ENTROPY_AUTHOR_CHECK_V1',
     'status':'AUTHOR_SIDE_EXACT_TYPED_BRC_SUBCARRIER_VERIFIED_NOT_SOURCE_ACCEPTED',
     'source_pin':'awdawmip/enterprise-math@a4880ba6486d150077c3c8acbf99c7ded0fd6ebd',
     'source_laws':['src/enterprise_math/brc_transport.py Affine.then and EffectHistogram.then',
                    'src/enterprise_math/brc_control_port.py labelled edges and ControlPacket.then'],
     'native_module_import_performed':False,
     'six_axis_carrier':'diag(eta,eta,1,1,1,1); displacement (k,0,0,0,0,0)',
     'positive_weight':'one exact unit weight per source edge; integer multiplicity',
     'selector_DFA':'substring 00 3-mode monitor; control Q={0,1,2}',
     'time':'formal edge depth, NOT physical heartbeat time',
     'data':{
       'sync_word':S,'sync_for_every_initial_control':'q=0,r=0,effect=(+1,-2)',
       'explicit_6_reset_blocks_length_12':[w+S for w in SIX],
       'all_equal_reset_block_effect':'(+1,-6)',
       'first_3_mode_common_fibre_depth':7,
       'max_per_mode_fibre_selected_depths':{str(m):str(Ms[m]) for m in
          (7,8,9,10,12,15,24,36,60,96,128)},
       'regular_word_fibre_counts':regular},
     'verification':{'full_positive_BRC_histogram_depths':129,
        'exhaustive_raw_word_crosscheck_depths':'0..10 (2047 words total)',
        'upper_Fibonacci_bound_depths':128,
        'finite_uniform_lower_checks':checks,'explicit_prefix_checks':samples},
     'analytic_claim':'lim_{m->infty} log(M_m)/m = log(phi), phi=(1+sqrt(5))/2',
     'claim_scope':'formal finite positive branch source-affine observer only',
     'next':'actual R193 labelled edge/query/time semantics; native package import with original ControlPacket/EffectHistogram and P000-faithfulness bridge'}
    print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
if __name__=='__main__':main()
