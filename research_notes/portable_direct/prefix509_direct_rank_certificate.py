#!/usr/bin/env python3
"""PREFIX-509: exact index-free V rank/unrank via PREFIX-508 mod-six row compiler.
Parent is native X6; model is its five-axis ordered path subfamily.
Requires neighboring prefix508_mod6_compiler.py. Exact integers, no floats.
"""
from __future__ import annotations
import json,random,time
from prefix508_mod6_compiler import GATES,SRC,compile_row,sum_moment,supported_from_compiler,native_baseline,terminal

DIRECTIONS='aAbBcCdDeE'
COLORS=(0,4,1,2,3,3,4,4,4,4)

def rrank(comp,V,q,t):
    ctrl=sorted(supported_from_compiler(comp,V))
    assert (q,t) in ctrl
    return sum_moment(comp,0,V-1)[0]+ctrl.index((q,t))

def runrank(comp,rank,L):
    total=sum_moment(comp,0,L-1)[0]
    assert 0<=rank<total
    low,high=0,L-1
    while low<high:
        mid=(low+high)//2
        if sum_moment(comp,0,mid)[0]>rank:high=mid
        else:low=mid+1
    V=low
    offset=sum_moment(comp,0,V-1)[0]
    ctrl=sorted(supported_from_compiler(comp,V))
    assert offset<=rank<offset+len(ctrl)
    return V,ctrl[rank-offset]

def append_observer(state,ch,gate):
    n,y,V,W,q,t=state
    i=DIRECTIONS.index(ch);axis=i//2;sgn=1 if i%2==0 else -1
    yy=list(y);c=int(yy[axis]*sgn<0); yy[axis]+=sgn
    V+=c*(1 if axis in (1,4) else 2 if axis==3 else 0)
    W+=c if axis in (2,4) else 0
    col=COLORS[i]
    qq=terminal(GATES[gate][:q]+(col,),GATES[gate]);tt=t if t!='N' else SRC.get(col,'N')
    return n+1,tuple(yy),V,W,qq,tt

def independent_word(w,gate):
    cnt=[0]*10;q=0;t='N'
    for ch in w:
        i=DIRECTIONS.index(ch); cnt[i]+=1
        col=COLORS[i]
        q=terminal(GATES[gate][:q]+(col,),GATES[gate])
        if t=='N':t=SRC.get(col,'N')
    y=tuple(cnt[2*i]-cnt[2*i+1] for i in range(5))
    p=[min(cnt[2*i],cnt[2*i+1]) for i in range(5)]
    return len(w),y,p[1]+2*p[3]+p[4],p[2]+p[4],q,t

def run():
    begin=time.perf_counter()
    out={'certificate':'PREFIX509_INDEX_FREE_V_RANK','result':'ALL_CHECKS_PASS',
         'frozen_science':'awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d',
         'domain':'native X6 restricted five-axis ordered path, gates aab/aba, BRC cancellation V/W, KMP/source',
         'arithmetics':'unbounded integer arithmetic', 'gates':{},'append':{},'long_rows':{}}
    for g in GATES:
        nresults=[]
        for n in range(9):
            native,nstates=native_baseline(n,g)
            rowkeys=sorted(native)
            # All native rows for n<=6; uniformly spaced samples n=7,8.
            subset=rowkeys if n<=6 else rowkeys[::max(1,len(rowkeys)//180)]
            rank_checks=0;moment_checks=0;gap_counts=0;global_checks=0
            # Independent outside-row offsets from native ordered reference.
            offsets={};current=0
            for key in rowkeys:
                offsets[key]=current
                current+=sum(len(t) for t in native[key].values())
            for y,W in subset:
                comp=compile_row(g,n,y,W); fiber=native[y,W]
                m=(n-sum(map(abs,y)))//2;L=2*m+1
                expected=[]
                for V in range(L):
                    K=fiber.get(V,set());actual=supported_from_compiler(comp,V)
                    assert K==actual,(g,n,y,W,V,K,actual)
                    gap_counts+=int(not actual)
                    for ctrl in sorted(K):expected.append((V,ctrl))
                assert sum_moment(comp,0,L-1)[0]==len(expected)
                for rank,(V,(q,t)) in enumerate(expected):
                    assert rrank(comp,V,q,t)==rank
                    assert runrank(comp,rank,L)==(V,(q,t))
                    assert offsets[y,W]+rrank(comp,V,q,t)==offsets[y,W]+rank
                    rank_checks+=1;global_checks+=1
                for L0 in range(-1,L+1):
                    for H0 in range(L0,L+1):
                        wantF=sum(len(fiber.get(v,set())) for v in range(L0,H0+1))
                        wantT=sum((v+1)*len(fiber.get(v,set())) for v in range(L0,H0+1))
                        assert sum_moment(comp,L0,H0)==(wantF,wantT)
                        moment_checks+=1
            nresults.append({'n':n,'all_native_rows':len(rowkeys),'rows_checked':len(subset),
                             'native_occupancy_controller_states':nstates,'rank_unrank_checked':rank_checks,
                             'global_lex_rank_checked':global_checks,'interval_moment_checked':moment_checks,
                             'zero_support_V_slots_checked':gap_counts})
        out['gates'][g]=nresults
        rng=random.Random(509)
        checks=0
        for length in range(17):
            for _ in range(15):
                word=[rng.choice(DIRECTIONS) for _ in range(length)]
                initial=independent_word(word,g)
                for ch in DIRECTIONS:
                    s=append_observer(initial,ch,g)
                    assert s==independent_word(word+[ch],g)
                    N,Y,V,W,q,t=s;comp=compile_row(g,N,Y,W)
                    L=N-sum(map(abs,Y))+1
                    assert runrank(comp,rrank(comp,V,q,t),L)==(V,(q,t))
                    checks+=1
        out['append'][g]=checks
        probes=[]
        for n in (16,32,64,128,256):
            y=(0,0,0,0,0);W=n//4
            comp=compile_row(g,n,y,W);L=n+1
            k=[len(supported_from_compiler(comp,V)) for V in range(L)]
            assert sum(k)==sum_moment(comp,0,L-1)[0]
            for rr in sorted(set((0,sum(k)//2,max(0,sum(k)-1)))):
                if sum(k)>0:
                    v,ctrl=runrank(comp,rr,L)
                    assert rrank(comp,v,*ctrl)==rr
            for a,b in ((0,L-1),(L//4,3*L//4),(L//2,L-1)):
                assert sum_moment(comp,a,b)==(sum(k[a:b+1]),sum((i+1)*k[i] for i in range(a,b+1)))
            probes.append({'n':n,'W':W,'row_support_count':sum(k),
                           'compiled_intervals':sum(len(z) for z in comp.values()),'V_slots':L})
        out['long_rows'][g]=probes
    out['runtime_seconds']=round(time.perf_counter()-begin,3)
    return out

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,separators=(',',':')))
