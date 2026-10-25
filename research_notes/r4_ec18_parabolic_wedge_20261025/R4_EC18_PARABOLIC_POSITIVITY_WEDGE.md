# R4-EC18 — Exact parabolic strict-positivity wedge for palindromic BRC grade kernels

**2026-10-25 | Author-side mathematical proof | UNREVIEWED / NOT_ADMITTED**

**Model and source pins.** GLOBAL_KNOWLEDGE_V1 `main@294dccb155e0724f83f41ea113ea6f89cb8f6c5e`; EM current control Source `main@2c1ee0430d9addc6e6c34122311f3ef7b81ea050`; direct mathematical antecedents EC13 `387c93150bcf0c98f543d991471fbb27501dfd05` and EC17 `21b4d804272b563191b46eaee6c436515781f077`. Full local author proof and verifier package are provided separately. This is the *auxiliary positive ordered binary affine BRC*, not a P000-native X6/Heartbeat dynamical theorem. The output observer retains path depth n, grade j, and absence of literal 00; it does not preserve all future words or full affine provenance.

## Exact inherited identities

Grade-j sign words are in bijection with j-subsets of negative positions, so there are exactly `binom(n,j)` words, and the clean counts `C[n,j]` satisfy `0<=C[n,j]<=binom(n,j)`.

Let `Delta=1-(1+u)x+2u^2 x^4-u^3 x^6`. EC13/EC17 give the exact formal series

[
F(x,u)=sum_{n,j}C[n,j]x^nu^j
=rac{(1-ux^2)(1-ux^3)}{Delta},qquad
E(x,u)=rac{1-ux^2}{Delta}.
]

`E[n,j]=[x^n u^j]E` is palindromic and nonnegative. From `F=(1-ux^3)E` and the EC17 reflection formula,
[
E[n,j]=sum_{hge0}C[n-3h,j-h],qquad
D[n,k]:=C[n,n-k]-C[n,k]=E[n-3,k-1]-E[n-3,k-2].
]
Out-of-range coefficients are zero.

## Source-aware uniform lower bound

The exact EC13 eight-state transition analysis proves: conditional on j negative sign positions, outside event B (a negative in the first or last two positions, or three negatives spanning at most four positions), a BRC word is clean iff no two negative positions have separation 1 or 2. Since each pair of positions occurs with probability `j(j-1)/(n(n-1))` and there are `2n-3` forbidden pairs, the union bound for `n>=5,j>=2` gives
[
Pr(hbox{pair gap at most 2}) le rac{2j(j-1)}n.
]
The four boundary slots have total probability at most `4j/n`. There are at most `6n` triples spanning at most four, with union probability `6j(j-1)(j-2)/((n-1)(n-2))` (zero for j<3). Therefore
[
oxed{C[n,j]ge {nchoose j}(1-epsilon_{n,j}),quad
epsilon_{n,j}=rac{2j(j+1)}n+
rac{6j(j-1)(j-2)}{(n-1)(n-2)}.}	ag{1}
]
The inequality follows from the actual automaton, not a heuristic independence assumption.

## Upper bound at the preceding grade

Use positivity and `E=F/(1-ux^3)`:
[
E[n,j-1]=sum_{hge0}C[n-3h,j-1-h]
lesum_{h=0}^{j-1}{n-3hchoose j-1-h}.
]
For each valid h, the binomial numerator is at most `binom(n-h,j-1-h)`; dividing by `binom(n,j-1)` gives the exact falling-factorial ratio `(j-1)_{\underline h}/n_{\underline h}le((j-1)/n)^h`. Hence
[
oxed{E[n,j-1]le {nchoose j-1}igl(1-(j-1)/nigr)^{-1}.}	ag{2}
]

## Theorem EC18-W (all-depth strict quantitative positivity)

For every pair of integers `j>=1, n>=4j^2`,
[
oxed{E[n,j]-E[n,j-1]>rac{13}{99}{nchoose j-1}>0.}	ag{3}
]
Consequently for every `k>=2,n>=4(k-1)^2+3`,
[
oxed{D[n,k]>rac{13}{99}{n-3choose k-2}>0.}	ag{4}
]
For k=1, EC16 gives `D[n,1]=1` for n>=3.

**Proof.** For j=1, direct extraction yields `E[n,0]=1,E[n,1]=n-1` for n>=2; at n>=4 the difference is `n-2>=2>13/99`. For j=2, n>=16, equation (1) has epsilon=12/n<=3/4. Thus `E[n,2]>=C[n,2]>=(1/4)binom(n,2)` and after dividing by `binom(n,1)` its lower bound is `(n-1)/8>=15/8`. Equation (2) bounds `E[n,1]/binom(n,1)<=16/15`, giving margin at least `15/8-16/15=97/120>13/99`.

For j>=3 and n>=4j^2, 
[
rac{2j(j+1)}nlerac{j+1}{2j}lerac23,qquad
rac{6j(j-1)(j-2)}{(n-1)(n-2)}
<rac{6j^3}{9j^4}=rac{2}{3j}lerac29.
]
Thus `epsilon<8/9` and `E[n,j]>=C[n,j]>(1/9)binom(n,j)`. Moreover `binom(n,j)/binom(n,j-1)=(n-j+1)/j>11`, while `(1-(j-1)/n)^{-1}<=12/11`. Subtract (2):
[
E[n,j]-E[n,j-1] >
(rac{11}{9}-rac{12}{11}){nchoose j-1}
=rac{13}{99}{nchoose j-1}.
]
This proves (3) for all integers in the domain. Apply the exact reflection identity with `m=n-3,j=k-1` to prove (4). QED.

This proves strict first-difference positivity on the infinite wedge `j<=sqrt(n)/2`, not unimodality over the entire left half, which remains OPEN for `sqrt(n)/2<j<=floor(n/2)`.

## Exact falsification of a tempting stronger shortcut

EC17's exact recurrence gives `E[10,2]=23,E[10,3]=23,E[10,4]=25`. Hence
[
E[10,3]^2=529<575=E[10,2]E[10,4].
]
The family is not row-wise log-concave for all n>=10, so neither all-row log-concavity nor real-rootedness is available as an unproved shortcut to unimodality. The weaker unimodality conjecture is unaffected.

## Validation, status and next unit

A standalone exact-Python author checker computed 8,191 raw words of lengths 0..12, an independent source-clean automaton through depth 200, the symmetric E recurrence through depth 650, **5,212** strict wedge checks using exact rational arithmetic, **25,599** reflection-identity cells, and the n=10 nonlogconcavity witness. All passed. This finite validation is NOT the proof of universality; the proof is the two bounds and case split above. A leaner remote executable checker is stored alongside this note; full actually executed program and structured report are preserved in this run's local research package. Remote checker execution must not be inferred merely from storage.

**Activity:** `RA-EMR4-20261025-1645-EC18WEDGE`; self-labeled author `EMR4-LOCAL-20261025-EC18` (not a service-issued CLAIM). A separate native D25 continuation returned a formal no-claim route, but `prepare_exact` was refused `CANONICAL_REJECTED: TYPED_CONTINUATION_REQUIRED_FOR_PREDECESSOR`; this EC18 unit does not take over that formal task.

**Next EC19:** extend the inequality through the unresolved central wedge or exhibit one exact counterexample, using a grade-preserving finite cone/injection or a rigorously uniform transfer bound; do not infer original X6 or full-port future equivalence from grade data.
