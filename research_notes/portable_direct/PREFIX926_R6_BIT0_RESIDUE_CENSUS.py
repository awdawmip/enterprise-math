#!/usr/bin/env python3
"""Exact i=0 named XOR witnesses on 64 full b rows; signed-source-preserving."""
import json,math,hashlib,sys
N=1<<32
QMIN,QMAX=262145,524287
M=131072
B=tuple(range(400001,400128,2))
assert len(B)==64 and all(QMIN<=b<=QMAX and b%2 for b in B)
D=set()
for b in range(QMIN,QMAX+1,2):
    x=2%b
    for d in range(1,32):
        if x==1 or x==b-1:
            D.add(b);break
        x=(2*x)%b
def outside(a,b):
    return not (b<33*((N+a-1)//a) or a<33*((N+b-1)//b) or (a//math.gcd(a,b))*b<N or b in D)
def ix(a,b):
    return ((a-QMIN)//2)*M+(b-QMIN)//2
def candidate(r,b):
    # Q has width less than b, hence at most one element in any residue class.
    if r<QMIN:r+=b
    if QMIN<=r<=QMAX and r%2:return r
    return None
pairs=set()
edge=set()
witness_cert=0
for b in B:
    for k in range(1,(N-1)//QMIN+1):
        if math.gcd(k,b)!=1:continue
        inv=pow(k,-1,b)
        for sign,r in ((-1,inv),(1,(-inv)%b)):
            a=candidate(r,b)
            if a is None:continue
            A=k*a
            if A+int(sign==1)>=N:continue
            assert (A+sign)%b==0
            x=int(sign==1)
            y=A+x
            assert 0<=x<N and 0<=y<N and (y-x)%a==0 and (y-(x^1))%b==0
            witness_cert+=1
            edge.add(ix(a,b));edge.add(ix(b,a))
            if outside(a,b):pairs.add(ix(a,b))
            if outside(b,a):pairs.add(ix(b,a))
b_idx={(b-QMIN)//2 for b in B}
forward_new=sum(1 for z in pairs if z%M in b_idx)
reverse_new=sum(1 for z in pairs if z//M in b_idx)
both=sum(1 for z in pairs if z%M in b_idx and z//M in b_idx)
res=dict(schema="PREFIX926_R6_BIT0_RESIDUE_CENSUS_V1",frozen_input="f42f2906d77f24085c123f3ccfe9667d41caa96d",
p=32,q_min=QMIN,q_max=QMAX,b_first=B[0],b_last=B[-1],b_count=len(B),
same_start_special_modulus_count=len(D),exact_parameter_witnesses=witness_cert,
orientation_union_before_BZS=len(edge),outside_BZS_union=len(pairs),
outside_BZS_forward=forward_new,outside_BZS_transpose=reverse_new,
outside_BZS_both_orientation=both,
bin_sha256=hashlib.sha256(b"".join(z.to_bytes(8,"little") for z in sorted(pairs))).hexdigest(),
validity="Entire 64 b rows; i=0 zero/flip witness family and time reversals, relative to B/Z/S")
assert (witness_cert,len(edge),len(pairs),forward_new,reverse_new,both)==(386923,773724,437560,218863,218819,122)
print(json.dumps(res,indent=2))
with open(sys.argv[1] if len(sys.argv)>1 else "PREFIX926_R6_BIT0_RESIDUE_RESULTS.json","w") as f:
    json.dump(res,f,indent=2);f.write("\n")
