"""R136: exact six-pair BRC Port-10 optimizer switch and membership strip.
Model and frozen Port pin: R121/R122; P000 remains unchanged.
All comparisons use integers or Fraction, with no floating approximations.
"""
from fractions import Fraction as F
from itertools import product, combinations

PAIRS=tuple(combinations(range(4),2))
T0=((0,220),(20,220),(20,292),(0,272))
T1=((0,272),(20,292),(20,500),(0,500))
CORE={(1,0,0),(5,-4,1),(5,-1,0),(9,-5,1)}
PAIR={(1,3,-1),(7,-1,0)}
V3=(4,-4,1)
V6=(6,-1,0)
EIGHT=CORE|PAIR|{V3,V6}

def port(a):
    return max(sum(max(v,0) for v in a),sum(max(-v,0) for v in a))

def gaps(a):
    x,y,z=a
    h=(0,x+3*y+6*z,3*x+12*y+30*z,7*x+39*y+126*z)
    return tuple(abs(h[i]-h[j]) for i,j in PAIRS)

DIRECTIONS=tuple(a for a in product(range(-10,11),repeat=3)
                 if any(a) and port(a)<=10 and next(v for v in a if v)>0)
G={a:gaps(a) for a in DIRECTIONS}
assert len(DIRECTIONS)==1935
assert EIGHT.issubset(G)

def caps(B,D):
    w=(F(136),F(B),F(176),F(D))
    return tuple(w[i]+w[j] for i,j in PAIRS)

def optimizer_lower_witness(a,triangle):
    # Exact inequality g_j/s_j >= k/s_anchor on the entire polygon.
    anchor,k,verts=(0,3,T0) if triangle==0 else (4,6,T1)
    return [j for j in range(6) if all(G[a][j]*caps(B,D)[anchor]
                           >= k*caps(B,D)[j] for B,D in verts)]

def outsider_exclusion_witness(a,triangle):
    # Strict-near exclusion via 2*g_j/s_j >= 3*eta.
    anchor,k,verts=(0,9,T0) if triangle==0 else (4,18,T1)
    return [j for j in range(6) if all(2*G[a][j]*caps(B,D)[anchor]
                           >= k*caps(B,D)[j] for B,D in verts)]

def near_forecast(B,D):
    B,D=F(B),F(D)
    answer=set(CORE)
    if D < 396+F(5,4)*B:answer.add(V3)
    if D < 408+2*B:answer.add(V6)
    if B<20 and D<min(306+F(5,4)*B,312-B):answer.update(PAIR)
    return answer

def near_exact(B,D):
    B,D=F(B),F(D)
    s=caps(B,D)
    eta=min(F(3,136+B),F(6,B+D))
    score={a:max(F(g,si) for g,si in zip(G[a],s)) for a in DIRECTIONS}
    return min(score.values()),{a for a in DIRECTIONS if 2*score[a]<3*eta}

def affine_expressions(a,triangle):
    """Return constant, B coefficient, D coefficient of strict L_j >0."""
    g=G[a]
    anchor,k=(0,9) if triangle==0 else (4,18)
    expr=[]
    for j in range(6):
        def val(B,D):
            s=caps(B,D)
            return k*s[j]-2*g[j]*s[anchor]
        u=val(0,0)
        expr.append((u,val(1,0)-u,val(0,1)-u))
    return expr

def geom_eval(abc,pt):
    return abc[0]+abc[1]*pt[0]+abc[2]*pt[1]

def verify():
    lower=[];outsider=[];common=0
    for a in DIRECTIONS:
        ws=[optimizer_lower_witness(a,phase) for phase in (0,1)]
        assert ws[0] and ws[1],('optimizer lower gap',a)
        lower.append((ws[0][0],ws[1][0]))
        if a not in EIGHT:
            ex=[outsider_exclusion_witness(a,phase) for phase in (0,1)]
            assert ex[0] and ex[1],('outsider gap',a)
            outsider.append((ex[0][0],ex[1][0]))
            if set(ex[0]) & set(ex[1]):common+=1
    assert common==1927
    for a,phase,k,anchor,verts in [
        (V6,0,3,0,T0),((1,0,0),1,6,4,T1)]:
        for j in range(6):
            assert all(G[a][j]*caps(B,D)[anchor]<=k*caps(B,D)[j]
                       for B,D in verts),(a,phase,j)
    # On T0 only pair 02 for the two paired rows can reach zero.
    for a in EIGHT:
        for j,expr in enumerate(affine_expressions(a,0)):
            values=[geom_eval(expr,v) for v in T0]
            assert min(values)>=0
            if min(values)==0:
                assert a in PAIR and j==1,(a,j,values)
    # In T1 these are exactly the potentially nonpositive comparisons.
    active={(1,3,-1):{0,1,3},(7,-1,0):{0,1,3},
            (4,-4,1):{1,3},(6,-1,0):{0,1}}
    for a in EIGHT:
        for j,expr in enumerate(affine_expressions(a,1)):
            values=[geom_eval(expr,v) for v in T1]
            if (a in active and j in active[a]):continue
            assert min(values)>0,(a,j,values)
    # Dominance of the discarded secondary boundaries, 0<=B<=20.
    for B in (F(0),F(20)):
        assert F(1584,5)+F(4,5)*B >= 306+F(5,4)*B
        assert 468-B >= 396+F(5,4)*B
        assert 468-B >= 408+2*B
    test_B=[F(1),F(8,3),F(8),F(19),F(20)]
    pts={(B,F(220)) for B in test_B}
    pts.update((B,F(500)) for B in test_B)
    for B in test_B:
        for t in (F(272)+B,306+F(5,4)*B,312-B,
                  396+F(5,4)*B,408+2*B):
            for D in (t-F(1,10),t,t+F(1,10)):
                if 220<=D<=500:pts.add((B,D))
    pts|={(F(1,2),F(280)),(F(13,2),F(343)),
          (F(17,2),F(425)),(F(20),F(292))}
    for B,D in sorted(pts):
        eta,actual=near_exact(B,D)
        assert eta==min(F(3,136+B),F(6,B+D)),('optimum',B,D)
        assert actual==near_forecast(B,D),('membership',B,D,
                                           actual^near_forecast(B,D))
    print('R136 CERTIFICATE PASS')
    print('port10_unoriented_directions',len(DIRECTIONS))
    print('optimizer_lower_pair_at_each_polygon',len(lower),'x 2')
    print('excluded_outsiders',len(outsider),'x 2; common_pair_witnesses',common)
    print('exact_full_direction_replays',len(pts))
    print('anchor_switch D=272+B; paired departure D=min(306+5B/4,312-B)')
    print('remaining departures D=396+5B/4, D=408+2B')
    print('sample B=8: D=220,280,304,406,424,500 counts',
          [(D,len(near_forecast(8,D))) for D in (220,280,304,406,424,500)])

if __name__=='__main__':verify()
