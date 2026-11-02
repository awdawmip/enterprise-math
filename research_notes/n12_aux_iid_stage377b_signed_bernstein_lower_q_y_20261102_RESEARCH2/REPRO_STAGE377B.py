#!/usr/bin/env python3
"""Stage377-B: exact signed-support Bernstein certificate excluding Q_y <= 0.5756.

Scientific freeze, deliberately unchanged:
  GLOBAL main bf84bd7c61a2444b59b1da96be57df0e9ae47e53
  Enterprise Math main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419
  P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488

Model: 16 individually weighted audit comparisons, four independent Bernoulli
residual channels. All certificate inequalities use fractions, not floats.
The enclosing rectangles and the budget base are those proved in Stages 375-376.
"""
from __future__ import annotations

import argparse
import csv
import io
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
from pathlib import Path

W = (1, 3, 3, 1)
M = (61, 21, 9, 9)
LAMBDA = F(97, 80)
E = F(11, 5000)
BUDGET_UP = F(97582683, 10**10)
# New rational feasible comparison pair, sharper than Stage376's pair.
P_REF = (F(23113910, 10**8), F(55568442, 10**8))
Q_REF = (F(23780690, 10**8), F(57569391, 10**8))
REFERENCE_COST = F(16174336378406867755705673, 256000000000000000000000000)
DUAL_THRESHOLD = REFERENCE_COST + LAMBDA * BUDGET_UP

# All intervals are CLOSED. Earlier stages restrict every global minimizer
# to the interiors of these containers (except x_Q can equal 0.239).
P_RECT = (F(577, 2500), F(469, 2000), F(11, 20), F(14, 25))
Q_LOW_RECT = (F(473, 2000), F(239, 1000), F(143, 250), F(1439, 2500))
RECTS = {'P': P_RECT, 'Q': Q_LOW_RECT}
# Exact source-wise Lagrangian lower targets whose sum exceeds the dual threshold.
TARGETS = {'P': F(3753605, 10**8), 'Q': F(3747692, 10**8)}


@lru_cache(None)
def bernoulli(k: int, z: F) -> F:
    return z**k * (1-z)**(3-k)


@lru_cache(None)
def bernoulli_derivative(k: int, z: F) -> F:
    first = k * z**(k-1) * (1-z)**(3-k) if k else F(0)
    second = (3-k)*z**k * (1-z)**(2-k) if k < 3 else F(0)
    return first - second


def residual(k: int, x: F, y: F) -> F:
    return (4*bernoulli(k, x)+bernoulli(k, y))/5-F(M[k],160)


def source(x: F, y: F) -> tuple[F, F]:
    """Exact b,c from every original label, with no aggregated label collapse."""
    b = F(5,32)*sum(W[k]*abs(residual(k,x,y)) for k in range(4))
    def distance(a: F, z: F) -> F:
        return F(1,2)*sum(W[k]*abs(bernoulli(k,a)-bernoulli(k,z)) for k in range(4))
    c = (63*distance(F(1,4),x)+distance(F(3,4),x)
         +9*distance(F(1,4),y)+7*distance(F(3,4),y))/256
    return b,c


def root_and_comparator_checks() -> tuple[F,F,F]:
    """Poincare-Miranda face signs isolate the pinned r0=r1=0 root.

    r0 decreases in x,y. r1 increases in x and decreases in y on the box.
    r2 increases in both, since both coordinates lie in (0,2/3).
    """
    xl,xu = F(231083940,10**9),F(231083942,10**9)
    yl,yu = F(555508852,10**9),F(555508864,10**9)
    assert 0<xl<xu<F(1,3)<yl<yu<F(2,3)
    assert residual(0,xl,yu)>0>residual(0,xu,yl)
    assert residual(1,xl,yl)>0 and residual(1,xu,yl)>0
    assert residual(1,xl,yu)<0 and residual(1,xu,yu)<0
    assert residual(2,xl,yl)>0 and residual(3,xu,yu)<0
    # At the simultaneous zero, sum_k w_k r_k=0 forces r3=-3*r2;
    # therefore b(q*)=(15/16)*r2(q*). B2 increases on this box.
    beta_lower = F(15,16)*residual(2,xl,yl)
    beta_upper = F(15,16)*residual(2,xu,yu)
    assert 0<beta_lower<beta_upper
    assert 2*beta_upper+E < BUDGET_UP
    bp,cp=source(*P_REF)
    bq,cq=source(*Q_REF)
    assert bp+bq < 2*beta_lower+E
    assert cp+cq == REFERENCE_COST
    assert sum(TARGETS.values()) > DUAL_THRESHOLD
    return beta_lower,beta_upper,bp+bq


