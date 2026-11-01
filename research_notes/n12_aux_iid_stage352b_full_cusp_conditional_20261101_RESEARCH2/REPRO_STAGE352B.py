#!/usr/bin/env python3
"""Stage352-B: exact global cusp-box and fused 16-tag audit certificates.

Run from a repository checkout with Stage348-B and Stage351-B research_notes
present, or provide both EM_STAGE348B_CHECKER and EM_STAGE351B_CHECKER file
paths. This extends, rather than recopies, their exact Fraction utilities.
All new mathematical checks use exact fractions; asserts must be enabled.
"""
from __future__ import annotations
from fractions import Fraction as F
from hashlib import sha256
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import os

assert __debug__, 'Run with assertions enabled.'
HERE=Path(__file__).resolve().parent
NOTES=HERE.parent
DEFAULT_348=NOTES/'n12_aux_iid_stage348b_global_initial_extension_20261101_RESEARCH2'/'REPRO_STAGE348B.py'
DEFAULT_351=NOTES/'n12_aux_iid_stage351b_exact_cusp_onset_20261101_RESEARCH2'/'REPRO_STAGE351B.py'

def import_file(name,path):
    sp=spec_from_file_location(name,str(path)); assert sp and sp.loader
    m=module_from_spec(sp);sp.loader.exec_module(m);return m

old=import_file('stage348b',Path(os.environ.get('EM_STAGE348B_CHECKER',DEFAULT_348)))
# Stage351-B's module-level assertions re-run its self-contained continuous-arc
# Fraction interval proof and root isolators. Its marker appears in stdout.
arc=import_file('stage351b',Path(os.environ.get('EM_STAGE351B_CHECKER',DEFAULT_351)))

Q=F(5961,10**6)
C0=F(3055,10**5)
LAMBDA=F(121,100)
E0=F(1,500) # previous global endpoint theorem's budget
RECT=(F(219,1000),F(6,25),F(101,200),F(16,25))
LOW=(RECT[0],RECT[1],RECT[2],F(531,1000))
HIGH=(RECT[0],RECT[1],F(5,8),RECT[3])

# Reuse the proven exact Bernstein formulas and quadtree partition checker.
old.QPUBLIC=Q;old.QAUDIT=C0;old.LAMBDA=LAMBDA
old.LIFT_THRESHOLD=C0+LAMBDA*Q
old.RECT=RECT;old.LOW=LOW;old.HIGH=HIGH

# Source provenance: 4 word laws * 4 port/anchor comparisons = 16 tagged
# comparisons, not a total-only projected observer. Check all fixed strip
# signs by exact cubic Bernstein coefficients on the *new* rectangles.
expected={('x',F(1,4)):'-+++',('x',F(3,4)):'--++',
          ('low',F(1,4)):'++--',('low',F(3,4)):'--++',
          ('high',F(1,4)):'++--',('high',F(3,4)):'---+'}
for name,a,d in [('x',RECT[0],RECT[1]),('low',LOW[2],LOW[3]),
                 ('high',HIGH[2],HIGH[3])]:
    for anchor in (F(1,4),F(3,4)):
        pattern=''
        for k in range(4):
            v=lambda z:old.B(k,anchor)-old.B(k,z)
            dv=lambda z:-old.Bp(k,z)
            t=(d-a)/3
            coeff=(v(a),v(a)+t*dv(a),v(d)-t*dv(d),v(d))
            assert all(x>0 for x in coeff) or all(x<0 for x in coeff), (name,anchor,k,coeff)
            pattern+='+' if coeff[0]>0 else '-'
        assert pattern==expected[(name,anchor)], (name,anchor,pattern)

# Verify the same full tagged piecewise c polynomial on new low/high strips,
# and check every corner of 16-tag polynomial identities using rational nodes.
for ix in range(4):
    x=RECT[0]+(RECT[1]-RECT[0])*ix/3
    for box,poly,K in [(LOW,old.pylo,old.KL),(HIGH,old.pyhi,old.KH)]:
        for iy in range(4):
            y=box[2]+(box[3]-box[2])*iy/3
            assert old.c(x,y)==K+old.px(x)+poly(y)

# Exact qstar and cusp isolation has already run on Stage351 import.
assert arc.beta_hi+arc.sc_hi<Q
assert E0<arc.sc_lo
assert F('0.0021814072266')<arc.sc_lo<arc.sc_hi<F('0.0021814072275')

