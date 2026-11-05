# Stage448-B — One-POP asymmetric future-observer quotient and polynomial BRC support

Date: 2026-11-05. Status: AUTHOR_SIDE_PROOF / EXACT_BIGINT_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Parent immutable source: `awdawmip/enterprise-math@0b804beb12f3515691c6e823ef48b70ba631880a`, Stage447-B.
Frozen scientific inputs: GLOBAL `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`; EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; original P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`.
Current normative overlays read separately from GLOBAL canonical main `994ad7ef9a8cf6e29c8d131387f6138534c873df` and EM main `4eecea0624c02fe0d395e14c04cd1b20443e549d`.
Researcher-ID: `EM-DIRECT-21C6E1`; Research-Activity-ID: `RA-5C1254A2BF7EA32D8838FA71`. Formal task owner/CLAIM unconfirmed; execution_authorized=false.

## Domain and exact future equivalence

Use the native X6 signed step set `D={±E1,...,±E6}`. Restrict *initial* ordered P,Q to `{A=+E1,B=-E1}`, with length `4<=m<n`, A endpoints, isolated internal Bs, fixed numbers `kP,kQ` of B and overlap mismatch count `d=m-K`. The current full observer `O=(m,n,V_P,V_Q,J_P,J_Q,K)` is fixed on this fiber; `J` is the complete directed native ordered-adjacency histogram. Q stays immutable; P can perform at most *one POP at any time* and at most `r>=1` APPENDs in any order; each APPEND accepts any of all twelve native directions. Each labelled action prefix produces a complete observation, including lengths.

Define `ell=min(r,n-m)`. Then the exact minimal future equivalence invariant on each fixed full-current-observation fiber is

`R_448(H) = (P_(m-1), Q_m, Q_(m+1),...,Q_(m+ell))`.

**Theorem 448.1.** For any two original histories H,H' in this declared fiber, all legal labelled future observation traces are equal if and only if `R_448(H)=R_448(H')`. Consequently the exact fixed-width quotient label uses `ceil(log2 q_F)` bits, where `q_F` is the number of supported distinct keys. No arbitrary initial histories or Q POP is claimed.

**Proof, sufficient direction.** Both initial P tails `P_m=A` are known, as are initial V and J. Before any POP the evolution of P under labelled APPENDs is known from O and those actions. A POP applied when an appended symbol is at the stack top removes a known labelled symbol and restores a known previous P state. If the single POP instead removes original `P_m=A`, the erased directed edge is `(P_(m-1),A)`, determined by R. The cross-source match count loses `[A=Q_m]`, also determined by R. Thereafter no POP is left; all new positions aligned against Q lie between m and `m+r-1`. Without original POP, they lie between `m+1` and `m+r`. Together, the possible previously hidden Q directions are `Q_m,...,Q_(m+ell)` and all other observer changes follow deterministically from the labelled action trace. Thus identical R and O give identical complete observations for every future prefix.

**Proof, necessary direction.** An initial POP of P removes the original edge `(P_(m-1),A)`; two distinct P_(m-1) directions remove different cells of the full J and are distinguished at the first POP observation. The same POP changes K by `-[A=Q_m]`; because Q_m is binary, unequal Q_m directions give unequal K immediately. Finally, if two keys differ first at `Q_(m+j)`, `1<=j<=ell`, use j APPENDs with final labelled direction equal to the first history's Q_(m+j). The difference in the K increment at j distinguishes them; earlier window coordinates match by first-difference choice. QED.

The one-POP model therefore adds exactly two repair coordinates to Stage447-B's APPEND-only output window: `P_(m-1)` and `Q_m`. Their roles are distinct: directed-edge removal and joint-match decrement respectively. This is an exact BRC observer-factorization result, not an unconditional lossless reconstruction of every original path.

## Positive-integer support, populations, and implicit rank

Set `s=number of Bs`. Compute integer prefix transfer `T(beta,q,b)`, the count of all length-m original paired prefixes whose P has kP defects, overlap mismatch d, Q prefix has b defects, previous P bit `beta=[P_(m-1)=B]`, and `q=[Q_m=B]`. Use states `(i,a,b,h,u,v)`: position, P/Q defect totals, mismatches, last P/Q defect flags. At final P_m=A, `u` from position m-1 records beta; Q_m is the last Q bit. Every legal source-pair prefix has one unique state path.

Let `w=Q_(m+1)...Q_(m+ell)` with B count s, first-bit f and last-bit v, no adjacent Bs; let `t=n-m-ell`. Let `U_t(v,R)` count length-t Q tails ending A, containing R Bs, and with no adjacent Bs across the previous-bit boundary v. For a fixed key `(beta,q,w)` the exact positive integer population is:

`M(beta,q,w) = [not(q=1 and f=1)] * sum_{b=0}^{kQ} T(beta,q,b) * U_t(v,kQ-b-s)`.

Its value depends only on `(beta,q,s,f,v)`, so the output-word automaton with states `(j,s,f,v)` counts all supported words by integer multiplicity without listing all words. Sum each word-state count if M>0 to obtain `q_F`, or multiply that word-state count by M to obtain the full original-history population `|F|`. This retains exact origin-specific populations, not only Boolean class support. Class lex ranking/unranking uses reverse word-state suffix-support counts for each beta,q; within-class original-history ranking/reconstruction uses an ordinary forced-window prefix/suffix integer DP.

With `H=4(kP+1)(kQ+1)(d+1)`, counting uses `O(mH+n(kQ+1)+(kQ+1)^2)` integer additions/multiply-adds and `O(H+n(kQ+1))` integer state storage (constant factors for beta,q). Each integer needs `O(m+n)` bits since it counts at most `2^(m+n)` binary history pairs. Account for arbitrary-precision multiplication bit cost; initial parsing and complete history recovery take Omega(m+n) time. The class encoding does not itself reconstruct a member without its within-class index.

## Strict two-boundary witnesses

Write A as 0, B as 1. Both examples have identical complete current O.

1. Q_m is necessary: m=4,n=5,kP=0,kQ=1,d=1, P=0000 for both; Q1=00010 and Q2=00100. The APPEND-only window Q5 is identical, but Q4 differs. A single POP changes K by one different unit.
2. P_(m-1) is necessary: m=4,n=5,kP=1,kQ=0,d=1; Q=00000 for both; P1=0010, P2=0100. The Q window, Q_m and original P_m are identical, yet a single POP removes an AB edge for P1 and an AA edge for P2, giving distinct complete J.

These show that replacing both repair coordinates by Stage447-B's output word loses future-observable information.

## Executed arithmetic and exact scope

The accompanying `STAGE448B.js` is an actually executed JavaScript BigInt standard-language verifier. Its `main()` return, exactly serialized into `STAGE448B_EXECUTED.json`, contains 424 parameter cases, 209 nonempty observation fibers, 2,123 enumerated histories and 530 direct integer class-population comparisons. For  small cases it enumerates every labelled POP/APPEND interleaving (one POP, two APPENDs, all 12 signed native options), calculating every prefix of the full six-dimensional endpoint, ordered J and K: 268,494 full future-tree evaluations and 1,340 history pairs. Equal-R paths yielded the same signature; different-R paths yielded distinct signatures in all cases tested. The independent exact DP matches direct enumerations for each nonempty fiber. The larger implicit calculation (m,n,kP,kQ,d,r)=(64,80,15,17,1,12) yields q_F=388 classes over 5,061,384,194,832,966 original histories, using 9,306 prefix transitions and without enumerating all histories or classes. Stage447-B without POP had q_F=188 on the same fiber. The general theorem follows from the argument above; the finite test checks implementation and representative future behaviour.

## Next

Stage449-B: allow one Q POP as well, with full interleavings. Determine which shifted alignment/equality bits and original terminal edges must be retained; seek polynomial exact support or an explicit noninterval-state obstruction. Retain the same frozen source pins, actual role constraints, and native 12-direction observer.
