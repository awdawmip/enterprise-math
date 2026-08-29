#!/usr/bin/env python3
"""Exact / deterministic audit for RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION.

No CAS and no factorization library are used. The exhaustive layer is generated from a
plain Eratosthenes sieve; 64-bit holdouts use deterministic Miller-Rabin only to generate
prime factors. Hidden factors are used only for labelled diagnostics, never as deployed
features.
"""
from __future__ import annotations
import argparse, bisect, json, math, random
from array import array
from collections import Counter
from statistics import median

BANDS=(("<=1.01",1.0,1.01),("1.01-1.1",1.01,1.1),("1.1-2",1.1,2.0),("2-10",2.0,10.0),(">10",10.0,float("inf")))
MODS=(64,3,5,7,11,13)
HOLDOUT_BITS=(24,32,40,48,64)
TARGET_RATIOS={"<=1.01":1.005,"1.01-1.1":1.05,"1.1-2":1.5,"2-10":5.0,">10":50.0}

def band_of(r):
    for name,lo,hi in BANDS:
        if (name=="<=1.01" and r<=hi) or (name!="<=1.01" and lo<r<=hi): return name
    raise AssertionError(r)
def in_band(r,name): return band_of(r)==name
def ceil_sqrt(n):
    s=math.isqrt(n); return s if s*s==n else s+1