def sign(value: F) -> int:
    return (value>0)-(value<0)


@lru_cache(None)
def signed_coefficients(k: int,sr: int,sxa: int,sxb: int,sya: int,syb: int):
    """Lower signed-support polynomial alpha B_k(x)+beta B_k(y)+constant.

    |u|>=s*u for each individual original audit comparison and residual.
    The sign s is chosen at the center but is valid for EVERY point.
    """
    w=W[k]
    ax=w*(LAMBDA*F(sr,8)-F(63*sxa+sxb,512))
    ay=w*(LAMBDA*F(sr,32)-F(9*sya+7*syb,512))
    constant=w*(F(63*sxa+9*sya,512)*bernoulli(k,F(1,4))
                +F(sxb+7*syb,512)*bernoulli(k,F(3,4))
                -LAMBDA*F(M[k]*sr,1024))
    return ax,ay,constant


def cubic_bernstein_lower(coeffs: list[F], lo: F, hi: F) -> F:
    """Global cubic min >= min of four exact Bezier control ordinates."""
    va=sum(coeffs[k]*bernoulli(k,lo) for k in range(4))
    vb=sum(coeffs[k]*bernoulli(k,hi) for k in range(4))
    da=sum(coeffs[k]*bernoulli_derivative(k,lo) for k in range(4))
    db=sum(coeffs[k]*bernoulli_derivative(k,hi) for k in range(4))
    h=hi-lo
    return min(va,va+h*da/3,vb-h*db/3,vb)


def source_lower(box: tuple[F,F,F,F]) -> F:
    """Global exact lower bound of c(x,y)+LAMBDA*b(x,y) on box."""
    xlo,xhi,ylo,yhi=box
    xm=(xlo+xhi)/2
    ym=(ylo+yhi)/2
    bx=[bernoulli(k,xm) for k in range(4)]
    by=[bernoulli(k,ym) for k in range(4)]
    ax=[];ay=[];constant=F(0)
    for k in range(4):
        sxa=sign(bernoulli(k,F(1,4))-bx[k])
        sxb=sign(bernoulli(k,F(3,4))-bx[k])
        sya=sign(bernoulli(k,F(1,4))-by[k])
        syb=sign(bernoulli(k,F(3,4))-by[k])
        sr=sign((4*bx[k]+by[k])/5-F(M[k],160))
        a,b,c=signed_coefficients(k,sr,sxa,sxb,sya,syb)
        ax.append(a);ay.append(b);constant+=c
    return (constant + cubic_bernstein_lower(ax,xlo,xhi)
            + cubic_bernstein_lower(ay,ylo,yhi))


def bisect(box: tuple[F,F,F,F]):
    axis=0 if box[1]-box[0]>=box[3]-box[2] else 2
    mid=(box[axis]+box[axis+1])/2
    left=box[:axis]+(box[axis],mid)+box[axis+2:]
    right=box[:axis]+(mid,box[axis+1])+box[axis+2:]
    return left,right


def emit_certificate():
    rows=[];statistics={}
    for name,rect in RECTS.items():
        stack=[(rect,'')]
        splits=0;depth_max=0;vol=F(0);minimum_margin=None
        while stack:
            box,path=stack.pop()
            depth=len(path)
            low=source_lower(box)
            delta=low-TARGETS[name]
            if delta>0:
                rows.append((name,path,depth,*box,low))
                depth_max=max(depth_max,depth)
                vol+=(box[1]-box[0])*(box[3]-box[2])
                minimum_margin=delta if minimum_margin is None else min(minimum_margin,delta)
                continue
            assert depth<70,('unresolved',name,path,box)
            left,right=bisect(box)
            stack.extend(((left,path+'0'),(right,path+'1')))
            splits+=1
        leaves=sum(row[0]==name for row in rows)
        assert splits+1==leaves and vol==(rect[1]-rect[0])*(rect[3]-rect[2])
        statistics[name]=(splits,leaves,depth_max,minimum_margin)
    header='source,path,depth,xlo,xhi,ylo,yhi,certified_L_lower\n'
    data=header+''.join(','.join(str(t) for t in row)+'\n' for row in rows)
    return data.encode('utf-8'),statistics


