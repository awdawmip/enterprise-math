#!/usr/bin/env python3
"""Replay/checker for the positive-support semiprime-shell second-order null.

No code path enumerates the registered new holdouts. Default mode reconstructs
exact discovery counts and the two exact support masks. --full additionally
replays the frozen 4096-replicate discovery nulls and verifies their hashes and
family-wise decision.
"""
from __future__ import annotations
import argparse, collections, hashlib, json, math
import numpy as np

DISCOVERY=[1_000_000,3_000_000,10_000_000,30_000_000,100_000_000]
HOLDOUTS=[300_000_000,1_000_000_000]
WIDTHS=[(1,100),(3,1000),(1,1000)]
BINS=32
F=5*3*BINS
REPS=4096
SEED_A=6970043005407847698
SEED_B=1878891929265112161
EXPECTED_A_HASH="c1c67979aa5d5c23dfaecafa92e788579513f244301cc0a02c9b159dc1cae610"
EXPECTED_B_HASH="df42c9a95f360f539b51f6fc6e176b950c4270332d295cee0d913edb348aed73"
EXPECTED_THR_A=3.6953790238805664
EXPECTED_THR_B=3.6931766083545967
EXPECTED_TOBS_A=1.8196292851063531
EXPECTED_TOBS_B=2.1614452449762354

def sieve(n:int)->np.ndarray:
    a=np.ones(n+1,dtype=np.bool_);a[:2]=False
    for p in range(2,math.isqrt(n)+1):
        if a[p]:a[p*p:n+1:p]=False
    return np.flatnonzero(a)

def fourth_root_floor(n:int)->int:
    x=math.isqrt(math.isqrt(n))
    while (x+1)**4<=n:x+=1
    while x**4>n:x-=1
    return x

def xi_bin(p:int,X:int)->int:
    u=math.log(p)/math.log(X);xi=1.0+math.log(u/(1.0-u))/math.log(3.0)
    return min(BINS-1,max(0,int(math.floor(xi*BINS))))

