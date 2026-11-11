# R5 — Symmetry-protected degeneracy strata of sharp four-circuit rays

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact theorem with exhaustive integer verifier. Scope: frozen seven-target P/Q–BRC Blackwell **observer** model; counterfactual parameter families used only to prove structural stability, without changing any frozen inputs or P000.

Frozen scientific provenance: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`, following the immutable scientific pins declared in [PR #2045](https://github.com/awdawmip/enterprise-math/pull/2045). Reuse resolution: REUSE_APPLIED for [PR #2017](https://github.com/awdawmip/enterprise-math/pull/2017) (six-arc K2,3 circuits), [PR #2043](https://github.com/awdawmip/enterprise-math/pull/2043) (sharp length-four bound), and PR #2045 (K4+double-edge criterion and frozen 14832 census).

## Carrier, observer, local question

Carrier = signed, target-labeled source/target branch differences; observer = marginal and first-likelihood-ratio moments C; operation = exact kernel repair, K2,3 decomposition, and adjacency in nonnegative transfer fiber F_b={E>=0:CE=b}. The observer erases joint branch incidence. The signed residual is not positive transfer mass.

The K4-plus-one-high/high-double-edge structure has four source ports J={1,2,3,5}, two low-degree ports and two high-degree ports, seven different target labels, and seven paired undirected incidence edges A=pq, B=ph, C=pk, D=qh, E=qk, F=hk, G=hk, each yielding two directed nonzero transfer differences. There are C(4,2)*7!/2=15120 labeled candidate assignments.

Write the seven **ratio numerators** on (A,B,C,D,E,F,G) as (a,b,c,d,e,f,g). Define
```
uA=(b-c)*(d-e)
uB=(c-a)*(d-e)
uC=(a-b)*(d-e)
uD=-(b-c)*(e-a)
uE=-(b-c)*(a-d)
Delta=g-f
vF=-uB*(b-g)-uD*(d-g)
vG=-uB*(f-b)-uD*(f-d)
```
The unique kernel flow up to scalar is (Delta*uA, Delta*uB, Delta*uC, Delta*uD, Delta*uE, vF, vG). Source zero-mass and first-moment equations and opposite target flows follow by substitution. Distinct target ratios force the first five coefficients nonzero. The two remaining coefficients cannot both vanish: subtract their two linear equations (at f and g), using f!=g and b!=d, to obtain uB=uD=0, a contradiction. Every degeneracy therefore removes exactly the *two* arcs of one doubled edge, changing a 14-arc circuit to a 12-arc residual.

## Theorem A — universal central-symmetry-protected family

Let seven target ratios be pairwise distinct and centrally symmetric about m, labeled (m-x3,m-x2,m-x1,m,m+x1,m+x2,m+x3) with 0<x1<x2<x3. Exactly **288 specific assignments** lose the pair with central target label 3, for every such spectrum; their structural recipe is:

Choose the low-degree source pair (6 choices); choose noncentral label A=a (6 choices); put {F,G}={m,2m-a}; among the remaining two mirror pairs choose B=b (4 choices) and D=d in the other mirror pair (2 choices), and set E=2m-b, C=2m-d. These are 6*6*4*2=288 distinct assignments; each loses precisely the central-label doubled edge.

**Proof.** With f=m, g=2m-a, d=2m-c and e=2m-b, the above formulas reduce to
```
uB=(c-a)*(b-c)
uD=(b-c)*(a+b-2*m)
b-g=a+b-2*m
d-g=a-c
vF=-(b-c)*(c-a)*(a+b-2*m)
   -(b-c)*(a+b-2*m)*(a-c) = 0.
