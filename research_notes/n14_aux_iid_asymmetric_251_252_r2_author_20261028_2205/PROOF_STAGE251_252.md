# Stage251–252: exact asymmetric sequential minimax values for N=11,12

**Date / provenance:** 2026-10-28. Portable author-side research. AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED. Continuation of Stage250 at immutable commit `50ccfad5c0052af422fff9a97854b05843f722ba` in Draft PR #1571. This is an **external ternary IID auxiliary problem**, not a P000 native X6 theorem.

## Statement

Under hypotheses P=(3,1,20)/24=(1/8,1/24,5/6) and Q=(2,2,20)/24=(1/12,1/12,5/6), let arbitrary full ordered-history randomized stopping/classification policies stop by integer horizon N. Write eP=Pr_P(decide Q), eQ=Pr_Q(decide P), tP=E_P(tau), tQ=E_Q(tau). Define V_N(a,b)=inf max(tP,tQ) over eP<=a and eQ<=b. **Theorems:** for a=3/10 and b=19/40,

- V_11 = **9981178986983/1729937295360** (approximately 5.769676747101933);
- V_12 = **4500007219693683431/814267306817003520** (approximately 5.526449584822892).

These equalities are for all randomized policies (including irrational coins) based on full ordered histories, not merely for count policies or rational coins.

## Exact sufficient-state lemma, restricted to four observables

At each ordered history h with count vector s=(i,j,k), all probabilities are positive and the likelihood ratio is Q(h)/P(h)=L(s)=(2/3)^i 2^j. Aggregate P-weighted action/continuation flows over all full ordered histories with the same s. Every corresponding Q mass equals L(s) times the P mass, and the successor factors are P_r or Q_r for the two measures. Normalizing P inflow yields an exact count-state randomized policy preserving (eP,eQ,tP,tQ) for the stated finite IID horizon. Every count policy is already an ordered-history policy. Thus optimizing the four outputs over full histories or counts gives exactly the same feasible observation set. This does **not** preserve unrelated path-dependent observers, native X6 dynamics, field structure, triadic constraints or future non-IID updates; a new factorization/bridge proof is needed for those.

BRC usage: this proof uses the positive-rational, P/Q source-labelled ordered branch masses, action labels, exact multiplicities and stop-depth observers before their declared sum, following the typed positive-weight carrier. The count quotient is made only after the preceding four-observer descent certificate. **REUSE_APPLIED**, not claimed execution of a native BRC tool or transfer to the native six-dimensional Enterprise coordinates.

## Universal Bellman lower bound

Fix K>0 and form J=tP+K(eP+eQ). P-normalized finite-horizon Bellman recursion is

```text
L(i,j,k)=(2/3)^i * 2^j
H_N(s)=min{
  K*L(s)                  [declare P],
  K                       [declare Q],
  1+sum_r P_r H_N(s+e_r) [continue only if |s|<N]
}
```

Finite backward induction over the count DAG proves H_N(0,0,0)=min J over the *full-history* policy class by the sufficient-state lemma. For any feasible policy,

```text
max(tP,tQ) >= tP >= H_N(0)-K*(3/10+19/40).
```

At N=11 the exact support is K=**3667352/54359**, H_11(0)=**381642144953761/6573761722368**. All **364** states (C(14,3)) were inspected with exact Fraction arithmetic. There are exactly two ties: A_11=(1,0,2) between declare P/continue, and B_11=(0,0,11) between declare P/declare Q. All remaining **648** action gaps are strictly positive.

At N=12 the exact support is K=**7416207288/112220771**, H_12(0)=**710830290256337191/12527189335646208**. All **455** states (C(15,3)) were inspected. The only ties are A_12=(1,0,1) between declare P/continue, and B_12=(0,0,12) between declare P/declare Q; the other **817** gaps are strictly positive.

For each horizon, the nontrivial tie at A determines K exactly: choose candidate successor actions by an explicitly rational affine-in-K backward pass, then equate the exact affine cost of continuing at A with K L(A). The separately evaluated Bellman recursion checks that the derived K globally supports all actions. The exact rational probe only identifies a candidate affine branch; no floating-point optimization or unproved probe assumption enters the certificate. The time-weight dual is **thetaP=1, thetaQ=0** at both horizons.

## Matching primal stopping rules

At A_N continue with independent probability x_N, otherwise declare P. At B_N declare P with independent probability y_N, otherwise Q. At every other state take its unique Bellman-minimizing action.

