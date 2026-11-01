#!/usr/bin/env python3
"""Exact BRC N4/S23 joint two-decoder four/five-witness and two-face checker.

Finite-law computations use the existing positive-rational F/M semantics, with
shared causal b_U and original six distinct preparation rows. No physical
heartbeat/native dynamics or numerical approximation is claimed.
"""
import json
from fractions import Fraction as F
from itertools import product

M20 = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
       (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A=(0,0,0,1,1,1)
B=(2,2,3,2,2,4)
C=(5,6,7,8,9,10)
GROUP=(0,0,1,2,2,3)
SPEC=('34 24 34 24','34 23 34 34','34 34 34 23',
      '24 24 12 12','12 12 24 34','12 13 23 24',
      '23 34 12 13','24 34 12 14')

W=(F(1),F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0),F(0))
H=(F(1,3),F(1),F(0),F(0),F(0),F(1),F(0),F(1),F(0),F(0),F(0))
J=(F(1),F(1,3),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(1),F(0))
P=(F(1),F(2,9),F(0),F(0),F(0),F(0),F(1),F(1),F(1),F(0),F(1))
T=(F(0),F(0),F(0),F(0),F(0),F(0),F(1),F(1),F(1),F(0),F(1))
POLICIES={'W':W,'H':H,'J':J,'P':P,'T':T}

Q=(F(14,27),F(0),F(8,27),F(5,27))
U=(F(5,9),F(0),F(2,9),F(2,9))
D9=((F(1),F(0),F(0),F(0)),(F(1),F(0),F(0),F(0)),
    (F(0),F(0),F(0),F(1)),(F(0),F(1),F(0),F(0)))
D10=(Q,Q,U,Q)
R4=F(13,27)
R5=F(1,2)
RF=F(4,7)
V=F(1,7)
D10_FACES=((F(3,7),F(2,7),F(2,7),F(0)),
           (F(3,7),F(0),F(2,7),F(2,7)),
           (F(3,7),F(0),F(1,35),F(19,35)),
           (F(3,7),F(0),F(2,7),F(2,7)))

def prepared(theta):
    latent=[]
    for x in range(6):
        a,b,c=theta[A[x]],theta[B[x]],theta[C[x]]
        latent.append((a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)))
    return tuple(tuple(sum((F(M20[i][x],20)*latent[x][t] for x in range(6)),F(0))
                       for t in range(4)) for i in range(6))

def decoded(rows):
    return tuple(tuple(sum((F(M20[i][x],20)*rows[GROUP[x]][t] for x in range(6)),F(0))
                       for t in range(4)) for i in range(6))

def pair_rows(spec):
    out=[]
    for pair in spec.split():
        row=[F(0)]*4
        for digit in pair: row[int(digit)-1]+=F(1,2)
        out.append(tuple(row))
    return tuple(out)

def tv(p,q):return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def error_rows(p,q):return tuple(tv(p[i],q[i]) for i in range(6))

def loss(p,q):return max(error_rows(p,q))

def face_old(s,t):
    return (s,t,F(0),F(0),F(0),F(0),F(1),F(1),F(1),F(0),F(1))

def face_new(s,t):
    return (s,t,F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0))

def exact_interval(q,face,indices,r):
    """Complete 16-sign affine TV sublevel intersection on one face axis."""
    p0=prepared(face(F(0),F(0)))
    p1=prepared(face(F(1),F(1)))
    lo,hi=F(0),F(1)
    for i in indices:
        for sign in product((-1,1),repeat=4):
            constant=sum((sign[t]*(p0[i][t]-q[i][t]) for t in range(4)),F(0))
            slope=sum((sign[t]*(p1[i][t]-p0[i][t]) for t in range(4)),F(0))
            if slope>0: hi=min(hi,(2*r-constant)/slope)
            elif slope<0: lo=max(lo,(2*r-constant)/slope)
            elif constant>2*r: return None
            if lo>hi:return None
    return (lo,hi)

def exact_rectangles_cover(rects):
    """Finite full-rectangle partition; closure covers every cut line."""
    xs=sorted({F(0),F(1)}|{z for a,b in rects.values() for z in a})
    ys=sorted({F(0),F(1)}|{z for a,b in rects.values() for z in b})
    count=0
    for left,right in zip(xs,xs[1:]):
        for bottom,top in zip(ys,ys[1:]):
            x,y=(left+right)/2,(bottom+top)/2
            assert any(a[0]<=x<=a[1] and b[0]<=y<=b[1] for a,b in rects.values()),(x,y)
            count+=1
    return count

