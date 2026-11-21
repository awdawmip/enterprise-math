# CBRC F7 Driver r461 — exact rational B=11 finite-box minimax certificate

Date: 2026-11-22 (Asia/Taipei). Original model author: `EM-CBRCF7-83A1D4`. This new exact finite-box construction/verification: Driver `EM-DVR-DEBB5E` in shared nonblind context. Frozen Result `RR-AA38973D56330E59D315` is unchanged; no Native Review, Result admission, Task completion, or Foundation/Working Truth promotion is asserted.

## The original F7 model and quantified theorem

Let
[
A=I+uv^T,quad u=(1,1,-1,-1)^T,quad v=(1,-2,-1,2)^T.
]
The globally defined function `q: Z² -> [0,infinity)` must satisfy
[
q(0,0)=0,qquad q(-x,y)=q(x,y),qquad q(s,0)=1 (s
e0),
]
[
q(x,y)ge 	frac12quad ((x,y)
e(0,0)),qquad
q(2,1)=q(-1,-1)=	frac12.
]
For `z=(a,b,c,d)`, define
[
D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(a,b)-q(c,d).
]
For integer `B>=1`, put `E_B^* = inf_q max_{z in [-B,B]^4 intersect Z^4} |D_q(z)|`, where the infimum is over globally scalar-admissible functions, and **only the error inputs** are restricted to the finite box.

**Theorem (r461).** For every integer `1<=B<=11`,
[
oxed{E_B^*=	frac12.}
]
This extends the independently saved r460 exact theorem from `B<=8` to `B<=11`, preserving its original matrix, scalar assumptions and marks.

## Lower bound (symbolic)

Choose `z=(1,-1,0,0)`, which belongs to every input box with `B>=1`. Here `k=v^Tz=3` and `Az=(4,2,-3,-3)`. Hence
[
D_q(z)=q(4,2)+q(3,-3)-q(1,-1)-q(0,0)ge	frac12+	frac12-	frac12=	frac12
]
for every globally admissible `q`. Thus `E_B^*>=1/2`.

## Exact upper certificate (all 23^4 inputs)

The linked Python-standard-library-only certificate fixes `DEN=40` and encodes 1,924 distinct triples `(abs(x),y,n)`, `1<=n<=24`. Define a single global `q_*` by

* `40q_*(0,0)=0`, `40q_*(s,0)=40` for `s!=0`;
* `40q_*(2,1)=40q_*(1,-1)=20`, extending to negative first coordinates by `q_*(-x,y)=q_*(x,y)`;
* on the encoded 1,924 other canonical non-axis coordinate pairs set `40q_*(x,y)=20+n`;
* on **every remaining** non-axis nonzero integer pair set `40q_*(x,y)=20`.

This is a globally defined, rational-valued function obeying every F7 scalar condition, not a finite-domain-only partial assignment. The certificate's decoded raw triples have SHA256 `65ec618247976ac8e7624323e052ae5cf51619a10b673b4b58f652635ad82070`, checked by the standalone verifier. The compressed encoding is merely transport; no external data/solver is required for verification.

For each of the `23^4 = 279841` ordered tuples `(a,b,c,d) in {-11,...,11}^4`, the checker computes the **integer**
[
k=a-2b-c+2d,qquad
40D_{q_*}=40q_*(a+k,b+k)+40q_*(c-k,d-k)-40q_*(a,b)-40q_*(c,d).
]
It asserts `-20<=40D<=20` for **every** input, then checks the exact maximum `max |40D|=20`, with `4156` saturating inputs. The local execution completed with zero violations, using integer arithmetic and complete enumeration. Therefore `E_{11}^*<=1/2`, and nesting yields the upper bound for every `B<=11`. Combined with the symbolic lower bound, the theorem follows.

**Standalone exact witness and verifier:** [CBRC_F7_R461_BOX11_EXACT_RATIONAL_CERT_20261122.py](../..//research_checks/CBRC_F7_R461_BOX11_EXACT_RATIONAL_CERT_20261122.py).

## Discovery, scope, and current review boundary

For discovery only, an integer-grid feasibility model of the original F7 finite-box inequalities used variables `q=(20+n)/40`, `n>=0`, and ordinary mixed-integer optimization at `B=11`. Its floating-point solver results are **not** used as proof: the final explicit integer table and exhaustive independent exact arithmetic are the finite certificate. A `B=12` exploratory larger search did not return a feasibility or infeasibility certificate, so nothing is inferred about `E_{12}^*`.

The infinite-domain target is still open, with the inherited interval `1/2 <= E_infinity <= 4/7`. A finite `B=11` solution does not construct a uniform infinite-domain solution. This scientific proof is authored in the shared-context Driver research line and does not claim independent Native review of the original contributor's frozen Result. Current first-Review Source/DA and frozen manifest-integrity issues remain separate, with no permission or Result admission inferred from a GitHub publication.