# New strict right-arc incumbent comparison at old E0=0.0020.
# These four rational corners enclose the r1=0 unique candidate q_E0.
xl,xu,yl,yu=F(2371,10000),F(2373,10000),F(287,500),F(359,625)
assert yl<yu<arc.yc_lo
assert old.r(1,xl,yl)<0
assert F(15,16)*old.r(2,xl,yl)<arc.beta_lo+E0
assert old.r(1,xu,yl)>0>old.r(1,xu,yu)
assert F(15,16)*old.r(2,xu,yl)>arc.beta_hi+E0
# On this lower-tag domain c_x<0,c_y>0, so upper cost is c(xl,yu).
C_E0_UPPER=old.c(xl,yu)
assert C_E0_UPPER<C0

# Verify the middle-band exact premises used in prior sourcewise chamber
# classification, now also over the newly included x∈[0.219,0.220].
assert old.r(2,RECT[0],LOW[3])>0  # r2 increasing for both z<2/3
p=lambda z:(1-z)*(189-183*z)/256
assert p(RECT[1])>F(43,100)
# (-,+) constant-b path has dy/dx=4(1-2x)/(2y-1).
assert F(3,256)*4*(1-2*RECT[0])/(2*LOW[3]-1)<F(43,100)
assert (8*F(23,40)-1)**2 < 13
assert F(1,40)*4*(1-2*RECT[0])/(2*F(23,40)-1)<F(43,100)
# r1=0 implicit slope <=5 across expanded middle rectangle.
g=lambda y:(1-y)*(3*y-1)
n=lambda x:4*(1-x)*(1-3*x)
assert n(RECT[0])/g(LOW[3])<5
assert p(RECT[1])>F(1,40)*5
# r0=0 lower-left branch sign comparisons, identical but valid on new box.
f=lambda z:z*(2-3*z)/(1-z)**2
assert f(F(3,5))>f(F(231084,10**6))
assert old.r(0,F(228,1000),F(3,5))<0
assert f(F(5,8))>f(F(228,1000))

certificate_info=[]
for mode,n in [('GLOBAL',391),('LOW',22),('HIGH',1)]:
    leaves=old.make_leaves(RECT,mode)
    assert len(leaves)==n,(mode,len(leaves))
    old.validate_partition(leaves,mode)
    contents=old.to_csv(leaves)
    name='CERTIFICATE_STAGE352B_'+mode+'.csv'
    target=HERE/name
    if target.exists():assert target.read_text(encoding='utf-8')==contents
    else:target.write_text(contents,encoding='utf-8')
    vals=[z[-1] for z in leaves if z[5]!='INNER']
    threshold=Q if mode=='GLOBAL' else old.LIFT_THRESHOLD
    assert min(vals)>threshold
    area=sum(((v[2]-v[1])*(v[4]-v[3]) for v in leaves),F(0))
    assert area==(F(1) if mode=='GLOBAL' else (LOW[1]-LOW[0])*(LOW[3]-LOW[2])
                  if mode=='LOW' else (HIGH[1]-HIGH[0])*(HIGH[3]-HIGH[2]))
    h=sha256(contents.encode('utf-8')).hexdigest()
    certificate_info.append((mode,len(leaves),max(z[0] for z in leaves),min(vals)-threshold,h))

# Margins are exact, although printed decimals below are only for readers.
print('STAGE352B_EXACT_GLOBAL_CUSP_ENCLOSURE_AND_FUSED_BARRIER_PASS')
print('Q=',str(Q),'C0=',str(C0),'lambda=',str(LAMBDA),'threshold=',str(old.LIFT_THRESHOLD))
print('beta_upper_plus_cusp_upper_less_than_Q=',str(Q-(arc.beta_hi+arc.sc_hi)))
print('arc_cost_at_E0_upper=',str(C_E0_UPPER),'gap_below_C0=',str(C0-C_E0_UPPER))
for mode,count,depth,margin,h in certificate_info:
    print('certificate',mode,'leaves',count,'max_depth',depth,'strict_min_margin',str(margin),'sha256',h)
print('middle_r3_nonnegative_dominance=INHERITED_AUTHOR_LEMMA_STAGE342B')
print('global_b_unique_minimum=INHERITED_AUTHOR_LEMMA_STAGE346B')
print('global_cusp_onset=CONDITIONAL_ON_INHERITED_AUTHOR_LEMMAS')
print('native_X6_bridge=NOT_ESTABLISHED; independent_review=NOT_DONE')
