# Stage156 — exact full-real N14 auxiliary optimum and sharp right endpoint

**Evidence class:** AUTHOR exact-rational computation-assisted proof. Not a native CLAIM, Result, independently reviewed theorem, Lean proof, or P000/X6 transfer.

## Frozen inputs and mathematical problem

GLOBAL_KNOWLEDGE_V1 fixed at `awdawmip/chatgpt-global-knowledge@3505cfab9caffaef02ec55bebc3e549d9e4a8389`; both normative entry files, Enterprise Math task bootstrap, P000 startup projection and ACTIVE worldview read. Original P000 blob SHA-1 `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matches the projection. Enterprise Math research input fixed at `awdawmip/enterprise-math@10d464f045afb66b679418a1acb386a910228c4b`, including Stage155 author proof and `docs/PORTABLE_RESEARCH_PROTOCOL.md`.

We consider the EXTERNAL finite ternary iid experiment with at most 14 observations, P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6). The policy may randomize using the complete ordered history, and its observers are eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau). Define V14(alpha)=min max(tP,tQ) among policies with both errors <=alpha.

## Main theorem

Stage155 author's proved endpoint is
```
alpha155=7319074367111079265/21035720123168587776
V155=5285134557084071317/438244169232678912.
```

For **EVERY REAL** delta in [0, 40773875/876488338465357824],

```
V14(alpha155+delta) = V155 - (219224880/326191)*delta.
alpha156=7319074368089652265/21035720123168587776
V156=5285134543382516317/438244169232678912.
```

The Bellman support is strictly below the optimum to the right of alpha156: it cannot be extended while retaining equality.

## Proof 1: exact dual-ray closure and universal Bellman bound

At count-state s=(n,a,b), a and b count the first two symbols, so Q/P(s)=2^(a+b)/3^a. For K=L=k, set the exact backward value

```
H(s)=min{ k*(Q/P)(s) [decide P], k [decide Q],
          1+sum_i P_i H(child_i(s)) [continue when n<14] }.
```

At Stage155 k0=5736/17, the only ties are B=(11,0,1) Q/continue and T=(14,0,0) P/Q. Along k=k0-t for small t>0, the lexicographically first (value, right-derivative) minimizer selects Q at B and leaves T tied. Exactly enumerating every action gap as an affine function of t across all 680 count states proves the first positive closure is

```
t*=7620096/5545247;
k156=5736/17-t*=109612440/326191;
G=(10,5,4), decide Q / continue.
```

A fresh Fraction Bellman evaluation at k156 gives exactly two ties: G=(10,5,4) Q/continue and T=(14,0,0) P/Q. All remaining 1,238 nonminimal action gaps are strictly positive, minimum 4961/978573; zero negative gaps. The root dual value is

```
H(root)=8787882497416006214970643/35737825951544191746048.
```

Each arbitrary *ordered-history* randomized policy satisfies the Bellman lower bound

```
H(root) <= tP + k156*eP + k156*eQ
        <= max(tP,tQ) + 2*k156*alpha.
```

Thus V14(alpha)>=H(root)-2*k156*alpha globally, without restricting policies to count-state behavior.

## Proof 2: ordered BRC histories and exactly affine observers

Use the BRC method as a positive-rational, ordered-branch provenance carrier. Retain all ordered first-hit prefixes, multiplicity and separate P/Q weights before taking the iid-sufficient quotient. Literal integer-weight DFS under strict Bellman minimizing actions establishes:

| Tie | Actual ordered first-hit histories | P mass | Q mass |
|---|---:|---|---|
| G=(10,5,4) | 300 | 125/5435817984 | 125/2579890176 |
| T=(14,0,0) | 1 | 6103515625/78364164096 | 6103515625/78364164096 |

The cones are disjoint: G has 5 occurrences of the first and 4 of the second symbol, while T is the all-third-symbol terminal path; monotone counts forbid G reaching T, and terminal T cannot precede G. At each ordered G prefix, iid suffix laws and the P/Q prefix ratio agree, so history-specific G randomization may be averaged into one effective coin for precisely the four chosen observers, not for an unspecified native dynamics.

Let g=Prob(immediately decide Q at G), x=Prob(decide P at terminal T). Elsewhere choose the strict Bellman minimizer. All four observers form the exact affine vector

```
M(g,x)=(eP,eQ,tP,tQ)=M00+g*dG+x*dT

