"""Exact BRC two-law observer facet at (s_a,s_b)=(1/3,2/5).
All branch masses and observables are integers in units of 1/240.
Run: python VERIFY.py (standard library only).
"""
from fractions import Fraction as F
from itertools import product
import json

D = 240
# name -> (time, compressed state, Q mass*D, P mass*D, ordered children)
N = {
    "": (0,0,240,240,["a","b"]),
    "a": (1,2,120,180,["ax","ay"]),
    "b": (1,1,120,60,["bu","bv"]),
    "ax": (2,4,60,60,["axL","axM","axH"]),
    "ay": (2,5,60,120,["ayT"]),
    "bu": (2,4,30,30,["buL","buM","buH"]),
    "bv": (2,3,90,30,["bvT"]),
    "axL": (3,7,20,10,[]),
    "axM": (3,8,20,20,[]),
    "axH": (3,9,20,30,[]),
    "ayT": (3,10,60,120,[]),
    "buL": (3,7,12,6,[]),
    "buM": (3,8,6,6,[]),
    "buH": (3,9,12,18,[]),
    "bvT": (3,6,90,30,[]),
}
L = (212,273,28,-12)


def check_model():
    assert len(N)==15 and sum(not u[4] for u in N.values())==8
    for h,(t,s,q,p,ch) in N.items():
        assert p>0 and q>0
        if ch:
            assert sum(N[k][2] for k in ch)==q,(h,'Q')
            assert sum(N[k][3] for k in ch)==p,(h,'P')
    assert N['ax'][1]==N['bu'][1]==4
    assert {N[h][1] for h in N if N[h][0]==3}=={6,7,8,9,10}
    assert F(N['axL'][2],N['ax'][2])==F(1,3)
    assert F(N['buL'][2],N['bu'][2])==F(2,5)


def evaluate(policy, by_history=False):
    def rec(h):
        t,s,q,p,ch=N[h]
        a=policy[h] if by_history else policy[s]
        if a==2:  # continue
            assert ch
            z=[0]*4
            for k in ch:
                w=rec(k)
                z=[x+y for x,y in zip(z,w)]
            return z
        assert a in (0,1)
        return [p if a==1 else 0, q if a==0 else 0, t*p,t*q]
    return tuple(rec(''))