def build_discovery():
    primes=sieve(1_000_000);obs=np.zeros((5,3,BINS),dtype=np.int64);cells={}
    for i,X in enumerate(DISCOVERY):
        pmin=int(primes[np.searchsorted(primes,fourth_root_floor(X)+1)])
        for j,(num,den) in enumerate(WIDTHS):
            U=X*(den+num)//den;ps=primes[(primes>=pmin)&(primes<=math.isqrt(U))]
            qlo=np.maximum(ps,X//ps+1);qhi=U//ps
            cnt=np.searchsorted(primes,qhi,side="right")-np.searchsorted(primes,qlo,side="left")
            sq=np.array([X<int(p)*int(p)<=U for p in ps],dtype=bool);cnt=cnt-sq.astype(np.int64)
            prof=np.zeros(BINS,dtype=np.int64)
            for p,w in zip(ps,cnt):prof[xi_bin(int(p),X)]+=int(w)
            obs[i,j]=prof;cells[(i,j)]=(ps,qlo,qhi)
    return primes,obs,cells

def build_sparse_weights(cells):
    total=sum(int(np.maximum(qhi-qlo+1,0).sum()) for ps,qlo,qhi in cells.values())
    qs=np.empty(total,dtype=np.int32);fs=np.empty(total,dtype=np.int16);pos=0
    for i,X in enumerate(DISCOVERY):
        for j,_ in enumerate(WIDTHS):
            ps,qlo,qhi=cells[(i,j)]
            for p,lo,hi in zip(ps,qlo,qhi):
                p=int(p);lo=int(lo);hi=int(hi);f=(i*3+j)*BINS+xi_bin(p,X)
                for aa,bb in ((lo,min(hi,p-1)),(max(lo,p+1),hi)):
                    if aa<=bb:
                        n=bb-aa+1;qs[pos:pos+n]=np.arange(aa,bb+1,dtype=np.int32);fs[pos:pos+n]=f;pos+=n
    qs=qs[:pos];fs=fs[:pos];keys=qs.astype(np.int64)*F+fs.astype(np.int64)
    o=np.argsort(keys,kind="mergesort");ks=keys[o];st=np.r_[True,ks[1:]!=ks[:-1]]
    uk=ks[st];ii=np.flatnonzero(st);ee=np.r_[ii[1:],len(ks)];vv=(ee-ii).astype(np.int16)
    uq=(uk//F).astype(np.int32);uf=(uk%F).astype(np.int16);ptr=np.zeros(1_000_002,dtype=np.int32)
    ptr[1:]=np.cumsum(np.bincount(uq,minlength=1_000_001),dtype=np.int64).astype(np.int32)
    return ptr,uf,vv

def add_q(row,q,ptr,uf,vv):
    for a in range(int(ptr[q]),int(ptr[q+1])):row[int(uf[a])]+=int(vv[a])

def qdict(q,ptr,uf,vv):
    return {int(uf[a]):int(vv[a]) for a in range(int(ptr[q]),int(ptr[q+1]))}

def build_a(primes,ptr,uf,vv):
    qmax=1_000_000;tmax=(qmax-209)//210
    residues=np.array([math.gcd(r,210)==1 for r in range(210)],dtype=np.bool_)
    cand=np.arange(1680,qmax+1,dtype=np.int32);cand=cand[residues[cand%210]]
    t=(cand//210).astype(np.int32);complete=t<=tmax;cand=cand[complete];t=t[complete]
    k=np.floor(np.log2(t)).astype(np.int16);s=np.array([1<<max(3,int(x)-10) for x in k],dtype=np.int32)
    base=(1<<k.astype(np.int64));j=((t.astype(np.int64)-base)//s).astype(np.int32)
    code=((k.astype(np.int64)*100000+j.astype(np.int64))*210+(cand%210)).astype(np.int64)
    o=np.argsort(code,kind="mergesort");cand=cand[o];code=code[o]
    ch=np.r_[True,code[1:]!=code[:-1]];gs=np.flatnonzero(ch);ge=np.r_[gs[1:],len(code)];gc=code[gs]
    pq=primes[(primes>=1680)&((primes//210)<=tmax)].astype(np.int32);tt=(pq//210).astype(np.int64)
    kk=np.floor(np.log2(tt)).astype(np.int64);ss=np.array([1<<max(3,int(x)-10) for x in kk],dtype=np.int64)
    bb=(1<<kk);jj=(tt-bb)//ss;pc=((kk*100000+jj)*210+(pq%210)).astype(np.int64)
    pcodes,pk=np.unique(pc,return_counts=True);gi=np.searchsorted(gc,pcodes);assert np.all(gc[gi]==pcodes)
    support=np.zeros(F,dtype=np.bool_);vs=[];vn=[];vk=[];vcodes=[]
    for h,g in enumerate(gi):
        c=int(gc[g]);cr=c//210;Klog=cr//100000;expected=1<<max(3,Klog-10);n=int(ge[g]-gs[g]);K=int(pk[h])
        if n!=expected:continue
        if 0<K<n:
            st=int(gs[g]);en=int(ge[g]);ds=[qdict(int(q),ptr,uf,vv) for q in cand[st:en]]
            feats=set().union(*(d.keys() for d in ds))
            for f in feats:
                x=ds[0].get(f,0)
                if any(d.get(f,0)!=x for d in ds[1:]):support[f]=True
            vs.append(st);vn.append(n);vk.append(K);vcodes.append(c)
    vset=set(vcodes);fixed=np.zeros(F,dtype=np.int32)
    for q0 in primes:
        q=int(q0);c=None
        if q>=1680:
            T=q//210
            if T<=tmax:
                K=T.bit_length()-1;S=1<<max(3,K-10);J=(T-(1<<K))//S;C=(K*100000+J)*210+(q%210);t0=(1<<K)+J*S
                if t0+S-1<=tmax:c=C
        if c is None or c not in vset:add_q(fixed,q,ptr,uf,vv)
    return support,fixed,np.array(vs,dtype=np.int32),np.array(vn,dtype=np.int8),np.array(vk,dtype=np.int8),cand

def build_b(primes,ptr,uf,vv):
    qmax=1_000_000;tmax=(qmax-209)//210
    mov=primes[(primes>=3360)&((primes//210)<=tmax)].astype(np.int32);t=(mov//210).astype(np.int32)
    k=np.floor(np.log2(t)).astype(np.int16);s=np.array([1<<max(4,int(x)-6) for x in k],dtype=np.int32)
    base=(1<<k.astype(np.int64));j=((t.astype(np.int64)-base)//s).astype(np.int32);code=k.astype(np.int64)*100000+j.astype(np.int64)
    o=np.argsort(code,kind="mergesort");mov=mov[o];code=code[o];ch=np.r_[True,code[1:]!=code[:-1]]
    bs=np.flatnonzero(ch);be=np.r_[bs[1:],len(code)];bc=code[bs]
    support=np.zeros(F,dtype=np.bool_);vbs=[];vbe=[];vb0=[];vbn=[];full=set()
    for g,c0 in enumerate(bc):
        c=int(c0);K=c//100000;J=c%100000;S=1<<max(4,K-6);t0=(1<<K)+J*S
        if t0+S-1>tmax:continue
        full.add(c);vbs.append(int(bs[g]));vbe.append(int(be[g]));vb0.append(t0);vbn.append(S)
        qs=mov[bs[g]:be[g]];aggs=[];union=set()
        for sh in range(S):
            d=collections.defaultdict(int)
            for q0 in qs:
                q=int(q0);T=q//210;r=q%210;qp=(t0+((T-t0+sh)%S))*210+r
                for a in range(int(ptr[qp]),int(ptr[qp+1])):d[int(uf[a])]+=int(vv[a])
            aggs.append(d);union.update(d)
        for f in union:
            x=aggs[0].get(f,0)
            if any(d.get(f,0)!=x for d in aggs[1:]):support[f]=True
    fixed=np.zeros(F,dtype=np.int32)
    for q0 in primes:
        q=int(q0);c=None
        if q>=3360:
            T=q//210
            if T<=tmax:
                K=T.bit_length()-1;S=1<<max(4,K-6);J=(T-(1<<K))//S;C=K*100000+J;t0=(1<<K)+J*S
                if t0+S-1<=tmax:c=C
        if c is None or c not in full:add_q(fixed,q,ptr,uf,vv)
    return support,fixed,np.array(vbs,dtype=np.int32),np.array(vbe,dtype=np.int32),np.array(vb0,dtype=np.int32),np.array(vbn,dtype=np.int32),mov

def exact_support():
    primes,obs,cells=build_discovery();ptr,uf,vv=build_sparse_weights(cells)
    sa,fa,ast,an,ak,acand=build_a(primes,ptr,uf,vv);sb,fb,bst,ben,bt0,bn,bmov=build_b(primes,ptr,uf,vv)
    ag=sa.reshape(5,3,32);bg=sb.reshape(5,3,32);eligible=np.all(ag&bg,axis=0)
    expected=np.zeros((3,32),dtype=np.bool_);expected[:,[1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21]]=True
    assert np.array_equal(eligible,expected)
    return {"primes":primes,"obs":obs,"ptr":ptr,"uf":uf,"vv":vv,"sa":sa,"sb":sb,"eligible":eligible,"fa":fa,"ast":ast,"an":an,"ak":ak,"acand":acand,"fb":fb,"bst":bst,"ben":ben,"bt0":bt0,"bn":bn,"bmov":bmov}

def full_replay(state):
    try:from numba import njit,prange
    except Exception as exc:raise SystemExit("--full requires numba: "+str(exc))
    ptr,uf,vv=state["ptr"],state["uf"],state["vv"]
    @njit
    def step(x):
        x^=(x>>np.uint64(12));x^=(x<<np.uint64(25));x^=(x>>np.uint64(27));return x,x*np.uint64(2685821657736338717)
    @njit(parallel=True)
    def runa(reps,seed,fixed,st,ns,ks,cand,ptr,uf,vv):
        out=np.empty((reps,F),dtype=np.int32)
        for r in prange(reps):
            row=fixed.copy();x=np.uint64(seed)^(np.uint64(r+1)*np.uint64(0x9E3779B97F4A7C15))
            for g in range(st.shape[0]):
                n=int(ns[g]);K=int(ks[g]);m=K if K<=n-K else n-K;mask=np.uint32(0);got=0
                while got<m:
                    x,z=step(x);h=int(z%np.uint64(n));bit=np.uint32(1<<h)
                    if (mask&bit)==0:mask|=bit;got+=1
                direct=K<=n-K;ss=int(st[g])
                for h in range(n):
                    hit=(mask&np.uint32(1<<h))!=0
                    if (hit and direct) or ((not hit) and (not direct)):
                        q=int(cand[ss+h])
                        for a in range(int(ptr[q]),int(ptr[q+1])):row[int(uf[a])]+=int(vv[a])
            out[r]=row
        return out
    @njit(parallel=True)
    def runb(reps,seed,fixed,st,en,t0,ns,mov,ptr,uf,vv):
        out=np.empty((reps,F),dtype=np.int32)
        for r in prange(reps):
            row=fixed.copy();x=np.uint64(seed)^(np.uint64(r+1)*np.uint64(0x9E3779B97F4A7C15))
            for g in range(st.shape[0]):
                x,z=step(x);S=int(ns[g]);sh=int(z%np.uint64(S));base=int(t0[g])
                for ii in range(int(st[g]),int(en[g])):
                    q=int(mov[ii]);T=q//210;rr=q%210;qp=(base+((T-base+sh)%S))*210+rr
                    for a in range(int(ptr[qp]),int(ptr[qp+1])):row[int(uf[a])]+=int(vv[a])
            out[r]=row
        return out
    A=runa(REPS,np.uint64(SEED_A),state["fa"],state["ast"],state["an"],state["ak"],state["acand"],ptr,uf,vv)
    B=runb(REPS,np.uint64(SEED_B),state["fb"],state["bst"],state["ben"],state["bt0"],state["bn"],state["bmov"],ptr,uf,vv)
    ah=hashlib.sha256(A.tobytes()).hexdigest();bh=hashlib.sha256(B.tobytes()).hexdigest();assert ah==EXPECTED_A_HASH and bh==EXPECTED_B_HASH
    obs=state["obs"].reshape(-1).astype(float);eligible=state["eligible"];ma=A.mean(0);sa=A.std(0,ddof=1);mb=B.mean(0);sb=B.std(0,ddof=1)
    zoA=np.zeros(F,dtype=float);zoB=np.zeros(F,dtype=float);ma_mask=sa>0;mb_mask=sb>0
    zoA[ma_mask]=(obs[ma_mask]-ma[ma_mask])/sa[ma_mask];zoB[mb_mask]=(obs[mb_mask]-mb[mb_mask])/sb[mb_mask]
    zgA=zoA.reshape(5,3,32);zgB=zoB.reshape(5,3,32)
    znA=((A-ma)/np.where(sa>0,sa,1)).reshape(REPS,5,3,32);znB=((B-mb)/np.where(sb>0,sb,1)).reshape(REPS,5,3,32)
    CA=zgA.sum(0)/math.sqrt(5);CB=zgB.sum(0)/math.sqrt(5);CNA=znA.sum(1)/math.sqrt(5);CNB=znB.sum(1)/math.sqrt(5)
    TA=np.max(np.abs(CNA[:,eligible]),axis=1);TB=np.max(np.abs(CNB[:,eligible]),axis=1)
    thA=float(np.quantile(TA,.99,method="higher"));thB=float(np.quantile(TB,.99,method="higher"));toA=float(np.max(np.abs(CA[eligible])));toB=float(np.max(np.abs(CB[eligible])))
    assert abs(thA-EXPECTED_THR_A)<1e-12 and abs(thB-EXPECTED_THR_B)<1e-12 and abs(toA-EXPECTED_TOBS_A)<1e-12 and abs(toB-EXPECTED_TOBS_B)<1e-12
    candidates=[]
    for j,b in np.argwhere(eligible):
        ca=float(CA[j,b]);cb=float(CB[j,b])
        if abs(ca)>thA and abs(cb)>thB and ca*cb>0:
            s=1 if ca>0 else -1
            if int(np.sum(s*zgA[:,j,b]>0))>=4 and int(np.sum(s*zgB[:,j,b]>0))>=4:candidates.append((int(j),int(b)))
    assert not candidates
    return {"null_a_sha256":ah,"null_b_sha256":bh,"threshold_A_99":thA,"threshold_B_99":thB,"observed_T_A":toA,"observed_T_B":toB,"empirical_tail_A":float((1+np.sum(TA>=toA))/(REPS+1)),"empirical_tail_B":float((1+np.sum(TB>=toB))/(REPS+1)),"candidate_count":0,"holdouts_accessed":False}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--full",action="store_true");args=ap.parse_args();s=exact_support()
    out={"support_A_by_scale":[int(x) for x in s["sa"].reshape(5,3,32).sum((1,2))],"support_B_by_scale":[int(x) for x in s["sb"].reshape(5,3,32).sum((1,2))],"eligible_count":int(s["eligible"].sum()),"eligible_bins_by_width":[np.flatnonzero(s["eligible"][j]).tolist() for j in range(3)],"observed_totals":[[int(s["obs"][i,j].sum()) for j in range(3)] for i in range(5)],"holdouts_accessed":False}
    if args.full:out["full_replay"]=full_replay(s)
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=="__main__":main()
