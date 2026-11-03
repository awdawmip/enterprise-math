from fractions import Fraction as Q
from random import Random
from itertools import product

M = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),(0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A=(0,0,0,1,1,1); B=(2,2,3,2,2,4); C=(5,6,7,8,9,10)
PAIRS=((3,31),(7,27),(11,23),(15,19))
BETAS=((Q(0),Q(0)),(Q(9,10),Q(0)),(Q(0),Q(9,10)),(Q(1,2),Q(1,3)),(Q(9,10),Q(3,4)),(Q(19,20),Q(3,4)))

def op_masks(pair):
    n,e = pair if not pair[0]&4 else (pair[1],pair[0])
    assert n&4 == 0 and e&4
    return n,e

def views(z,pair,bn,be):
    n,e=op_masks(pair)
    out={}
    for key,mask,beta in (("N",n,bn),("E",e,be)):
        v=list(z)
        for i in range(5):
            if mask>>i & 1: v[i]=beta
        raws=[]
        for i in range(6):
            p,q,r=v[A[i]],v[B[i]],v[C[i]]
            raws.append((p,(1-p)*q,(1-p)*(1-q)*r,(1-p)*(1-q)*(1-r)))
        for row in range(6):
            for k in range(4):
                out[(key,row,k)]=sum((Q(M[row][i],20)*raws[i][k] for i in range(6)),Q(0))
    return out

def gate_views(pair,g):
    n,e=op_masks(pair)
    return ("N","E") if not (n>>g & 1) else ("E","N")

def bank(z,pair,j,bn,be):
    t=views(z,pair,bn,be)
    keys=[(v,r,k) for v,r,k in product(("N","E"),range(6),range(4)) if r!=j]
    if j in (0,1,3,4): keys.append(("E",j,2))
    else:
        g=3 if j==2 else 4
        u,v=gate_views(pair,g)
        keys.extend(((u,j,1),(v,j,2)))
    assert len(keys)==(42 if j in (2,5) else 41)
    return {key:t[key] for key in keys}

def features(bank_values,pair,j):
    u3,v3=gate_views(pair,3);u4,v4=gate_views(pair,4)
    return tuple(bank_values[key] for key in (("N",1 if j==0 else 0,1),(u3,2,1),(u4,5,1),(v3,2,2),(v4,5,2),("E",0,2),("E",1,2),("E",3,2),("E",4,2)))

def recover(y,pair,bn,be):
    an,ae=1-bn,1-be
    u3,v3=gate_views(pair,3);u4,v4=gate_views(pair,4)
    av=lambda v:an if v=="N" else ae
    t0,t1,t3,t4=(v/(ae*ae) for v in y[5:9])
    return (y[0]/an,y[1]/av(u3),y[2]/av(u4),11*t0-10*t1,-9*t0+10*t1,y[3]/av(v3)**2,(9*t3-5*t4)/4,(-t3+5*t4)/4,y[4]/av(v4)**2)

def coeff(pair,bn,be):
    an,ae=1-bn,1-be
    return max(Q(21)/(ae*ae),Q(1)/an if pair==(3,31) else Q(1)/(an*an))

def witness(mode,pair,bn,be):
    base=[Q(1,2)]*11
    z=base[:];w=base[:]
    if mode=="E":
        z[2]=w[2]=Q(1)
        h=Q(1,1000)*(1-be)**2
        z[5]+=21*h;w[5]-=21*h
        z[6]-=19*h;w[6]+=19*h
        expect=Q(21)/(1-be)**2
    elif mode=="N":
        h=Q(1,1000)*(1-bn)
        z[2]+=h;w[2]-=h
        expect=Q(1)/(1-bn)
    else:
        n,e=op_masks(pair)
        gs=[g for g in (3,4) if n>>g&1 and not e>>g&1]
        assert gs
        g=gs[0];x=7 if g==3 else 10
        z[g]=w[g]=Q(1)
        h=Q(1,1000)*(1-bn)**2
        z[x]+=h;w[x]-=h
        expect=Q(1)/(1-bn)**2
    assert all(0<=v<=1 for v in z+w)
    return z,w,expect

def sup_diff(a,b):return max(abs(x-y) for x,y in zip(a,b))

rng=Random(202611031658)
checked_pairs=checked_witness=checked_noise=0
for pair,beta_pair,j in product(PAIRS,BETAS,range(6)):
    bn,be=beta_pair
    cc=coeff(pair,bn,be)
    for _ in range(8):
        z=[Q(rng.randrange(0,17),16) for i in range(11)]
        w=[Q(rng.randrange(0,17),16) for i in range(11)]
        p=bank(z,pair,j,bn,be);q=bank(w,pair,j,bn,be)
        assert recover(features(p,pair,j),pair,bn,be)==tuple(z[2:])
        assert recover(features(q,pair,j),pair,bn,be)==tuple(w[2:])
        assert sup_diff(z[2:],w[2:])<=cc*max(abs(p[k]-q[k]) for k in p)
        checked_pairs+=1
    for mode in (("E","N") if pair==(3,31) else ("E","N","G")):
        z,w,expected=witness(mode,pair,bn,be)
        p=bank(z,pair,j,bn,be);q=bank(w,pair,j,bn,be)
        ratio=sup_diff(z[2:],w[2:])/max(abs(p[k]-q[k]) for k in p)
        assert ratio==expected,(pair,bn,be,j,mode,ratio,expected)
        midpoint=[(a+b)/2 for a,b in zip(z,w)]
        bmid=bank(midpoint,pair,j,bn,be)
        assert all(bmid[k]==(p[k]+q[k])/2 for k in p)
        checked_witness+=1
    modes=("E","N") if pair==(3,31) else ("E","N","G")
    assert any(witness(mode,pair,bn,be)[2]==cc for mode in modes)
    checked_noise+=1
print("PASS_BRC_S23_FULL_BANK_ALL_BETAS_SHARP_INVERSE_20261103")
print("reconstruction_and_upper_checks",checked_pairs)
print("exact_sharpness_and_coherent_midpoint_checks",checked_witness)
print("global_minimax_modes",checked_noise)
print("special_case_(3,31)_j0_bn9/10_be0_C",coeff((3,31),Q(9,10),Q(0)))