M00=(1220395839133721035/3505953353861431296,
     223259695416865/641959232274432,
     5285134557084071317/438244169232678912,
     619867207655561/53496602689536)
dG=(57875/66795331387392,
    -41375/53496602689536,
    -783125/25048249270272,
    -265625/4458050224128)
dT=(-6103515625/78364164096,
     6103515625/78364164096,
     0,0).
```

The mixed four-vector M11-M10-M01+M00 is exactly zero. TWO structurally different author implementations independently match all four deterministic corner vectors: conditional exact-rational suffix Bellman recursion and literal unmerged ordered prefix DFS with integer likelihood weights. DFS node counts at (g,x)=(0,0),(1,0),(0,1),(1,1) are respectively 473080,465880,473080,465880; all leaf probabilities separately sum to 1 under both P and Q.

## Proof 3: every real point is attainable

Exact equality eP=eQ gives

```
x(g)=660133538249389/327680000000000000
    +(3449577/327680000000000)*g.
```

For every real g in [0,1] this x(g) is strictly inside (0,1). At g=0 the common error and tP reproduce exactly alpha155,V155; at g=1,

```
eP=eQ=alpha156=7319074368089652265/21035720123168587776
tP=V156=5285134543382516317/438244169232678912
tQ=619867204468061/53496602689536.
```

The common error grows strictly affinely by 40773875/876488338465357824. The tP-tQ gaps at the two endpoints are

```
23020265774412845/48693796581408768 >0,
69060801460053535/146081389744226304 >0,
```

so tP>tQ for every real g by affinity. Both endpoints satisfy the exact dual equality tP+k156*(eP+eQ)=H(root). Affinity gives equality throughout and proves the full-real theorem and exact slope 2*k156=219224880/326191.

## Proof 4: strict right sharpness over all history policies

The finite-horizon ordered-history behavioral-policy cube is compact; every observer is continuous, hence the optimum is attained. Equality to the same support for any alpha>alpha156 would force both errors to equal alpha, tP>=tQ, and Bellman-minimal actions at every positive-mass reached history, since k156>0 and every other action gap is strictly positive. Only G and T remain. Complete-history-dependent randomization at all G prefixes yields the same four observers as a single effective g, because the iid-suffix distributions and P/Q prefix ratio agree. T is a single ordered history, and first-hit cones are disjoint. Hence any equality case has some (g,x) in [0,1]^2 and observations M(g,x). Equal errors force x=x(g), with common error strictly increasing in g; its maximal value is alpha156 at g=1. Contradiction. Thus the same affine support is strict to the right.

## Verifications, limitations and successor

The portable Python standard-library checker `VERIFY_STAGE156.py` performs full exact state/gap enumeration, both independent-structure author observer routes, integer first-hit masses, four deterministic corners, mixed-term identity, endpoint dominance and dual equalities. `certificate156.json` and `verification_stdout.txt` preserve the output of one actual local run. No remote execution or independent Research Driver review is claimed. A nonzero BRC-to-P000 native dynamics transfer is **not** established; this remains an EXTERNAL finite iid theorem.

After g saturates to 1, continue along K=L=k156-t. The exact first next closure is

```
t157=63783344160/3434465039,
K157=L157=3342600/10529,
J=(10,2,0), decide P / continue.
```

At the candidate, only J and T=(14,0,0) tie; the other 1,238 action gaps are strictly positive (minimum 232231247/11789784576). **Stage157 remains dual-only**, with no proved primal interval. The next task is in `NEXT_TASK_PACKET_157.md`.

GitHub authenticated actor: `awdawmip`. Native control task listing returned `CONTROL_QUOTA`; native RESEARCHER session start returned `STATIC_READONLY_SCOPE_DENIED`, operation_sent=false. Therefore current active native owner, formal researcher session, CLAIM, Result and independent review are unverified. GitHub source publication is author evidence, not native task admission.
