#!/usr/bin/env python3
"""BRC N4 S23: exact four-witness 11/18 obstruction and two-face cover."""
from fractions import Fraction as F
from itertools import product

M = ((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
     (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20))
A=(0,0,0,1,1,1); B=(2,2,3,2,2,4); C=(5,6,7,8,9,10)
GROUP=(0,0,1,2,2,3)
SPEC=('34 24 34 24','34 23 34 34','34 34 34 23',
      '24 24 12 12','12 12 24 34','12 13 23 24',
      '23 34 12 13','24 34 12 14','13 12 13 13')
D10=((F(7,18),F(4,9),F(1,6),F(0)),
     (F(7,18),F(5,18),F(1,6),F(1,6)),
     (F(7,18),F(0),F(2,9),F(7,18)),
     (F(7,18),F(7,18),F(1,6),F(1,18)))
R=F(11,18)

def prepared(z):
    latent=[]
    for x in range(6):
        a,b,c=z[A[x]],z[B[x]],z[C[x]]
        latent.append((a,(1-a)*b,(1-a)*(1-b)*c,(1-a)*(1-b)*(1-c)))
    return tuple(tuple(sum((F(M[i][x],20)*latent[x][t] for x in range(6)),F(0))
                       for t in range(4)) for i in range(6))

def decoded(rows):
    return tuple(tuple(sum((F(M[i][x],20)*rows[GROUP[x]][t]
                            for x in range(6)),F(0)) for t in range(4))
                 for i in range(6))

def pair_rows(spec):
    result=[]
    for pair in spec.split():
        row=[F(0)]*4
        for char in pair: row[int(char)-1]+=F(1,2)
        result.append(tuple(row))
    return tuple(result)

BANK=tuple(decoded(pair_rows(s)) for s in SPEC)+(decoded(D10),)
assert all(sum(row)==1 and min(row)>=0 for row in D10)

def tv(p,q): return sum((abs(x-y) for x,y in zip(p,q)),F(0))/2

def loss(p,q): return max(tv(p[i],q[i]) for i in range(6))

def face_old(s,t): return (s,t,F(0),F(0),F(0),F(0),F(1),F(1),F(1),F(0),F(1))

def face_new(s,t): return (s,t,F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0))

W=(F(1),F(0),F(0),F(0),F(1),F(0),F(0),F(0),F(0),F(0),F(0))
H=(F(1,3),F(1),F(0),F(0),F(0),F(1),F(0),F(1),F(0),F(0),F(0))
J=(F(1),F(1,3),F(0),F(0),F(0),F(0),F(0),F(0),F(0),F(1),F(0))
P=face_old(F(1),F(2,9))

# A fixed-label TV sublevel region is an exact rectangle on either face.
# Intersect all 16 sign halfspaces for the chosen A or B prepared rows.
def interval(q, face, indices):
    p0=prepared(face(F(0),F(0)))
    p1=prepared(face(F(1),F(1)))
    low,high=F(0),F(1)
    for i in indices:
        for sigma in product((-1,1),repeat=4):
            c=sum((sigma[t]*(p0[i][t]-q[i][t]) for t in range(4)),F(0))
            b=sum((sigma[t]*(p1[i][t]-p0[i][t]) for t in range(4)),F(0))
            if b>0: high=min(high,(2*R-c)/b)
            elif b<0: low=max(low,(2*R-c)/b)
            elif c>2*R: return None
            if low>high: return None
    return low,high

# Exact sublevel rectangles, using 1-based decoder labels.
EXPECTED={
    'new':{1:((F(0),R),(F(0),R)),
           4:((F(0),F(2,9)),(F(7,18),F(1))),
           5:((F(7,18),F(1)),(F(0),R)),
           10:((F(2,9),F(1)),(F(1,3),F(1)))},
    'old':{2:((F(0),R),(F(0),R)),
           7:((F(0),F(2,9)),(F(7,18),F(1))),
           5:((F(7,18),F(1)),(F(0),F(2,9))),
           10:((F(2,9),F(1)),(F(2,9),F(1)))}
}

def covers_all(rects):
    # A finite union of closed axis-aligned rectangles covers [0,1]^2
    # iff it contains each open cell cut out by all boundary coordinates,
    # including the boundary by closure.
    xs=sorted({F(0),F(1)}|{v for a,b in rects for v in a})
    ys=sorted({F(0),F(1)}|{v for a,b in rects for v in b})
    cells=0
    for x0,x1 in zip(xs,xs[1:]):
        for y0,y1 in zip(ys,ys[1:]):
            x,y=(x0+x1)/2,(y0+y1)/2
            assert any(a[0]<=x<=a[1] and b[0]<=y<=b[1] for a,b in rects)
            cells+=1
    return cells

def main():
    assert len(BANK)==10
    expected_old=(F(1),F(2,3),F(2,3),R)
    expected_bv=((F(0),F(1),F(0),F(0)),
                 (F(1),F(0),F(0),F(0)),
                 (F(1,3),F(0),F(0),F(2,3)),
                 (F(2,9),F(0),F(7,9),F(0)))
    for name,z,e,bv in zip(('W','H','J','P'),(W,H,J,P),expected_old,expected_bv):
        p=prepared(z)
        assert p[5]==bv
        v=tuple(loss(p,q) for q in BANK)
        assert min(v[:9])==e and v[9]==R and min(v)==R
        print(name,'old9_min=',e,'new10_loss=',v[9],'BV=',','.join(map(str,bv)))
    # BV dual inequality for r<R: q1,q2>=1-r; q4>=2/3-r;
    # q3>=7/9-r, hence 1>=31/9-4r, i.e. r>=11/18.
    assert 2*(1-R)+(F(2,3)-R)+(F(7,9)-R)==1
    for name,face in (('new',face_new),('old',face_old)):
        checked=[]
        for label,rect in EXPECTED[name].items():
            got=(interval(BANK[label-1],face,range(3)),
                 interval(BANK[label-1],face,range(3,6)))
            assert got==rect,(name,label,got,rect)
            checked.append(rect)
            print('face',name,'label',label,'A=',rect[0],'B=',rect[1])
        print('face',name,'certified_open_cells=',covers_all(checked))
    print('SHARP_INF_SUP=11/18; ANY_REAL_TENTH_DECODER_LOWER_ANALYTIC; TWO_FACES_ALL_REAL_PARAMETERS_UPPER_CERTIFIED')
    print('PASS_BRC_N4_S23_FOUR_WITNESS_TWO_FACE_SHARP_11_18_20261101')

if __name__=='__main__':main()
