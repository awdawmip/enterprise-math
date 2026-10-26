"""Exact six-edge BRC source DP vs layer-sign and Lucas formulas."""
from collections import defaultdict
from math import comb
import json

edge = {0:{0:(2,-1,-1),1:(2,1,-1)},
        1:{0:(0,-1,-1),1:(0,1,-1)},
        2:{0:(1,1,1),1:(2,1,-1)}}
def total(n,b):
    r=n-3*b
    if r<0:return 0
    if r==0:return 1
    return sum((2**j)*comb(b,j)*comb(r-1,j-1)
               for j in range(1,min(b,r)+1))

N=80
S={(0,2,1,0,0):1}  # q, prior_bit (2 initially), epsilon, k, completed blocks
L0,L1=2,1
checks=0
examples=[]
for n in range(N+1):
    if n>0:
        counts=defaultdict(lambda:[0,0]); fibers=defaultdict(int)
        for (q,prev,e,k,b),v in S.items():
            if q==0:
                counts[b][e<0]+=v
                fibers[e,k]+=v
        P=M=0
        for b in range(1,n//3+1):
            p,m=counts[b]
            assert p+m==total(n,b) and p-m==(n==3*b)
            checks+=1;P+=p;M+=m
        if n==1:L=L1
        else:
            L0,L1=L1,L0+L1
            L=L1
        chi=(3,-1,-3,1)[n%4]
        assert (L+chi)%5==0 and P+M==(L+chi)//5
        assert P-M==(n%3==0)
        if n==7:
            assert fibers[1,-3]>=1 and fibers[-1,-1]>=1
        if n in (3,4,6,7,9,20,40,80):
            examples.append({'n':n,'plus':str(P),'minus':str(M),'total':str(P+M)})
    if n==N:break
    nxt=defaultdict(int)
    for (q,prev,e,k,b),v in S.items():
        for bit,(q2,eta,c) in edge[q].items():
            if prev==0 and bit==0:continue
            nxt[q2,bit,eta*e,eta*k+c,b+(q==1 and q2==0)]+=v
    S=nxt
print(json.dumps({'schema':'EM_R3_BSIGN_V1','status':'PASS',
 'method':'independent six-edge BigInt source DP retaining q/previous/epsilon/k/blocks',
 'range_n':[1,N],'layer_checks':checks,
 'all_length_sign_excess':'1 iff n divisible by 3',
 'Lucas_periodic_total':'(L_n+chi_n)/5; chi=(3,-1,-3,1)',
 'full_effect_witness':'A1 A2: (+,-3); A1 B2: (-,-1), same profile (3,4)',
 'samples':examples,'finite_check_is_universal_proof':False,
 'independent_driver_review':'NOT_PERFORMED'},ensure_ascii=False,indent=2))
