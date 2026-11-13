#!/usr/bin/env python3
"""PREFIX-597-R2: standalone exact native X6-BRC instantaneous decoder certificate.
Frozen original phase model, 96 ports, 576 labeled actions. Python stdlib only.
The interpolation tests establish a universal polynomial matrix identity.
"""
from itertools import product
from pathlib import Path
from random import Random
import json

STARS=((1,3,6),(1,4,5),(2,3,5),(2,4,6))
def near(a,c):
    return tuple(-k if c>0 else k for k in STARS[a] if k!=abs(c))
P=tuple((a,p,t*k) for a in range(4) for k in STARS[a]
        for t in (-1,1) for p in near(a,t*k))
IX={v:i for i,v in enumerate(P)}
def nxt(i):
    a,p,c=P[i]
    b=next(b for b in range(4) if b!=a and abs(c) in STARS[b])
    return tuple(IX[v] for v in ([(a,c,k) for k in near(a,c) if k!=p]
                                  +[(b,c,k) for k in near(b,c)]))
N=tuple(nxt(i) for i in range(48))
G=IX[(0,1,-3)]
REV=tuple(IX[(a,c,p)] for a,p,c in P)
RG=REV[G]
H=tuple(i for i in range(48) if G in N[i])
AXIS=tuple(abs(c)-1 for a,p,c in P)
assert len(P)==48 and G==4 and H==(3,14,15) and RG==2
assert G not in N[G] and RG not in H and all(AXIS[i]==0 for i in H+(RG,))

def native_step(r,x,z):
    """Every original one of 576 distinct typed port actions."""
    out=[0]*96
    for i in range(48):
        k=AXIS[i]
        for j in N[i]:
            for u,v in product((0,1),repeat=2):
                weight=x[0]*z if (j==G and u==v==1) else x[k]
                out[2*i+u]+=weight*r[2*j+v]
    return out

def encode(r):
    return [r[2*i] if i==G else r[2*i]+r[2*i+1] for i in range(48)]
def embed(v):
    r=[0]*96
    for i in range(48):
        r[2*i]=v[i]
        r[2*i+1]=v[i] if i==G else 0
    return r

def q_step(v,x,z):
    out=[0]*48
    for i in range(48):
        if i==G:
            out[i]=x[AXIS[i]]*sum(v[j] for j in N[i])
        else:
            out[i]=x[AXIS[i]]*(2*sum(v[j] for j in N[i] if j!=G)
                       +(z+3)*v[G]*int(G in N[i]))
    return out

def L(v):
    return sum(v[i] for i in H)-2*v[RG]
def decoder_numerator(v,z):
    """6*(z+3) times the memoryless 96-port decoder."""
    d=(z-1)*L(v)
    out=[0]*96
    for i in range(48):
        if i==G:
            out[2*i]=out[2*i+1]=6*(z+3)*v[i]
        else:
            c=3*(z+3)*v[i]
            e=d if i in H else 0
            out[2*i],out[2*i+1]=c-e,c+e
    return out

def decoder_integer(v,z):
    den=3*(z+3)
    dnum=(z-1)*L(v)
    assert dnum%den==0,(z,L(v))
    d=dnum//den
    out=[0]*96
    for i in range(48):
        if i==G:
            out[2*i]=out[2*i+1]=v[i]
        else:
            e=d if i in H else 0
            assert (v[i]-e)%2==0 and (v[i]+e)%2==0
            out[2*i]=(v[i]-e)//2
            out[2*i+1]=(v[i]+e)//2
    return out,d

# Six original axis basis weights times three gate points z=0,1,2,
# times 48 coordinate basis vectors. Both sides are linear in the x_a
# and degree <=2 in z after clearing 6(z+3); hence this certifies the
# full polynomial identity, not just the tested parameter values.
poly_checks=0
for a in range(6):
    x=[int(k==a) for k in range(6)]
    for z in (0,1,2):
        for j in range(48):
            e=[int(k==j) for k in range(48)]
            o=native_step(embed(e),x,z)
            v=encode(o)
            assert v==q_step(e,x,z)
            assert decoder_numerator(v,z)==[6*(z+3)*w for w in o]
            assert L(v)==3*x[0]*(z+3)*e[G]
            poly_checks+=1
assert poly_checks==864

# Full original 96-port comparison, nonstationary integer weights.
rng=Random(5971108)
inputs=[[int(i==j) for i in range(96)] for j in range(96)]
inputs += [[rng.randrange(0,5) for i in range(96)] for t in range(24)]
seqs=[]
for p in range(6):
    seq=[]
    for t in range(9):
        x=[rng.randrange(0,8) for i in range(6)]
        if p==0:x=[1]*6
        if p==1:x=[2,3,5,7,11,13]
        z=[0,1,2,3,5,0,1,4,7][(t+p)%9]
        seq.append((x,z))
    seqs.append(seq)
path_checks=0
for r0 in inputs:
    for seq in seqs:
        r=native_step(r0,*seq[0])
        v=encode(r)
        for x,z in seq[1:]:
            previous_g=v[G]
            r=native_step(r,x,z)
            v=q_step(v,x,z)
            assert v==encode(r)
            decoded,delta=decoder_integer(v,z)
            assert decoded==r and min(decoded)>=0
            assert delta==x[0]*(z-1)*previous_g
            assert L(v)==3*x[0]*(z+3)*previous_g
            path_checks+=1
assert path_checks==5760

# Necessary t>=2 boundary: initial marked bit pair may be unequal.
r0=[0]*96;r0[2*G+1]=1
r1=native_step(r0,[1]*6,0)
v1=encode(r1)
assert decoder_numerator(v1,0)!=[18*w for w in r1]

result={
    "schema":"PREFIX597_R2_INSTANTANEOUS_NATIVE_BRC_DECODER_V1",
    "scientific_input":"f42f2906d77f24085c123f3ccfe9667d41caa96d",
    "phase_count":48,"port_count":96,"labeled_edges":576,
    "gate_phase":G,"gate_predecessors":H,"reversal_phase":RG,
    "decoder":"delta=(z-1)*(v[3]+v[14]+v[15]-2*v[2])/(3*(z+3))",
    "exact_polynomial_basis_checks":poly_checks,
    "exact_local_row_identity_checks":poly_checks,
    "nonstationary_full_port_checks":path_checks,
    "integer_parity_coordinate_checks":path_checks*47,
    "initial_input_families":len(inputs),
    "sequences":len(seqs),"boundary_first_step_counterexample":True,
    "result":"ALL_ASSERTIONS_PASS",
    "review":"AUTHOR_SIDE_UNREVIEWED"
}
out=Path(__file__).with_name("PREFIX597_R2_instantaneous_gate_decoder_results.json")
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(result["result"],"polynomial",poly_checks,"native",path_checks)
