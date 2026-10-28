from fractions import Fraction as F
from itertools import product

def O(x,a,b,swap=F(0)):
    assert all(F(0)<=t<=F(1) for t in (x,a,b,swap))
    # Each tuple is (unconditional Q terminal mass, likelihood ratio, time, P[declare Q|leaf]).
    E=[(F(1,3),F(1,4),2,F(1)), (F(1,4),F(2),2,F(0)),
       (F(1,6)*(1-x),F(1),2,F(0)),
       (F(1,6)*x*(1-a),F(1),3,F(0)),
       (F(1,12)*x*a,F(1,2),4,F(1)),
       (F(1,12)*x*a,F(3,2),4,F(0)),
       (F(1,4)*(1-b),F(1),3,F(0)),
       (F(1,8)*b,F(1,4),4,1-swap),
       (F(1,8)*b,F(7,4),4,swap)]
    assert sum(q for q,r,t,d in E)==1
    assert sum(q*r for q,r,t,d in E)==1
    return (sum(q*r*d for q,r,t,d in E),
            sum(q*(1-d) for q,r,t,d in E),
            sum(q*r*t for q,r,t,d in E),
            sum(q*t for q,r,t,d in E))

def add(A,B): return tuple(a+b for a,b in zip(A,B))
def sub(A,B): return tuple(a-b for a,b in zip(A,B))
def mul(s,A): return tuple(s*a for a in A)
def det(A,B,C):
    return (A[0]*(B[1]*C[2]-B[2]*C[1])
            -B[0]*(A[1]*C[2]-A[2]*C[1])
            +C[0]*(A[1]*B[2]-A[2]*B[1]))

if __name__=='__main__':
    # Rational tree root and t=2 parent-child P/Q mass conservation.
    for q,r,children in [(F(1,2),F(1,2),[(F(1,6),F(1)),(F(1,3),F(1,4))]),
                         (F(1,2),F(3,2),[(F(1,4),F(1)),(F(1,4),F(2))])]:
        assert sum(t for t,s in children)==q
        assert sum(t*s for t,s in children)==q*r
    corners=[O(F(x),F(y),F(y)) for x,y in ((0,0),(0,1),(1,0),(1,1))]
    A,B,C,D=corners
    u,v,w=sub(C,A),sub(B,A),add(sub(D,C),sub(A,B))
    minor=det(*[(t[0],t[1],t[3]) for t in (u,v,w)])
    assert minor==F(1,2304)
    for x,y in product([F(0),F(1,5),F(1,2),F(4,5),F(1)],repeat=2):
        assert O(x,y,y)==add(A,add(mul(x,u),add(mul(y,v),mul(x*y,w))))
    Z=mul(F(1,2),add(A,D))
    assert Z==(F(23,192),F(9,16),F(61,24),F(61,24))
    assert Z==O(F(1,2),F(1),F(1,2))==O(F(1,2),F(5,8),F(5,8),F(1,30))
    # If B(x,y)=Z, rank-three uniqueness forces x=y=xy=1/2 (impossible).
    assert F(1,2)*F(1,2)!=F(1,2)
    for name,val in zip(('B00','B01','B10','B11'),corners): print(name,val)
    print('minor=',minor,' Z=',Z)
    print('full witness: x=1/2, y_U=1, y_V=1/2')
    print('LR unrestricted repair: x=1/2, y=5/8, V terminal swap=1/30')
    print('PASS_EXACT_R5_FACE_RANK_AND_TERMINAL_REPAIR')
