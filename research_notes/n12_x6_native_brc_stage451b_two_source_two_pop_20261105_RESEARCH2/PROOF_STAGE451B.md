# Stage451-B — both sources may POP twice: exact future quotient and grouped BRC counting

Date: 2026-11-05. Status: AUTHOR_SIDE_PROOF / EXECUTED_EXACT_INTEGER_TESTS / UNREVIEWED.

Parent Stage450-B: `d4add800abcce3e4325394405cb538d79ca9e97e`. Preserved scientific source pins: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current behavioral norms were independently refreshed. P000 uses native signed X6, and the initial A=+E1/B=-E1 family is embedded in X6; both future APPEND alphabets are the **full twelve native signed axes**.

## Model

Fix integers `3<=m<n`, `kP,kQ>=0`, and `d=m-K`. Let P and Q be ordered words of lengths m,n. Each starts/ends in A; B occurs only at mutually nonadjacent internal positions. Defect counts are kP and kQ. Work within one fixed complete initial observer fiber

`O=(m,n,Vp,Vq,Jp,Jq,K)`,

where V are complete six-component signed endpoints, J are complete directed native-adjacency histograms, and K counts equal letters at the same absolute position up to the shorter length.

Both sources permit **at most two POPs each** and nonnegative budgets `rP,rQ` of APPEND. An APPEND selects any of all 12 native signed directions. Operations may interleave in every legal way; POP of an appended direction spends the same POP budget. Compare the complete O observer *after every identical labeled operation prefix*, not merely the endpoint.

## Theorem 451.1 (exact future-equivalence repair)

Use one-based original indices and `h=min(n-1,m+rP)`. Define

`R451=(P[m-2],P[m-1],Q[n-2],Q[n-1],Q[m-1],Q[m],...,Q[h])`,

where an original Q coordinate appearing more than once is stored once.

For any two original histories H,H' in the same O fiber, and every finite `rP,rQ>=0`,

`H and H' have identical full observations under every legal labeled future prefix iff R451(H)=R451(H')`.

This is a fiberwise exact criterion. Coordinates constant within a particular fiber contribute no additional supported classes.

**Sufficiency.** The operation word alone determines which original direction prefixes survive and which appended labeled directions are present. Two POPs on P can remove only original edges `(P[m-1],A)`, `(P[m-2],P[m-1])`; two POPs on Q can remove only `(Q[n-1],A)`, `(Q[n-2],Q[n-1])`. Every other removed or inserted edge contains known appended labels. Therefore the six-component endpoints V and all directed J histograms are computable from initial O, the repair key and the operation sequence.

Both original prefixes through position `m-2` remain present in every future: P can lose at most two original letters, Q at most two and `n-2>=m-1`. Their joint hidden matching contribution is fixed by initial K after removing the two explicitly known indicators at positions m-1 and m. At indices above m-2, every surviving P letter is either P[m-1], original P[m]=A, or a labeled APPEND. Every Q letter that could be compared to P is in the visible original window `Q[m-1..h]`, the fixed original Q[n]=A, or a labeled APPEND; any additionally relevant terminal original Q letters are in Q[n-2],Q[n-1]. Since P's length never exceeds `m+rP`, K is computed exactly. This argument includes arbitrary POP/APPEND interleavings and both-source APPEND, establishing sufficiency.

**Necessity.** If P[m-1] differs, one P POP gives different P directed-edge histograms. If P[m-1] agrees but P[m-2] differs, two P POPs distinguish. Likewise one and then two Q POPs distinguish differences in Q[n-1] and Q[n-2]. After these four edge slots agree, differences at Q[m] or Q[m-1] are exposed by the loss of the corresponding match after one or two P POPs, because the P letters are then known. For `m<i<=h`, append `i-m` directions to P with the final appended direction chosen as one of the two differing Q[i] directions. At the first differing window position, the K increment differs. Thus every differing repair key has a legal distinguishing prefix. QED.

## Theorem 451.2 (polynomial-time exact support and positive integer BRC population)

Write `a=P[m-2], b=P[m-1], u=Q[n-2], v=Q[n-1]`. Let `W=Q[m-1..h]`, `c=W[0]=Q[m-1]`, `e=W[1]=Q[m]`, `t=W[last]`, and `s=#B(W)`.

