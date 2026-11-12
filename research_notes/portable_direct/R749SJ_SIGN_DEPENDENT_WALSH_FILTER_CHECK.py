"""R749SJ exact positive selection likelihood and Bayes–Walsh recurrence test.
Source-aware selected observer is an explicit extension of R749SF, not native V29.
"""
from fractions import Fraction as F
from itertools import product,combinations
import math,json
states=list(product((-1,1),repeat=3));axes=(0,1,2)
def ch(s,U):return math.prod(s[axes.index(i)] for i in U)
def hat(mu):
    return {tuple(U):sum((mu[s]*ch(s,U) for s in states),F(0))
            for k in range(4) for U in combinations(axes,k)}
def w(s,which):return F(2+(1 if which==0 else -1)*s[0],4)
def kern(s,is_forced,p,other):
    theta=F(8)*p/(1+7*p)
    new=0 if is_forced else other
    for bit in (-1,1):
        y={1:s[1],2:s[2],new:bit}
        v=F(1+theta*bit*s[0],2) if is_forced else F(1,2)
        if v:yield y,v
def direct(mu,which,is_forced,p,other):
    out={}
    for s in states:
        for y,v in kern(s,is_forced,p,other):
            key=tuple(sorted(y.items()))
            out[key]=out.get(key,F(0))+mu[s]*w(s,which)*v
    normal=sum(out.values(),F(0))
    assert normal>0
    return out,normal
def predict(mu,which,is_forced,p,S,other):
    if not is_forced and other in S:return F(0)
    h=hat(mu);t=set(S)
    theta=F(8)*p/(1+7*p)
    c=theta if is_forced and 0 in t else F(1)
    sigma=1 if which==0 else -1
    return c*(F(1,2)*h[tuple(sorted(t))]+F(sigma,4)*h[tuple(sorted(t.symmetric_difference({0})))])
def main():
    priors={
        'uniform':{s:F(1,8) for s in states},
        'nonuniform':{s:F(i+1,36) for i,s in enumerate(states)},
        'plus':{s:F(1,4) if s[0]==s[1] else F(0) for s in states},
        'minus':{s:F(1,4) if s[0]==-s[1] else F(0) for s in states}
    }
    num=0
    for name,mu in priors.items():
        for p in (F(0),F(1,2)):
            for which in (0,1):
                for is_forced in (False,True):
                    other=3
                    out,norm=direct(mu,which,is_forced,p,other)
                    out_axes=tuple(sorted(dict(next(iter(out))).keys()))
                    for bits in range(8):
                        S={out_axes[i] for i in range(3) if bits>>i&1}
                        got=sum((v*math.prod(dict(key)[i] for i in S)
                                for key,v in out.items()),F(0))
                        exp=predict(mu,which,is_forced,p,S,other)
                        assert got==exp,(name,p,which,is_forced,S,got,exp)
                        num+=1
    check=[]
    for name in ('plus','minus'):
        out,L=direct(priors[name],0,False,F(1,2),3)
        ey=sum((v*dict(k)[1] for k,v in out.items()),F(0))/L
        py=sum((v for k,v in out.items() if dict(k)[1]==1),F(0))/L
        check.append([str(L),str(ey),str(py)])
    assert check==[['1/2','1/2','3/4'],['1/2','-1/2','1/4']]
    print(json.dumps({'status':'PASS','walsh_exact_compares':num,'case_priors':4,
         'p_tested':['0','1/2'],'selected_C_plus_minus':[{'P(C)':z[0],
          'E[Y1|C]':z[1],'P(Y1=+|C)':z[2]} for z in check],
         'equal_prior_postselection_Bayes_error':'1/4',
         'unselected_baseline_Bayes_error':'1/2',
         'scope':'pre-update source-dependent observation selection; exact signed R749SF conditional kernels'},
         indent=2))
if __name__=='__main__':main()
