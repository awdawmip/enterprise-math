#!/usr/bin/env python3
"""Exact checks for frozen X6 candidate signed BRC negative-port Hankel theorem.
Pure integer arithmetic. This reproduces finite cases, not the general proof.
"""
from collections import defaultdict
from functools import lru_cache
from math import factorial
import json

D = 6
E0 = (0,) * D
E1 = (1, 0, 0, 0, 0, 0)
PORTS = tuple((j,sgn) for j in range(D) for sgn in (1,-1))


def compositions(n,d):
    if d==1:
        yield (n,)
    else:
        for k in range(n+1):
            for rest in compositions(n-k,d-1):
                yield (k,)+rest

@lru_cache(None)
def power_S(n):
    f=factorial
    result={}
    for a in compositions(n,D):
        w=f(n)
        for ai in a: w//=f(ai)
        result[a]=w
    return result


def amplitude_N(n,j):
    """z_j^-1 S^(n-3)(S-6z_j)(S-z_1); n >= 5."""
    assert n>=5 and 0<=j<D
    m=n-3
    ej=tuple(int(k==j) for k in range(D))
    e1=E1
    p=defaultdict(int)
    terms=((m+2,1,tuple(-v for v in ej)),
           (m+1,-6,E0),
           (m+1,-1,tuple(a-b for a,b in zip(e1,ej))),
           (m,6,e1))
    for r,mul,shift in terms:
        for a,v in power_S(r).items():
            key=tuple(ai+si for ai,si in zip(a,shift))
            p[key]+=mul*v
    return {k:v for k,v in p.items() if v}


def norm2(poly):
    return sum(int(x)**2 for x in poly.values())


def native_grade_one_masses():
    # Native integer, named-port W(h,d)=1-6*[h=d], signed paths
    states={(E0,(0,-1),0):1}
    observed={}
    for n in range(1,9):
        nxt=defaultdict(int)
        for (x,h,k),amp in states.items():
            for j,sgn in PORTS:
                newk=k+int(sgn==-1)
                if newk>1:continue
                if (x==E0 and j==0 and sgn==1) or (x==E1 and j==0 and sgn==-1):
                    continue
                nx=list(x);nx[j]+=sgn
                weight=1-6*int(h==(j,sgn))
                nxt[(tuple(nx),(j,-sgn),newk)]+=amp*weight
        states={key:amp for key,amp in nxt.items() if amp}
        if n>=5:
            q=[[0]*D for _ in range(2)]
            for (x,h,k),amp in states.items():
                if k!=1:continue
                j,insign=h
                q[int(insign==1)][j]+=amp*amp
            observed[n]={"positive":q[0],"negative":q[1]}
    return observed


def determinant(mat):
    a=[list(row) for row in mat]
    N=len(a)
    if N==1:return a[0][0]
    sign=1; old=1
    for k in range(N-1):
        if a[k][k]==0:
            found=next((t for t in range(k+1,N) if a[t][k]),None)
            if found is None:return 0
            a[k],a[found]=a[found],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,N):
            for j in range(k+1,N):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value%old==0
                a[i][j]=value//old
        for i in range(k+1,N):a[i][k]=0
        old=pivot
    return sign*a[-1][-1]


def main():
    native=native_grade_one_masses()
    neg1={n:norm2(amplitude_N(n,0)) for n in range(5,12)}
    neg2={n:norm2(amplitude_N(n,1)) for n in range(5,12)}
    for n,record in native.items():
        assert record["negative"][0]==neg1[n]
        assert record["negative"][1]==neg2[n]
        assert len(set(record["negative"][1:]))==1
    delta={n:neg1[n]-neg2[n] for n in neg1}
    assert all(v>0 for v in delta.values())
    dets={}
    for name,seq in (("Q_minus_axis1",neg1),("Q_minus_axis2",neg2),("delta_minus",delta)):
        dets[name]={}
        for size in range(1,4):
            matrix=[[seq[5+i+j] for j in range(size)] for i in range(size)]
            v=determinant(matrix)
            assert v>0
            dets[name][str(size)]=str(v)
    result={
        "schema":"PREFIX1022_R6_BRC_HANKEL_INTEGER_EVIDENCE_V1",
        "scientific_pin":"enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json",
        "candidate_kernel":"W(h,d)=1-6[h=d], 12 named ports, signed X6 cell torsor",
        "absorbing_link":"{0,e1} both orientations",
        "seed":"(chosen cell 0, incoming neighbour port -e1)",
        "grade":"exactly one negative outgoing native direction",
        "operations":"native integer BRC n=1..8; independent integer Laurent coefficient norm n=5..11; exact Bareiss 1x1 to 3x3 Hankel determinants",
        "negative_port_n5_to_n11":{"axis1":{str(k):str(v) for k,v in neg1.items()},"axis2":{str(k):str(v) for k,v in neg2.items()},"delta":{str(k):str(v) for k,v in delta.items()}},
        "native_grade1_port_masses_n5_to_n8":{str(k):v for k,v in native.items()},
        "hankel_leading_principal_minors_at_n5":dets,
        "finite_check_status":"PASS",
        "all_H_and_n_proof_status":"Separate Laurent-domain Gram proof in paper; not inferred from finite checks",
        "review":"NOT_REVIEWED"
    }
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result


if __name__=='__main__':
    import pathlib
    data=main()
    out=pathlib.Path(__file__).with_name('PREFIX1022_R6_INTEGER_CERT.json')
    out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Saved',out)
