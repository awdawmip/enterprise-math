#!/usr/bin/env python3
"""Exact arithmetic certificate for X6 R108, all C>=1 ray atlas.

Independent limited research verifier, no third-party dependencies.
The finite all-lattice certificate is the analytic moment-box reduction in the paper;
the q<=40 brute force below is a separate finite cross-check.
"""
from fractions import Fraction as Q
from math import lcm
import json

LOW = [
    ((4,-1,0),4,Q(4,3),Q(17,4)),
    ((5,-1,0),5,Q(4,3),Q(13,2)),
    ((6,-4,1),7,Q(1),Q(17,4)),
    ((10,-5,1),11,Q(4,3),Q(9)),
    ((11,-5,1),12,Q(4,3),Q(13,2)),
    ((15,-6,1),16,Q(1),Q(4)),
    ((16,-9,2),18,Q(4,3),Q(97,23)),
    ((21,-10,2),23,Q(1),Q(4)),
    ((25,-11,2),27,Q(4,3),Q(11,4)),
    ((31,-15,3),34,Q(4,3),Q(11,4)),
]
MID = [
    ((1,0,0),1,Q(37,3)),
    ((5,-4,1),6,Q(37,3)),
    ((9,-5,1),10,Q(19)),
    ((10,-5,1),11,Q(17,3)),
    ((14,-9,2),16,Q(97,3)),
    ((15,-9,2),17,Q(19)),
    ((19,-10,2),21,Q(77,3)),
    ((23,-14,3),26,Q(157,3)),
    ((24,-14,3),27,Q(39)),
    ((25,-14,3),28,Q(77,3)),
    ((29,-18,4),33,Q(157,3)),
    ((34,-19,4),38,Q(137,3)),
]
HIGH_E8 = [(1,0,0),(5,-4,1),(9,-5,1),(15,-9,2),
           (19,-10,2),(23,-14,3),(25,-14,3),(29,-18,4)]
HIGH_E3 = [(10,-5,1),(14,-9,2),(34,-19,4)]
HIGH_E1 = [(24,-14,3)]


def moments(a):
    x,y,z=a
    return x+3*y+6*z, 3*x+12*y+30*z, 7*x+39*y+126*z


def port(a):
    return max(sum(max(t,0) for t in a),sum(max(-t,0) for t in a))


def canonical(a):
    for t in a:
        if t>0:return a
        if t<0:return tuple(-i for i in a)
    raise ValueError('zero vector')


def score(a,C):
    u,v,h=moments(a)
    return max(Q(abs(u),10),Q(abs(v))/(C+9),Q(abs(h),50),
               Q(abs(v-u))/(C+1),Q(abs(h-u),42),Q(abs(h-v))/(C+41))


def eta(C,p):
    if C<=Q(5,2):return Q(2,7)
    if C<=9:return Q(1)/(C+1)
    if C<=59:return Q(1,10)
    if p<=26:return Q(1,10)
    return Q(6)/(C+1)


def predict_near(C,p):
    if C<=9:
        return {a for a,q,L,U in LOW if q<=p and
                (C>L or C==1 and L==1) and (C<U or C==9 and U==9)}
    if C<=59:
        return {a for a,q,L in MID if q<=p and C>L}
    if p<=26:
        return {a for a,q,_ in MID if q<=p and q<=26}
    if C<62: return {a for a,q,_ in MID if q<=p}
    if C<89: return {a for a in HIGH_E3+HIGH_E1 if port(a)<=p}
    return set(HIGH_E1)


def congruent_moments(u,v,h):
    return v%3==0 and (h-u)%6==0 and (h-u-6*v)%12==0


