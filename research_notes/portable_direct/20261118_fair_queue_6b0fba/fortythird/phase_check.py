"""Recompute the norm-7 Gauss atoms, rational positive transition kernels and exact readouts."""
import argparse
from contextlib import contextmanager
from fractions import Fraction as Q
from itertools import product
from math import pi,sqrt,tan
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory


PIN="e7b9fb5084f93a9b2dbc16225629b667fb7bf46c"
ZERO=(Q(0),Q(0))
ONE=(Q(1),Q(0))
OMEGA=(Q(0),Q(1))
PI=(Q(1),Q(3))


def plus(x,y):return (x[0]+y[0],x[1]+y[1])
def scale(c,x):return (c*x[0],c*x[1])
def times(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x):return (x[0]-x[1],-x[1])
def exp_eis(x,n):
    y=ONE
    while n:
        if n%2:y=times(y,x)
        x=times(x,x);n//=2
    return y

UNITS=[exp_eis((Q(1),Q(1)),j) for j in range(6)]

def q4mul(x,y):
    return (plus(times(x[0],y[0]),scale(7,times(x[1],y[1]))),
            plus(times(x[0],y[1]),times(x[1],y[0])))

def zpow(n):
    if n<0:return tuple(conj(a) for a in zpow(-n))
    x=exp_eis(PI,n)
    if n%2:return ZERO,scale(Q(1,7**((n+1)//2)),x)
    return scale(Q(1,7**(n//2)),x),ZERO

def six_coeffs(t):
    def det(x,y):return x[0]*y[1]-x[1]*y[0]
    for i,v in enumerate(UNITS):
        w=UNITS[(i+1)%6]
        a,b=det(t,w)/det(v,w),det(v,t)/det(v,w)
        if a>=0 and b>=0:
            assert plus(scale(a,v),scale(b,w))==t
            return [(i,a),((i+1)%6,b)]
    raise AssertionError("hexagon sectors must cover the plane")

def dec_packet(mass,L):
    x,y=ZERO,ZERO
    for (r,j),a in mass.items():
        v,w=zpow(r)
        x=plus(x,scale(a,times(v,UNITS[j])))
        y=plus(y,scale(a,times(w,UNITS[j])))
    return x,y

def edges(L,r,j,sgn,wrap):
    if 0<=r+sgn<L:
        return [((r+sgn,j),Q(1))]
    return [(((r+sgn)%L,(j+sgn*k)%6),a) for k,a in wrap]

@contextmanager
def native(repo):
    with TemporaryDirectory() as d:
        pkg=Path(d)/"phase_frozen";pkg.mkdir();(pkg/"__init__.py").write_text("")
        for name in ["core","division","exact_arithmetic","brc_logarithm","brc_weighted","brc_weighted_recurrent"]:
            data=subprocess.check_output(["git","-C",str(repo),"show",f"{PIN}:src/enterprise_math/{name}.py"])
            (pkg/(name+".py")).write_bytes(data)
        sys.path.insert(0,d)
        try:
            from phase_frozen import brc_weighted as wt, brc_weighted_recurrent as rec
            yield wt,rec
        finally:sys.path.remove(d)

def kernel_matrix(L,wrap,sgn):
    M=[[Q(0)]*(6*L) for _ in range(6*L)]
    for r,j in product(range(L),range(6)):
        for (s,k),w in edges(L,r,j,sgn,wrap):M[6*r+j][6*s+k]+=w
    return M

def walk(wt,L,word,wrap,tag=(1,3),conjugate=False):
    state={(tag,0,0):wt.CWM_ONE};r=0;total_exponent=0;wrap_count=0
    for sgn in word:
        assert sgn in (-1,1)
        new={}
        wrap_count+=int(not 0<=r+sgn<L)
        r=(r+sgn)%L
        total_exponent+=sgn
        for (source,i,j),state0 in state.items():
            assert source==tag
            for (a,b),co in edges(L,i,j,sgn,wrap):
                direct=wt.cwm_propagate(state0,wt.cwm_edge(co))
                key=(source,a,b)
                new[key]=wt.cwm_recoalesce(new.get(key,wt.CWM_ZERO),direct)
        state=new
    mass={(r,j):s.total for (source,r,j),s in state.items() if source==tag}
    read=dec_packet(mass,L)
    if conjugate:read=tuple(conj(q) for q in read)
    assert read==zpow(-total_exponent if conjugate else total_exponent)
    qtot=sum(mass.values());cost=sum(t for _,t in wrap)
    assert qtot==cost**wrap_count
    assert sum(s.count for s in state.values())==2**wrap_count
    assert max(s.dominant for s in state.values())==max(t for _,t in wrap)**wrap_count
    return state

def gauss_atom(gen):
    a,b=gen
    w=-a*pow(b,-1,7)%7
    cube={pow(w,k,7):exp_eis(OMEGA,k) for k in range(3)}
    out=[ZERO]*7
    for t in range(1,7):out[((2*a-b)*t)%7]=cube[t*t%7]
    return out

def cyc(A,B):
    out=[ZERO]*7
    for i,a in enumerate(A):
        for j,b in enumerate(B):out[(i+j)%7]=plus(out[(i+j)%7],times(a,b))
    return out

def modphi(A):return [plus(a,scale(-1,A[-1])) for a in A[:-1]]

def gauss_checks():
    ga=gauss_atom((1,3));gb=gauss_atom((-2,-3))
    assert gb==[conj(ga[-j%7]) for j in range(7)]
    for atom,g in [(ga,PI),(gb,conj(PI))]:
        assert modphi(cyc(cyc(atom,atom),atom))==[scale(-7,g)]+[ZERO]*5
    assert modphi(cyc(ga,gb))==[scale(7,ONE)]+[ZERO]*5
    # At equal n the twisted pair gives two different labelled evaluations. Projected
    # onto total amplitude, swapping the raw conjugate atoms would hide the change.
    return {"field":"Q(omega)[U]/(1+U+...+U^6), U=zeta_7",
            "sum_convention":"unnormalized g; G=g/sqrt(7)",
            "primary":[1,3],"primary_conjugate":[-2,-3],
            "character_additive_coefficients":[[int(a),int(b)] for a,b in ga],
            "exact_cube_coefficients":[[-7,-21],[14,21]],"exact_product_with_conjugate":7}

def integral_det(A):
    a=[row[:] for row in A]
    out,prev=1,1
    for k in range(len(a)-1):
        h=next((i for i in range(k,len(a)) if a[i][k]),None)
        if h is None:return 0
        if h!=k:a[k],a[h]=a[h],a[k];out=-out
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                v=a[i][j]*a[k][k]-a[k][j]*a[i][k]
                assert v%prev==0
                a[i][j]=v//prev
        prev=a[k][k]
    return out*a[-1][-1]

def resultant_check():
    H=[7,0,13,0,7]
    G=[6,-7,1]
    S=[]
    for f,m,n in [(H,4,2),(G,2,4)]:
        for i in range(n):S.append([0]*i+f+[0]*(n-1-i))
    R=integral_det(S)
    def val(z):
        q=q4mul(z,z)
        return tuple(plus(plus(scale(6,q[i]),scale(-7,z[i])),ONE if i==0 else ZERO) for i in range(2))
    a=val(zpow(1));b=val(tuple(scale(-1,v) for v in zpow(1)))
    aa=q4mul(a,tuple(conj(g) for g in a));bb=q4mul(b,tuple(conj(g) for g in b))
    assert q4mul(aa,bb)==((Q(R,49),Q(0)),ZERO)
    assert R>0
    return {"stochastic_rows":[["1/2","1/2"],["1/3","2/3"]],"row_denominator_product":6,
            "integer_characteristic_polynomial_descending":G,"nonzero_integer_resultant":R,
            "error_floor":"1/4032"}

def separation_check():
    eps=Q(1,1000);thr=1-4*eps+2*eps**2
    # The normalized readout argument uses Re(z^k) < thr.
    t=[2,-1]
    for _ in range(2,81):t.append(-t[-1]-7*t[-2])
    def sep(k):
        return t[k]<0 or t[k]**2<4*7**k*thr**2
    selected=[]
    for n in range(81):
        if all(sep(n-m) for m in selected):selected.append(n)
    return {"window":[0,80],"normalized_readout_error":"1/1000",
            "certified_state_lower_bound":len(selected),"separated_times":selected}

def runtime_checks(wt,rec):
    rows=[]
    for L in (2,4,6,8,12,16):
        q,w=zpow(L)
        assert w==ZERO
        wrap=six_coeffs(q);cost=sum(a for _,a in wrap)
        assert Q(1)<cost and 3*cost**2<=4 and all(a>0 for _,a in wrap)
        # Direct native powers are intentionally limited to the two smallest matrices.
        exponents={2:(0,1,2,3,4,8),4:(0,3,4,5,8)}.get(L,())
        if exponents:
            W=kernel_matrix(L,wrap,1)
            for n in exponents:
                row=rec.recurrent_mass_power(W,n)[0]
                cells=walk(wt,L,[1]*n,wrap)
                target=[Q(0)]*len(row)
                for (_,i,j),s in cells.items():target[6*i+j]=s.total
                assert tuple(target)==row
        words=[(1,)*L,(-1,)*L,(-1,1)*5,(1,1,-1,-1,-1)*4]
        if L==2:words.extend(word for k in range(6) for word in product((-1,1),repeat=k))
        for word in words:
            walk(wt,L,word,wrap)
            walk(wt,L,word,wrap,tag=(-2,-3),conjugate=True)
        rows.append({"L":L,"states":6*L,"wrap_coefficients":[[k,str(a)] for k,a in wrap],
                     "one_wrap_total":str(cost),"matrix_powers_checked":exponents,
                     "signed_words_checked_per_source":len(words)})
    return rows

def polygon_checks(wt,rec):
    rows=[]
    det=lambda x,y:x[0]*y[1]-x[1]*y[0]
    for d in (6,8,12,18,32,50):
        H=d**4
        top=[]
        for j in range(d//2):
            # Float proposes the integer parameter only. All subsequent assertions are exact.
            theta=2*pi*j/d
            m=round(6*j/d)
            t=Q(round(H*tan((theta-m*pi/3)/2)/sqrt(3)),H)
            den=1+3*t*t
            v=((1-3*t*t+2*t)/den,4*t/den)
            top.append(times(UNITS[m%6],v))
        U=top+[scale(-1,x) for x in top]
        assert U[0]==ONE and len(set(U))==d
        assert all(times(u,conj(u))==ONE for u in U)
        for j,u in enumerate(U):
            v=U[(j+1)%d]
            assert all(det(plus(v,scale(-1,u)),plus(w,scale(-1,u)))>=0 for w in U)
        transitions={}
        r=zpow(2)[0]
        for sign,rot in [(1,r),(-1,conj(r))]:
            T=[]
            for u in U:
                t=times(u,rot)
                for j,v in enumerate(U):
                    w=U[(j+1)%d];den=det(v,w)
                    assert den>0
                    a,b=det(t,w)/den,det(v,t)/den
                    if min(a,b)>=0:
                        assert a and b and plus(scale(a,v),scale(b,w))==t
                        T.append({j:a,(j+1)%d:b});break
                else:raise AssertionError("missing polygon sector")
            transitions[sign]=T
        g=max(sum(row.values()) for T in transitions.values() for row in T)
        assert g>1
        for sign,T in transitions.items():
            for j,weights in enumerate(T):
                pad=(g-sum(weights.values()))/2
                for k in (0,d//2):weights[k]=weights.get(k,0)+pad
                assert sum(weights.values())==g
                v=ZERO
                for k,w in weights.items():
                    if w:
                        edge=wt.cwm_edge(w)
                        v=plus(v,scale(edge.total,U[k]))
                assert v==times(U[j],r if sign==1 else conj(r))
        if d==6:
            W=[[Q(0)]*(2*d) for _ in range(2*d)]
            for j in range(d):
                W[j][d+j]=Q(1)
                for k,w in transitions[1][j].items():W[d+j][k]=w
            v=rec.recurrent_mass_power(W,4)[0]
            got=ZERO
            for j in range(d):got=plus(got,scale(v[j],U[j]))
            assert got==zpow(4)[0] and sum(v)==g**2
        rows.append({"d":d,"states":2*d,"rational_mesh_denominator":H,"uniform_wrap_total":str(g),
                     "decimal_for_display":float(g),"exact_forward_and_reverse_rows_checked":2*d})
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True,help="public enterprise-math checkout with the pinned commit")
    args=parser.parse_args()
    with native(args.repo) as (wt,rec):
        runs=runtime_checks(wt,rec)
        polys=polygon_checks(wt,rec)
    print(json.dumps({"public_git":PIN,"Gauss_atoms":gauss_checks(),
                      "positive_mass_replays":runs,"inscribed_polygon_replays":polys,"resultant_precision":resultant_check(),
                      "finite_separation":separation_check()},indent=2,sort_keys=True))
if __name__=="__main__":main()
