#!/usr/bin/env python3
"""PREFIX-967: parity-directed quotient inversion + target-side sign reconstruction.
No external dependencies. Auxiliary integer observer, not a native P000/BRC proof.
"""
import json, hashlib
from collections import defaultdict, Counter
from time import perf_counter

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'

def slots_by_value(p):
    z=defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (-1,1):
                z[(1<<i)-s*(1<<j)].append((i,j,s))
    even=sorted((c,tuple(src)) for c,src in z.items() if c%2==0)
    odd=sorted((c,tuple(src)) for c,src in z.items() if c%2)
    return even,odd

def target_sign_ok(t,b,i,j,s):
    # y = x xor 2^j = t*b+2^i. For x=y-s*2^j, s=+1 iff bit_j(y)=1.
    return ((t*b+(1<<i))>>j)&1 == (s==1)

def reconstruct(p,k,m):
    assert p>=4 and k>=1 and (k&1) and k+2 < 1<<(p-1) and m in (1,3,5)
    H=1<<(p-1); lo=H+1; hi=2*H-1
    ev,od=slots_by_value(p)
    hist=Counter(); tuples=[]; stats=Counter()
    for t in range(1,2*k+1):
        # ka-tb ≡ 1-t (mod 2); odd m reverses the second parity
        left,right=(ev,od) if (t&1) else (od,ev)
        for c,cs in left:
            for C,Cs in right:
                stats['divisibility_tests']+=1
                N=k*C-(k+2)*c;d=2*t-k*m
                assert N&1 and d&1
                if N%d:continue
                b=N//d
                if not(lo<=b<=hi and b&1):continue
                a2=m*b+C-c
                if a2&3 != 2:continue
                a=a2//2
                if not(lo<=a<=hi and a&1) or a==b:continue
                stats['arithmetic_candidates']+=1
                assert k*a-t*b==c and (k+2)*a-(t+m)*b==C
                sl=[(i,j) for i,j,s in cs if target_sign_ok(t,b,i,j,s)]
                sr=[(I,J) for I,J,S in Cs if target_sign_ok(t+m,b,I,J,S)]
                stats['slot_sign_predicates']+=len(cs)+len(Cs)
                for i,j in sl:
                    for I,J in sr:
                        assert (((k*a)^(1<<j))-(1<<i))==t*b
                        assert ((((k+2)*a)^(1<<J))-(1<<I))==(t+m)*b
                        tup=(a,b,t,t+m,i,j,I,J)
                        tuples.append(tup)
                if sl and sr:
                    hist[(a,b)] += len(sl)*len(sr)
    assert len(tuples)==sum(hist.values())
    assert len(set(tuples))==len(tuples)
    lines=''.join(','.join(map(str,x))+'\n' for x in sorted(tuples))
    return hist, {
        'p':p,'k':k,'m':m,'number_of_modulus_pairs':len(hist),
        'named_joint_histories':len(tuples), 'stats':dict(stats),
        'tuples_sha256':hashlib.sha256(lines.encode()).hexdigest(),
        'examples':sorted(tuples)[:3],
    }

def direct(p,k,m):
    H=1<<(p-1);lo=H+1;res=Counter()
    for a in range(lo,2*H,2):
        left=defaultdict(list);right=defaultdict(list)
        for i in range(p):
            for j in range(p):
                x=((k*a)^(1<<j))-(1<<i)
                y=(((k+2)*a)^(1<<j))-(1<<i)
                if x>0:left[x].append((i,j))
                if y>0:right[y].append((i,j))
        for x,li in left.items():
            for y,ri in right.items():
                # y-x=m*b; direct source-first, no numeric residual search
                d=y-x
                if d<=0 or d%m:continue
                b=d//m
                if b!=a and lo<=b<2*H and b&1 and x%b==0:
                    res[(a,b)]+=len(li)*len(ri)
    return res

def main():
    cases=[]; started=perf_counter()
    for p in range(4,8):
        H=1<<(p-1)
        for k in range(1,H-2,2):
            for m in (1,3,5):
                found,meta=reconstruct(p,k,m)
                check=direct(p,k,m)
                assert found==check,(p,k,m,found-check,check-found)
                cases.append({'p':p,'k':k,'m':m,'pairs':len(found),'named':sum(found.values())})
    big=[]
    for m in (1,3,5):
        found,meta=reconstruct(19,21,m)
        big.append(meta)
    assert [(z['number_of_modulus_pairs'],z['named_joint_histories']) for z in big]==[(442,614),(839,1286),(3,3)]
    assert [z['tuples_sha256'] for z in big]==[
        'ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71',
        '1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3',
        'c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b']
    r={'schema':'PREFIX967_R6_PARITY_DIRECTED_TARGET_SIDE_BITS_V1','pin':PIN,
       'model':'auxiliary named integer XOR collisions, k and k+2 odd, strict p-bit odd moduli',
       'proof_status':'AUTHOR_PROOF_EXACT_INTEGER_VERIFIED_NOT_REVIEWED',
       'direct_independent_small_cases':cases,'q19_k21_odd_gap_results':big,
       'total_elapsed_seconds':round(perf_counter()-started,4),
       'limitation':'Candidate arithmetic tests only, not full runtime speedup; no native X6 or BRC status change'}
    with open('PREFIX967_R6_EXACT_RESULTS.json','w') as f:json.dump(r,f,indent=2);f.write('\n')
    print(json.dumps({'small_checks':len(cases),'big':big,'total_elapsed_seconds':r['total_elapsed_seconds']},indent=2))

if __name__=='__main__':main()