def inverse(u,v,h):
    assert congruent_moments(u,v,h)
    return ( (h+19*u-8*v)//2, (-h-14*u+7*v)//3, (h+11*u-6*v)//12 )


def moment_box_check():
    d=set()
    all_valid=0
    for u in range(-4,5):
        for v in range(-4,5):
            for h in range(-21,22):
                if abs(v-u)>1 or abs(h-u)>17 or abs(h-v)>18:continue
                if not congruent_moments(u,v,h):continue
                a=inverse(u,v,h)
                if a==(0,0,0):continue
                assert moments(a)==(u,v,h)
                all_valid+=1
                d.add(canonical(a))
    assert d=={x[0] for x in LOW},(d,{x[0] for x in LOW})
    assert all_valid==20
    return {'moment_box':'9*9*43_with_exact_intersection_constraints',
            'nonzero_oriented':all_valid,'unoriented_candidates':len(d)}


def interval_check():
    # No sampling inference: formula cutoffs are derived by solving linear
    # inequalities against the exact two eta(C) expressions.
    for a,q,L,U in LOW:
        assert port(a)==q
        u,v,h=moments(a)
        fixed=max(Q(abs(u),10),Q(abs(h),50),Q(abs(h-u),42))
        l=max(Q(1),Q(7*abs(v),3)-9,Q(7*abs(v-u),3)-1,
              Q(7*abs(h-v),3)-41)
        upper=min(Q(9),Q(3,2)/fixed-1) if fixed else Q(9)
        if 2*abs(v)>3: upper=min(upper,Q(27-2*abs(v),2*abs(v)-3))
        if 2*abs(h-v)>3: upper=min(upper,Q(123-2*abs(h-v),2*abs(h-v)-3))
        assert (L,U)==(l,upper), (a,(L,U),(l,upper))
    for a,q,L in MID:
        assert port(a)==q
        u,v,h=moments(a)
        lower=max(Q(9),Q(20*abs(v),3)-9,
                  Q(20*abs(v-u),3)-1,Q(20*abs(h-v),3)-41)
        assert max(Q(9),L)==lower,(a,L,lower)
        assert max(Q(abs(u),10),Q(abs(h),50),Q(abs(h-u),42))<Q(3,20)
    return {'low_rows':len(LOW),'mid_rows':len(MID), 'linear_inequality_cutoffs':'PASS'}


def high_low_port_box_check():
    # For C>=59 and p<=26: F_C<3/20 forces |u|<=1, |h|<=7,
    # |h-u|<=6 independently of C. Port bounds imply |v|<=55.
    result=set()
    oriented=0
    for u in range(-1,2):
      for h in range(-7,8):
        if abs(h-u)>6:continue
        for v in range(-55,56):
          if not congruent_moments(u,v,h):continue
          a=inverse(u,v,h)
          if a==(0,0,0) or port(a)>26:continue
          oriented+=1
          result.add(canonical(a))
    target={a for a,q,_ in MID if q<=26}
    assert result==target,(result,target)
    assert oriented==16,oriented
    return {'oriented':oriented,'unoriented':len(result),'complete':'PASS'}


def finite_crosscheck():
    # Independent enumeration of entire unoriented integer difference set q<=40.
    a_list=[]
    for x in range(-40,41):
      for y in range(-40,41):
       for z in range(-40,41):
        a=(x,y,z)
        if a==(0,0,0) or canonical(a)!=a or port(a)>40:continue
        a_list.append((port(a),a,moments(a)))
    assert len(a_list)==110740, len(a_list)
    test_C = [Q(1),Q(4,3),Q(2),Q(5,2),Q(11,4),Q(4),Q(97,23),
              Q(17,4),Q(6),Q(13,2),Q(7),Q(9),Q(10),Q(37,3),
              Q(19),Q(77,3),Q(97,3),Q(39),Q(137,3),
              Q(157,3),Q(58),Q(59),Q(61),Q(62),Q(88),Q(89),Q(100)]
    critical={a[2] for a in MID}|{a[2] for a in LOW}|{a[3] for a in LOW}|{Q(5,2),Q(9),Q(59),Q(62),Q(89)}
    for t in critical:
        if t>=1:test_C.extend([t-Q(1,1000),t+Q(1,1000)])
    test_C=sorted({C for C in test_C if C>=1})
    budgets=[11,12,16,17,18,21,23,26,27,28,33,34,38,40]
    total_checks=0
    for C in test_C:
        cn,cd=C.numerator,C.denominator
        denom=[10,cn+9*cd,50,cn+cd,42,cn+41*cd]
        L=lcm(*denom)
        scores=[]
        for q,a,(u,v,h) in a_list:
            s=max(abs(u)*(L//10),abs(v)*cd*(L//denom[1]),abs(h)*(L//50),
                  abs(v-u)*cd*(L//denom[3]),abs(h-u)*(L//42),
                  abs(h-v)*cd*(L//denom[5]))
            scores.append((q,a,s))
        for p in budgets:
            feasible=[(a,s) for q,a,s in scores if q<=p]
            best=min(s for a,s in feasible)
            expected=eta(C,p)*L
            assert best==expected,(C,p,'eta',best,expected)
            actual={a for a,s in feasible if 2*s<3*best}
            predicted=predict_near(C,p)
            assert actual==predicted,(C,p,'near',actual^predicted)
            total_checks+=1
    return {'q_max':40,'unoriented_vectors':len(a_list),
            'exact_rational_parameters':len(test_C), 'port_budgets':len(budgets),
            'complete_optimum_and_near_set_checks':total_checks, 'all':'PASS'}


def main():
    out={'schema':'EM_X6_R108_EXACT_VERIFICATION_V1',
         'scientific_model':'four-positive-weight six-pair BRC observer w=(9,1,C,41)',
         'parameter_domain':'real C >= 1, integer p>=11',
         'moment_box':moment_box_check(), 'high_low_port':high_low_port_box_check(),
         'cutoffs':interval_check(), 'crosscheck':finite_crosscheck(),
         'scope':'analytic proof infinite-lattice; finite integer q<=40 crosscheck; author-side only'}
    print(json.dumps(out,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
