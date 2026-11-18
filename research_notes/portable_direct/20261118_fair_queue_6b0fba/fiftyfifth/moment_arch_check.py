"""Exact real-moment certificate for the p17 q14 split (7,7) signed roster.
Only integer arithmetic is used. The optional --roster verifies the frozen
November 16 side roster. No affine backend or prime-power congruences.
"""
import argparse
import hashlib
import json
from collections import defaultdict
from fractions import Fraction
from math import lcm
from pathlib import Path

BUDGET = 2331
COEF_DEN = 10**8
SCALE = 10**6
ROUNDING_ERROR = 299
ROSTER_SHA256 = '242e4872003368905b9355fc666c307a6182482152922b83273708b1a1d07e54'
# Rational Chebyshev-basis coefficients. Only their exact values enter the proof.
POLYS = {
    2: (16799881, 31091531, 24267299, 15774313, 8202092, 3113292, 751592),
    3: (15101253, 28875391, 23449537, 16635022, 9947186, 4393456, 1598155),
    4: (13556593, 27499935, 22535858, 16914984, 11445960, 5209084, 2837586),
    5: (12011651, 26752270, 21722381, 16711890, 12944516, 5427431, 4429861),
    6: (10560755, 26189496, 21340959, 15837013, 14830399, 4884349, 6357029),
    7: (9408379, 25401933, 21510523, 14357257, 17021697, 3777658, 8522553),
    8: (11876605, 22103857, 20639299, 14995734, 16300533, 4272194, 9811778),
    9: (14304454, 19192403, 19539689, 16118206, 15168326, 4532199, 11144723),
    10: (15974036, 16824133, 19029493, 16363984, 14927224, 4034820, 12846310),
    11: (17857623, 14514289, 18361717, 16612806, 14727085, 3491939, 14434541),
    12: (19672985, 12283764, 17842523, 16866470, 14214164, 3092870, 16027224),
    13: (21643713, 10015961, 17283867, 17199678, 13907077, 2380205, 17569499),
    14: (23294532, 8245612, 16689177, 17035177, 13293752, 2352022, 19089728),
    15: (25229988, 5752343, 16544608, 17641548, 13369687, 937295, 20524531),
    16: (26894956, 3764891, 16287760, 17662585, 13122686, 286166, 21980956),
    17: (24878623, 3533575, 16179302, 17507596, 13678908, 2829026, 21392970),
    18: (17839676, 15825659, 19807558, 17285701, 12737978, 5825865, 10677563),
    20: (33310834, -4448106, 16497481, 16941837, 13451930, -3257094, 27503118),
    21: (33202012, -5867796, 16716247, 16552109, 14325951, -2873440, 27944917),
    22: (20438684, 11195556, 19863809, 16480510, 13650376, 4493671, 13877394),
    24: (39626879, -13543452, 18744359, 14055680, 16137614, -7653849, 32632769),
    25: (41829120, -16407328, 19856118, 12946231, 17063245, -9436722, 34149336),
    26: (42512353, -18095297, 20329621, 12228824, 17818487, -9864125, 35070137),
    27: (45766374, -21145259, 21299464, 11167800, 18525581, -12578409, 36964449),
    28: (26000199, 2920867, 21367301, 13786390, 15818708, 763560, 19342975),
    30: (28261042, -418543, 22435180, 12667484, 16964950, -1060138, 21150025),
    32: (55634858, -34459249, 27494780, 4926465, 23499613, -20686813, 43590346),
    33: (57756311, -37261214, 28874830, 3231620, 24769491, -22162449, 44791411),
    34: (53250336, -36798574, 28509415, 3343021, 25607340, -17669279, 43757741),
    35: (57623740, -38399718, 27609194, 4440397, 23949286, -20660577, 45437678),
    36: (22171669, 5282116, 25039803, 12147284, 16852691, 2459889, 16046548),
    39: (57483551, -36995141, 33512123, -5059899, 24146124, -17006442, 43919684),
    40: (36082387, -18710041, 34213402, 3358015, 22907286, -7395912, 29544863),
    42: (38192314, -25065900, 39032140, -642919, 26351855, -8409085, 30541595),
    44: (58142698, -38438235, 42702466, -19603209, 27237428, -12086905, 42045757),
    45: (19335168, -4595437, 37713264, 4878108, 19212819, 3067996, 20388082),
    48: (60002255, -42180912, 49347404, -27721818, 30034896, -10171572, 40689747),
    49: (59629024, -42877344, 50157726, -29191098, 30818701, -8827008, 40289999),
    50: (61217174, -44237243, 52232497, -31553075, 31260705, -9165439, 40245381),
    51: (61894395, -45353454, 53636914, -33416740, 31839024, -8688156, 40088017),
    52: (38020957, -21819765, 42447070, -12870721, 26920996, 766045, 26535418),
    54: (62422725, -48931697, 56541628, -37431615, 34077029, -6178502, 39500432),
    55: (65313533, -50828489, 59430685, -40363020, 34220935, -7467896, 39694252),
    56: (14431206, -634453, 39794146, 4271171, 17788175, 7766419, 16583336),
    60: (14311526, -15353671, 52776216, -4083522, 19387276, 8408876, 24553299),
    63: (75162790, -66667320, 73090708, -53431714, 39366132, -7560875, 40040279),
    64: (76193734, -69056344, 74655149, -54777880, 40189513, -7387248, 40183076),
    65: (78227181, -71651094, 76964801, -56912883, 40751825, -7832624, 40452794),
    66: (54914605, -42157564, 58485568, -31893204, 33080945, -878888, 28448538),
    68: (57653126, -46548042, 61677981, -34598869, 34280275, -1418017, 28953546),
    70: (60383924, -50484687, 64423918, -37230045, 35258248, -1758552, 29407194),
    72: (27012447, -40978564, 71416618, -17364383, 25008756, 3853038, 31052088),
    75: (66969351, -62277798, 72576426, -43281555, 38152324, -2924565, 30785817),
    77: (99218181, -108001181, 103695385, -76289721, 49561274, -11609689, 43425751),
    78: (71917651, -69697526, 78170273, -47504925, 39585821, -4210055, 31738761),
    80: (104050770, -117095103, 109570940, -80313499, 51576530, -12222677, 44433039),
    81: (45540509, -66831404, 87014658, -31035085, 32633231, -2052362, 34730453),
    84: (113726104, -132144339, 121055019, -87603921, 54377760, -15302779, 45892156),
    85: (45165573, -70539127, 88731545, -31419398, 33247078, -1480964, 36295293),
    88: (90381174, -101119056, 100184971, -62354117, 46410537, -9330791, 35827282),
    90: (129468012, -159984790, 140499565, -99438045, 60474783, -19968867, 48949342),
    91: (30529761, -26605437, 54955439, -8493226, 23375587, 3807987, 22429889),
}


