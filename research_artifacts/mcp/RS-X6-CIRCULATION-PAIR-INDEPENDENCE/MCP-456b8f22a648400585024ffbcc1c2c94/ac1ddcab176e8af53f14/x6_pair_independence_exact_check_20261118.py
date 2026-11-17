"""Dependency-free exact checks of X6 circulation-pair independence."""
from fractions import Fraction as F

def cycle(d, vertices):
    mat=[[0]*d for _ in range(d)]
    for i,j in zip(vertices,vertices[1:]+vertices[:1]):
        mat[i][j]+=1
        mat[j][i]-=1
    assert all(sum(row)==0 for row in mat)
    return mat

def prod(a,b):
    d=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(d))
             for j in range(d)] for i in range(d)]

def norm2(a):
    return sum(x*x for row in a for x in row)

def limit_cumulant22(a,b):
    ab,ba=prod(a,b),prod(b,a)
    anti=[[ab[i][j]+ba[i][j] for j in range(len(a))]
          for i in range(len(a))]
    return F(norm2(ab),720)+F(norm2(anti),1440)

def finite_word_moments(n):
    # 0,1,2 and 2,3,4 correspond to one-based 123/345.
    cyc_a={(0,1),(1,2),(2,0)}
    cyc_b={(2,3),(3,4),(4,2)}
    counts=[0]*5
    z=[0]*7  # word count; X,Y,X²,Y²,XY,X²Y², for scaled integer numerators
    def go(length,sa,sb):
        if length==5*n:
            x,y=2*sa-3*n*n,2*sb-3*n*n
            z[0]+=1; z[1]+=x; z[2]+=y
            z[3]+=x*x; z[4]+=y*y; z[5]+=x*y
            z[6]+=x*x*y*y
            return
        for v in range(5):
            if counts[v]>=n:
                continue
            da=sum(counts[u] for u in range(5) if (u,v) in cyc_a)
            db=sum(counts[u] for u in range(5) if (u,v) in cyc_b)
            counts[v]+=1
            go(length+1,sa+da,sb+db)
            counts[v]-=1
    go(0,0,0)
    m=z[0]
    ex,ey=F(z[1],m*2*n),F(z[2],m*2*n)
    ex2,ey2,exy=(F(z[3],m*4*n*n),F(z[4],m*4*n*n),
                   F(z[5],m*4*n*n))
    joint4=F(z[6],m*16*n**4)
    assert ex==ey==exy==0
    assert ex2==ey2==F(1,4)
    assert joint4==F(1,16)+F(n-1,90*n)
    return m,joint4,joint4-ex2*ey2

if __name__=="__main__":
    a=cycle(6,(0,1,2))
    b=cycle(6,(2,3,4))
    c=cycle(6,(3,4,5))
    assert norm2(prod(a,b))==4
    assert limit_cumulant22(a,b)==F(1,90)
    assert norm2(prod(a,c))==0
    assert limit_cumulant22(a,c)==0
    assert finite_word_moments(1)==(120,F(1,16),F(0))
    assert finite_word_moments(2)==(113400,F(49,720),F(1,180))
    print("PASS: 120+113400 exact words; overlap and separated matrix criteria")
