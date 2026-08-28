#!/usr/bin/env python3
"""Checker/replay for RS-PRIME-FACTOR-SEMIPRIME-SHELL-SECOND-ORDER-DENSITY-NULL.

Default mode proves the terminal null-model misspecification without touching the
registered new holdouts. --full additionally replays the frozen 4096-replicate
discovery diagnostics when numba is available.
"""
from __future__ import annotations
import argparse, hashlib, math, json
import numpy as np

DISCOVERY = [1_000_000, 3_000_000, 10_000_000, 30_000_000, 100_000_000]
WIDTHS = [(1,100), (3,1000), (1,1000)]
BINS = 32
F = len(DISCOVERY)*len(WIDTHS)*BINS
NULL_A_REPS = 4096
NULL_B_REPS = 4096
SEED_A = 1251874746125827120
SEED_B = 10723725512002858063
HOLDOUTS = [300_000_000, 1_000_000_000]  # registration only; never enumerated here
EXPECTED_A_HASH = "adffaf6ee4e3098caf53d0ee2c3c63bcfb8dd1c218d654341a57c4794b5175a9"
EXPECTED_B_HASH = "a2d3ef1315397c97c3dcc0ba3ef4aabec532dc307aecd6909d173cd312f86577"

def sieve(n:int):
    a=np.ones(n+1,dtype=np.bool_); a[:2]=False
    for p in range(2, math.isqrt(n)+1):
        if a[p]: a[p*p:n+1:p]=False
    return np.flatnonzero(a)

def fourth_root_floor(n:int)->int:
    x=math.isqrt(math.isqrt(n))
    while (x+1)**4<=n: x+=1
    while x**4>n: x-=1
    return x

def pmin_and_qmax(X:int, num:int, den:int, primes:np.ndarray):
    r=fourth_root_floor(X)
    pmin=int(primes[np.searchsorted(primes,r+1)])
    U=X*(den+num)//den
    return pmin, U//pmin

def xi_bin(p:int,X:int)->int:
    u=math.log(p)/math.log(X)
    xi=1.0+math.log(u/(1.0-u))/math.log(3.0)
    return min(BINS-1,max(0,int(math.floor(xi*BINS))))

