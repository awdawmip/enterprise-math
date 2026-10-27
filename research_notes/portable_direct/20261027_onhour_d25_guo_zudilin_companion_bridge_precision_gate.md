# D25 / SECOND-DIGIT-LIFT — known supercongruence companion and a sharp third-digit transfer obligation

**Status:** AUTHOR-SIDE / EXACT CONDITIONAL REDUCTION / FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED.  
**Date:** 2026-10-27.  
**Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.  
**Publication:** TP2-B6F4FC938FF94941C1B7.  
**Frozen scientific source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (must not change on control-head updates).  
**Research logical conversation:** chatgpt-research-onhour-enterprise-math-20260923.  
**Source class:** independent author-side research, not a native checkpoint, Result, review or CLAIM.

## 1. Precise mother target and consumed prior result

Accepted D24 UR/JT0 is frozen. The remaining LIFT/JT2 scalar observer is
`Delta_p-R_p = (W_p-p)/p^2 (mod p)`, where, for p == 13 or 19 modulo 24,

    W_p = sum_{k=0}^{p-1} (6k+1) C(2k,k)^2 C(3k,k)/216^k.

This exact task-specific port reduction was already derived in earlier D25 source-bound notes; it is CONSUMED, not credited to this unit. A prior deterministic regression tested all 815 target primes p<30000; do not repeat that census or claim it proves LIFT.

## 2. A published theorem with exactly the target modulus

Victor J. W. Guo and Wadim Zudilin, **A q-microscope for supercongruences** (2018; revised 2019), arXiv:1803.01830, Introduction equation (2) and Theorem 1.1 after q -> 1:

    S_p = sum_{k=0}^{p-1} (8k+1) C(4k,2k) C(2k,k)^2 / (2^(8k)*3^(2k))

    S_p == p * chi_p (mod p^3),   p > 3 prime,
    chi_p = Kronecker(-3,p) = +1 if p == 1 (mod 3), -1 if p == 2 (mod 3).

Paper: https://arxiv.org/html/1803.01830
Abstract/record: https://arxiv.org/abs/1803.01830

The binomial product equals (4k)!/(k!)^4, so the source's summand is EXACTLY

    (8k+1) (1/4)_k (1/2)_k (3/4)_k / (9^k*(k!)^3),

and is NOT the original D25 summand. The published theorem is independently proved for S_p, NOT for W_p. No hypergeometric transformation between these truncated sums is claimed here.

## 3. An exact, theorem-backed alternative certificate

For every p>3, the published S_p evaluation gives the equivalence

    [W_p == p*chi_p (mod p^3)]
      if and only if
    [W_p-S_p == 0 (mod p^3)].                               (BRIDGE)

In particular p == 13 or 19 (mod 24) implies p == 1 (mod 3), chi_p=+1, so

    boxed: LIFT on the frozen target classes
      iff  W_p-S_p == 0 (mod p^3) on those classes.

This is a **proved equivalence conditional only on the cited published theorem's correctness**, not a proof of the unknown bridge. It exchanges the unknown third digit of one weighted 3F2 for a two-model mod-p^3 transfer, with one endpoint completely evaluated by prior art. The transfer's all-prime proof is still OPEN. No claim is made that its complexity has yet been proved strictly lower than the prior single-family global-jet certificate.

Source/observer audit: both sums are full k=0,...,p-1 and each is weighted; retain the two different numerator parameter families, denominators 216 versus 2304, character chi_p, both residue classes, exact p^3 modulus and source provenance. BRC comparison does not erase their distinct representations. An ordinary real-analytic Ramanujan 1/pi ratio between infinite sums is NOT an admissible finite p-adic transport.

## 4. Independent, exact bounded test and a sharp precision counterexample

For the explicit 15-prime discriminator set

    [5,7,11,13,17,19,23,37,43,61,67,73,103,211,373]

both a binomial-coefficient implementation and an independent rational coefficient recurrence agree modulo p^4, without floating point. In these 15 cases, W_p == S_p == p*chi_p (mod p^3); this is only finite evidence for the still-open universal bridge.

The p^4 bridge fails exactly at p=7 and p=13:

    W_7-S_7 == 4*7^3 = 1372 (mod 7^4),
    W_13-S_13 == 11*13^3 = 24167 (mod 13^4).

At the native target p=373:

    W_373 == S_373 == 373 (mod 373^3),
    W_373-S_373 == 114*373^3 (mod 373^4).

Thus even within the target classes the proposed bridge is *not* a p^4 identity. The mod-p^3 precision is demonstrably sharp in general. These are exact arithmetic negative certificates for a TOO-STRONG transfer, not counterexamples to LIFT.

