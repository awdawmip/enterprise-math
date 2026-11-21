#!/usr/bin/env python3
"""R284CO: 63-point rigidity of the frozen Port k-fold spectrum.
Exact finite integer checker; standard library only; no native-X6 transfer.
"""
import hashlib, json
from itertools import product

P = 17179869143
D = (1120832, 6, 13, 1651128)
Z = (0, 390139, 394465, 1497639)
SELECT = (0, 1, 2, 4, 5, 6)
FROZEN_SHA = 'b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4'

def det(L, top):
    u1,a,x,y,u2,w,b,z,u3,g,h,r = L
    t,s = 6-a,13-b
    u = t*s-x*w
    v = -r*u-z*(t*h+x*g)-y*(w*h+s*g)
    p1,p2 = s*u1+x*u2,t*u2+w*u1
    q1 = -r*p1-u1*z*h+x*z*u3+y*(u2*h+s*u3)
    q2 = -r*p2+t*z*u3+u1*z*g+y*(w*u3-u2*g)
    q3 = u*u3+p1*g+p2*h
    k = (u*D[3]+v,p1*D[3]+q1,p2*D[3]+q2,q3)
    base = D[0]*k[0]-Z[1]*k[1]-Z[2]*k[2]-Z[3]*k[3]-sum(k)
    return base-sum(k[j] for j in range(4) if top & (1<<j))

def arcs():
    out=[]
    for key in range(64):
        lo=[1]*12; hi=[2]*12
        for j,pos in enumerate(SELECT):
            lo[pos]=hi[pos]=1+((key>>(5-j))&1)
        h=det(hi,15)
        out.append((h%P,det(lo,0)-h))
    return out

def words():
    digest=hashlib.sha256(); vals=[]
    for upper in product((1,2),repeat=4):
        top=sum((v-1)<<j for j,v in enumerate(upper))
        for lower in product((1,2),repeat=12):
            x=det(lower,top)%P
            digest.update(x.to_bytes(8,'big'))
            vals.append(x)
    assert digest.hexdigest()==FROZEN_SHA
    assert len(vals)==len(set(vals))==65536
    return vals

def dist(x,arc):
    a,w=arc; d=(x-a)%P
    return 0 if d<=w else min(d-w,P-d)

def main():
    A=arcs(); X=words()
    assert len(A)==64 and all(0<w<P//2 for a,w in A)
    U=[-1]*64; second=[-1]*64; index=[-1]*64; ties=[0]*64
    for i,x in enumerate(X):
        ds=sorted(dist(x,a) for a in A)
        for j,d in enumerate(ds):
            if d>U[j]:
                second[j],U[j]=U[j],d
                index[j],ties[j]=i,1
            elif d==U[j]:
                ties[j]+=1
            elif d>second[j]:
                second[j]=d
    assert U[0]==0 and ties[0]==65536
    assert all(ties[j]==1 and U[j]>second[j] for j in range(1,64))
    assert len(set(index[1:]))==63
    core=[X[index[j]] for j in range(1,64)]
    assert [max(sorted(dist(x,a) for a in A)[j] for x in core)
            for j in range(64)]==U
    margins=[U[j]-second[j] for j in range(1,64)]
    assert min(margins)==64
    cert={
      'schema':'R284CO_SPECTRAL_WITNESS_RIGIDITY_V1',
      'scope':'frozen auxiliary Port observer; 65536 distinct codewords, 64 arcs',
      'status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'pins':{'P':P,'D':D,'Z':Z,'SELECT':SELECT,'frozen_sha256':FROZEN_SHA},
      'counts':{'codewords':65536,'arcs':64,'distance_evaluations':4194304,
                'essential_witnesses':63,'minimal_spectrum_preserving_subset':63},
      'U_all_64':U,'k1_ties':ties[0],
      'winner_index_k2_to_k64':index[1:],
      'winner_residue_k2_to_k64':core,
      'strict_margin_k2_to_k64':margins,
      'minimum_margin':min(margins),
      'minimum_margin_levels':[j+2 for j,d in enumerate(margins) if d==min(margins)],
      'k54':{'winner_index':index[53],'winner_residue':core[52],
             'U54':U[53],'runner_up':second[53],'margin':margins[52]},
      'verification':{'arithmetic':'Python unbounded exact integer',
                      'population_exhausted':True,'maximizers_unique_k2_to_k64':True,
                      'maximizers_pairwise_distinct':True,'core_recomputation_equal':True,
                      'independent_review':'NOT_REVIEWED'}
    }
    with open('/mnt/data/R284CO_spectral_witness_certificate.json','w',encoding='utf-8') as f:
        json.dump(cert,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({'core':63,'margin_min':min(margins),
                      'margin_levels':cert['minimum_margin_levels'],'k54':cert['k54']}))

if __name__=='__main__':main()
