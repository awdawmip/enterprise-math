"""Construct a uniformly visible 3-by-2 rational readout switching its global winner at N -> N+1."""
from argparse import ArgumentParser
from fractions import Fraction as Q
from math import gcd, lcm
import json
from suffix_limits import block, compose, evaluate, interval_image, terminal, derivative_ratio, enclose_decimals
from observable_minimum import T


def determinant(matrix):
    a,b,c,d=matrix
    return a*d-b*c


def model_suffix(first,second,last):
    return compose(terminal(last+2),compose(block(1,3-first,second),block(2,3,first)))


A=model_suffix(1,0,0)
C=model_suffix(0,0,1)
B=model_suffix(0,1,0)
ALPHA=Q(3,20)
EPS=Q(1,8)
LOW,HIGH=Q(7,50),Q(147,1000)


def slope_bounds(matrix):
    c,d=matrix[2:]
    return sorted(Q(abs(determinant(matrix)),v*v) for v in (d,c+d))


def global_checks():
    assert A==(-115,124096,-51520,27872768) and C==(828,87776,267237,11696360)
    loA,hiA=slope_bounds(A)
    loB,hiB=slope_bounds(B)
    loC,hiC=slope_bounds(C)
    assert hiC<Q(1,1000) and hiA<Q(1,1000)
    assert loC/hiA>23 and hiC/loA<25 and loB/hiA>14
    assert (ALPHA-LOW)/LOW*23*Q(15,16)>1
    assert (ALPHA-HIGH)/HIGH*25*Q(16,15)<1
    assert Q(2*267237,11696360+267237)>Q(1,25)
    assert Q(2,15)*Q(2,1000)<Q(1,25)
    assert Q(3,1000)*180>max(HIGH,25*(ALPHA-LOW))*Q(16,15)
    assert LOW*14>max(HIGH,25*(ALPHA-LOW))*Q(16,15)
    for a in (LOW,HIGH):
        labels=[Q(1,2)+EPS*v for v in (2*a+Q(1,3),-3*a-3,a+Q(8,3))]
        assert all(Q(1,16)<p<Q(15,16) for p in labels)
        assert [sum(p*w for p,w in zip(labels,row)) for row in T]==[Q(5,8),Q(1,2),Q(1,2)+EPS*a]
    def composite(gaps):
        c=4
        z=(1,0,0,1)
        for r,m in zip((3,2,1),gaps[:-1]):
            z=compose(block(r,c,m),z)
            c-=m
        return compose(terminal(c),z)
    prefix=(1,0,0,1)
    for r in range(4,10):
        prefix=compose(prefix,block(r,r+1,1))
    u=interval_image(prefix,(Q(0),Q(1)))
    assert min(derivative_ratio(composite((0,0,2,0)),composite((1,1,0,0)),z) for z in u)>180
    alpha=Q(0)
    weight=Q(1)
    for length in range(11):
        if length: weight*=Q(4*length+9,4*length+12)
        x=Q(840,(length+4)*(length+5)*(length+6))
        alpha=x*(1-weight)/(1+x)
        assert alpha<=LOW-Q(3,1000) or alpha>=HIGH+Q(3,1000)
    assert alpha<LOW-Q(3,1000)


def polynomial_product(*linear_factors):
    result=[Q(1)]
    for base,slope in linear_factors:
        temp=[Q(0)]*(len(result)+1)
        for i,v in enumerate(result):
            temp[i]+=v*base
            temp[i+1]+=v*slope
        result=temp
    return result


def point(matrix,z):
    return evaluate(matrix,z)


def secant(matrix,x,y):
    c,d=matrix[2:]
    return Q(abs(determinant(matrix)),(c*x+d)*(c*y+d))


def probability_forms(matrix,alpha,kappa,x,y):
    mx,my=point(matrix,x),point(matrix,y)
    return ((Q(1,2)+EPS*(kappa-alpha*mx),EPS*mx),
            (Q(1,2)-EPS*(kappa-alpha*my),-EPS*my))