Define `T(a,b,c,e,j)` as the **exact number** of original P/Q prefixes through m that meet P's total kP defects and d mismatch count, have those four prescribed slots, and have j Q defects. Define `Wcnt(c,e,s,t,u,v)` as the number of *distinct legal visible words W*, with forced u and v whenever their original positions lie inside W. Define `U(t,u,v,z)` as the number of legal Q suffix completions at indices h+1..n containing z defects, beginning after Q[h]=t, ending Q[n]=A, and satisfying prescribed Q[n-2]=u,Q[n-1]=v whenever those indices lie in the suffix.

For an exact supported repair key, its original-history population is

`M(a,b,u,v,W)=sum_j T(a,b,c,e,j)*U(t,u,v,kQ-j-(s-[c=B]-[e=B]))`,

with U=0 outside its domain. This formula follows from the unique split into paired prefix, prescribed visible middle, and Q-only suffix; every admissible original history is counted exactly once.

In particular M depends on W only through `(c,e,s,t)`, along with `(a,b,u,v)`. Hence

`qF = sum_(a,b,c,e,s,t,u,v) Wcnt(c,e,s,t,u,v) * [ M(a,b,u,v,W)>0 ]`

and `|F|=sum Wcnt*M`. These are distinct quantities: Boolean support, BRC positive integer population, and the ordered raw source pair.

Straight finite-state integer transfer for T,Wcnt,U, with fixed-width boundary letter bits, uses `O(m*(kP+1)*(kQ+1)*(d+1)+n*(kQ+1)+(kQ+1)^2)` exact integer operations, up to an absolute constant factor; working storage is polynomial. Every computed count is at most `2^(m+n)`, so its bit length is `O(m+n)`, and the bit-cost upper bound multiplies the integer-operation bound by the applicable `O(m+n)`-bit arithmetic cost. Reading raw input or reconstructing an original pair takes `Omega(m+n)` operations. For a specified key, conditional T and U transfers furnish lexicographic internal-history recovery without loss of provenance; global class ranking remains a next-stage implementation target.

## Concrete information-loss witness

Set `m=3,n=7,kP=0,kQ=1,d=0,rP=0` and consider:
- `P=AAA`, `Q1=AAABAAA`.
- `P=AAA`, `Q2=AAAABAA`.

They have the same original complete O and the same older Stage450 key `(P[m-2],P[m-1],Q[n-1],Q[m-1..m])`. But `Q1[n-2]=A` and `Q2[n-2]=B`. Execute Q:POP, Q:POP. Their Q directed-adjacency histograms now differ. The new coordinate Q[n-2] is genuinely necessary in this common fiber; the old key is insufficient for two Q POPs.

## Executed verification (2026-11-05)

Python 3 standard-library program `STAGE451B.py` and `STAGE451B_EXECUTED.json` are part of this checkpoint. The program (a) computes grouped transfer support/population, (b) independently generates all initial A/B defect histories and compares key classes for 3,782 parameter/fiber tests spanning 57,115 raw history instances, and (c) builds exact interned full future-operation trees, including all 12 native APPEND directions and legal interleavings, in 20 finite test fibers totaling 52,002 memoized future states. Tests passed.

Large example `(m,n,kP,kQ,d,rP)=(64,80,15,17,1,12)`: `qF=1,232`, `|F|=5,061,384,194,832,966`, 62 supported aggregate key descriptors; `h=76`. A shortest fixed-length support-class label uses 11 bits. Parent Stage450-B on the same parameters gave 1,046 classes. The large count comes from exact integer transfer; direct history enumeration was confined to the stated small test domains.

Status: mathematical author-side theorem and finite exact cross-check; independent Driver review and formal Source Result are separate project states.

## Next task

Stage452-B: allow P to POP three times and Q twice, or investigate a general `(pP,pQ)` formula; derive the needed exact joint-match window for arbitrary relative original lengths. Construct a shortest counterexample to the naive `pQ`-tail-only extension if it exists, and establish a genuinely budget-parametric polynomial count or a scoped complexity boundary. Continue preserving the same frozen science pins and the currently valid behavioral rules.
