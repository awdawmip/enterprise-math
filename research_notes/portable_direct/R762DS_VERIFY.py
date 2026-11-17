#!/usr/bin/env python3
"""R762DS: exact positive BRC XZ endpoint content using cyclic modular recurrence.

No external packages, floating point or probabilistic checks. The modulus 3**30
determines the predicted 3-adic valuation exactly whenever e<30 and one
coefficient is nonzero mod 3**(e+1).
"""
import json
from hashlib import sha256
from pathlib import Path

CASES = [(9, 80), (27, 160), (81, 297), (243, 245)]
K = 30
MOD = 3**K

def predicted(Q, n):
    d = Q // 3
    return 2 * max(0, (n-d) // (2*d))

def run_case(Q, N):
    d = Q // 3
    size = Q*Q
    a = [0]*size
    a[0] = 1
    prev_rows = [((i-1)%Q)*Q for i in range(Q)]
    mass = 1
    transitions = []
    previous = -1
    boundaries = {}
    boundary_ns = {3*d-1,3*d,5*d-1,5*d,7*d-1,7*d,9*d-1,
                   9*d,11*d,13*d,N}
    for n in range(1,N+1):
        b = [0]*size
        for i in range(Q):
            base = i*Q
            prev = prev_rows[i]
            row = a[base:base+Q]
            prow = a[prev:prev+Q]
            for j in range(Q):
                jm = (j-1)%Q
                b[base+j] = (row[j]+2*prow[j]+2*row[jm]+prow[jm])%MOD
        a = b
        exponent = predicted(Q,n)
        assert exponent < K
        level = 3**exponent
        higher = 3*level
        assert all(v % level == 0 for v in a), ("divisibility",Q,n,exponent)
        witness = next(((p//Q,p%Q,v) for p,v in enumerate(a)
                        if v % higher != 0), None)
        assert witness is not None, ("sharpness",Q,n,exponent)
        mass = mass*6%MOD
        assert sum(a)%MOD == mass, ("mass",Q,n)
        if exponent != previous:
            transitions.append({"n":n,"v3_content":exponent})
            previous = exponent
        if n in boundary_ns:
            boundaries[str(n)] = {"v3_content":exponent,
                                   "witness_i":witness[0],
                                   "witness_j":witness[1],
                                   "coefficient_mod_3K":str(witness[2])}
    digest = sha256(','.join(map(str,a)).encode()).hexdigest()
    return {"Q":Q,"d":d,"N":N,"configs":N,
            "coefficient_visits":size*N,
            "transitions":transitions,"boundaries":boundaries,
            "final_residue_sha256":digest}

def main():
    obj = {"schema":"EM_R762DS_EXACT_MODULAR_VERIFICATION_V1",
           "polynomial":"1+2X+2Z+XZ",
           "arithmetic":"exact Python integer mod 3**30",
           "theorem":"v3(c_Q(n))=2*max(0,floor((n-Q/3)/(2Q/3)))",
           "cases":[run_case(Q,N) for Q,N in CASES]}
    obj["checked_exponents"] = sum(x["configs"] for x in obj["cases"])
    obj["coefficient_visits"] = sum(x["coefficient_visits"] for x in obj["cases"])
    obj["status"] = "PASS"
    path = Path(__file__).with_name("R762DS_EVIDENCE.json")
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",
                    encoding="utf-8")
    print(json.dumps({"status":obj["status"],
          "checked_exponents":obj["checked_exponents"],
          "coefficient_visits":obj["coefficient_visits"],
          "evidence":str(path)},ensure_ascii=False))

if __name__=="__main__":
    main()
