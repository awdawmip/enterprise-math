"""Stage320-B: exact rational sharpened B-box cusp and Pareto extension certificate.

No floating-point arithmetic is used for mathematical comparisons.
This checker verifies the NEW polynomial and interval inequalities. It reuses
Stage318-B's separately published 274-leaf exterior and R-chamber certificates.
"""
from fractions import Fraction as Q
from math import comb

B = (Q(23,100), Q(24,100))
Y = (Q(55,100), Q(56,100))
R_X = (Q(231,1000), Q(2312,10000))
R_Y = (Q(555,1000), Q(556,1000))

# B_k(z) = z^k (1-z)^(3-k), coefficients in ascending degree.
BK = [(Q(1), Q(-3), Q(3), Q(-1)),
      (Q(0), Q(1), Q(-2), Q(1)),
      (Q(0), Q(0), Q(1), Q(-1)),
      (Q(0), Q(0), Q(0), Q(1))]
P = [Q(61,160),Q(21,160),Q(9,160),Q(9,160)]

def polyeval(coef,z):
    out=Q(0)
    for c in reversed(coef): out=out*z+c
    return out

def grad_coeff(k):
    return tuple(i*BK[k][i] for i in range(1,4))

def q_grad_coeff(e0,e1,scale):
    # derivative of q=3r2+e0*r0+3*e1*r1 on one of the axes
    return tuple(scale*(3*grad_coeff(2)[i]
                              +e0*grad_coeff(0)[i]
                              +3*e1*grad_coeff(1)[i])
                 for i in range(3))

def exact_quadratic_range(coef,interval):
    lo,hi=interval
    samples=[lo,hi]
    if coef[2] != 0:
        vertex=-coef[1]/(2*coef[2])
        if lo <= vertex <= hi: samples.append(vertex)
    vals=[polyeval(coef,z) for z in samples]
    return min(vals),max(vals)

def r_value(k,u,v):
    return Q(4,5)*polyeval(BK[k],u)+Q(1,5)*polyeval(BK[k],v)-P[k]

# Sign region on the entire global box B, justified by derivative signs.
for k in (2,3):
    for scale,box in ((Q(4,5),B),(Q(1,5),Y)):
        lo,hi=exact_quadratic_range(tuple(scale*z for z in grad_coeff(k)),box)
        assert lo>0, (k,box,lo,hi)
r2_min=r_value(2,B[0],Y[0])
r3_max=r_value(3,B[1],Y[1])
assert r2_min==Q(17807,5000000)>0
assert r3_max==Q(-25169,2500000)<0

# For r2>0,r3<0, the exact Bernoulli TV has the 4-support representation:
# d = max_{e0,e1 in {0,1}} Q_e0,e1;
# Q_e0,e1=3*r2+e0*r0+3*e1*r1.
# The global unique minimizer (x*,y*) has r0=r1=0.
grad={}
for e0 in (0,1):
    for e1 in (0,1):
        gx=exact_quadratic_range(q_grad_coeff(e0,e1,Q(4,5)),B)
        gy=exact_quadratic_range(q_grad_coeff(e0,e1,Q(1,5)),Y)
        grad[e0,e1]=(gx,gy)

assert grad[0,0] == ((Q(9039,12500),Q(2304,3125)),(Q(336,3125),Q(231,2000)))
assert grad[0,1] == ((Q(156,125),Q(162,125)),(Q(-9,125),Q(-3,50)))
assert grad[1,0] == ((Q(-2187,3125),Q(-2028,3125)),(Q(-27,3125),Q(-3,500)))
assert grad[1,1] == ((Q(-432,3125),Q(-1587,12500)),(Q(-588,3125),Q(-363,2000)))

# Four quadrants of (dx,dy). On dx<0,dy>0 use 7/16*Q00+9/16*Q10.
alpha=Q(2109,50000)
assert min(grad[0,0][0][0],grad[0,0][1][0])>alpha      # ++
assert min(grad[0,1][0][0],-grad[0,1][1][1])>alpha    # +-
assert min(-grad[1,1][0][1],-grad[1,1][1][1])>alpha  # --
a_coeff=Q(7,16)*(-grad[0,0][0][1])+Q(9,16)*(-grad[1,0][0][1])
b_coeff=Q(7,16)*grad[0,0][1][0]+Q(9,16)*grad[1,0][1][0]
assert a_coeff==Q(2124,50000)>alpha
assert b_coeff==alpha

# Thus globally in B: d(x,y)-d* >= alpha*(|x-x*|+|y-y*|).
# b=(5/16)*d. Stage318's exterior cover gives b-beta*>1/640000
# outside B, and here delta<1/640000, hence every feasible block is in B.
delta=Q(11,10**7)
assert delta>Q(1,5000000)
assert delta<Q(1,640000)

x_star_lo=Q(231083940855521,10**15)
x_star_hi=Q(231083940855522,10**15)
y_star_lo=Q(555508857277,10**12)
y_star_hi=Q(555508857278,10**12)
margin=min(x_star_lo-R_X[0],R_X[1]-x_star_hi,
           y_star_lo-R_Y[0],R_Y[1]-y_star_hi)
assert margin==x_star_lo-R_X[0]
radius=delta/(Q(5,16)*alpha)
assert radius==Q(22,263625)
assert radius<margin

# Stage318's certified uniform bounds over R: |dy/dx|<12 and
# outward |db/dx|>18/100. Each of the four kink arms therefore reaches
# delta before leaving R, with x extension L=1/100000.
L=Q(1,100000)
assert L<min(x_star_lo-R_X[0], R_X[1]-x_star_hi)
assert 12*L < min(y_star_lo-R_Y[0],R_Y[1]-y_star_hi)
assert Q(18,100)*L>delta

# Stage318's uniform det/sign/slope/curvature certificates on R and
# Stage315-316 block identities may be reused verbatim because localization
# and kink reach have now been checked for the larger delta.
assert delta / Q(1,5000000)==Q(11,2)

print('B r2_lower =',r2_min,'r3_upper =',r3_max)
for e in sorted(grad): print('grad Q'+str(e)+' =',grad[e])
print('CUSP_ALPHA =',alpha,'MIXED_DIRECTION_A =',a_coeff,'MIXED_DIRECTION_B =',b_coeff)
print('NEW_DELTA =',delta,'old_to_new_factor =',Q(11,2))
print('LOCAL_RADIUS =',radius,'ROOT_TO_R_MARGIN_LOWER =',margin)
print('LOCAL_MARGIN_GAP =',margin-radius)
print('KINK_REACH_LOWER =',Q(18,100)*L)
print('STAGE320B_GLOBAL_BOX_SHARPNESS_AND_5P5X_PARETO_EXTENSION_EXACT_PASS')