def verify_certificate(data: bytes):
    """Replay from a CSV alone; verify every split path and full binary cover."""
    parsed=list(csv.DictReader(io.StringIO(data.decode('utf-8'))))
    groups=defaultdict(dict)
    for row in parsed:
        name=row['source'];assert name in RECTS
        path=row['path'];assert set(path)<=set('01')
        assert path not in groups[name]
        assert int(row['depth'])==len(path)
        box=RECTS[name]
        for bit in path:
            box=bisect(box)[int(bit)]
        expected=(F(row['xlo']),F(row['xhi']),F(row['ylo']),F(row['yhi']))
        assert box==expected
        lower=source_lower(box)
        assert lower==F(row['certified_L_lower'])
        assert lower>TARGETS[name]
        groups[name][path]=box
    for name,rect in RECTS.items():
        paths=groups[name]
        prefixes={p[:j] for p in paths for j in range(len(p)+1)}
        def verify_full_tree(node):
            if node in paths:return 1
            assert node+'0' in prefixes and node+'1' in prefixes,('hole',name,node)
            return verify_full_tree(node+'0')+verify_full_tree(node+'1')
        assert verify_full_tree('')==len(paths)
        assert sum((v[1]-v[0])*(v[3]-v[2]) for v in paths.values())==(rect[1]-rect[0])*(rect[3]-rect[2])
    return {name:len(groups[name]) for name in RECTS}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--emit',type=Path,help='Write complete deterministic exact CSV')
    parser.add_argument('--verify',type=Path,help='Replay an existing exact CSV')
    args=parser.parse_args()
    beta_lo,beta_hi,b_reference=root_and_comparator_checks()
    if args.verify:
        data=args.verify.read_bytes()
        counts=verify_certificate(data)
        assert data==emit_certificate()[0]
    else:
        data,stats=emit_certificate()
        counts=verify_certificate(data)
        if args.emit:
            args.emit.parent.mkdir(parents=True,exist_ok=True)
            args.emit.write_bytes(data)
            assert args.emit.read_bytes()==data
    print('STAGE377B_EXACT_SIGNED_SUPPORT_BERNSTEIN_LOW_Q_STRIP_PASS')
    print('scientific_input_pin_GLOBAL=bf84bd7c61a2444b59b1da96be57df0e9ae47e53')
    print('scientific_input_pin_EM=2af3fc484eb11060b69e0afc1b562bcaf5ad1419')
    print('scientific_input_pin_P000_blob=bcc2590d3168a28f72e8b9f0f9b1f76faadcd488')
    print('E='+str(E)+';lambda='+str(LAMBDA)+';budget_upper='+str(BUDGET_UP))
    print('reference_P='+str(P_REF)+';reference_Q='+str(Q_REF))
    print('reference_cost='+str(REFERENCE_COST)+';dual_threshold='+str(DUAL_THRESHOLD))
    print('root_beta_lower='+str(beta_lo)+';root_beta_upper='+str(beta_hi))
    print('reference_b='+str(b_reference))
    for name in RECTS:
        print('region',name,'leaves',counts[name],
              ('splits='+str(stats[name][0])+' max_depth='+str(stats[name][2])+' minimum_margin='+str(stats[name][3]) if not args.verify else 'replay_only'))
    print('sourcewise_certified_L_lower='+str(TARGETS))
    print('strict_total_dual_margin='+str(sum(TARGETS.values())-DUAL_THRESHOLD))
    print('all_leaf_paths_complete=YES;all_exact_fraction_inequalities=PASS')
    print('total_leaves='+str(len(list(csv.DictReader(io.StringIO(data.decode('utf-8')))))))
    print('certificate_bytes='+str(len(data))+';certificate_sha256='+sha256(data).hexdigest())

if __name__=='__main__':
    main()