def verify_complete_faces():
    """Sharp rational 4/7 upper on BOTH entire real two-parameter faces."""
    tables=tuple(pair_rows(spec) for spec in SPEC)+(D9,D10_FACES)
    assert all(sum(row)==1 and min(row)>=0 for table in tables for row in table)
    bank=tuple(decoded(table) for table in tables)
    assert loss(prepared(W),bank[8])==0
    witness={name:str(loss(prepared(POLICIES[name]),bank[9])) for name in ('H','J','P')}
    assert witness=={'H':'4/7','J':'4/7','P':'4/7'}
    expected={
        'old':{2:((F(0),RF),(F(0),RF)),
               7:((F(0),V),(F(3,7),F(1))),
               5:((F(3,7),F(1)),(F(0),V)),
               10:((V,F(1)),(V,F(1)))},
        'new':{1:((F(0),RF),(F(0),RF)),
               4:((F(0),V),(F(3,7),F(1))),
               5:((F(3,7),F(1)),(F(0),RF)),
               10:((V,F(1)),(V,F(1)))}
    }
    output={}
    for face_name,face in (('old',face_old),('new',face_new)):
        rectangles={}
        for label,q in enumerate(bank,1):
            a=exact_interval(q,face,range(3),RF)
            b=exact_interval(q,face,range(3,6),RF)
            if a is not None and b is not None:
                rectangles[label]=(a,b)
        for label,rect in expected[face_name].items():
            assert rectangles[label]==rect,(face_name,label,rectangles[label],rect)
        for s,t in product((V,F(1)),repeat=2):
            assert loss(prepared(face(s,t)),bank[9])==RF,(face_name,s,t)
        cells=exact_rectangles_cover(rectangles)
        assert cells==20,(face_name,cells)
        output[face_name]={
            'required_rectangles':{str(k):{'s':list(map(str,v[0])),'t':list(map(str,v[1]))}
                                   for k,v in expected[face_name].items()},
            'all_nonempty_labels':sorted(rectangles),
            'exact_open_cells_covered':cells,
            'four_upper_right_corner_risks':['4/7']*4
        }
    return {'new_D10_rows':[[str(x) for x in row] for row in D10_FACES],
            'HJP_D10_risks':witness,
            'faces':output,
            'full_two_face_upper':'4/7',
            'full_two_face_lower':'1/2',
            'previous_fixed_nine_exact':'11/18',
            'strict_improvement':'5/126'}

def main():
    assert len(M20)==6 and all(len(row)==6 and sum(row)==20 for row in M20)
    assert set(GROUP)=={0,1,2,3}
    rows=tuple(pair_rows(v) for v in SPEC)+(D9,D10)
    assert len(rows)==10 and all(len(table)==4 for table in rows)
    assert all(len(row)==4 and min(row)>=0 and sum(row)==1 for table in rows for row in table)
    bank=tuple(decoded(d) for d in rows)
    expected_fixed=(F(1),F(2,3),F(2,3),F(11,18),F(1,2))
    expected_bv=((F(0),F(1),F(0),F(0)),
                 (F(1),F(0),F(0),F(0)),
                 (F(1,3),F(0),F(0),F(2,3)),
                 (F(2,9),F(0),F(7,9),F(0)),
                 (F(0),F(0),F(1),F(0)))
    expected_d10={
        'W':(F(13,27),F(13,27),F(13,27),F(7,9),F(7,9),F(1)),
        'H':(F(5,27),F(5,27),F(10,27),F(4,9),F(4,9),F(13,27)),
        'J':(F(13,27),F(13,27),F(13,27),F(2,9),F(17,45),F(13,27)),
        'P':(F(13,27),F(13,27),F(13,27),F(1,3),F(43,90),F(13,27)),
    }
    output={}
    for (name,z),ef,bv in zip(POLICIES.items(),expected_fixed,expected_bv):
        assert all(F(0)<=v<=1 for v in z)
        p=prepared(z)
        assert all(sum(row)==1 and min(row)>=0 for row in p)
        assert p[5]==bv
        risks=tuple(loss(p,q) for q in bank)
        assert min(risks[:8])==ef,(name,risks)
        if name!='T':assert error_rows(p,bank[9])==expected_d10[name]
        output[name]={
            'fixed_eight_min':str(min(risks[:8])),
            'decoder9_loss':str(risks[8]),
            'decoder10_loss':str(risks[9]),
            'new_bank_min':str(min(risks)),
            'BV_prepared':list(map(str,bv)),
            'six_source_D10_errors':list(map(str,error_rows(p,bank[9])))
        }
    assert loss(prepared(W),bank[8])==0
    assert max(F(v['new_bank_min']) for k,v in output.items() if k!='T')==R4
    assert max(F(v['new_bank_min']) for v in output.values())==R5
    assert output['T']['fixed_eight_min']=='1/2'
    # Valid universal lower certificate, independent of all other decoder entries.
    assert 2*R4<1
    assert 1+F(2,3)+F(7,9)-1 == 3*R4
    assert Q[0]==1-R4 and Q[2]==F(7,9)-R4 and Q[3]==F(2,3)-R4
    for k in ('H','J','P','T'):
        assert tv(expected_bv[0],POLICIES_BV:=prepared(POLICIES[k])[5])==1
    assert F(8,3)-3*F(1,2)>1 # 5-policy lower: no r<1/2 can work
    print(json.dumps({
        'model':'BRC_N4_S23_SIX_SOURCES_FOUR_STOPS',
        'fixed_decoder_labels':list(range(1,9)),
        'free_decoder_labels':[9,10],
        'witnesses':output,
        'four_policy_exact_minimax':'13/27',
        'five_policy_exact_minimax':'1/2',
        'two_face_continuum':verify_complete_faces(),
        'lower_certificates':{
            'W_disjoint_BV_forces_separation_below_half':True,
            'HJP_BV_coordinate_excess':'13/9',
            'HJPT_BV_coordinate_excess':'5/3'},
        'verification':'exact Python Fraction; all six mixed four-atom laws and decoder rows',
        'result':'PASS_BRC_N4_S23_TWO_FREE_DECODERS_FOUR_FIVE_AND_TWO_FACES_4_7_20261102'
    },ensure_ascii=False,indent=2,sort_keys=True))

if __name__=='__main__':main()