def smooth(n):
    for p in (2,3,5,7,11,13,17):
        while n%p==0:
            n//=p
    return n==1


def source_sides():
    atoms=[(q,r) for q in range(1,8) for r in range(1,17) if smooth(17*q+r)]
    den=[17*(17*q+r) for q,r in atoms]
    sides=[]
    def visit(start,order,budget,side):
        if order==0:
            sides.append(tuple(side))
            return
        for i in range(start,len(atoms)):
            q,r=atoms[i]
            if q>order:break
            if den[i]-1<=budget:
                visit(i,order-q,budget-den[i]+1,side+[i])
    visit(0,7,BUDGET,[])
    budget=[BUDGET-sum(den[i]-1 for i in row) for row in sides]
    assert len(sides)==1907 and min(budget)==4 and max(budget)==292
    return atoms,den,sides,budget


def evaluate(t,center,coefs):
    # round-to-nearest (ties to even); exact Fraction throughout.
    x=Fraction(2*center,t)-1
    a,b=1,x
    value=coefs[0]+coefs[1]*x
    for c in coefs[2:]:
        a,b=b,2*x*b-a
        value+=b*c
    return round(SCALE*value/COEF_DEN)


def knapsack(values,nodes,bmax):
    current=[0]*(bmax+1)       # maximum among multisets of mass AT MOST b
    for t in nodes:
        w=t-1
        v=values[t]
        if v<=0:continue
        for b in range(w,bmax+1):
            current[b]=max(current[b],v+current[b-w])
    return current


def bounds(knap,vertical,bmax):
    # vertical maps each actual remaining budget to the largest vertical signal.
    extremes=[None]*(bmax+1)
    for b,sig in vertical.items():
        for cost in range(b+1):
            val=sig+knap[b-cost]
            if extremes[cost] is None or val>extremes[cost]:
                extremes[cost]=val
    assert all(v is not None for v in extremes)
    return extremes


