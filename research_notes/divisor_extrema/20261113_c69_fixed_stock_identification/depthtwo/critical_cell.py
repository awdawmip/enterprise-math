"""Exact area of the locally unique quantization phases for a rational Jacobian.

The two rows of --matrix are already scaled by the desired lambda.  This
computes the integrand Psi of CRITICAL_PATCH.md, not the spatial integral.
"""
from fractions import Fraction
from itertools import product
from argparse import ArgumentParser
import json


def parse_matrix(values):
    a, b, c, d = [Fraction(x) for x in values]
    det = a*d-b*c
    if not det:
        raise ValueError('matrix must be invertible')
    return a,b,c,d,det


def local_area(values):
    a,b,c,d,det = parse_matrix(values)
    # Intersecting unit squares have displacement in (-1,1)^2.
    n = int((abs(d)+abs(b))/abs(det))
    m = int((abs(c)+abs(a))/abs(det))
    rectangles = []
    for i,j in product(range(-n,n+1),range(-m,m+1)):
        if i==j==0:
            continue
        x,y = a*i+b*j,c*i+d*j
        if abs(x)>=1 or abs(y)>=1:
            continue
        rectangles.append((max(0,-x),min(1,1-x),max(0,-y),min(1,1-y)))
    borders = sorted({0,1}|{x for l,r,_,_ in rectangles for x in (l,r)})
    occupied = Fraction(0)
    for x1,x2 in zip(borders,borders[1:]):
        intervals = sorted((y1,y2) for l,r,y1,y2 in rectangles
                           if l<=x1 and r>=x2)
        length, end = 0,0
        for y1,y2 in intervals:
            if y2>end:
                length += y2-max(y1,end)
                end = y2
        occupied += (x2-x1)*length
    return 1-occupied,len(rectangles)


def checks():
    expected = [
        (('1','0','0','1'),'1'),
        (('1/2','0','0','1/2'),'0'),
        (('3/4','0','0','4/5'),'3/10'),
        (('3/4','1/3','0','1'),'1/2'),
        (('4/5','0','15/11','2/3'),None),
        (('4/5','-4/5','1/6','1/2'),None),
    ]
    rows=[]
    for values,answer in expected:
        area,n=local_area(values)
        if answer is not None:
            assert area==Fraction(answer)
        a,b,c,d,det=parse_matrix(values)
        # Basis changes of Z^2 and square-coordinate exchange leave Psi fixed.
        assert local_area([a,b+a,c,d+c])[0]==area
        assert local_area([c,d,a,b])[0]==area
        assert local_area([-a,b,-c,d])[0]==area
        assert 0<=area<=min(1,abs(det))
        rows.append(dict(matrix=values,unique_phase_area=str(area),
                         nonempty_overlap_rectangles=n))
    return rows


if __name__=='__main__':
    p=ArgumentParser(description=__doc__)
    p.add_argument('--matrix',nargs=4,metavar=('a','b','c','d'))
    args=p.parse_args()
    if args.matrix:
        area,n=local_area(args.matrix)
        print(json.dumps(dict(unique_phase_area=str(area),nonempty_overlap_rectangles=n)))
    else:
        print(json.dumps(checks(),indent=2))