def sieve(limit):
    isp=bytearray(b"\x01")*(limit+1); isp[:2]=b"\x00\x00"
    for i in range(2,math.isqrt(limit)+1):
        if isp[i]:
            st=i*i; isp[st:limit+1:i]=b"\x00"*(((limit-st)//i)+1)
    return isp,[i for i in range(2,limit+1) if isp[i]]
def allowed_table(m):
    sq={x*x%m for x in range(m)}
    return [sum(1 for a in range(m) if (a*a-n)%m in sq) for n in range(m)]
ALLOWED={m:allowed_table(m) for m in MODS}
def modular_retention(n):
    f=1.0
    for m in MODS: f*=ALLOWED[m][n%m]/m
    return f
def qnearest(xs,q):
    if not xs:return 0
    ys=sorted(xs); return int(ys[max(0,min(len(ys)-1,math.ceil(q*len(ys))-1))])

def is_prime64(n):
    if n<2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n%p==0:return n==p
    d,s=n-1,0
    while d%2==0:s+=1;d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%n==0:continue
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True
def next_prime64(n):
    if n<=2:return 2
    x=n if n&1 else n+1
    while not is_prime64(x):x+=2
    return x
def prev_prime64(n):
    if n<=2:return 2
    x=n if n&1 else n-1
    while x>2 and not is_prime64(x):x-=2
    return x

def divisor_pairs(k):return [(a,k//a) for a in range(1,math.isqrt(k)+1) if k%a==0]
def oracle_tk(p,q,n,k,pairs):
    base=ceil_sqrt(4*k*n);best=None
    for a,b in pairs[k]:
        for x in (a*p+b*q,a*q+b*p):
            t=x-base
            if t>=0 and (best is None or t<best):best=t
    assert best is not None;return best
def shell_k(n,k):
    z=4*k*n;c=ceil_sqrt(z);b=c*c-z;return c,b,b/(2*c)

def exact_witness():
    n,p,q,kmax=9171667,2851,3217,64
    assert p*q==n and is_prime64(p) and is_prime64(q)
    pairs={k:divisor_pairs(k) for k in range(1,kmax+1)};vals=[]
    for k in range(1,kmax+1):
        if math.gcd(k,n)!=1:continue
        c,b,rho=shell_k(n,k);vals.append((k,b,rho,oracle_tk(p,q,n,k,pairs)))
    best=min(vals,key=lambda z:(z[3],z[0]));raw=sorted(vals,key=lambda z:(z[1],z[0]));norm=sorted(vals,key=lambda z:(z[2],z[0]))
    rr=1+next(i for i,z in enumerate(raw) if z[0]==best[0]);nr=1+next(i for i,z in enumerate(norm) if z[0]==best[0])
    assert best[0]==56 and best[3]==0 and rr==64 and nr==62
    c56,b56,_=shell_k(n,56);assert c56==7*q+8*p and b56==(7*q-8*p)**2
    return {"N":n,"p":p,"q":q,"best_k":56,"best_Tk":0,"raw_residual":b56,"raw_residual_rank_ascending":rr,"normalized_residual_rank_ascending":nr,"factor_split":[7,8],"identity":"ceil(sqrt(4*k*N))=7q+8p and b_k=(7q-8p)^2"}

def exhaustive(limit,reservoir_size,kmax):
    _,primes=sieve(limit);rng=random.Random(20260829)
    stats={name:Counter() for name,_,_ in BANDS}; vals={name:{"T":array("I"),"J":array("I")} for name,_,_ in BANDS}
    seen=Counter();reservoirs={name:[] for name,_,_ in BANDS};total=adj=p_prev=q_next=both=improve=worse=equal=0;maxshift=maxgap=maxT=maxJ=0;sievesum=0.0
    for ip in range(1,len(primes)):
        p=primes[ip]
        if p*p>limit:break
        for iq in range(ip+1,bisect.bisect_right(primes,limit//p)):
            q=primes[iq];n=p*q;s=math.isqrt(n);a0=s+1;A=(p+q)//2;T=A-a0
            idx=bisect.bisect_right(primes,s)-1;prevp,nextp=primes[idx],primes[idx+1];c=(prevp+nextp)//2;gap=nextp-prevp;err=abs(A-c);J=idx-ip;name=band_of(q/p);st=stats[name]
            st["n"]+=1;vals[name]["T"].append(T);vals[name]["J"].append(J);st["fermat_le_downprime"]+=int(T<=J+1);st["center_improve"]+=int(err<T);st["center_worse"]+=int(err>T);st["center_equal"]+=int(err==T)
            if iq==ip+1:adj+=1;st["adjacent"]+=1;assert q<2*p and T<=s-p
            if prevp==p:p_prev+=1
            if nextp==q:q_next+=1
            if prevp==p and nextp==q:both+=1
            improve+=int(err<T);worse+=int(err>T);equal+=int(err==T);maxshift=max(maxshift,abs(c-a0));maxgap=max(maxgap,gap);maxT=max(maxT,T);maxJ=max(maxJ,J);sievesum+=modular_retention(n);total+=1
            if p>kmax:
                seen[name]+=1;item=(n,p,q,q/p);R=reservoirs[name]
                if len(R)<reservoir_size:R.append(item)
                else:
                    j=rng.randrange(seen[name])
                    if j<reservoir_size:R[j]=item
    assert both==adj
    bands={}
    for name,_,_ in BANDS:
        st=stats[name];n=st["n"]
        bands[name]={"n":n,"T_median":qnearest(vals[name]["T"],.5),"T_p90_nearest_rank":qnearest(vals[name]["T"],.9),"J_median":qnearest(vals[name]["J"],.5),"J_p90_nearest_rank":qnearest(vals[name]["J"],.9),"fermat_le_downprime_fraction":st["fermat_le_downprime"]/n,"center_improve_fraction":st["center_improve"]/n,"center_worse_fraction":st["center_worse"]/n,"center_equal_fraction":st["center_equal"]/n,"adjacent_factor_count":st["adjacent"]}
    return {"limit":limit,"odd_distinct_semiprimes":total,"adjacent_factor_pairs":adj,"p_is_local_predecessor":p_prev,"q_is_local_successor":q_next,"both_local_neighbors":both,"local_center_improve_count":improve,"local_center_worse_count":worse,"local_center_equal_count":equal,"max_abs_local_center_shift_from_A0":maxshift,"max_local_prime_gap":maxgap,"max_Fermat_T":maxT,"max_downprime_rank_J":maxJ,"mean_modular_wheel_retention_64_3_5_7_11_13":sievesum/total,"bands":bands},reservoirs

def multik(reservoirs,kmax):
    pairs={k:divisor_pairs(k) for k in range(1,kmax+1)};out={}
    for name,_,_ in BANDS:
        rr=[];nr=[]
        for n,p,q,_ in reservoirs[name]:
            v=[]
            for k in range(1,kmax+1):
                if math.gcd(k,n)!=1:continue
                _,b,rho=shell_k(n,k);v.append((k,b,rho,oracle_tk(p,q,n,k,pairs)))
            good=min(v,key=lambda z:(z[3],z[0]));raw=sorted(v,key=lambda z:(z[1],z[0]));norm=sorted(v,key=lambda z:(z[2],z[0]))
            rr.append(1+next(i for i,z in enumerate(raw) if z[0]==good[0]));nr.append(1+next(i for i,z in enumerate(norm) if z[0]==good[0]))
        out[name]={"n":len(rr),"raw_residual_best_k_median_rank":median(rr),"raw_residual_best_k_top10_fraction":sum(x<=10 for x in rr)/len(rr),"raw_residual_best_k_max_rank":max(rr),"normalized_residual_best_k_median_rank":median(nr),"normalized_residual_best_k_top10_fraction":sum(x<=10 for x in nr)/len(nr)}
    return out

def gen_semiprime_bits(bits,name,target,rng):
    pbase=math.sqrt(2**(bits-.5)/target)
    for _ in range(20000):
        p0=max(3,int(pbase*math.exp(rng.uniform(-.12,.12))));p=next_prime64(p0 if p0&1 else p0+1);rt=target*math.exp(rng.uniform(-.01,.01));q0=max(p+2,int(p*rt));q=next_prime64(q0 if q0&1 else q0+1);n=p*q;r=q/p
        if n.bit_length()==bits and in_band(r,name):return n,p,q,r
    raise RuntimeError((bits,name,target))
def rankdata(xs):
    order=sorted(range(len(xs)),key=lambda i:xs[i]);ranks=[0.0]*len(xs);i=0
    while i<len(order):
        j=i+1
        while j<len(order) and xs[order[j]]==xs[order[i]]:j+=1
        r=(i+1+j)/2.0
        for k in range(i,j):ranks[order[k]]=r
        i=j
    return ranks
def pearson(xs,ys):
    mx,my=sum(xs)/len(xs),sum(ys)/len(ys);vx=sum((x-mx)**2 for x in xs);vy=sum((y-my)**2 for y in ys)
    return 0.0 if not vx or not vy else sum((x-mx)*(y-my) for x,y in zip(xs,ys))/math.sqrt(vx*vy)
def spearman(xs,ys):return pearson(rankdata(xs),rankdata(ys))
def holdout(per_cell,kmax):
    rng=random.Random(8292026);pairs={k:divisor_pairs(k) for k in range(1,kmax+1)};rows=[]
    for bits in HOLDOUT_BITS:
        for name,_,_ in BANDS:
            for _ in range(per_cell):
                n,p,q,r=gen_semiprime_bits(bits,name,TARGET_RATIOS[name],rng);s=math.isqrt(n);a0=s+1;prevp,nextp=prev_prime64(s),next_prime64(s+1);c=(prevp+nextp)//2;L=2*s+1;b0=a0*a0-n;v=[]
                for k in range(1,kmax+1):
                    if math.gcd(k,n)!=1:continue
                    _,bk,rho=shell_k(n,k);v.append((k,bk,rho,oracle_tk(p,q,n,k,pairs)))
                good=min(v,key=lambda z:(z[3],z[0]));raw=sorted(v,key=lambda z:(z[1],z[0]));norm=sorted(v,key=lambda z:(z[2],z[0]))
                rows.append({"bits":bits,"band":name,"phase":b0/L,"log_ratio":math.log(r),"center_shift":abs(c-a0),"wheel":modular_retention(n),"raw_rank":1+next(i for i,z in enumerate(raw) if z[0]==good[0]),"norm_rank":1+next(i for i,z in enumerate(norm) if z[0]==good[0])})
    bybit={};byband={}
    for bits in HOLDOUT_BITS:
        rr=[x for x in rows if x["bits"]==bits];bybit[str(bits)]={"n":len(rr),"shell_phase_vs_log_factor_ratio_spearman":spearman([x["phase"] for x in rr],[x["log_ratio"] for x in rr]),"max_local_center_shift":max(x["center_shift"] for x in rr),"mean_modular_wheel_retention":sum(x["wheel"] for x in rr)/len(rr)}
    for name,_,_ in BANDS:
        rr=[x for x in rows if x["band"]==name];byband[name]={"n":len(rr),"raw_residual_best_k_median_rank":median(x["raw_rank"] for x in rr),"raw_residual_best_k_top10_fraction":sum(x["raw_rank"]<=10 for x in rr)/len(rr),"normalized_residual_best_k_median_rank":median(x["norm_rank"] for x in rr),"normalized_residual_best_k_top10_fraction":sum(x["norm_rank"]<=10 for x in rr)/len(rr),"max_local_center_shift":max(x["center_shift"] for x in rr),"mean_modular_wheel_retention":sum(x["wheel"] for x in rr)/len(rr)}
    return {"per_bit_ratio_cell":per_cell,"total":len(rows),"by_bit":bybit,"by_ratio_band":byband}
def odd_prime_residue_count_theorem_check():
    rows=[]
    for ell in (3,5,7,11,13,17,19,23,29,31):
        sq={x*x%ell for x in range(ell)}
        for n in range(1,ell):
            got=sum(1 for a in range(ell) if (a*a-n)%ell in sq);leg=1 if pow(n,(ell-1)//2,ell)==1 else -1;assert got==(ell+leg)//2
        rows.append({"prime":ell,"verified_nonzero_N_residues":ell-1})
    return rows

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--limit",type=int,default=10_000_000);ap.add_argument("--reservoir",type=int,default=1000);ap.add_argument("--kmax",type=int,default=64);ap.add_argument("--holdout-per-cell",type=int,default=40);ap.add_argument("--output",default=None);a=ap.parse_args()
    census,res=exhaustive(a.limit,a.reservoir,a.kmax);out={"schema":"SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_CERTIFICATE_V1","task_id":"RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION","classification":"STRUCTURAL_ONLY","exact_theorem_checks":{"shell_to_fermat":"B^2=b+2*A0*T+T^2","hyperbolic_midpoint":"A/sqrt(N)=cosh(log(q/p)/2), B/sqrt(N)=sinh(log(q/p)/2)","neighbor_center":"A-c=(A-sqrt(N))+(sqrt(N)-c), so local-prime correction is bounded by half the local prime gap","multiplier_split":"for k=ab: (ap+bq)^2-(ap-bq)^2=4kN and ap+bq-2sqrt(kN)=(sqrt(ap)-sqrt(bq))^2","odd_prime_modular_filter_count":odd_prime_residue_count_theorem_check()},"exhaustive":census,"multik_reservoir_p_gt_kmax":multik(res,a.kmax),"holdout":holdout(a.holdout_per_cell,a.kmax),"counterexample":exact_witness(),"prior_art_boundary":{"Fermat_modular_wheel":"quadratic-residue filtering of A^2-N; shell form is a coordinate rewrite","Lehman":"systematic x^2-y^2=4kN multiplier near-square search; shell b_k is its starting residual","Hart_OLF":"sequential multiplier near-square test; raw shell-residual magnitude is not a new multiplier-selection principle"}}
    text=json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True)
    if a.output:open(a.output,"w",encoding="utf-8").write(text+"\n")
    print(text);print("SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_CHECK=PASS")
if __name__=="__main__":main()