def rank(matrix):
    A=[[F(x) for x in row] for row in matrix]
    if not A:return 0
    m,n=len(A),len(A[0]);r=0
    for c in range(n):
        k=next((i for i in range(r,m) if A[i][c]),None)
        if k is None:continue
        A[r],A[k]=A[k],A[r]
        pivot=A[r][c]
        A[r]=[v/pivot for v in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                mul=A[i][c]
                A[i]=[a-mul*b for a,b in zip(A[i],A[r])]
        r+=1
        if r==m:break
    return r


def bellman(forced=None):
    action={}
    def rec(h):
        t,s,q,p,ch=N[h]
        elapsed=t*(L[2]*p+L[3]*q)
        cost=[L[1]*q+elapsed,L[0]*p+elapsed]
        if ch:cost.append(sum(rec(k) for k in ch))
        a=forced if h in ('ax','bu') and forced is not None else min(range(len(cost)),key=lambda k:cost[k])
        action[h]=a
        return cost[a]
    return rec(''),action


def symbolic_phase(sa,sb):
    """Closed-form exact Bellman values for all rational 0<s_a,s_b<1/2."""
    assert F(0)<sa<F(1,2) and F(0)<sb<F(1,2)
    u=lambda s:min(F(212), F(228)-45*s)
    full=F(503,4)+u(sa)/4+u(sb)/8
    comp=min(F(821,4),F(16)+F(1,2)*min(F(273),F(561,2)-F(45,2)*sa)
             +F(1,2)*min(F(106),F(110)-F(45,4)*sb))
    threshold=F(16,45)
    gap=(min((45*sb-16)/8,F(1,4),(16-45*sa)/4)
         if sa<threshold<sb else F(0))
    assert comp-full==gap
    return full,comp,gap


def independent_bellman(sa,sb,forced):
    """Fresh tree recurrence independent of the simplified phase formula."""
    term=lambda r:min(F(273),F(212)*r)
    Vay=min(F(273),F(424),F(44)+term(F(2)))
    Vbv=min(F(273),F(212,3),F(28,3)-12+term(F(1,3)))
    def collision(s):
        costs=[F(273),F(212),F(16)+s*term(F(1,2))+(1-2*s)*term(F(1))+s*term(F(3,2))]
        return min(costs) if forced is None else costs[forced]
    Va=min(F(273),F(318),F(30)+(collision(sa)+Vay)/2)
    Vb=min(F(273),F(106),F(2)+collision(sb)/4+Vbv*F(3,4))
    return min(F(273),F(212),F(16)+(Va+Vb)/2)


def main():
    check_model()
    # Exact independent check at 52^2 parameter points, including the threshold.
    values=sorted({F(i,100) for i in range(1,50)} | {F(1,3),F(2,5),F(16,45)})
    for sa in values:
        for sb in values:
            full,comp,gap=symbolic_phase(sa,sb)
            assert full==independent_bellman(sa,sb,None)
            assert comp==min(independent_bellman(sa,sb,a) for a in range(3))
    assert symbolic_phase(F(1,3),F(2,5))==(F(205),F(821,4),F(1,4))
    vectors={}
    tables=0
    for nt in product(range(3),repeat=6):
        for tr in product(range(2),repeat=5):
            v=evaluate(nt+tr)
            vectors.setdefault(v,nt+tr)
            tables+=1
    assert tables==23328 and len(vectors)==326
    dot=lambda v:sum(c*x for c,x in zip(L,v))
    best=min(map(dot,vectors))
    assert best==49260  # 821/4 after dividing by 240
    equal=[v for v in vectors if dot(v)==best]
    expected=[(120,60,420,360),(42,132,360,480),
              (120,60,510,570),(72,92,600,660)]
    assert sorted(equal)==sorted(expected)
    face_rank=rank([[v[i]-equal[0][i] for i in range(4)] for v in equal[1:]])
    ambient=[(0,240,0,0),(240,0,0,0),(0,240,240,240),
             (180,120,240,240),(0,240,420,360)]
    assert all(v in vectors for v in ambient)
    ambient_rank=rank([[v[i]-ambient[0][i] for i in range(4)] for v in ambient[1:]])
    assert face_rank==3 and ambient_rank==4
    f,full_actions=bellman()
    forced_results={a:bellman(a)[0] for a in range(3)}
    assert f==49200 and forced_results=={0:49320,1:49260,2:49260}
    witness={
        '':2,'a':2,'b':2,'ax':1,'ay':0,'bu':2,'bv':2,
        'axL':1,'axM':1,'axH':0,'ayT':0,
        'buL':1,'buM':1,'buH':0,'bvT':1
    }
    w=evaluate(witness,by_history=True)
    assert w==(102,72,540,600) and dot(w)==f
    result={
        'status':'PASS_EXACT_INTEGER_240',
        'input':'s_a=1/3,s_b=2/5; P,Q strictly positive',
        'ordered_prefix_count':len(N), 'terminal_count':8,
        'phase_formula_grid_points':len(values)**2,
        'global_phase_threshold':'16/45',
        'global_separation_region':'0<s_a<16/45<s_b<1/2',
        'sharp_global_gap_maximum':'1/4',
        'pure_compressed_tables':tables,'distinct_vectors':len(vectors),
        'lambda':list(L), 'compressed_bound':str(F(best,D)),
        'full_history_min':str(F(f,D)),
        'exact_gap':str(F(best-f,D)),
        'forced_collision_minima':{str(a):str(F(z,D)) for a,z in forced_results.items()},
        'full_history_witness':[str(F(x,D)) for x in w],
        'full_witness_actions':witness,
        'facet_equality_vector_count':len(equal),
        'facet_affine_dimension':face_rank,'ambient_affine_dimension':ambient_rank,
        'equality_vectors':[list(map(str,(F(x,D) for x in v))) for v in equal],
        'scope':'Complete deterministic seedless state-action class; multi-affine proof extends linear support bound to all independent fresh-coin behavioral policies.'
    }
    print(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False))

if __name__=='__main__':main()
