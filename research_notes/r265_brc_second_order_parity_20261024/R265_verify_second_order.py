#!/usr/bin/env python3
"""R265 exact symbolic + positive-integer BRC provenance monitor.
Only the fixed formal 3-control, 2-action toy observer; NOT native P000/R193.
"""
from collections import defaultdict
from pathlib import Path
import json
import sympy as S

rt5=S.sqrt(5)
phi=(1+rt5)/2
var=S.Rational(3,2)+7*rt5/10
k4_expected=-S.Rational(153,2)-S.Rational(1711,50)*rt5
states=[(q,last,eps) for q,last in ((0,1),(2,0),(2,1),(1,0)) for eps in (1,-1)]

def edge(q,eps,a):
    if q==0:
        nq,eta,b=2,(-1 if a==0 else 1),-1
    elif q==1:
        nq,eta,b=0,(-1 if a==0 else 1),-1
    else:
        nq,eta,b=(1 if a==0 else 2),1,(1 if a==0 else -1)
    ne=eta*eps
    return nq,ne,ne*b

def next_r(r,a):
    return (1,2,2)[r] if a==0 else (0,0,2)[r]

def simp(x):
    return S.simplify(S.radsimp(x))

def symbolic():
    z,x,u,L=S.symbols("z x u L")
    T=S.zeros(8)
    for col,(q,last,e) in enumerate(states):
        for a in (0,1):
            if last==0 and a==0:continue
            nq,ne,g=edge(q,e,a)
            T[states.index((nq,a,ne)),col]+=z**g
    characteristic=(L*L+1)*(L**6-(z+1/z)*L**5+2*L*L-1)
    assert S.cancel(T.charpoly(L).as_expr()-characteristic)==0
    Y=(S.eye(8)-x*T).inv()[:,0]
    den=(x*x+1)*(x**6-2*x**4+x*(z+1/z)-1)
    Gp=x**5*(x-z)/den
    Gm=-x*(x-z)*(x**3*z+x*z-1)/den
    assert S.cancel(Y[2]-Gp)==0
    assert S.cancel(Y[3]-Gm)==0
    F=L**6-2*S.cosh(u)*L**5+2*L**2-1
    fl=simp(S.diff(F,L).subs({L:phi,u:0}))
    fuu=simp(S.diff(F,u,2).subs({L:phi,u:0}))
    fll=simp(S.diff(F,L,2).subs({L:phi,u:0}))
    fluu=simp(S.diff(F,L,u,2).subs({L:phi,u:0}))
    fuuuu=simp(S.diff(F,u,4).subs({L:phi,u:0}))
    alpha=simp(-fuu/(2*fl))
    beta=simp(-(S.Rational(1,2)*fll*alpha**2+S.Rational(1,2)*fluu*alpha+fuuuu/24)/fl)
    k2=simp(2*alpha/phi)
    k4=simp(24*(beta/phi-S.Rational(1,2)*(alpha/phi)**2))
    assert simp(k2-var)==0 and simp(k4-k4_expected)==0
    dx=6*x**5-8*x**3+z+1/z
    C={"+":-x**4*(x-z)/((x*x+1)*dx),
       "-":(x-z)*(x**3*z+x*z-1)/((x*x+1)*dx)}
    X=simp(1/phi)
    xdd=simp(-2*alpha/phi**2)
    derivatives={}
    for sign,expr in C.items():
        ev=lambda term:simp(term.subs({x:X,z:1}))
        c0=ev(expr)
        c1=ev(S.diff(expr,z))
        c2=ev(S.diff(expr,z,2)+S.diff(expr,z)+xdd*S.diff(expr,x))
        derivatives[sign]={"c0":c0,"a1":simp(c1/c0),"a2":simp(c2/c0)}
        assert simp(c0-1/(10*phi))==0
    assert simp(derivatives["+"]["a1"]-(3+rt5)/2)==0
    assert simp(derivatives["-"]["a1"]+(1+rt5))==0
    assert simp(derivatives["+"]["a2"]+(99+45*rt5)/10)==0
    assert simp(derivatives["-"]["a2"]+(37+20*rt5)/5)==0
    def corr(sign,t):
        d=derivatives[sign]
        return simp(k4/(8*k2*k2)-d["a2"]/(2*k2)+(d["a1"]*t-S.Rational(t*t,2))/k2)
    he=corr("+",2)
    ho=corr("-",-3)
    assert simp(he-(S.Rational(23,2)-33*rt5/8))==0
    assert simp(ho-(S.Rational(281,4)-243*rt5/8))==0
    assert corr("+",2)>corr("-",-4) and corr("-",-3)>corr("+",3)
    return {
      "characteristic_8":str(characteristic),"GF_B_plus":str(Gp),
      "GF_B_minus":str(Gm),"lambda_expansion_coefficient_u2":str(alpha),
      "lambda_expansion_coefficient_u4":str(beta),
      "variance":str(k2),"fourth_cumulant":str(k4),
      "C_and_derivatives":{k:{a:str(v) for a,v in d.items()} for k,d in derivatives.items()},
      "even_optimal":{"epsilon":1,"t":2,"correction":str(he),"approx":str(S.N(he,16))},
      "odd_optimal":{"epsilon":-1,"t":-3,"correction":str(ho),"approx":str(S.N(ho,16))},
      "even_competitor":str(corr("-",-4)),"odd_competitor":str(corr("+",3)),
      "GF_char_cumulant_residue_identity":"PASS"
    }

