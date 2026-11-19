#!/usr/bin/env python3
"""Exact-rational checks for EC49FTM pushforward of BRC16943 parent price law.
No native Bellman rerun; no external packages required.
"""
from fractions import Fraction as Q
from math import comb
import json

A0,A1=Q(3,4),Q(49,64)
B0,B1=Q(7,16),Q(57,128)
AREA=(A1-A0)*(B1-B0)
C0,C1=Q(77,105),Q(2,35)  # a_c(b)=C0+C1*b

def lin(const=0, a=0, b=0):
    return {(0,0):Q(const),(1,0):Q(a),(0,1):Q(b)}

def mul(p,q):
    out={}
    for (i,j),x in p.items():
        for (k,l),y in q.items():
            out[(i+k,j+l)]=out.get((i+k,j+l),Q(0))+x*y
    return out

def integrate_a_then_b(p, interior):
    # Each a^i b^j is integrated on [A0,a_c(b)] or [a_c(b),A1].
    total=Q(0)
    for (i,j),c in p.items():
        n=i+1
        for k in range(n+1):
            ck=Q(comb(n,k))*C0**(n-k)*C1**k
            piece=ck * ((B1**(j+k+1)-B0**(j+k+1))/Q(j+k+1))
            total+=c*piece/Q(n)*(1 if interior else -1)
        endpoint=(A0 if interior else A1)**n
        total-=c*endpoint/Q(n)*((B1**(j+1)-B0**(j+1))/Q(j+1))*(1 if interior else -1)
    return total

def E(p_in,p_top):
    return (integrate_a_then_b(p_in,True)+integrate_a_then_b(p_top,False))/AREA

Z=lin(Q(-5,96), Q(105,96), Q(-6,96))
M=lin(Q(-9,8), Q(525,8), Q(-462,8))
ZT=lin(Q(3,4)); MT=lin(47,b=-54)
ONE=lin(1)
pclip=E(lin(0),ONE)
pinner=E(ONE,lin(0))
EZ=E(Z,ZT); EM=E(M,MT); EMZ=E(mul(M,Z),mul(MT,ZT))
EZ2=E(mul(Z,Z),mul(ZT,ZT)); EM2=E(mul(M,M),mul(MT,MT))
COV=EMZ-EM*EZ
VARZ=EZ2-EZ*EZ; VARM=EM2-EM*EM
assert pclip==Q(19,42) and pinner==Q(23,42)
assert EZ==Q(964373,1290240) and EM==Q(494813,21504)
assert EMZ==Q(13634293007,792723456)
assert COV==Q(1329833,2312110080)
assert VARZ==Q(654049,69363302400) and VARM==Q(60097,1204224)
assert COV**2/(VARZ*VARM)==Q(1768455807889,2515608496192)
assert E(lin(0),MT)/pclip==Q(140851,6080)
assert E(M,lin(0))/pinner==Q(1347257,58880)

jac=Q(525,8)*Q(-1,16)-Q(-231,4)*Q(35,32)
assert jac==Q(945,16)
density=Q(1)/AREA/jac
assert density==Q(131072,945)
M2,M3=Q(1469,64),Q(187,8)
def line_density(m):
    return Q(64,25515)*(64*m-1055)
line_mass=Q(64,25515)*(32*(M3*M3-M2*M2)-1055*(M3-M2))
assert line_mass==pclip

for i in range(31):
    for j in range(31):
        a=A0+(A1-A0)*Q(i,30)
        b=B0+(B1-B0)*Q(j,30)
        ac=C0+C1*b
        if a<=ac:
            z=Q(105,96)*a-Q(1,16)*b-Q(5,96)
            m=Q(525,8)*a-Q(231,4)*b-Q(9,8)
            assert a==Q(47,945)-m/Q(945)+Q(44,45)*z
            assert b==Q(1,27)-m/Q(54)+Q(10,9)*z
        else:
            z=Q(3,4); m=Q(47)-54*b
            assert M2<=m<=M3 and line_density(m)>0

def fm_high(m):
    return (6555968-274432*m)/Q(127575)
assert line_density(M2)/fm_high(M2)==Q(115,223)
assert line_density(M3)/fm_high(M3)==1

fmt=lambda q: str(q.numerator)+'/'+str(q.denominator)
res={'schema':'EC49FTM_EXACT_JOINT_LAW_V1','status':'AUTHOR_CHECKED_PARENT_DEPENDENT_NOT_REVIEWED',
    'parent':'EC49FTL #2779 / EC49FTH #2774',
    'frozen_science':'fc0f038e7bfd12c886b4d37f900bfb770c0f61ab',
    'joint_density_interior':fmt(density), 'jacobian':fmt(jac),
    'singular_line_density':'64*(64*m-1055)/25515 on m in [1469/64,187/8] at z=3/4',
    'interior_mass':fmt(pinner),'boundary_mass':fmt(pclip),
    'E_MZ':fmt(EMZ),'Cov_MZ':fmt(COV),'Var_M':fmt(VARM),'Var_Z':fmt(VARZ),
    'Pearson_R_squared':fmt(COV**2/(VARZ*VARM)),
    'E_M_given_clipped':fmt(E(lin(0),MT)/pclip),
    'E_M_given_interior':fmt(E(M,lin(0))/pinner),
    'P_clipped_given_M_m2_right':fmt(line_density(M2)/fm_high(M2)),
    'P_clipped_given_M_m3_left':fmt(line_density(M3)/fm_high(M3)),
    'rational_inverse_grid':'31x31',
    'verification':'all assertions passed; pure Fraction polynomial integration and 961 inverse-grid tests'}
print(json.dumps(res,ensure_ascii=False,indent=2))
