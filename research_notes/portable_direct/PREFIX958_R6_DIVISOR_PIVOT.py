#!/usr/bin/env python3
"""PREFIX-958: signed-divisor pivot for adjacent odd-core named XOR collisions.
Exact integer computation. Primary Q19 generator never reads prior pair IDs.
Usage: python3 PREFIX958_R6_DIVISOR_PIVOT.py --prefix PREFIX958_R6
"""
from collections import Counter, defaultdict
from hashlib import sha256
from struct import pack
from time import perf_counter
import json, argparse

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
OLD_SHA = '1caec71f97ddb97c60c8506629f65651f0f3030b3526aeca30195948ee0cff75'

def residuals(p):
    z = defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (-1, 1):
                z[(1 << i)-s*(1 << j)].append((i,j,s))
    return z

def names(prod, triples):
    return sum(s == (1-2*((prod >> j) & 1)) for _,j,s in triples)

def reconstruct(p,k,m_min,m_max):
    H=1<<(p-1); low=H+1; high=2*H-1; half=H//2
    D=residuals(p); named=Counter(); gap_named=defaultdict(Counter); stats=Counter()
    tmax=2*k
    for m in range(m_min,m_max+1):
        for c,cs in D.items():
            for C,Cs in D.items():
                delta=C-c
                if m&1:
                    if not delta&1: continue
                elif m%4==0:
                    if delta%4!=2: continue
                else:
                    if delta%4!=0: continue
                stats['residual_pairs_mod4']+=1
                N=k*C-(k+2)*c
                if N==0:
                    stats['zero_numerator_resonance_candidates']+=1
                    # d=0 implies t=k*m/2. t<=2*k and t>=1 imply m in (2,4).
                    if m in (2,4) and c%k==0:
                        r=m//2
                        h=c//k
                        for b in range(low,high+1,2):
                            a=r*b+h
                            if a<low or a>high or not (a&1) or a==b:continue
                            stats['resonance_domain_candidates']+=1
                            v=names(k*a,cs);w=names((k+2)*a,Cs)
                            stats['named_sign_triples_tested']+=len(cs)+len(Cs)
                            if v and w:
                                ident=((a-low)//2)*half+(b-low)//2
                                named[ident]+=v*w;gap_named[m][ident]+=v*w
                                stats['resonant_named_histories']+=v*w
                    continue
                mag_lo=max(1,(abs(N)+high-1)//high)
                mag_hi=abs(N)//low
                if mag_lo>mag_hi: continue
                dlow=2-k*m; dhigh=2*tmax-k*m
                if N>0:
                    a0=max(dlow,mag_lo); b0=min(dhigh,mag_hi)
                else:
                    a0=max(dlow,-mag_hi); b0=min(dhigh,-mag_lo)
                if a0>b0:continue
                a0+= (k*m-a0)&1
                for d in range(a0,b0+1,2):
                    if not d:continue
                    t=(d+k*m)//2;T=t+m
                    if t<1 or t>tmax or T<1: continue
                    stats['divisor_interval_candidates']+=1
                    if N%d:continue
                    stats['actual_divisors']+=1
                    b=N//d
                    if b<low or b>high or not(b&1):continue
                    twice_a=m*b+delta
                    if twice_a&1:continue
                    a=twice_a//2
                    if a<low or a>high or not(a&1) or a==b:continue
                    stats['domain_candidates']+=1
                    assert k*a-t*b==c and (k+2)*a-T*b==C
                    v=names(k*a,cs);w=names((k+2)*a,Cs)
                    stats['named_sign_triples_tested']+=len(cs)+len(Cs)
                    if v and w:
                        ident=((a-low)//2)*half+(b-low)//2
                        named[ident]+=v*w;gap_named[m][ident]+=v*w
    out={'p':p,'k':k,'m_range':[m_min,m_max],'frozen_science':PIN,
         'distinct_non_diagonal_pairs':len(named),'joint_named_histories':sum(named.values()),
         'gap_pairs':{str(m):len(gap_named[m]) for m in range(m_min,m_max+1)},
         'gap_named':{str(m):sum(gap_named[m].values()) for m in range(m_min,m_max+1)},
         'stats':dict(stats),
         'named_multiplicity_histogram':dict(sorted(Counter(named.values()).items()))}
    binary=b''.join(pack('<Q',i) for i in sorted(named))
    out['sorted_ids_sha256']=sha256(binary).hexdigest()
    out['sorted_ids_bytes']=len(binary)
    return named,gap_named,binary,out

def original_brute(p,k):
    h=1<<(p-1); Q=range(h+1,2*h,2); half=h//2
    pair=Counter(); gaps=defaultdict(Counter)
    for a in Q:
        for b in Q:
            if a==b:continue
            by=[]
            for core in [k,k+2]:
                f=Counter();v=core*a
                for i in range(p):
                    for j in range(p):
                        q=(v^(1<<j))-(1<<i)
                        if q>0 and q%b==0:
                            f[q//b]+=1
                by.append(f)
            ident=((a-h-1)//2)*half+(b-h-1)//2
            for t,v in by[0].items():
                for T,w in by[1].items():
                    pair[ident]+=v*w;gaps[T-t][ident]+=v*w
    return pair,gaps

def small_tests():
    reports=[]
    for p in range(4,7):
        h=1<<(p-1)
        for k in range(1,h-2,2):
            exact,g=original_brute(p,k)
            got,gg,_,_=reconstruct(p,k,1-2*k,2*(k+2)-1)
            assert exact==got,(p,k,'pair')
            assert dict(g)=={m:gg[m] for m in gg if gg[m]},(p,k,'gap')
            reports.append([p,k,len(exact),sum(exact.values())])
    return reports

def main():
    a=argparse.ArgumentParser();a.add_argument('--prefix',default='PREFIX958_R6');args=a.parse_args()
    t=perf_counter(); small=small_tests(); t_small=perf_counter()-t
    t=perf_counter(); named,gap,binary,r=reconstruct(19,21,0,6); t_big=perf_counter()-t
    assert len(named)==6203 and sum(named.values())==8649
    assert [len(gap[m]) for m in range(7)]==[6,442,4724,839,190,3,0]
    assert [sum(gap[m].values()) for m in range(7)]==[6,614,6509,1286,231,3,0]
    assert sha256(binary).hexdigest()==OLD_SHA
    r.update({'small_width_checked':small,'small_width_elapsed_seconds':round(t_small,5),
              'q19_elapsed_seconds':round(t_big,5),
              'old_generator_scalar_divisibility_tests':22699951,
              'prior_sha256_expected':OLD_SHA})
    open(args.prefix+'_EXACT_RESULTS.json','w').write(json.dumps(r,indent=2,sort_keys=True)+'\n')
    open(args.prefix+'_OFFDIAG_IDS.bin','wb').write(binary)
    print(json.dumps(r,indent=2,sort_keys=True))
if __name__=='__main__': main()