Deterministic JSON record uses sorted keys with separators (",",":") and fields p, character_minus3, W_mod_p3, S_mod_p3, bridge_digit_p3_to_p4. SHA-256 of the 15-row JSON:

    25192236d995db6b688d9ced7be7b3d85fd9c67d34de6bcdf155445f2e62d2bd

Reproduction (Python standard library; checker executed on 2026-10-27):

```python
from math import comb
from hashlib import sha256
import json

PRIMES = (5,7,11,13,17,19,23,37,43,61,67,73,103,211,373)

def binomial_paths(p):
    M = p**4
    inverse216 = pow(216, -1, M)
    inverse2304 = pow(2304, -1, M)
    a, b = 1, 1
    W = S = 0
    for k in range(p):
        c2 = comb(2*k, k)
        W = (W + (6*k+1)*c2*c2*comb(3*k,k)*a) % M
        S = (S + (8*k+1)*comb(4*k,2*k)*c2*c2*b) % M
        a = a * inverse216 % M
        b = b * inverse2304 % M
    return W,S

def recurrence_paths(p):
    M=p**4
    x=y=1
    W=S=0
    for k in range(p):
        W=(W+(6*k+1)*x)%M
        S=(S+(8*k+1)*y)%M
        if k+1 < p:
            x=x*(2*k+1)*(3*k+1)*(3*k+2)*pow(36*(k+1)**3,-1,M)%M
            y=y*(4*k+1)*(2*k+1)*(4*k+3)*pow(288*(k+1)**3,-1,M)%M
    return W,S

rows=[]
for p in PRIMES:
    W,S=binomial_paths(p)
    assert (W,S) == recurrence_paths(p), p
    chi=1 if p%3==1 else -1
    assert (W-chi*p) % p**3 == 0, p
    assert (S-chi*p) % p**3 == 0, p
    assert (W-S)%p**3 == 0, p
    rows.append(dict(p=p,character_minus3=chi,W_mod_p3=W%p**3,
                     S_mod_p3=S%p**3,
                     bridge_digit_p3_to_p4=((W-S)%p**4)//p**3))
payload=json.dumps(rows,sort_keys=True,separators=(",",":"))
digest=sha256(payload.encode()).hexdigest()
assert digest=="25192236d995db6b688d9ced7be7b3d85fd9c67d34de6bcdf155445f2e62d2bd"
assert {d["p"]:d["bridge_digit_p3_to_p4"] for d in rows}[13] == 11
assert {d["p"]:d["bridge_digit_p3_to_p4"] for d in rows}[373] == 114
print(len(rows), digest)
```

## 5. Canonical-continuation handoff — do NOT close or route around native work

- **Mother:** D25 SECOND-DIGIT-LIFT of accepted D24 supersingular UR/JT0, frozen scalar interface, p == 13/19 mod 24.
- **Immutable frontier consumed:** original source pin c47e13e4aba0e006366f989d6334d443f6333ae3; existing exact W_p-p relation; the p=373 native-experiment specification; all existing first/second-digit and E3 author notes remain independently attributed.
- **New author-side reusable fact:** published all-p S_p theorem together with the *proved logical equivalence* BRIDGE above, and exact p^4 sharpness witnesses. No claim the unknown bridge is proved.
- **Missing highest-priority evidence:** actual fixed-original H0/B0 divided-power [X]U mod 373^2, rank, semilinear Frobenius direction/normalization and signed kappa on the same genuine object; #1559 remains unowned, native NOT_EXECUTED.
- **Known Source lane state:** recovery_status at original request research-onhour-20261026-1403-recovery-r12 observed session MCP-de3e5bafb24f43f4a5e6285e7601676a ACTIVE but source_authority_verified=false and no own claim/run; dispatch research-onhour-20261026-1355-dispatch-r11 ultimately FAILED / TimeoutExpired; new read-only native continuation returned CONTROL_QUOTA. These observations grant no ownership, no reuse of maintenance identity.
- **Next exact action:** obtain authorized original H0/B0 native executor/source realization and run p=373 under #1559. For portable mathematics, seek an *actual, universal* p^3 transformation/telescoper proving BRIDGE with both summand families and p-dependent boundary defects, potentially adapting the cited q-microscope; a finite scan or the analytic 3/2 ratio is not proof. First check contemporary literature for prior exact bridge theorem.
- **Request/session/claim/run:** original recovery request research-onhour-20261026-1403-recovery-r12; old dispatch research-onhour-20261026-1355-dispatch-r11 CLOSED FAILED; Research session MCP-de3e5bafb24f43f4a5e6285e7601676a shown by its own read-only projection; valid current CLAIM=NONE VERIFIED, OPEN RUN=NONE VERIFIED; no new native write/release attempted.
- **Status:** AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED; NOT a canonical checkpoint, freeze, Result or independent mathematical review. D25 remains OPEN. No scheduler, notification, global policy or frozen source mutation.
