"""PREFIX-995: exact source-defined Stage46 BRC port coefficient audit.
Checks algebraic and word-combinatorial identities, not a new BRC run.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial, prod
import json
from pathlib import Path

D=12
POS=tuple(range(6))

def c(h,j):
    return Fraction(1,6)-int(h==j)

def ray(v):
    pivot=next((x for x in v if x),None)
    return tuple(x/pivot for x in v) if pivot is not None else None

def classes(cols,absolute=False):
    return len({ray(tuple(abs(c(h,j)) if absolute else c(h,j) for j in cols)) for h in range(D)})

def expected(k,n):
    result=[0]*6
    for j,x in enumerate(k):
        if x:
            result[j]=factorial(n-1)//prod(factorial(y-int(i==j)) for i,y in enumerate(k))
    return result

def direct(n):
    output=defaultdict(lambda:[0]*6)
    for word in product(POS,repeat=n):
        k=[0]*6
        for j in word:k[j]+=1
        output[tuple(k)][word[-1]]+=1
    return output

def verify():
    for h in range(D):
        assert sum((c(h,j) for j in range(D)),Fraction())==1
        for k in range(D):
            assert sum((c(h,j)*c(k,j) for j in range(D)),Fraction())==int(h==k)
    assert classes(range(D))==12
    assert classes(POS)==7
    assert classes(POS,True)==7
    results={}
    for n in range(1,7):
        observed=direct(n)
        assert sum(map(sum,observed.values()))==6**n
        for k,names in observed.items():
            assert names==expected(k,n)
            assert sum(names)==factorial(n)//prod(factorial(x) for x in k)
        results[str(n)]={"named_words":6**n,"endpoints":len(observed)}
    for n in range(1,5):
        for word in product(range(D),repeat=n):
            ell=sum(1 if j in POS else -1 for j in word)
            assert (ell==n)==all(j in POS for j in word)
    p2=direct(2)[(1,1,0,0,0,0)]
    p3=direct(3)[(2,1,0,0,0,0)]
    assert p2==[1,1,0,0,0,0] and p3==[2,1,0,0,0,0]
    a2=Fraction(sum(x*x for x in p2),6**4)
    b2=Fraction(sum(p2)**2,6**4)
    a3=Fraction(sum(x*x for x in p3),6**6)
    b3=Fraction(sum(p3)**2,6**6)
    assert (a2,b2,a3,b3)==(Fraction(1,648),Fraction(1,324),Fraction(5,46656),Fraction(1,5184))
    signed=sum((c(0,j)*c(j,1) for j in range(D)),Fraction())
    unsigned=sum((abs(c(0,j))*abs(c(j,1)) for j in range(D)),Fraction())
    assert signed==0 and unsigned==Fraction(5,9)
    return {
      "source_model":"Stage46 BRC candidate C[h,j]=2/d-delta[h,j]",
      "native_x6_degree":12,
      "projective_classes_all_named_outputs":12,
      "projective_classes_six_positive_outputs":7,
      "positive_word_coefficient":"6^-n",
      "verified_word_depths":results,
      "verified_named_word_total":sum(6**n for n in range(1,7)),
      "grade_support_test":"All twelve-direction signed words through n=4: ell=n iff every step positive",
      "n2":{"k":[1,1,0,0,0,0],"last_port_counts":p2,"correct_cell_probability":str(a2),"wrong_endpoint_only_square":str(b2)},
      "n3":{"k":[2,1,0,0,0,0],"last_port_counts":p3,"correct_cell_probability":str(a3),"wrong_endpoint_only_square":str(b3)},
      "local_signed_off_diagonal":str(signed),
      "local_absolute_off_diagonal":str(unsigned),
      "future_scope":"Stage46 candidate outer positive-grade boundary; all-n analytic formula",
      "native_physics_claim":False,
      "review":"NOT_REVIEWED"}
if __name__=="__main__":
    results=verify()
    Path(__file__).with_name("PREFIX995_R6_EXACT_RESULTS.json").write_text(json.dumps(results,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps(results,indent=2,ensure_ascii=False))
