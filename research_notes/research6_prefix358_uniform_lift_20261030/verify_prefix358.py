#!/usr/bin/env python3
"""PREFIX-358: exact rational Banach certificates around an auxiliary 5-Port projection collision.
Scope: static complex amplitude inverse model only; NOT native X6/BRC temporal evolution.
All acceptance comparisons use SymPy exact QQ arithmetic (no floats, pi, or trig).
"""
import json
from pathlib import Path
import sympy as S

x = S.symbols('x0:4')    # Re(u), Im(u), Re(v), Im(v)
t = S.Symbol('t')        # intensity-path parameter, NOT heartbeat time
Q = [34000+204144*t, 3200+56336*t, 58250+1286*t,
     46600+12936*t, 31525+28011*t]
R = S.Rational
I = S.I
A = S.Matrix([[4,4,0],[0,-4,4],[-5+3*I,0,-3+I],
              [-2-2*I,4+4*I,2+2*I],[-2,0,5+2*I]])
B = S.simplify(A[3:,:]*A[:3,:].inv())
expected_B = S.Matrix([[R(5,2)+R(9,2)*I,R(3,2)+R(7,2)*I,4*I],
                       [R(11,4)+R(15,8)*I,R(11,4)+R(15,8)*I,R(5,4)+R(9,4)*I]])
assert B == expected_B
H = [x[0]**2+x[1]**2, x[2]**2+x[3]**2]
for k in range(2):
    b0,b1,b2 = list(B.row(k))
    h_re = S.re(b0)+S.re(b1)*x[0]-S.im(b1)*x[1]+S.re(b2)*x[2]-S.im(b2)*x[3]
    h_im = S.im(b0)+S.im(b1)*x[0]+S.re(b1)*x[1]+S.im(b1)*x[1]+S.im(b2)*x[2]+S.re(b2)*x[3]
    H.append(S.expand(h_re*h_re+h_im*h_im))
F = S.Matrix([S.expand(Q[0]*H[k]-Q[k+1]) for k in range(4)])
J = F.jacobian(x)
Hess = [S.hessian(h,x) for h in H]
H3 = S.Poly(20146977828425934386944*t**3-1153636440395600981600*t**2
            -3151971160768643750*t-1890887364703125,t,domain=S.QQ)
lo,hi = R('0.0598990506977195435624'),R('0.0598990506977195435625')
assert hi-lo==R(1,10**22)
assert H3.eval(lo)*H3.eval(hi)<0
assert H3.count_roots(0,R(1,4))==1
assert H3.count_roots(lo,hi)==1
t0=(lo+hi)/2
radius=R(1,10000)
epsilon=R(1,500000)
D=epsilon+(hi-lo)/2
assert lo-epsilon>0 and hi+epsilon<R(1,4)
centers=[
    ['-0.350254450435209402','-0.139786042875789802',
     '-0.717408911887365257','0.864319809947346322'],
    ['-0.350254450435209402','-0.139786042875789802',
     '-0.998209376262943823','0.515075064299927955']]

def ceil_scaled(z,unit=10**12):
    z=R(z)
    return int(S.ceiling(z*unit))

def round_nearest(z,unit=10**12):
    z=R(z)
    return R(int(S.floor(z*unit+R(1,2))),unit)