| N | A_N | B_N | x_N=Pr(continue at A_N) | y_N=Pr(declare P at B_N) |
| --- | --- | --- | --- | --- |
| 11 | (1,0,2) | (0,0,11) | **1571672/3218625** | **50828734113/111757812500** |
| 12 | (1,0,1) | (0,0,12) | **1564797113/11222077100** | **1121360544147507/3372018359375000** |

All four coin parameters lie strictly between 0 and 1. A and B cannot lie on one realized ordered path, since A requires a symbol-0 occurrence and B is an all-symbol-2 prefix. Hence the exact four-observer vector has no mixed x*y term: w(x,y)=w(0,0)+x[w(1,0)-w(0,0)]+y[w(0,1)-w(0,0)]. The verifier checks the (1,1) corner, derives the nonzero 2x2 error determinant and solves eP=3/10, eQ=19/40 to obtain exactly the displayed rational coins.

At N=11 the exact four-observer output is

```text
(eP,eQ,tP,tQ)=(3/10,19/40,
               9981178986983/1729937295360,
               3252255862529/576645765120).
tP-tQ=56102849849/432484323840 > 0.
```

At N=12 it is

```text
(eP,eQ,tP,tQ)=(3/10,19/40,
               4500007219693683431/814267306817003520,
               4465227036670939309/814267306817003520).
tP-tQ=17390091511372061/407133653408501760 > 0.
```

Because every chosen action is Bellman minimizing, tP+K(eP+eQ)=H_N(0), and both errors attain their caps. Since tP>tQ, max(tP,tQ)=tP=H_N(0)-K*(3/10+19/40). The primal exactly attains the **global full-history** lower bound, proving both stated values for the unrestricted randomized policy class.

## Executed verification and source scope

`STAGE251_252_EXACT_REPRO.py` uses only Python standard-library Fraction and functools; `RUN_STAGE251_252.txt` contains actual stdout. In addition to the full exact Bellman action checks and rational suffix-DP, it independently visits unmerged ordered-history prefixes, keeping P/Q positive rational branch weights separate and summing terminal errors/depths. Both terminal masses exactly equal one and all four outputs exactly match suffix-DP.

- Stage251 PASS: 364 states; 2 ties; 648 strict positive gaps; **637** unmerged DFS nodes; **429** terminal decision branches.
- Stage252 PASS: 455 states; 2 ties; 817 strict positive gaps; **472** unmerged DFS nodes; **318** terminal decision branches.
- Total ordered DFS nodes: **1109**. This is complete for the constructed finite policies; the all-policy mathematical conclusion follows from the exact Bellman dual/descent theorem, not an enumeration of all possible randomized policies.

Combining these two author-side proofs with the separately recorded Stage248–250 author-side results yields the entire **fixed-cap horizon classification**: N<=8 infeasible (Stage248); N9=65983208881/10195269120 (Stage249); N10=46306027119263/7618838952960 (Stage250); N11 and N12 as above; N>=13=27/5 (Stage248). Exact strict gaps: V10-V11=8060429786873375/26156997893302272; V11-V12=113325312271029278125/465923752960689414144; V12-27/5=102963762881864423/814267306817003520. Earlier results retain their actual independent-review and admission status; this corollary does not upgrade them.

**Source pins for this author phase:** GLOBAL_KNOWLEDGE_V1 canonical main c5547c717135d4d54d93d79fd47daecf9a9fb138; P000 original global blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc (matches the same-pin startup projection); Enterprise Math control main 9e83fc5d85159bf95cc51138e3da34a1843f0282. ACTIVE worldview, positive weighted BRC and joint-observer preservation contracts, and portable research protocol were read. Native gateway status currently reports research_authority_granted=false and quota 5/5; current owner was not confirmed. No native CLAIM, Source Result, independent Driver acceptance or native X6 correspondence is asserted.

## Next issue

Stage253: determine the exact nonzero-area rational region in the independent error caps (a,b) near (3/10,19/40) where the N12 dual support remains optimal and the two-coin policy remains feasible with tP>=tQ. Derive explicit affine x(a,b), y(a,b) and a polyhedral boundary, giving the full-real-variable formula V12(a,b)=H12(0)-K12*(a+b) on that region. This requires a separate parametric proof; see `NEXT_TASK_PACKET_253.md`.
