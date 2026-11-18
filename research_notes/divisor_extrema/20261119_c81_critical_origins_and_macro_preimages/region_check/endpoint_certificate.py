"""One-dimensional exact area bound for the part separated by h alone."""
import argparse
from fractions import Fraction as F
from crosscheck_region import power_bracket

Q = 1 << 35
BITS = 76
START = F(1093,1000)

def right_min():
    m=F(7,16)*4**4*4
    return F(1,3)+5-4*m/(1+m)-20*m/(1+4*m)

def zero_bracket(d, left):
    target = right_min() if left else F(4)
    den=16*Q**4*d.denominator
    num_factor=7*d.numerator
    a,b=target.as_integer_ratio()
    def at_least(i):
        # Compare h(i/Q,d) with a/b using the sign of one integer.
        num=num_factor*i**4
        s=den+num
        t=Q*den+i*num
        diff=Q*b*s*t+(i-Q)*((5*b-a)*s*t-4*b*num*t-5*b*i*num*s)
        return diff<=0 if left else diff>=0
    lo,hi=(0,Q-1) if left else (Q+1,4*Q)
    assert at_least(lo) and not at_least(hi)
    while hi-lo>1:
        mid=(lo+hi)//2
        if at_least(mid):
            lo=mid
        else:
            hi=mid
    return lo,hi

def area(n,start=START):
    assert (start-1)**3*start**8 > F(3**3*8**8,11**11)
    cuts=[start+(4-start)*i/n for i in range(n+1)]
    width_right=[zero_bracket(d, False) for d in cuts]
    width_left=[zero_bracket(d, True) for d in cuts]
    d_power=[power_bracket(d.numerator,4*d.denominator,4,9,BITS) for d in cuts]
    total_lo=total_hi=0
    for i in range(n):
        left_hi=power_bracket(width_left[i][1],4*Q,8,15,BITS)[1]
        right_lo=power_bracket(width_right[i+1][0],4*Q,8,15,BITS)[0]
        left_lo=power_bracket(width_left[i+1][0],4*Q,8,15,BITS)[0]
        right_hi=power_bracket(width_right[i][1],4*Q,8,15,BITS)[1]
        total_lo+=(right_lo-left_hi)*(d_power[i+1][0]-d_power[i][1])
        total_hi+=(right_hi-left_lo)*(d_power[i+1][1]-d_power[i][0])
    scale=10**12
    return [total_lo*scale//(1<<(2*BITS)), -((-total_hi*scale)//(1<<(2*BITS)))]

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('n',type=int,nargs='*',default=[64,256,1024])
    ap.add_argument('--weak', action='store_true',help='use the original 1119/1000 cutoff')
    args=ap.parse_args()
    for n in args.n:
        print(n,area(n,F(1119,1000) if args.weak else START),flush=True)