def witness_polynomial(x,y):
    # Its sign is that of (H_C-1)/(H_A-1)-1. Both row probabilities increase.
    sx,sy=probability_forms(A,Q(0),Q(7,8),x,y)
    tx,ty=probability_forms(C,ALPHA,Q(4,5),x,y)
    s=polynomial_product((ALPHA,-1),sx,sy)
    t=polynomial_product((0,1),tx,ty)
    coef=[secant(C,x,y)*v-secant(A,x,y)*w for v,w in zip(s,t)]
    den=lcm(*(v.denominator for v in coef))
    ints=[int(den*v) for v in coef]
    divisor=gcd(*ints)
    return tuple(v//divisor for v in ints)


def sign(poly,a):
    n,d=a.numerator,a.denominator
    value=poly[3]*n**3+poly[2]*n*n*d+poly[1]*n*d*d+poly[0]*d**3
    return (value>0)-(value<0)


def root_bracket(poly,steps):
    lo,hi=LOW,HIGH
    assert sign(poly,lo)>0 and sign(poly,hi)<0
    for _ in range(steps):
        mid=(lo+hi)/2
        value=sign(poly,mid)
        if value==0: return mid,mid
        if value>0: lo=mid
        else: hi=mid
    return lo,hi


def rational_witness(poly,following):
    lo,hi=LOW,HIGH
    assert all(sign(p,lo)>0 and sign(p,hi)<0 for p in (poly,following))
    steps=0
    while True:
        a=(lo+hi)/2
        before,after=sign(poly,a),sign(following,a)
        steps+=1
        if before>0 and after<0: return a,steps
        if after>=0: lo=a
        elif before<=0: hi=a
        else: raise AssertionError("unexpected orientation")


def exact_panel(matrix,alpha,kappa,x,y,a):
    gen=lambda u: Q(1,2)+EPS*(kappa+(a-alpha)*point(matrix,u))
    px,py=gen(x),gen(y)
    assert py>px
    return py*(1-px)/(px*(1-py))


def rational_exact_tie(x,y):
    delta_a,delta_c=secant(A,x,y),secant(C,x,y)
    a=ALPHA*delta_c/(delta_a+delta_c)
    assert LOW<a<HIGH
    hA=lambda u: Q(7,8)+a*point(A,u)
    hC=lambda u: Q(4,5)+(a-ALPHA)*point(C,u)
    eps=Q(1,16)
    t=(1-eps*(hA(x)+hC(y)))/2
    pA=lambda u: t+eps*hA(u)
    pC=lambda u: t+eps*hC(u)
    assert pA(x)+pC(y)==pA(y)+pC(x)==1 and pA(x)<pA(y)
    assert pA(y)*(1-pA(x))/(pA(x)*(1-pA(y)))==pC(y)*(1-pC(x))/(pC(x)*(1-pC(y)))>1
    positions=[t+eps*v for v in (2*a+Q(1,3),-3*a-3,a+Q(8,3))]
    assert all(Q(1,5)<p<Q(4,5) for p in positions)
    assert [sum(p*w for p,w in zip(positions,row)) for row in T]==[t+eps,t,t+eps*a]
    return a,t


def run(scales):
    global_checks()
    prefix=(1,0,0,1)
    panels={}
    needed=set(scales)|{n+1 for n in scales}|{20}
    for k in range(3,max(needed)+1):
        if k>3: prefix=compose(prefix,block(k-1,k,1))
        if k in needed:
            x,y=interval_image(prefix,(Q(0),Q(1)))
            panels[k]=(x,y,witness_polynomial(x,y))
    rows=[]
    for n in scales:
        a,steps=rational_witness(panels[n][2],panels[n+1][2])
        tie_a,tie_t=rational_exact_tie(panels[n][0],panels[n][1])
        comparison=[]
        for k in (n,n+1):
            x,y,_=panels[k]
            actual_a=exact_panel(A,Q(0),Q(7,8),x,y,a)
            actual_c=exact_panel(C,ALPHA,Q(4,5),x,y,a)
            comparison.append('A<C' if actual_a<actual_c else 'C<A' if actual_a>actual_c else '=')
        assert comparison==['A<C','C<A']
        l1,h1=root_bracket(panels[n][2],steps+90)
        l2,h2=root_bracket(panels[n+1][2],steps+90)
        w=panels[n][1]-panels[n][0]
        ratio=enclose_decimals(((l1-h2)/w,(h1-l2)/w),18)
        rows.append(dict(last_A_winner=n,first_C_winner=n+1,a=str(a),width_over_input_width=ratio,
                         bisections=steps,exact_H_order=comparison,
                         rational_equal_at_n=True,
                         exact_tie_parameters=([str(tie_a),str(tie_t)] if n==min(scales) else None)))
    x,y,_=panels[20]
    amin,_=root_bracket(witness_polynomial(y,y),180)
    _,amax=root_bracket(witness_polynomial(x,x),180)
    return dict(critical_limit_enclosure=enclose_decimals((amin,amax),40),probe_first_column=['5/8','1/2','1/2+a/8'],valid_for_all_n_ge=10,
                uniform_logH_over_TV_lower='3/2000',constructed=rows)


if __name__=='__main__':
    ap=ArgumentParser(description=__doc__)
    ap.add_argument('--scales',type=int,nargs='+',default=[10,25,50,100])
    args=ap.parse_args()
    assert min(args.scales)>=10
    print(json.dumps(run(args.scales),indent=2))
