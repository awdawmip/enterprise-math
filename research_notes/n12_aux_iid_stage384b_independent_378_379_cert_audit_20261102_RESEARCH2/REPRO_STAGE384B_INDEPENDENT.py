#!/usr/bin/env python3
"""Independent exact-continuum verification of Stage378-B and Stage379-B incremental exclusions.

Accepts Stage378-B and Stage379-B CSVs as untrusted input. Does not import
or execute the earlier checkers, and reconstructs signed supports from the 16 labeled audit
comparisons and four residuals for each arbitrary closed leaf rectangle.
Stdlib-only; all relevant decisions use fractions.Fraction.
"""
from __future__ import annotations
import csv
import hashlib
import io
import json
import sys
from fractions import Fraction as F
from pathlib import Path

CUBICS = ((F(1),F(-3),F(3),F(-1)),
          (F(0),F(1),F(-2),F(1)),
          (F(0),F(0),F(1),F(-1)),
          (F(0),F(0),F(0),F(1)))
WEIGHTS=(1,3,3,1)
MEANS=(61,21,9,9)
LAMBDA=F(483,400)
BUDGET_UPPER=F(97582683,10**10)
C_REF=F(16174336378406867755705673,256000000000000000000000000)
PREF=(F(23113910,10**8), F(55568442,10**8))
QREF=(F(23780690,10**8), F(57569391,10**8))
STAGE378 = {
    'lambda':F(97,80),
    'boxes':{
      'P':(F(2308,10000),F(2345,10000),F(55,100),F(56,100)),
      'Q_LO':(F(2365,10000),F(239,1000),F(5756,10000),F(57565,100000)),
      'Q_HI':(F(2365,10000),F(239,1000),F(57575,100000),F(576,1000))},
    'limits':{'P':F(37536223,10**9),'Q_LO':F(37476695,10**9),'Q_HI':F(37476680,10**9)},
    'counts':{'P':637,'Q_LO':57,'Q_HI':100},
    'sha':'1c7552cc6ae40cb133faee01b59b47329e4357691bb58e7198cabda2b5a826bc',
}
STAGE379 = {
    'lambda':F(483,400),
    'boxes':{
 'P':(F(2308,10000),F(2345,10000),F(55,100),F(56,100)),
 'Q_LO':(F(2365,10000),F(239,1000),F(57565,100000),F(57566,100000)),
 'Q_HI':(F(2365,10000),F(239,1000),F(57574,100000),F(57575,100000)),
},
'limits':{'P':F(37517335,10**9),'Q_LO':F(37446850,10**9),'Q_HI':F(37446805,10**9)},
'counts':{'P':1344,'Q_LO':37,'Q_HI':72},
'sha':'aa48034a214df51a493d387862e12d05eed5b18681299574f41264656262d828',
}
BOXES=STAGE379['boxes']
LIMITS=STAGE379['limits']

def eval_poly(p,z):
    return ((p[3]*z+p[2])*z+p[1])*z+p[0]
def eval_derivative(p,z):
    return (3*p[3]*z+2*p[2])*z+p[1]
def bk(k,z):
    return eval_poly(CUBICS[k],z)
def residual(k,x,y):
    return (4*bk(k,x)+bk(k,y))/5-F(MEANS[k],160)
def original(x,y):
    b=F(5,32)*sum(WEIGHTS[k]*abs(residual(k,x,y)) for k in range(4))
    def D(a,z):
        return sum(WEIGHTS[k]*abs(bk(k,a)-bk(k,z)) for k in range(4))/2
    c=(63*D(F(1,4),x)+D(F(3,4),x)+9*D(F(1,4),y)+7*D(F(3,4),y))/256
    return b,c

def support(box):
    """Independently expand signed lower supports into power-basis cubics.

    By |u| >= s*u, where s = +/-1 (or zero), valid over entire leaf.
    Each signed source is a sum of a constant and one-variable cubics.
    Bernstein degree-3 range enclosure is valid on every real point.
    """
    xl,xu,yl,yu=box
    xm=(xl+xu)/2; ym=(yl+yu)/2
    px=[F(0)]*4; py=[F(0)]*4; const=F(0)
    def add(target,k,factor):
        for j,v in enumerate(CUBICS[k]):
            target[j]+=factor*v
    for k,w in enumerate(WEIGHTS):
        rr=residual(k,xm,ym)
        sr=(rr>0)-(rr<0)
        add(px,k,LAMBDA*w*sr/8)
        add(py,k,LAMBDA*w*sr/32)
        const-=LAMBDA*w*sr*MEANS[k]/1024
        for a,mult,target,z in (
            (F(1,4),63,px,xm),(F(3,4),1,px,xm),
            (F(1,4),9,py,ym),(F(3,4),7,py,ym)):
            v=bk(k,a)-bk(k,z)
            sg=(v>0)-(v<0)
            add(target,k,-F(mult*w*sg,512))
            const+=F(mult*w*sg,512)*bk(k,a)
    def ber_lo(coeff,a,b):
        va=eval_poly(coeff,a); vb=eval_poly(coeff,b)
        h=(b-a)/3
        return min(va,va+h*eval_derivative(coeff,a),vb-h*eval_derivative(coeff,b),vb)
    return const+ber_lo(px,xl,xu)+ber_lo(py,yl,yu)

def bisect_box(box,bit):
    a,b,c,d=box
    if b-a>=d-c:
        midpoint=(a+b)/2
        return (a,midpoint,c,d) if bit=='0' else (midpoint,b,c,d)
    midpoint=(c+d)/2
    return (a,b,c,midpoint) if bit=='0' else (a,b,midpoint,d)