def exact_dp():
    D={(0,0,1,0):1}
    samples={}
    raw_checked=0
    raw_atoms=0
    lens={31,32,63,64,95,96,127,128,139,140,159,160,199,200,239,240}
    for m in range(241):
        if m<=13:
            raw=defaultdict(int)
            for w in range(1<<m):
                q,r,e,t=0,0,1,0
                for i in range(m-1,-1,-1):
                    a=(w>>i)&1
                    nq,ne,g=edge(q,e,a)
                    q,r,e,t=nq,next_r(r,a),ne,t+g
                raw[(q,r,e,t)]+=1
            assert dict(raw)==D
            raw_checked+=1<<m
            raw_atoms+=len(raw)
        assert sum(D.values())==1<<m
        assert all((t-m)%2==0 and cnt>0 for (q,r,e,t),cnt in D.items())
        if m in lens:
            keys={(q,e,t) for q,r,e,t in D}
            fib=lambda q,e,t:tuple(D.get((q,r,e,t),0) for r in (0,1,2))
            best=max((min(fib(q,e,t)),q,e,t) for q,e,t in keys)
            r1_best=max((D.get((2,1,e,t),0),e,t)
                        for e in (1,-1) for t in range(-m,m+1,2))
            M,q,e,t=best
            assert q==2 and M==r1_best[0]
            samples[str(m)]={"M_m":str(M),"max_fibre":{"q":q,"epsilon":e,"t":t},
                              "r1_peak":{"epsilon":r1_best[1],"t":r1_best[2]},
                              "M_eq_r1_peak":True}
        if m==240:break
        E=defaultdict(int)
        for (q,r,e,t),count in D.items():
            for a in (0,1):
                nq,ne,g=edge(q,e,a)
                E[(nq,next_r(r,a),ne,t+g)]+=count
        D=dict(E)
    assert samples["140"]["M_m"]=="438611399828372525268845634"
    assert samples["200"]["M_m"]=="1263924779564116173737130828762162554832"
    for m in (95,96,127,128,139,140,159,160,199,200,239,240):
        expected=(1,2) if m%2==0 else (-1,-3)
        assert (samples[str(m)]["r1_peak"]["epsilon"],
                samples[str(m)]["r1_peak"]["t"])==expected
    return {"raw_words_checked":raw_checked,"raw_dp_atoms_checked":raw_atoms,
            "dp_up_to_length":240,"samples":samples,"positive_integer_checks":"PASS",
            "parity_lattice_checks":"PASS"}

def main():
    d={"schema":"EM_R265_BRC_SECOND_ORDER_AUTHOR_EVIDENCE_V1",
       "scope":"fixed R260-R264 formal positive BRC observer, not P000-native",
       "source_global_snapshot":"94cc7009b96256b6a59a2cf950081112c411365a",
       "source_em_main_snapshot":"b1e773f528ecec65959c46881e698c27331190ab",
       "symbolic":symbolic(),"integer":exact_dp(),
       "asymptotic_claim":"analytic transfer-operator Fourier/saddle argument; not inferred from finite DP",
       "native_enterprise_math_executed":False,"independent_review":False,
       "tool_reuse":"T0_BRC affine-effect composition law REUSE_APPLIED; local independent implementation not native runtime"}
    target=Path(__file__).with_name("EXACT_EVIDENCE.json")
    target.write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print("PASS raw words",d["integer"]["raw_words_checked"],"dp",d["integer"]["dp_up_to_length"])
    for m in ("95","96","139","140","199","200","239","240"):
        print(m,d["integer"]["samples"][m]["r1_peak"],d["integer"]["samples"][m]["M_m"])
    print("sym_even",d["symbolic"]["even_optimal"]["correction"])
    print("sym_odd",d["symbolic"]["odd_optimal"]["correction"])
if __name__=="__main__":
    main()
