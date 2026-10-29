#!/usr/bin/env python3
"""Exact finite two-law bypass/merger regression for R5 rectangle veto.

Independent of any mathematical reviewer/Source admission. Python standard library only.
"""
from fractions import Fraction as F
from itertools import product

ZERO = F(0)
A = F(1,2)
B = F(1,2)
ACTION = ('SP','SQ','C')
TWO = F(2)
THREE = F(3)
# For each origin: (P_low, Q_low, P_high, Q_high).
KERNELS = {
    'A': (F(1,4),F(3,4),F(3,4),F(1,4)),
    'B': (F(2,5),F(3,5),F(3,5),F(2,5)),
}
W = (F(100), F(100), F(11), F(11))


def add(*vectors):
    return tuple(sum(v[k] for v in vectors) for k in range(4))


def sub(u,v):
    return tuple(u[k]-v[k] for k in range(4))


def mul(s,v):
    return tuple(s*x for x in v)


def score(v):
    return sum(x*y for x,y in zip(W,v))


def terminal(p,q,time,decision):
    """Masses p and q are the P and Q measures at terminal declaration."""
    return (p if decision == 'Q' else ZERO,
            q if decision == 'P' else ZERO,
            p*time, q*time)


def source_y(origin,y_action,decl):
    """Source enters merger y at time 2 with P=Q=mass 1/2."""
    mass = A if origin == 'A' else B
    if y_action != 'C':
        return terminal(mass,mass,TWO,'P' if y_action == 'SP' else 'Q')
    kp,kq,hp,hq = KERNELS[origin]
    return add(terminal(mass*kp,mass*kq,THREE,decl[origin+'L']),
               terminal(mass*hp,mass*hq,THREE,decl[origin+'H']))


def evaluate(x_action, y_a, y_b, decl):
    # Origin B bypasses the time-1 A-only choice (forced transit), then reaches y.
    if x_action == 'C':
        out_a=source_y('A',y_a,decl)
    else:
        out_a=terminal(A,A,F(1),'P' if x_action == 'SP' else 'Q')
    return add(out_a,source_y('B',y_b,decl))


def determinant3(m):
    a,b,c=m[0];d,e,f=m[1];g,h,i=m[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def main():
    # Every terminal signal has both-law positive mass; normalization and distinct LR keys.
    ratios=[]
    for src,ks in KERNELS.items():
        kp,kq,hp,hq=ks
        assert kp+hp ==1 and kq+hq==1
        assert all(t>0 for t in ks)
        ratios.extend((kp/kq,hp/hq))
    assert len(set(ratios))==4 and ratios == [F(1,3),F(3),F(2,3),F(3,2)]
    dec_keys=['AL','AH','BL','BH']
    terminal_declarations=[dict(zip(dec_keys,p)) for p in product(('P','Q'),repeat=4)]
    lr=[]
    full=[]
    for d in terminal_declarations:
        for x,y in product(ACTION,repeat=2):
            lr.append((score(evaluate(x,y,y,d)),x,y,d))
        for x,ya,yb in product(ACTION,repeat=3):
            full.append((score(evaluate(x,ya,yb,d)),x,ya,yb,d))
    assert len(lr)==144 and len(full)==432
    min_lr=min(x[0] for x in lr)
    min_full=min(x[0] for x in full)
    assert min_lr==F(131) and min_full==F(130)
    assert min_lr-min_full==F(1)

    dstar={'AL':'Q','AH':'P','BL':'Q','BH':'P'}
    witness=evaluate('C','C','SP',dstar)
    assert witness==(F(1,8),F(5,8),F(5,2),F(5,2))
    assert score(witness)==130
    corner={
        (0,0):evaluate('SP','SP','SP',dstar),
        (0,1):evaluate('SP','C','C',dstar),
        (1,0):evaluate('C','SP','SP',dstar),
        (1,1):evaluate('C','C','C',dstar),
    }
    assert corner[(0,0)] == (ZERO,F(1),F(3,2),F(3,2))
    assert corner[(0,1)] == (F(1,5),F(7,10),F(2),F(2))
    assert corner[(1,0)] == (ZERO,F(1),F(2),F(2))
    assert corner[(1,1)] == (F(13,40),F(13,40),F(3),F(3))
    affine_obstruction = add(corner[(0,0)],corner[(1,1)],mul(-1,corner[(0,1)]))
    assert affine_obstruction==witness
    base=corner[(0,0)]
    directions=[sub(corner[t],base) for t in ((1,0),(0,1),(1,1))]
    # Columns of the 3x3 matrix indexed by error_P,error_Q,T_P.
    det=determinant3([[v[i] for v in directions] for i in range(3)])
    assert det != 0

    # Abstract exact exposed-face separator construction. This illustrates
    # linear-algebra mechanics only; the main theorem is proved symbolically.
    V00=(F(0),F(0),F(0),F(0))
    V10=(F(1),F(0),F(0),F(0))
    V01=(F(0),F(1),F(0),F(0))
    V11=(F(0),F(0),F(1),F(0))
    off=(F(0),F(-2),F(0),F(1))
    # Exposed face w=(0,0,0,1), L_01(y)=second coordinate.
    # Off-face L01(off)=-2 and slack=1 -> exact M=2.
    H=add(V00,V11,mul(-1,V01))
    Phi=lambda z:z[1]+F(2)*z[3]
    assert Phi(H)==-1
    assert all(Phi(z)>=0 for z in (V00,V10,V01,V11,off))
    assert sum(abs(x) for x in (F(0),F(1),F(0),F(2)))==3
    print('INPUT_TWO_LAW: A=B=1/2; A kernel P=(1/4,3/4), Q=(3/4,1/4); B P=(2/5,3/5), Q=(3/5,2/5)')
    print('LR_TERMINAL_RATIOS:',', '.join(map(str,ratios)))
    print('POLICIES: LR deterministic 144; FULL deterministic 432')
    print('RECTANGLE V00:',corner[(0,0)])
    print('RECTANGLE V01:',corner[(0,1)])
    print('RECTANGLE V10:',corner[(1,0)])
    print('RECTANGLE V11:',corner[(1,1)])
    print('RECTANGLE_RANK3_DETERMINANT:',det)
    print('FULL_BYPASS_VIA_WITNESS:',witness)
    print('BYPASS_DECOMPOSITION_EQUALITY: TRUE')
    print('EXACT_GLOBAL_LR_MIN:',min_lr,'EXACT_FULL_MIN:',min_full)
    print('SIGNED_SEPARATOR: 100e_P + 100e_Q + 11T_P + 11T_Q >= 131 for all LR; FULL witness=130')
    print('L_INFINITY_DISTANCE_LOWER_BOUND: 1/222')
    print('ABSTRACT_FACE_SEPARATION: Phi=coordinate_2+2*coordinate_4 >= 0 for LR corners+off-face; Phi(H)=-1')
    print('PASS_EXACT_R5_BYPASS_RECTANGLE_FACET_VETO')

if __name__=='__main__':
    main()
