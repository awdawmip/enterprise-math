"""Compare finite angular windows in the physical and Fourier coordinates."""
import cmath
import json
from math import ceil, cos, exp, log, pi, sqrt

from angular_check import prime_values


def wrapped(angle, width):
    angle = (angle+pi) % (2*pi) - pi
    return sum(exp(-0.5*((angle+2*pi*r)/width)**2) for r in range(-4,5))


def centered(angle, width):
    return wrapped(angle,width)-sum(wrapped(angle+2*pi*j/3,width) for j in range(3))/3


def main():
    limit=997
    values,_=prime_values(limit)
    phases=[cmath.phase(z) for _,_,z in values]
    L=log(limit)
    rows=[]
    for width in (0.25,0.5,1):
        top=ceil(2*sqrt(L)/width)
        tail_per_prime=2*exp(-0.5*(width*top)**2)/(sqrt(2*pi)*width*top)
        for shift in (0,pi/3,pi/2,pi):
            space=sum(centered(phi-shift,width) for phi in phases)
            truncated=0
            for k in range(1,top+1):
                if k%3:
                    coeff=width/sqrt(2*pi)*exp(-0.5*(width*k)**2)
                    truncated+=2*coeff*sum(cos(k*(phi-shift)) for phi in phases)
            assert abs(space-truncated)<=len(values)*tail_per_prime+1e-10
            rows.append(dict(delta=width, center_over_pi=round(shift/pi,6),
                             max_frequency=top, direct_window_sum=round(space,8),
                             fourier_truncation=round(truncated,8),
                             total_tail_bound=round(len(values)*tail_per_prime,10)))
    return dict(norm_limit=limit, number_of_prime_ideals=len(phases), windows=rows)


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