def moment_tail(den,sides,bs,lower):
    possible=[d for d in range(lower,max(bs)+2) if smooth(d)]
    scale=lcm(*den,*possible)
    weights={t:(scale//t)**6 for t in set(possible)|set(den)}
    seen=set()
    by_rosters=0
    def visit(first,room,value):
        if value in seen:
            raise AssertionError('sixth-moment tie at high minimum denominator')
        seen.add(value)
        for j in range(first,len(possible)):
            t=possible[j]
            if t-1>room:break
            visit(j,room-(t-1),value+weights[t])
    for s,b in zip(sides,bs):
        visit(0,b,sum(weights[den[i]] for i in s))
        by_rosters+=1
    return dict(minimum_low_denominator=lower,scaled_reciprocal_lcm=scale,
                vertical_rosters=by_rosters,distinct_complete_sides=len(seen),
                distinct_sixth_moments=len(seen),largest_sixth_moment_bits=max(seen).bit_length())


def ceildiv(a,b):
    return -((-a)//b)


def certificate(roster):
    atoms,den,sides,bs=source_sides()
    if roster:
        raw=roster.read_bytes()
        assert hashlib.sha256(raw).hexdigest()==ROSTER_SHA256
        source=json.loads(raw)
        assert source['atoms']==[list(x) for x in atoms]
        assert source['roster_index_arrays']==[list(s) for s in sides]
    bmax=max(bs)
    future=[t for t in range(2,bmax+2) if smooth(t)]
    assert list(POLYS)==[t for t in future if t<=95]
    assert all(sum(cs)==COEF_DEN for cs in POLYS.values())
    refs=list(POLYS); n=len(refs)
    tidx={t:j for j,t in enumerate(refs)}
    z={t:tuple(evaluate(t,k,POLYS[k]) for k in refs) for t in set(den+future)}
    assert all(z[t][j]==SCALE for j,t in enumerate(refs))
    assert ROUNDING_ERROR>=(2*(bmax+7))//2
    # In each coordinate retain the source roster's contribution and true
    # remaining budget jointly. All opposing rosters are relaxed independently.
    upp=[{} for _ in refs]
    neg=[{} for _ in refs]
    for s,b in zip(sides,bs):
        for k in range(n):
            v=sum(z[den[i]][k] for i in s)
            upp[k][b]=max(upp[k].get(b,v),v)
            neg[k][b]=max(neg[k].get(b,-v),-v)
    abs_up=[{t:z[t][k] for t in future} for k in range(n)]
    abs_dn=[{t:-z[t][k] for t in future} for k in range(n)]
    levels={}
    # Store bounds [cost][polynomial] for each visited cutoff.
    for j,d in enumerate(refs):
        later=[t for t in future if t>d]
        up=[bounds(knapsack(abs_up[k],later,bmax),upp[k],bmax) for k in range(n)]
        dn=[bounds(knapsack(abs_dn[k],later,bmax),neg[k],bmax) for k in range(n)]
        levels[d]=(list(zip(*up)),list(zip(*dn)))
    stats={}
    for j,d0 in enumerate(refs):
        if d0>=56:break
        # Force the sign of the least lower atom positive by exchanging the sides.
        width_sequences=[]
        active=[(0,0,(0,)*n)]
        for d in refs[j:]:
            w=d-1
            k=tidx[d]
            u,v=levels[d]
            now=[]
            for pos,minus,pre in active:
                # Before spending on the current digit the bounds only enlarge.
                lo=max(ceildiv(-u[pos][k]-v[minus][k]-ROUNDING_ERROR-pre[k],SCALE),
                       -((bmax-minus)//w))
                hi=min((v[pos][k]+u[minus][k]+ROUNDING_ERROR-pre[k])//SCALE,
                       (bmax-pos)//w)
                if d==d0:lo=max(1,lo)
                for a in range(lo,hi+1):
                    p=pos+max(0,a)*w
                    m=minus+max(0,-a)*w
                    sig=tuple(x+a*y for x,y in zip(pre,z[d]))
                    if all(-xp-ym-ROUNDING_ERROR<=s<=yp+xm+ROUNDING_ERROR
                           for s,xp,ym,yp,xm in zip(sig,u[p],v[m],v[p],u[m])):
                        now.append((p,m,sig))
            active=now
            width_sequences.append(len(active))
            if not active:break
        assert not active,(d0,len(active))
        stats[d0]=dict(last_tested=d,maximum_surviving_prefixes=max(width_sequences),
                       frontier_sizes=width_sequences)
    tail=moment_tail(den,sides,bs,56)
    assert tail['distinct_complete_sides']==174525
    masks=[sum(1<<i for i in set(s)) for s in sides]
    pairs=sum(not(a&b) for i,a in enumerate(masks) for b in masks[:i])
    assert pairs==809566
    return dict(scope='maximal-p17 q14 vertical orders (7,7), exact side mass <=2331',
                vertical_side_roster_sha256=ROSTER_SHA256, vertical_rosters=len(sides),
                unordered_disjoint_vertical_pairs=pairs, budget_max=bmax,
                certificate='ordinary rational polynomials and unbounded integer knapsack',
                largest_allowed_future=max(future),degree=6,integer_scale=SCALE,
                total_rounding_bound=ROUNDING_ERROR,
                excluded_first_denominators=stats,tail=tail,
                surviving_full_rational_collisions=0)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--roster',type=Path)
    args=parser.parse_args()
    print(json.dumps(certificate(args.roster),sort_keys=True,indent=2))