def verify_prerequisites():
    # Direct root-existence certificate: Poincare-Miranda face signs.
    xl=F(231083940,10**9); xu=F(231083942,10**9)
    yl=F(555508852,10**9); yu=F(555508864,10**9)
    assert residual(0,xl,yu)>0>residual(0,xu,yl)
    assert residual(1,xl,yl)>0 and residual(1,xu,yl)>0
    assert residual(1,xl,yu)<0 and residual(1,xu,yu)<0
    # r0 decreases in x,y; r1 increases in x and decreases in y.
    # Hence simultaneous root exists uniquely in open box.
    blo=F(15,16)*residual(2,xl,yl)
    bhi=F(15,16)*residual(2,xu,yu)
    assert 0<blo<bhi and 2*bhi+F(11,5000)<BUDGET_UPPER
    bp,cp=original(*PREF); bq,cq=original(*QREF)
    assert bp+bq<2*blo+F(11,5000)
    assert cp+cq==C_REF
    dual=C_REF+LAMBDA*BUDGET_UPPER
    gaps={name:LIMITS['P']+LIMITS[name]-dual for name in ('Q_LO','Q_HI')}
    assert all(z>0 for z in gaps.values())
    # Only the incremental strips are checked; inherited Stage378 is separate.
    assert BOXES['Q_LO'][3]<BOXES['Q_HI'][2]
    return {'root_beta_lower':str(blo),'root_beta_upper':str(bhi),
            'reference_cost':str(C_REF),'reference_budget':str(bp+bq),
            'dual_threshold':str(dual),'strict_exclusion_gaps':{k:str(v) for k,v in gaps.items()}}

def audit_csv(path):
    raw=Path(path).read_bytes()
    text=raw.decode('utf-8')
    assert text.startswith('region,path,xlo,xhi,ylo,yhi,lower\n')
    rows=csv.DictReader(io.StringIO(text))
    tree={name:{} for name in BOXES}
    minmargins={name:None for name in BOXES}
    for row in rows:
        region=row['region'];assert region in BOXES
        route=row['path']; assert set(route)<=set('01')
        assert route not in tree[region]
        box=BOXES[region]
        for bit in route:
            box=bisect_box(box,bit)
        supplied=tuple(F(row[s]) for s in ('xlo','xhi','ylo','yhi'))
        assert supplied==box
        lower=support(box)
        assert lower==F(row['lower'])
        strict_margin=lower-LIMITS[region]
        assert strict_margin>0
        minmargins[region]=strict_margin if minmargins[region] is None else min(minmargins[region],strict_margin)
        tree[region][route]=box
    for region,paths in tree.items():
        assert paths
        all_prefixes={p[:i] for p in paths for i in range(len(p)+1)}
        def covered(prefix):
            if prefix in paths:
                return 1
            assert prefix+'0' in all_prefixes and prefix+'1' in all_prefixes
            return covered(prefix+'0')+covered(prefix+'1')
        assert covered('')==len(paths)
        area=sum((b-a)*(d-c) for a,b,c,d in paths.values())
        a,b,c,d=BOXES[region]
        assert area==(b-a)*(d-c)
    return {'certificate_sha256':hashlib.sha256(raw).hexdigest(),
            'certificate_bytes':len(raw),
            'leaves':{key:len(v) for key,v in tree.items()},
            'minimal_strict_support_margins':{key:str(v) for key,v in minmargins.items()},
            'coverage':'full-closed-boxes-with-exact-prefix-tree-and-area'}

def main():
    if len(sys.argv)!=3:raise SystemExit('usage: REPRO_STAGE384B_INDEPENDENT.py Stage378.csv Stage379.csv')
    global LAMBDA,BOXES,LIMITS
    report={'scope':'Stage378+Stage379 consecutive exact exclusions, conditional on inherited Stage377 box and earlier localization',
            'method':'independent Fraction polynomial expansion, signed supporting hyperplanes, cubic Bernstein range and binary prefix cover',
            'stages':{}}
    for tag,config,path in [('378',STAGE378,sys.argv[1]),('379',STAGE379,sys.argv[2])]:
        LAMBDA=config['lambda'];BOXES=config['boxes'];LIMITS=config['limits']
        pre=verify_prerequisites()
        cert=audit_csv(path)
        assert cert['leaves']==config['counts']
        assert cert['certificate_sha256']==config['sha']
        report['stages'][tag]={'prerequisites':pre,'certificate':cert}
    # Chaining: Stage377 Q_y (0.5756,0.576) minus 378's two closed
    # strips becomes Stage378 (0.57565,0.57575), minus 379's strips
    # becomes Stage379 (0.57566,0.57574), retaining strict ends.
    assert STAGE378['boxes']['Q_LO'][2]==F(5756,10000)
    assert STAGE378['boxes']['Q_HI'][3]==F(576,1000)
    assert STAGE379['boxes']['Q_LO'][2]==STAGE378['boxes']['Q_LO'][3]
    assert STAGE379['boxes']['Q_HI'][3]==STAGE378['boxes']['Q_HI'][2]
    assert STAGE379['boxes']['Q_LO'][3]==F(57566,100000)
    assert STAGE379['boxes']['Q_HI'][2]==F(57574,100000)
    print('STAGE384B_INDEPENDENT_STAGE378_STAGE379_CHAIN_PASS')
    print(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()
