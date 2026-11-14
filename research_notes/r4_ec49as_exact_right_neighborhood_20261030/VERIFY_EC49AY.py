"""EC49AY: exact postcritical causal optimum; requires sibling VERIFY_EC49AX.py.
Only Fraction and Q(sqrt(215)); exhaustive 168/924 edge certificate inherited
from the published EC49AX verifier. Independent review/admission not claimed.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from pathlib import Path
import importlib.util, json

spec = importlib.util.spec_from_file_location('ec49ax', Path(__file__).with_name('VERIFY_EC49AX.py'))
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)

@dataclass(frozen=True)
class R:
    a: F = F(0)
    b: F = F(0)
    def __add__(self, o):
        o=Q(o);return R(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return R(-self.a,-self.b)
    def __sub__(self,o):return self+(-Q(o))
    def __rsub__(self,o):return Q(o)+(-self)
    def __mul__(self,o):
        o=Q(o);return R(self.a*o.a+215*self.b*o.b, self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def inverse(self):
        den=self.a*self.a-215*self.b*self.b
        assert den
        return R(self.a/den,-self.b/den)
    def __truediv__(self,o):return self*Q(o).inverse()
    def __rtruediv__(self,o):return Q(o)*self.inverse()
    def sign(self):
        if not self.a:return (self.b>0)-(self.b<0)
        if not self.b:return (self.a>0)-(self.a<0)
        if (self.a>0)==(self.b>0):return (self.a>0)-(self.a<0)
        z=self.a*self.a-215*self.b*self.b
        assert z
        return ((self.a>0)-(self.a<0)) if z>0 else ((self.b>0)-(self.b<0))
    def __lt__(self,o):return (self-Q(o)).sign()<0
    def __gt__(self,o):return (self-Q(o)).sign()>0
    def __str__(self):return f'{self.a}+({self.b})*sqrt(215)'
def Q(v):return v if isinstance(v,R) else R(F(v),F(0))

def check():
    regular=0;residual=[];infeasible=0
    for supp,u,v in prior.edges(prior.vertices()):
        pair=prior.clip(u,v)
        if pair is None:infeasible+=1;continue
        intervals=[prior.price_interval(x,e) for e in (prior.E0,prior.E1) for x in pair]
        if all(i is not None for i in intervals) and max(i[0] for i in intervals)<=min(i[1] for i in intervals):
            lam=max(i[0] for i in intervals)
            assert all(prior.dual(x,prior.E1,lam)<=prior.h(prior.E1) for x in pair)
            regular+=1
        else:residual.append((supp,pair))
    assert (infeasible,regular,len(residual))==(720,196,8)
    sig=prior.signature(residual[0][1]);assert all(prior.signature(pair)==sig for _,pair in residual)
    s=R(F(0),F(1));t=Q(F(115,72))-s/18
    p=(Q(16)+s)/36
    gap=Q(-F(41,5760))+s/2160
    assert Q(0)<t<Q(1) and Q(0)<p<Q(1)
    # (tvar-1)(72*tvar-35)-240*gap*(115-72*tvar) = 72*(tvar-t)^2.
    coeff=[Q(35)-240*gap*115, Q(-107)+240*gap*72, Q(72)]
    rhs=[72*t*t,-144*t,Q(72)]
    assert coeff==rhs
    row0=((Q(11)-8*t)/16,Q(0),t/4,Q(0),(Q(5)+4*t)/16)
    rows=(row0,(Q(0),Q(1),Q(0),Q(0),Q(0)),(Q(1),Q(0),Q(0),Q(0),Q(0)))
    assert all(sum(row,Q(0))==Q(1) for row in rows)
    assert all(not v<Q(0) for row in rows for v in row)
    assert sum((rows[w][c]*cost for w in range(3) for c,cost in enumerate((1,1,2,2,0))),Q(0))==Q(F(43,16))
    eta=F(2,5); beta=Q(0);alpha=Q(0);payment=Q(0);accepted=[]
    for c in range(4):
        for u in range(2):
            qs=[rows[z][c]*Q(F(1,2)+(2*u-1)*(1-z)*eta)/3 for z in range(3)]
            T=sum(qs,Q(0));coin=p if (c,u)==(0,1) else Q(1)
            payment+=coin*T
            for z,q in enumerate(qs):
                if (43*q-16*T)>Q(0):
                    accepted.append((c,u,z))
                    alpha+=coin*(T+q)/4
                    beta+=coin*T/3
    assert payment==Q(F(13,16))
    assert accepted==[(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)]
    h=Q(F(9713,82560));H=alpha-Q(F(177,172))*beta
    optimum=h-gap
    assert alpha==Q(F(581,1440))-s/2160
    assert beta==Q(F(13,48))
    assert H==optimum==Q(F(15451,123840))-s/2160
    assert H>h and gap<Q(0)
    return dict(schema='EC49AY_EXACT_ALGEBRAIC_CERT_V1',model='positive_18+18_auxiliary_probability_BRC',eta='2/5',
      vertices=168,base_edges=924,purchase_infeasible_edges=infeasible,dual_certified_edges=regular,
      residual_permutation_equivalent_edges=len(residual),h_old=str(h),
      t_star=str(t),sensor_p_c0_u1=str(p),alpha=str(alpha),beta=str(beta),H_exact=str(H),
      H_gain=str(H-h),global_postcritical_interval='eta_star<=eta<=2/5, see proof',
      proof_dependencies=['EC49AV sparse lemma','EC49AX 196 four-corner rational price certificates','EC49AX eight-edge affine signatures'],
      arithmetic='Fraction + exact Q(sqrt(215)) sign by squared rational comparison',
      status='AUTHOR_EXACT_CHECK_UNREVIEWED_NOT_ADMITTED')

if __name__=='__main__':print(json.dumps(check(),ensure_ascii=False,indent=2))
