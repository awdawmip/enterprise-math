"""Exact Fraction verification of general terminal two-law hinge zonotope repair.
Universal real-domain proof is in PROOF.md; finite tests are separate evidence.
"""
from fractions import Fraction as F
from itertools import product
import json

def support(m,r,u,v):
    return sum((m[i]*max(F(),u+v*r[i]) for i in range(len(r))), F())

def point(m,r,x):
    return (sum((m[i]*x[i] for i in range(len(r))),F()),
            sum((m[i]*r[i]*x[i] for i in range(len(r))),F()))

def hinges(m,n,r):
    d=[a-b for a,b in zip(m,n)]
    assert sum(d,F())==0 and sum((a*b for a,b in zip(d,r)),F())==0
    return [sum((d[i]*max(F(),r[i]-t) for i in range(len(r))),F()) for t in r]

def excess(m,n,r):
    h=hinges(m,n,r)
    assert h[0]==h[-1]==0
    return max([F()]+[h[i]/(1+r[i]) for i in range(1,len(r)-1)])

def distance(n,r,z):
    normals=[(F(1),F()),(-F(1),F()),(F(),F(1)),(F(),-F(1))]
    for t in r: normals += [(-t,F(1)),(t,-F(1))]
    return max([F()]+[(u*z[0]+v*z[1]-support(n,r,u,v))/(abs(u)+abs(v))
                     for u,v in normals])

def vertex_excess(m,n,r):
    return max((distance(n,r,point(m,r,x))
                for x in product((F(),F(1)),repeat=len(r))),default=F())

def reconstruct(h,r):
    s=[(h[k-1]-h[k])/(r[k]-r[k-1]) for k in range(1,len(r))]
    return tuple([-s[0]]+[s[k-1]-s[k] for k in range(1,len(s))]+[s[-1]])

def family(r,n,coefficients):
    count=0
    for coeff in coefficients:
        delta=[F()]*len(r)
        for k,c in enumerate(coeff):
            left,right=r[k+1]-r[k],r[k+2]-r[k+1]
            delta[k]+=c*right
            delta[k+1]-=c*(left+right)
            delta[k+2]+=c*left
        m=tuple(a+b for a,b in zip(n,delta))
        assert all(a>0 for a in m)
        h=hinges(m,n,r)
        assert reconstruct(h,r)==tuple(delta)
        assert vertex_excess(m,n,r)==excess(m,n,r)
        assert vertex_excess(n,m,r)==excess(n,m,r)
        count+=1
    return count

def main():
    r=(F(1,4),F(3,4),F(5,4),F(7,4))
    m=(F(9,32),F(5,32),F(11,32),F(7,32))
    n=(F(1,4),)*4
    assert sum(m)==sum(n)==1
    assert sum((x*y for x,y in zip(m,r)),F())==1
    assert sum((x*y for x,y in zip(n,r)),F())==1
    h=hinges(m,n,r)
    assert h==[F(),F(1,64),F(-1,64),F()]
    assert reconstruct(h,r)==tuple(a-b for a,b in zip(m,n))
    assert excess(m,n,r)==vertex_excess(m,n,r)==F(1,112)
    assert excess(n,m,r)==vertex_excess(n,m,r)==F(1,144)

    old=point(m,r,(F(),F(),F(1),F(1)))
    repair=point(n,r,(F(),F(2,7),F(1),F(1)))
    assert old==(F(9,16),F(13,16)) and repair==(F(4,7),F(45,56))
    assert tuple(a-b for a,b in zip(old,repair))==(-F(1,112),F(1,112))
    assert old[1]-F(3,4)*old[0]-support(n,r,-F(3,4),F(1))==F(1,64)
    reverse=point(n,r,(F(),F(),F(),F(1)))
    reverse_repair=point(m,r,(F(),F(),F(1,9),F(1)))
    assert reverse==(F(1,4),F(7,16))
    assert reverse_repair==(F(37,144),F(31,72))
    assert tuple(a-b for a,b in zip(reverse,reverse_repair))==(-F(1,144),F(1,144))
    assert reverse[1]-F(5,4)*reverse[0]-support(m,r,-F(5,4),F(1))==F(1,64)

    # Single strictly positive N=3 tree: root -> A/B -> A1/B1 -> four terminal ports.
    qa=tuple(F(1,2)*x for x in m)
    qb=tuple(F(1,2)*x for x in n)
    assert sum(qa)==sum(qb)==F(1,2)
    assert sum(qa)+sum(qb)==1
    assert sum((r[i]*(qa[i]+qb[i]) for i in range(4)),F())==1
    assert all(qa[i]>0 and qb[i]>0 and r[i]>0 for i in range(4))
    M=qa
    B=tuple(F(1,2)*(qa[i]+qb[i]) for i in range(4))
    assert sum(M)==sum(B)==F(1,2)
    assert sum((r[i]*M[i] for i in range(4)),F())==F(1,2)
    assert sum((r[i]*B[i] for i in range(4)),F())==F(1,2)
    assert hinges(M,B,r)==[F(),F(1,256),F(-1,256),F()]
    assert excess(M,B,r)==vertex_excess(M,B,r)==F(1,448)
    assert excess(B,M,r)==F(1,576)
    full=point(M,r,(F(),F(),F(1),F(1)))
    projected=point(B,r,(F(),F(16,91),F(1),F(1)))
    assert full==(F(9,32),F(13,32))
    assert projected==(F(127,448),F(181,448))
    assert tuple(a-b for a,b in zip(full,projected))==(-F(1,448),F(1,448))
    assert full[1]-F(3,4)*full[0]-support(B,r,-F(3,4),F(1))==F(1,256)

    r5=(F(1,5),F(3,5),F(1),F(7,5),F(9,5))
    n5=(F(1,5),)*5
    checked4=family(r,n,product((F(-1,16),F(),F(1,16)),repeat=2))
    checked5=family(r5,n5,product((F(-1,20),F(),F(1,20)),repeat=3))
    print(json.dumps({
        "status":"ALL_EXACT_FRACTION_CHECKS_PASSED",
        "scope":"36 exact rational mass pairs; universal theorem is symbolic",
        "four_port_pairs":checked4,"five_port_pairs":checked5,
        "two_sided_vertex_checks":2*(16*checked4+32*checked5),
        "hinges_four_port":[str(x) for x in h],
        "old_to_new":"1/112","new_to_old":"1/144",
        "causal_8leaf":{
            "all_leaf_Q_P_positive":True,
            "t2_stopped_Q_P":"1/2",
            "hinges":[str(x) for x in hinges(M,B,r)],
            "full_terminal":[str(x) for x in full],
            "compressed_terminal":[str(x) for x in projected],
            "optimal_terminal_policy":["0","16/91","1","1"],
            "sharp_fixed_early_occupancy_TV":"1/448",
            "reverse_fixed_early_occupancy_TV":"1/576"
        }
    },sort_keys=True,indent=2))

if __name__=="__main__":
    main()