def build_discovery():
    primes=sieve(1_000_000)
    obs=np.zeros((5,3,BINS),dtype=np.int64); cell_data={}; qmax_by_scale={}
    for i,X in enumerate(DISCOVERY):
        qmx=0
        for j,(num,den) in enumerate(WIDTHS):
            U=X*(den+num)//den
            pmin,qm=pmin_and_qmax(X,num,den,primes); qmx=max(qmx,qm)
            ps=primes[(primes>=pmin)&(primes<=math.isqrt(U))]
            qlo=np.maximum(ps, X//ps+1); qhi=U//ps
            c=np.searchsorted(primes,qhi,side="right")-np.searchsorted(primes,qlo,side="left")
            sq=np.array([X<int(p)*int(p)<=U for p in ps],dtype=bool)
            c=c-sq.astype(np.int64)
            prof=np.zeros(BINS,dtype=np.int64)
            for p,w in zip(ps,c): prof[xi_bin(int(p),X)]+=int(w)
            obs[i,j]=prof; cell_data[(i,j)]=(ps,qlo,qhi)
        qmax_by_scale[X]=qmx
    return primes, obs, cell_data, qmax_by_scale

def structural_misspecification():
    primes,obs,cell_data,qmaxs=build_discovery(); cutoff=1<<18
    assert qmaxs[1_000_000]==27297 and qmaxs[3_000_000]==70465 and qmaxs[10_000_000]==171186
    assert all(qmaxs[x]<cutoff for x in DISCOVERY[:3])
    for k in range(1,18): assert (1<<k)/1024 <= 128 < 210
    X=1_000_000; U=X*101//100; ps,qlo,qhi=cell_data[(0,0)]
    target=[(int(p),int(lo),int(hi)) for p,lo,hi in zip(ps,qlo,qhi) if xi_bin(int(p),X)==1]
    band_primes=primes[(primes>=26880)&(primes<=27299)]
    def contribution(shift_blocks:int)->int:
        s=0
        for q0 in band_primes:
            q=int(q0); t=q//210; r=q%210; nt=128+((t-128+shift_blocks)%2); qq=210*nt+r
            for p,lo,hi in target:
                if lo<=qq<=hi and qq!=p: s+=1
        return s
    c0,c1=contribution(0),contribution(1); assert (c0,c1)==(25,31),(c0,c1)
    return {"holdouts_accessed":False,"null_a_singleton_cutoff_exclusive":cutoff,
      "qmax_by_scale":{str(k):int(v) for k,v in qmaxs.items()},
      "null_a_first_three_scales_variance":"EXACTLY_ZERO_FOR_EVERY_REGISTERED_CELL",
      "null_b_exact_witness":{"X":X,"eta":"1/100","xi_bin":1,"band_t":[128,130],
        "q_range":[26880,27299],"shift0_contribution":c0,"shift1_contribution":c1},
      "observed_totals":[[int(obs[i,j].sum()) for j in range(3)] for i in range(5)]}

def build_sparse_weights(primes,cell_data):
    qmax=1_000_000; total=0
    for ps,qlo,qhi in cell_data.values(): total += int(np.maximum(qhi-qlo+1,0).sum())
    qs=np.empty(total,dtype=np.int32); fs=np.empty(total,dtype=np.int16); pos=0
    for i,X in enumerate(DISCOVERY):
        for j,_ in enumerate(WIDTHS):
            ps,qlo,qhi=cell_data[(i,j)]
            for p,lo,hi in zip(ps,qlo,qhi):
                p=int(p); lo=int(lo); hi=int(hi); f=(i*3+j)*BINS+xi_bin(p,X)
                for aa,bb in ((lo,min(hi,p-1)),(max(lo,p+1),hi)):
                    if aa<=bb:
                        n=bb-aa+1; qs[pos:pos+n]=np.arange(aa,bb+1,dtype=np.int32); fs[pos:pos+n]=f; pos+=n
    qs=qs[:pos]; fs=fs[:pos]; keys=qs.astype(np.int64)*F+fs.astype(np.int64)
    o=np.argsort(keys,kind="mergesort"); ks=keys[o]; st=np.r_[True,ks[1:]!=ks[:-1]]
    uk=ks[st]; ii=np.flatnonzero(st); ee=np.r_[ii[1:],len(ks)]; vv=(ee-ii).astype(np.int16)
    uq=(uk//F).astype(np.int32); uf=(uk%F).astype(np.int16); ptr=np.zeros(qmax+2,dtype=np.int32)
    ptr[1:]=np.cumsum(np.bincount(uq,minlength=qmax+1),dtype=np.int64).astype(np.int32)
    return ptr,uf,vv

def full_replay():
    try: from numba import njit, prange
    except Exception as exc: raise SystemExit("--full requires numba: "+str(exc))
    primes,obs,cell_data,qmaxs=build_discovery(); ptr,uf,vv=build_sparse_weights(primes,cell_data); qmax=1_000_000
    res=np.array([math.gcd(r,210)==1 for r in range(210)],dtype=np.bool_)
    cand=np.arange(11,qmax+1,dtype=np.int32); cand=cand[res[cand%210]]; pq=primes[primes>=11].astype(np.int32)
    def mcode(q):
        q=np.asarray(q,dtype=np.int64); k=np.floor(np.log2(q)).astype(np.int16); base=(1<<k.astype(np.int64))
        j=((q-base)*1024//base).astype(np.int16); r=(q%210).astype(np.int16)
        return ((k.astype(np.int64)*1024+j.astype(np.int64))*210+r.astype(np.int64))
    cc=mcode(cand); pc=mcode(pq); o=np.argsort(cc,kind="mergesort"); cand=cand[o]; cc=cc[o]
    change=np.r_[True,cc[1:]!=cc[:-1]]; gs=np.flatnonzero(change); ge=np.r_[gs[1:],len(cc)]; gc=cc[gs]
    pcodes,pk=np.unique(pc,return_counts=True); gi=np.searchsorted(gc,pcodes)
    starts=gs[gi].astype(np.int32); lens=(ge[gi]-gs[gi]).astype(np.int8); kk=pk.astype(np.int8)
    baseA=np.zeros(F,dtype=np.int32); vs=[];vl=[];vk=[]
    for g in range(len(starts)):
        st0=int(starts[g]); n=int(lens[g]); k0=int(kk[g])
        if n==k0:
            for q in cand[st0:st0+n]:
                for a in range(int(ptr[q]),int(ptr[q+1])): baseA[int(uf[a])]+=int(vv[a])
        else: vs.append(st0);vl.append(n);vk.append(k0)
    vs=np.array(vs,dtype=np.int32);vl=np.array(vl,dtype=np.int8);vk=np.array(vk,dtype=np.int8)
    @njit
    def rngstep(state):
        x=state; x^=(x>>np.uint64(12)); x^=(x<<np.uint64(25)); x^=(x>>np.uint64(27)); return x,x*np.uint64(2685821657736338717)
    @njit(parallel=True)
    def runA(reps,seed,baseA,vs,vl,vk,cand,ptr,uf,vv):
        out=np.empty((reps,F),dtype=np.int32)
        for r in prange(reps):
            row=baseA.copy(); state=np.uint64(seed)^(np.uint64(r+1)*np.uint64(0x9E3779B97F4A7C15))
            for g in range(vs.shape[0]):
                state,z=rngstep(state); n=int(vl[g]); k=int(vk[g]); st=int(vs[g])
                if k==1:
                    q=int(cand[st+int(z%np.uint64(n))])
                    for a in range(int(ptr[q]),int(ptr[q+1])): row[int(uf[a])]+=int(vv[a])
                else:
                    omit=int(z%np.uint64(3))
                    for h in range(3):
                        if h!=omit:
                            q=int(cand[st+h])
                            for a in range(int(ptr[q]),int(ptr[q+1])): row[int(uf[a])]+=int(vv[a])
            out[r]=row
        return out
    tmax=(qmax-209)//210; qend=210*tmax+209
    movable=primes[(primes>=210)&(primes<=qend)].astype(np.int32); fixed=primes[(primes<210)|(primes>qend)].astype(np.int32)
    t=(movable//210).astype(np.int32); k=np.floor(np.log2(t)).astype(np.int16); base=(1<<k.astype(np.int64))
    j=((t-base)*64//base).astype(np.int16); code=k.astype(np.int32)*64+j; o=np.argsort(code,kind="mergesort")
    movable=movable[o];t=t[o];code=code[o];ch=np.r_[True,code[1:]!=code[:-1]]
    bs=np.flatnonzero(ch).astype(np.int32);be=np.r_[bs[1:],len(code)].astype(np.int32);codes=code[bs];b0=[];bn=[]
    for c in codes:
        K=int(c)//64;J=int(c)%64;B=1<<K;lo=B+(J*B+63)//64;hi=B+(((J+1)*B+63)//64)-1
        lo=max(lo,1);hi=min(hi,tmax);b0.append(lo);bn.append(max(0,hi-lo+1))
    b0=np.array(b0,dtype=np.int32);bn=np.array(bn,dtype=np.int32);baseB=np.zeros(F,dtype=np.int32);vbs=[];vbe=[];vb0=[];vbn=[]
    def add(row,q):
        for a in range(int(ptr[q]),int(ptr[q+1])): row[int(uf[a])]+=int(vv[a])
    for q in fixed:add(baseB,int(q))
    for g in range(len(bs)):
        if bn[g]<=1:
            for q in movable[bs[g]:be[g]]:add(baseB,int(q))
        else:vbs.append(int(bs[g]));vbe.append(int(be[g]));vb0.append(int(b0[g]));vbn.append(int(bn[g]))
    vbs=np.array(vbs,dtype=np.int32);vbe=np.array(vbe,dtype=np.int32);vb0=np.array(vb0,dtype=np.int32);vbn=np.array(vbn,dtype=np.int32)
    @njit(parallel=True)
    def runB(reps,seed,baseB,vbs,vbe,vb0,vbn,movable,ptr,uf,vv):
        out=np.empty((reps,F),dtype=np.int32)
        for r in prange(reps):
            row=baseB.copy();state=np.uint64(seed)^(np.uint64(r+1)*np.uint64(0x9E3779B97F4A7C15))
            for g in range(vbs.shape[0]):
                state,z=rngstep(state);nb=int(vbn[g]);sh=int(z%np.uint64(nb));t0=int(vb0[g])
                for ii in range(int(vbs[g]),int(vbe[g])):
                    q=int(movable[ii]);tt=q//210;rr=q%210;qp=(t0+((tt-t0+sh)%nb))*210+rr
                    for a in range(int(ptr[qp]),int(ptr[qp+1])):row[int(uf[a])]+=int(vv[a])
            out[r]=row
        return out
    A=runA(NULL_A_REPS,np.uint64(SEED_A),baseA,vs,vl,vk,cand,ptr,uf,vv)
    B=runB(NULL_B_REPS,np.uint64(SEED_B),baseB,vbs,vbe,vb0,vbn,movable,ptr,uf,vv)
    ah=hashlib.sha256(A.tobytes()).hexdigest();bh=hashlib.sha256(B.tobytes()).hexdigest()
    assert ah==EXPECTED_A_HASH,(ah,EXPECTED_A_HASH);assert bh==EXPECTED_B_HASH,(bh,EXPECTED_B_HASH)
    sda=A.std(axis=0,ddof=1).reshape(5,3,32);sdb=B.std(axis=0,ddof=1).reshape(5,3,32)
    return {"null_a_sha256":ah,"null_b_sha256":bh,
      "null_a_nonzero_variance_features_by_scale":[int(np.sum(sda[i]>1e-12)) for i in range(5)],
      "null_b_nonzero_variance_features_by_scale":[int(np.sum(sdb[i]>1e-12)) for i in range(5)],
      "null_a_all_five_scale_cells":int(np.sum(np.all(sda>1e-12,axis=0))),
      "null_b_all_five_scale_cells":int(np.sum(np.all(sdb>1e-12,axis=0))),"deterministic_hash_match":True}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--full",action="store_true");args=ap.parse_args()
    out={"structural":structural_misspecification()}
    if args.full:out["full_replay"]=full_replay()
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=="__main__":main()
