"""Exact Fraction checker for R5 family-optimal affine-section cube (stdlib only)."""
from fractions import Fraction as Q
from itertools import product

h=Q(10395,788344); u=Q(30800,98543)
x=Q(10395,197086); y=Q(30933,394172); g0=Q(298375,788344)
R=(Q(1,10),Q(1,2),Q(3,4),Q(1),Q(5,4),Q(3,2),Q(19,10))
q3=((Q(13,20),Q(1,5),Q(3,20)),(Q(1,40),Q(9,20),Q(21,40)))
r2=(Q(3,4),Q(5,4)); r3=(Q(1,2),Q(1),Q(3,2))
alpha,beta=Q(47,180),Q(67,162)
phi=(4*alpha+9*beta)/13
V=(Q(27,80)*u,Q(13,40)*u,Q(27,80)*u)
m0=Q(259,450)*x+phi*y
m1=Q(1,8)+Q(53,40)*u+Q(641,225)*x+Q(4,15)*y
assert phi==Q(11,30)
assert x==4*h and V[2]-x==4*h and g0-u==5*h
assert 0<y<V[1] and g0+5*h<1
assert m0==Q(233079,3941720) and m1==Q(2799887,3941720)
assert m0-h/25==Q(5775,98543)
assert 20*h/(9*(m0-h/25))==Q(1,2)
assert 11*h/(9*(m1-Q(1507,225)*h))==Q(12705,490354)<Q(1,2)

def inverse(a,b,c,d):
    g=g0+3*b-2*a
    X=(x,y,x+2*(a-b))
    assert u<=g<=1 and all(0<=z<=v for z,v in zip(X,V))
    A=u/10; B=Q(9,40)*u
    J=X[1]*(alpha*A+beta*B)/(A+B)
    m={r:Q(0) for r in R}
    m[Q(1)]+=1-g
    for i in range(2): m[r2[i]]+=(g-u)/2
    for j in range(3): m[r3[j]]+=V[j]-X[j]
    m[Q(1,10)]+=(509*X[0]+9*X[2])/900+J
    m[Q(1)]+=Q(382,900)*(X[0]+X[2])+X[1]-2*J
    m[Q(19,10)]+=(9*X[0]+509*X[2])/900+J
    assert all(v>=0 for v in m.values())
    assert sum(m.values())==1 and sum(r*m[r] for r in R)==1
    tp=1+g+u+X[0]/2+X[1]+3*X[2]/2
    tq=1+g+u+sum(X)
    assert (tp,tq)==(Q(15,8)+a,Q(15,8)+b)
    assert m[Q(1,10)]==m0+(a-b)/50
    assert m[Q(1)]==m1+(2+Q(191,225))*a-(3+Q(191,225))*b
    t={r:Q(1,2) for r in R}
    t[Q(1,10)]+=10*(c+d)/(9*m[Q(1,10)])
    t[Q(1)]-=(10*c+d)/(9*m[Q(1)])
    assert all(0<=z<=1 for z in t.values())
    ep=1-sum(r*m[r]*t[r] for r in R)
    eq=sum(m[r]*t[r] for r in R)
    assert (ep,eq)==(Q(1,2)+c,Q(1,2)+d)
    return t

assert all(sum(row)==1 for row in q3)
assert all(sum(q3[i][j]*r3[j] for j in range(3))==r2[i] for i in range(2))
q4={(i,0):(Q(509,900),Q(382,900),Q(9,900)) for i in range(2)}
q4.update({(i,2):(Q(9,900),Q(382,900),Q(509,900)) for i in range(2)})
q4[(0,1)]=(Q(47,180),Q(43,90),Q(47,180))
q4[(1,1)]=(Q(67,162),Q(14,81),Q(67,162))
r4=(Q(1,10),Q(1),Q(19,10))
for (i,j),row in q4.items():
    assert all(z>0 for z in row) and sum(row)==1
    assert sum(row[k]*r4[k] for k in range(3))==r3[j]

n=0
for vals in product((-2,-1,0,1,2),repeat=4):
    a,b,c,d=(h*Q(v,2) for v in vals)
    inverse(a,b,c,d)
    n+=1
assert n==625
corners=0
for vals in product((-1,1),repeat=4):
    a,b,c,d=(h*v for v in vals)
    inverse(a,b,c,d)
    corners+=1
assert corners==16
assert inverse(-h,h,h,h)[Q(1,10)]==1
assert Q(259,450)-Q(11,30)*Q(214,27)<0
assert Q(259,450)*4*h+Q(11,30)*(Q(7,8)-Q(214,27)*4*h-Q(775,27)*h)==Q(1009,225)*h
assert Q(77,240)-Q(7*91864,32400)*h==Q(1009,225)*h
print("radius=",h,"approx=",float(h))
print("old_radius=",Q(11283,1291520),"improvement_factor=",h/Q(11283,1291520))
print("parameters_u_x_y_g0=",u,x,y,g0)
print("center_stopped_Q_masses_ratio_1_10_and_1=",m0,m1)
print("exact_grid_targets=",n,"corner_targets=",corners)
print("sharp_corner_t_ratio_1_10=",1)
print("family_upper_bound_via_four_linear_necessary_constraints=",h)
print("PASS_EXACT_R5_OPTIMAL_AFFINE_SECTION_CUBE")
