"""Source-pinned X6 Unit149: exact finite carrier-class BRC fibre check.
Frozen science 59538f585d037d09ef687b28715c4bc1a3f9fe03
Native signed BRC kernel blob 300a96e3dc24bf6fff73743037a0347a8bc83176.
Current R062 bridge blob 97ab1403ab04b4fa80034625fb1b2e3ed115e59b.
This checker is independent reproduction, not execution of the pinned six-file benchmark.
"""
from collections import defaultdict
from math import factorial
import json

D = (1,1,1,0,0,0)
NAX=6

def compositions(n,r):
    if r==1:
        yield (n,)
    else:
        for i in range(n+1):
            for a in compositions(n-i,r-1):
                yield (i,)+a

def native_endpoint_multiplicity(length,z):
    if len(z)!=6: raise ValueError('6 signed axes required')
    pos=[max(x,0) for x in z]
    neg=[max(-x,0) for x in z]
    gap=length-sum(pos)-sum(neg)
    if gap<0 or gap%2: return 0
    total=0
    for ks in compositions(gap//2,6):
        den=1
        for a,b,k in zip(pos,neg,ks):
            den*=factorial(a+k)*factorial(b+k)
        total+=factorial(length)//den
    return total

def dp_walks(max_length):
    v={(0,)*6:1}
    for length in range(max_length+1):
        yield length,v
        nxt=defaultdict(int)
        for z,count in v.items():
            for i in range(6):
                for s in (-1,1):
                    nz=list(z);nz[i]+=s
                    nxt[tuple(nz)]+=count
        v=nxt

records=[]
for length, endpoints in dp_walks(8):
    max_k=length//3
    kernel={str(k):native_endpoint_multiplicity(length,tuple(k*x for x in D)) for k in range(-max_k,max_k+1)}
    dp={str(k):endpoints.get(tuple(k*x for x in D),0) for k in range(-max_k,max_k+1)}
    assert kernel==dp,(length,kernel,dp)
    mass=sum(kernel.values())
    nat=endpoints.get((0,)*6,0)
    assert nat==native_endpoint_multiplicity(length,(0,)*6)
    assert mass==sum(v for z,v in endpoints.items() if z[3:]==(0,0,0) and z[0]==z[1]==z[2])
    assert (mass>0 if length>=3 and length%2 else True)
    records.append({'length':length,'native_return':nat,'carrier_class_zero_mass':mass,'hidden_extra':mass-nat,'k_support':{k:v for k,v in kernel.items() if v},'dp_endpoints':len(endpoints)})
assert records[3]['native_return']==0 and records[3]['carrier_class_zero_mass']==12
assert records[5]['native_return']==0 and records[5]['carrier_class_zero_mass']==1080
print(json.dumps({'schema':'X6_UNIT149_CARRIER_CLASS_BRC_EXACT_RESULTS_V1','scope':'Z6 signed primitive +/- unit events, D=(1,1,1,0,0,0), L=0..8, Source-pinned kernel mathematical replica independently checked against full dynamic programming','cases':records,'claims_checked':['DP kernel exact for all kD with |k|<=L//3','carrier class zero mass equals full DP projection','L=3 mass=12; L=5 mass=1080; native odd returns=0'],'status':'FINITE_EXACT_EXECUTED_AUTHOR_UNREVIEWED_NOT_ADMITTED'},sort_keys=True,indent=2))
