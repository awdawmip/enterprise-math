"""Verify finite Abel reduction for individual mirror jets (author-side)."""
import json, importlib.util, pathlib
path=pathlib.Path(__file__).with_name('d25_WV_mirror_firstjet_reproducer_20261109.py')
spec=importlib.util.spec_from_file_location('mirror',path)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

def check(p):
    H=[0]*p
    for j in range(1,p):H[j]=(H[j-1]+pow(j,-1,p))%p
    result={}
    for kind,bound,den,w in [('A',3,36,6),('C',4,288,8)]:
        co=mod.coefficients(p,kind)
        Q=(pow(216 if kind=='A' else 2304,p-1,p*p)-1)//p
        qs=[q for q in range(1,p) if bound*q>p and 2*q<p]
        prefix=0; total=0; corrections=0; previous=None
        js=[];weights=[]
        for q in qs:
            aq=(co[q]%p**3)//p
            b=pow(den*q**3*(aq%p),-1,p)
            v=(3*pow(q,-1,p)-Q+(2*H[2*q]+3*H[3*q-p]-5*H[q] if kind=='A' else
                 4*H[4*q-p]-4*H[q]))%p
            js.append(v);weights.append((1-w*q)*b%p)
        for t,q in enumerate(qs):
            prefix=(prefix+weights[t])%p
            if t+1<len(qs):
                if kind=='A':
                    d=(2*pow(2*q+1,-1,p)+3*pow(3*q+1,-1,p)+3*pow(3*q+2,-1,p)-3*pow(q,-1,p))%p
                else:
                    d=(4*pow(4*q+1,-1,p)+4*pow(4*q+2,-1,p)+4*pow(4*q+3,-1,p)-3*pow(q,-1,p))%p
                assert d==(js[t+1]-js[t])%p,(kind,p,q,'jet-difference')
                corrections=(corrections+prefix*d)%p
        direct=sum(weights[i]*js[i] for i in range(len(qs)))%p
        endpoint=prefix*js[-1]%p if qs else 0
        assert direct==(endpoint-corrections)%p
        result[kind]={'interval':[qs[0],qs[-1]],'jet_sum':direct,'Abel_endpoint':endpoint,'Abel_prefix_delta':corrections}
    return result

if __name__=='__main__':
    ps=[p for p in range(5,212) if mod.prime(p)]+[373]
    data={str(p):check(p) for p in ps}
    print(json.dumps({'schema':'D25_JET_ABEL_BOUNDARY_V1','tested_primes':len(ps),
           'special':{str(p):data[str(p)] for p in (13,19,373)},
           'status':'PASS_EXACT_FINITE_UNREVIEWED'},indent=2))