```
All noncentral labels are distinct and B,C lie in different mirror pairs, so the remaining high/high flow vG is nonzero. The general no-simultaneous-zero lemma also proves uniqueness. Counting yields 288. QED.

## Theorem B — generic centrally symmetric census

For all centrally symmetric ratio tuples outside finitely many **proper algebraic hypersurfaces** in the open domain 0<x1<x2<x3, the 288 symmetry identities of Theorem A are the **only** degeneracies. Hence exactly 14832 of the 15120 assignments are full 14-arc K4+double-edge circuits.

**Proof.** The double-edge coefficients for each assignment are polynomials in the three gaps. Every nonforced assignment is witnessed nonzero at the frozen exact tuple
```
(2,10,15,20,25,30,38)=20+(-18,-10,-5,0,5,10,18).
```
The accompanying executable exact finite verification checks all 15120 assignments, finding precisely the 288 forced cases and no others. Therefore every other polynomial is nonzero as a polynomial; its zero set is proper. The complement of the finite union of these zero loci is Zariski open and dense. QED.

## Theorem C — arithmetic-progression resonance and affine invariance

Every **seven-term arithmetic progression of distinct target ratios** has 864 degeneracies and 14256 full 14-arc circuits; 288 degeneracies are symmetry-forced, and 576 are additional special-ratio resonances.

**Proof.** Each *actual* paired flow coefficient (Delta*uA through Delta*uE, and vF,vG) is homogeneous of degree 3 in differences of the target ratios. A common affine replacement r->alpha*r+beta (alpha!=0) therefore multiplies every flow by alpha^3 and preserves its zero pattern. All seven-term arithmetic progressions have the same census as the positive reference (1,2,3,4,5,6,7). The exact finite verifier checks 864 degeneracies at that reference, locating 288 each at labels 0,3,6. QED.

## Theorem D — generic nonsymmetric spectra

Outside a finite union of proper algebraic hypersurfaces in the **unrestricted seven-parameter** distinct-ratio domain, all 15120 assignments are full circuits (zero degeneracies).

**Proof.** The vF/vG for all assignments are finitely many nonzero polynomial expressions in seven independent ratios; an explicit common witness is the strictly positive distinct tuple (1,2,4,8,13,21,32), for which the exhaustive exact verifier finds neither coefficient zero in any assignment. QED.

## Exact verification and numerical meaning

Command: `python3 VERIFY_SYMMETRY_DEGENERACY.py`. Only Python 3 standard library and **exact integers** are used; zero tests and the completeness of the 6*2520 assignment enumeration are exact. Each assignment is checked for four zero row sums and four zero first moments. The actual observed record is in `EXACT_OUTPUT.txt`.

| Spectrum | Full 14-arc | Degenerate | Symmetry-forced | Extra |
|---|---:|---:|---:|---:|
| frozen (2,10,15,20,25,30,38) | 14832 | 288 | 288 | 0 |
| arithmetic progression (1,2,3,4,5,6,7) | 14256 | 864 | 288 | 576 |
| nonsymmetric (1,2,4,8,13,21,32) | 15120 | 0 | 0 | 0 |

Terminal marker: `PASS_EXACT_R5_SYMMETRY_PROTECTED_288_AND_DISCRIMINANT_STRATA`.

Generic statements use separate algebraic nonvanishing arguments rather than extrapolating from a numerical sample. The 288 protected degeneracies are observer-kernel identities, not physical-observer fiber edge counts. The hypothetical spectra are analytical counterfactuals; they do **not** rebase the frozen science. P000 remains locked.

## Next concrete research unit

Use the exact *pinned physical witness* from PR #2017/#2021 to test which of the 14832 full-support candidate circuits actually form edges of **that single** legally fixed physical observer fiber: for every candidate, solve fixed-right-hand-side linear equations CE=b with support restricted to that circuit, then rational nonnegative feasibility and endpoints. Deduplicate endpoints and count actual incidence. Record a feasible rational witness or infeasibility certificate per orbit. Another useful continuation is factoring the exceptional discriminant hypersurfaces in mirror-gap variables to classify resonances beyond central symmetry (the arithmetic-progression stratum supplies an explicit second case).

Status: verified author-side exact proof+finite calculation; no new immutable R5 CLAIM, formal Source Result, independent review or changed source authority asserted.