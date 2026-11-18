"""R264 exact six-phase mod-169 certificate; frozen science 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Run: python R264_six_phase_mod169_certificate.py. Pure standard-library fractions/integers.
"""
import json
from fractions import Fraction as F
from math import gcd
from pathlib import Path

S = F(67,169)
J,T,K,P,MASK = 1184397599,989553240,3805974000,169,57
W = (144,576,1440,4320,17280,86400,518400)

def mul_linear(f,a):
    z=[F(0)]*(len(f)+1)
    for i,v in enumerate(f):
        z[i]-=a*v; z[i+1]+=v
    return z

def characteristic(ids,a,b):
    c=[F(1)]
    for i in ids: c=mul_linear(c,a[i])
    for i in ids:
        z=[F(1)]
        for j in ids:
            if i!=j: z=mul_linear(z,a[j])
        for j,v in enumerate(z): c[j]-=b[i]*v
    return c

def reconstruct():
    t=(1691*S-2615)/(2615*S-3539)
    a=[F(1,5),F(1,4),F(3,10),F(9,20),S,F(2,3),t]
    b=[F(13,60)]+[F(5,18)*abs(F(1,2)-a[i]) for i in range(1,7)]
    pi=[b[i]/(1-a[i]) for i in range(7)]
    assert sum(pi)==1
    z=sum(b[i]/(1-a[i])**2 for i in range(7))
    rho=[b[i]/(z*(1-a[i])**2) for i in range(7)]
    ids=[0]+[i+1 for i in range(6) if MASK & (1<<i)]
    assert ids==[0,1,4,5,6]
    d=len(ids)
    c=[v*T**(d-j) for j,v in enumerate(characteristic(ids,a,b))]
    assert all(v.denominator==1 for v in c)
    state=[F(1)]*d; q=[]
    for k in range(d+3):
        if k>=3:
            val=F(J*T**k,K)*W[MASK.bit_count()]*sum(rho[i]*state[j] for j,i in enumerate(ids))
            assert val.denominator==1
            q.append(int(val)%P)
        total=sum(pi[i]*state[j] for j,i in enumerate(ids))
        state=[a[i]*state[j]+(1-a[i])*total for j,i in enumerate(ids)]
    return [int(v)%P for v in c],q

def run():
    c,q=reconstruct()
    assert c==[0,0,104,166,2,1]
    assert q==[54,58,150,4,156]
    # Independent product of factors x^2*(x-91)*(x-101)*(x-144).
    f=[1]
    for root in (0,0,91,101,144):
        z=[0]*(len(f)+1)
        for j,v in enumerate(f):
            z[j]=(z[j]-root*v)%P
            z[j+1]=(z[j+1]+v)%P
        f=z
    assert f==c
    assert [(16*pow(144,n,P)+38*pow(101,n,P))%P for n in range(5)]==q
    for root in (101,144):
        assert sum(c[i]*pow(root,i,P) for i in range(6))%P==0
    assert pow(101,6,P)==pow(144,6,P)==14
    seeds=[(16*pow(144,r,P)+38*pow(101,r,P))%P for r in range(6)]
    assert seeds==[54,58,150,4,156,155]
    assert [v%13 for v in seeds]==[2,6,7,4,0,12]
    assert seeds[4]==12*13 and all(seeds)
    assert pow(14,13,P)==1 and gcd(14,P)==1
    assert all(pow(14,t,P)==(1+13*t)%P for t in range(300))
    # Formula comparison over two 78-event periods; infinite proof is recurrence induction.
    assert all((16*pow(144,n,P)+38*pow(101,n,P))%P ==
               seeds[n%6]*(1+13*(n//6))%P for n in range(160))
    residues=[seeds[n%6]*(1+13*(n//6))%P for n in range(78)]
    assert all(residues)
    assert all(any(residues[i]!=residues[(i+h)%78] for i in range(78))
               for h in (1,2,3,6,13,26,39))
    assert pow(10,6,13)==1 and all(pow(10,h,13)!=1 for h in (1,2,3))
    witnesses={str(k):seeds[(k-3)%6]*(1+13*((k-3)//6))%P
               for k in (3,4,7,1093,2185)}
    assert witnesses['1093']==witnesses['2185']==156
    cert={
      "schema":"EM_R264_SIX_PHASE_13ADIC_OBSERVER_V1",
      "frozen_science_pin":"43ec6098b1330ae86d0a7863be336c5d97f6ef34",
      "parent":"R263@a21165ac0d4bc144a3d405a468c041b419fc2bd8",
      "parameter":"67/169","source_mask":57,"modulus":169,
      "model_constants":{"J":J,"T":T,"K":K},
      "characteristic_ascending_mod169":c,"initial_window_at_k_3_to_7_mod169":q,
      "two_root_formula_mod169":{"A":16,"root_A":144,"B":38,"root_B":101},
      "six_phase_seeds":seeds,
      "six_step_multiplier_mod169":14,
      "affine_formula":"q_(57,k)=c_((k-3)%6)*(1+13*floor((k-3)/6)) mod 169",
      "valuation_rule":"v13(q_(57,k))=1 iff k%6==1; otherwise 0, for all k>=3",
      "least_period_mod13":6,"least_period_mod169":78,
      "residues_one_period":residues,"event_witnesses":witnesses,
      "zero_only_minimum_for_all_powers_13_to_a_with_a_at_least_2":1,
      "validation":"PASS: exact Fraction reconstruction, root factors, five taps, exact phase identities, proper period-divisor checks, event witnesses",
      "mathematical_status":"AUTHOR_PROVED / EXACT_COMPUTATION / NOT_REVIEWED",
      "scope":"auxiliary positive scalar model, original mask 57; no native BRC promotion"
    }
    out=Path(__file__).with_name("R264_verification.json")
    out.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("R264 PASS: six-phase, exact v13, least periods 6/78, singleton all a>=2")

if __name__=="__main__": run()