results=[]
for label,coords in enumerate(centers,1):
    X=[R(c) for c in coords]
    sub={**dict(zip(x,X)),t:t0}
    j0=J.subs(sub)
    M=j0.inv().applyfunc(round_nearest)
    err=S.eye(4)-M*j0
    f0=F.subs(sub)
    dt=[204144*H[k].subs(sub)-S.diff(Q[k+1],t) for k in range(4)]
    delta=[]
    for k in range(4):
        z=[]
        for j in range(4):
            g=S.diff(H[k],x[j]).subs(sub)
            hrow=sum(abs(Hess[k][j,m])*radius for m in range(4))
            z.append(204144*D*abs(g)+(Q[0].subs(t,t0)+204144*D)*hrow)
        delta.append(z)
    contraction=max(sum(abs(err[i,j]) for j in range(4))+
                    sum(abs(M[i,k])*sum(delta[k]) for k in range(4))
                    for i in range(4))
    displacement=max(sum(abs(M[i,k])*(abs(f0[k])+D*abs(dt[k]))
                         for k in range(4)) for i in range(4))
    assert contraction < R(1,10)
    assert displacement < R(3,40000)  # 0.000075, strictly less than (1-1/10)*radius
    assert displacement+contraction*radius < radius
    assert M.det()!=0
    results.append({
        'branch':label,'center_decimals':coords,
        'approx_inverse_integer_numerators_over_10e12':[
            [int(M[i,j]*10**12) for j in range(4)] for i in range(4)],
        'contraction_bound_ceiling_over_10e12':ceil_scaled(contraction),
        'center_displacement_bound_ceiling_over_10e12':ceil_scaled(displacement),
        'ball_self_mapping_margin_floor_over_10e12':
            int(S.floor((radius-displacement-contraction*radius)*10**12)),
        'exact_checks':{'M_invertible':True,'contraction_lt_1_over_10':True,
                        'displacement_lt_3_over_40000':True,
                        'strict_cube_self_mapping':True}})

v_re_gap=abs(R(centers[0][2])-R(centers[1][2]))
v_im_gap=abs(R(centers[0][3])-R(centers[1][3]))
assert v_re_gap>2*radius and v_im_gap>2*radius
vsep_lower=(v_re_gap-2*radius)**2+(v_im_gap-2*radius)**2
assert vsep_lower > R(1,6)
# Because both branch centers have exactly the same (u_re,u_im), and each cube
# has radius 1/10000, their complex u-readouts differ by <=sqrt(8)*radius.
u_sep_sq_upper=8*radius*radius
assert u_sep_sq_upper<R(1,10**7)

result={
  'schema':'PREFIX358_EXACT_RATIONAL_TWO_BRANCH_BANACH_CERTIFICATE_V1',
  'verdict':'PASS_PREFIX358_EXACT_TWO_UNIFORMLY_REGULAR_PHYSICAL_LIFTS',
  'classification':'AUTHOR_SIDE_STATIC_AUXILIARY_ONLY_UNREVIEWED_NOT_ADMITTED',
  'model':'A complex 5x3; Q(t)/59536; quotient by global U(1)',
  't_is_heartbeat_time':False,
  'A_as_strings':[[str(A[i,j]) for j in range(3)] for i in range(5)],
  'Q_as_strings':[str(z) for z in Q],
  'H3_root_bracket':[str(lo),str(hi)],
  'certified_parameter_interval_containing_tc_neighborhood':[
      str(lo-epsilon),str(hi+epsilon)],
  'epsilon':'1/500000','cube_radius':'1/10000',
  'interval_method':'Exact infinity-norm Banach with rational inverse M, 4 real quadratic intensity equations, derivative Hessian bounds, t0 bracket midpoint',
  'branches':results,
  'v_squared_separation_lower_ceil_descriptive':'strict > 1/6',
  'v_squared_separation_lower_floor_over_10e12':int(S.floor(vsep_lower*10**12)),
  'u_squared_difference_upper':'8/100000000',
  'physical_source_construction':'Take y1=sqrt(Q1(t)/59536)>0, y2=u*y1, y3=v*y1, z=A[:3,:]^-1*y[:3]; certified |Az|^2=Q(t)/59536',
  'limitations':'No completeness outside the two disjoint certified cubes; no native X6/BRC computation, no future-operation transfer; no native Result or independent review.'}
Path(__file__).with_name('RESULTS_PREFIX358.json').write_text(
    json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(result['verdict'])
print('epsilon=',epsilon,'radius=',radius)
for b in results:
 print('branch',b['branch'],'kappa*1e12_ceil',b['contraction_bound_ceiling_over_10e12'],
       'res*1e12_ceil',b['center_displacement_bound_ceiling_over_10e12'],
       'margin*1e12_floor',b['ball_self_mapping_margin_floor_over_10e12'])
print('v separation squared lower*1e12_floor',int(S.floor(vsep_lower*10**12)))
print('u separation squared upper',u_sep_sq_upper)
