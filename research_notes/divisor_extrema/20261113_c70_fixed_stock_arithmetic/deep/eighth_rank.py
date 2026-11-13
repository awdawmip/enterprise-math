import argparse
from fractions import Fraction as Q
import json
from math import prod
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
default = next((ROOT / name / 'arithmetic' for name in ('C69','c69') if (ROOT / name / 'arithmetic').is_dir()), ROOT / 'C69' / 'arithmetic')
parser = argparse.ArgumentParser(description='Depth-eight ranks and finite center control')
parser.add_argument('--prior', type=Path, default=default)
sys.path.insert(0, str(parser.parse_args().prior))
from sixth_rank import P, dual_run, tangent_duals, gap_derivative
from mixed_rank import add,mul,power
def det(l):
 m=[v[:] for v in l];d=1;n=len(m)
 for i in range(n):
  j=next((j for j in range(i,n) if m[j][i]%P),None)
  if j is None:return 0
  if j!=i:m[i],m[j]=m[j],m[i];d=-d
  p=m[i][i]%P;d=d*p%P
  for k in range(i+1,n):
   z=m[k][i]*pow(p,-1,P)%P
   m[k]=[(v-z*w)%P for v,w in zip(m[k],m[i])]
 return d
def roots(r):
 def const(x):return (x%P,*([0]*r))
 one=const(1); xs=[one]
 for i in range(1,r+1):xs.append(((13-i)*pow(13+i,-1,P)%P,*(int(j==i) for j in range(1,r+1))))
 rates=[]
 for j in range(1,r+1):
  rate=mul(const(4),power(mul(xs[j],power(xs[j-1],-1)),3*(2*(r-j+1)+1)))
  rates.append(power(mul(const(7*pow(16,-1,P)),power(rate,4)),-1))
 cs=[]
 for length in range(r+1):
  z=const(0)
  for a in reversed(rates[:length]):z=power(add(one,mul(a,z)),-1)
  cs.append(z)
 return cs

def terminal_controls():
    from second_order_control import actual_and_curves, compose
    from verify_density import parameters, order
    records=[]
    for g in [(43,63,78,98,117,136,158,187,24),(54,73,92,111,130,154,181,32,19),
              (57,35,75,98,44,119,142,160,13)]:
        r=len(g)-1
        n=sum(g)+2
        M=(1,0,0,1)
        for i,steps in enumerate(g[:-1]):
            a,_=parameters(2*(r-i)+1,n,n-steps)
            M=compose(M,(0,1,a,1))
            n-=steps
        A,B,C,D=M
        W=Q((n+2)*(n+3)*(n+4),840)
        p,q=1/(1+W/2),1/(1+5*W)
        f=lambda z:(A*z+B)/(C*z+D)
        slope=lambda z:(A*D-B*C)/(C*z+D)**2
        X,Y=f(p),f(q)
        u, d=actual_and_curves(g)[0]
        v, e=actual_and_curves(g)[1]
        derivative0=d[-1][0]
        S=derivative0/e[-1][0]
        assert derivative0**2==(X-Y)**2*64*S*(1+5*W)*(1+W/2)/(36*Q(9,2)**2)
        bysecant=(X-Y)/(p-q)
        assert slope(p)*slope(q)==bysecant**2
        factor=Q(prod(4*k+4 for k in range(3,n+1)),prod(4*k+1 for k in range(3,n+1)))
        u2=u+X-f(p*(1+factor*W/6))
        v2=v+Y-f(q*(1+factor*W/Q(3,32)))
        j=min(range(r),key=lambda i:g[i])
        jmatch=order(u2/v2-d[j][0]/e[j][0])
        assert jmatch>10
        records.append({'gaps':g,'least_visible_index':j+1,'second_tangent_matched_bits':jmatch,
                        'residual_order':order(u2)})
    return records


def main():
    r=8
    base=dual_run(r)
    slopes=tangent_duals(r)
    slope_values = [row[0] for row in slopes]
    assert len(set(slope_values)) == r+1
    convergents=roots(r)
    far_tests={}
    eligible=[]
    for i in range(3,r+1):
        row=[]
        for j in range(1,r+2):
            if i==j:
                row.append(None)
                continue
            J=base+[list(slopes[i-1][1:]),gap_derivative(r,i-1),gap_derivative(r,j-1)]
            pair=[det(J+[list(convergents[h][1:])]) for h in (i-2,i)]
            if any(pair):
                eligible.append((i,j))
            row.append(pair)
        far_tests[str(i)]=row
    stable=base+[list(convergents[r-1][1:]),gap_derivative(r,r)]
    second=[det(stable+[gap_derivative(r,j),list(slopes[j][1:])]) for j in range(r)]
    third=[det(stable+[gap_derivative(r,7),gap_derivative(r,j)]) for j in range(r-1)]
    assert len(eligible)==38 and all(second[1:-1]) and all(third)
    result={'prime':P,'normalized_tangent_values':slope_values,'eligible_far_pairs':len(eligible),'far_determinants':far_tests,
            'terminal_secondary':second,'terminal_tertiary':third,
            'terminal_controls':terminal_controls(),'density_floor':str(Q(3,9)+Q(38,72)*Q(9,17))}
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
