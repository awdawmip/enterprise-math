# Stage452-B — three P POPs and two Q POPs: exact X6 future observer quotient

Date: 2026-11-05. Status: AUTHOR_SIDE_MATHEMATICAL_PROOF / FINITE_EXACT_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Scientific frozen pins: global `bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, EM `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 original blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current rules read from canonical main independently. This is an A/B (`A=+E1,B=-E1`) **initial-word submodel** of native signed X6, with *all twelve* signed X6 directions available for future APPEND.

## Precise domain and observer

Fix `4<=m<n`, nonnegative integer defect numbers `kP,kQ`, and integer `d=m-K`. Initial P,Q are ordered words of lengths m,n, start/end in A, and have exactly the specified numbers of nonadjacent *internal* B occurrences. Fix the entire common initial observer fiber `O=(m,n,Vp,Vq,Jp,Jq,K)`, where V are six-component signed endpoint vectors, J are complete 12x12 **directed** adjacency multiplicities, and K is absolute-index equality for positions up to `min(lengthP,lengthQ)`.

Future action labels are P:POP, Q:POP, P:APPEND(z), Q:APPEND(z), `z` one of twelve signed X6 directions. At most three P POPs, two Q POPs and respectively `rP,rQ>=0` APPENDs are legal in any interleaving; popping an appended step consumes a POP. Compare full O after **every** identically labeled legal operation prefix. Empty-word POP is illegal. No future dynamics or physical-law claim is made.

## Theorem 452.1 (exact fiberwise future-equivalence repair)

Let `h=min(n-1,m+rP)`. The ordered repair key, with any repeated indexed coordinate stored once, is

\[
R_{452}(P,Q)=\big(P_{m-3},P_{m-2},P_{m-1};
Q_{n-2},Q_{n-1};
Q_{m-2},Q_{m-1},\ldots,Q_h\big).
\]

For every two initial histories H,H' in the fixed initial O fiber, and for **all** nonnegative rP,rQ,

\[
H\sim_{3,2,rP,rQ}H'\quad\Longleftrightarrow\quad R_{452}(H)=R_{452}(H').
\]

**Sufficiency.** Every operation sequence uniquely specifies which original prefixes remain and all appended labeled steps, even when APPEND and POP interleave. At most three original P letters and two original Q letters can be removed. Thus the common original indices 1 through `m-3` always remain: `n-2 >= m-1 > m-3`. Their matching contribution is the original K minus the *initially known* indicators at m-2,m-1,m, all computable from P's saved last three predecessor directions, the fixed P[m]=A, and Q[m-2..m] in the key. All subsequent matched original Q letters are in `Q[m-2..h]`, or at Q[n]=A, or are explicitly appended labels. P's remaining original letters beyond m-3 are `P[m-2],P[m-1],P[m]=A`; any later P letters are explicit appended labels. So K after every future prefix is determined by (initial O,key,operation prefix). Every original P edge that can be deleted has predecessor in `P[m-3..m-1]` and the fixed P[m]=A; every original Q edge that can be deleted has predecessor in `Q[n-2..n-1]` and fixed Q[n]=A. All other new/deleted edges involve known appended labels. Consequently both six-component endpoints and both complete directed J arrays are determined.

**Necessity.** Full future equality gives the original O. Comparing directed J after one, two and three consecutive P POPs successively recovers `P[m-1],P[m-2],P[m-3]`, because each newly deleted directed edge is known once the previous predecessor is recovered. Analogously two consecutive Q POPs recover `Q[n-1],Q[n-2]`. Differences of the K observations before and after the first, second and third consecutive P POPs recover, successively, the indicators `[P[m]=Q[m]], [P[m-1]=Q[m-1]], [P[m-2]=Q[m-2]]`; the P symbols are now known, and each Q symbol is in {A,B}, so this identifies `Q[m],Q[m-1],Q[m-2]`. For every index `m<i<=h`, APPEND `i-m` steps to P (no POP needed). For the final step, choosing A and reading the incremental K determines whether `Q[i]=A` or B; all earlier added letters cancel in the last increment. Hence the exact Q window is recoverable. This works even for rP=0 and arbitrary Q APPEND budgets. QED.

A boundary coordinate that is constant in the chosen fiber generates no extra supported class; equivalence is stated as equality of full indexed keys, not as a universal assertion that every bit is variable in every fiber.

## Theorem 452.2 (grouped exact integer support and BRC population)

For fixed P predecessor triple `a=P[m-3],b=P[m-2],c=P[m-1]`, Q paired triple `x=Q[m-2],y=Q[m-1],z=Q[m]`, and Q terminal pair `u=Q[n-2],v=Q[n-1]`, define the integer paired-prefix transfer `T(a,b,c,x,y,z;j)`. It counts all P/Q original prefixes through m consistent with these slots, full prescribed P defect total, the prescribed mismatch total d, and j Q defects in positions 1..m. It is computed by left-to-right transfer with state `(index, P_defects, Q_defects, mismatches, lastP, lastQ)` and forced boundary letters; all transitions add nonnegative integers.

Let W denote the *individual indexed Q word* from m+1 to h, and `s=#B(W)`, `t=Q[h]` (when h=m, W is empty, s=0 and t=z). `C(x,y,z,u,v;s,t)` counts distinct admissible W of this aggregate, enforcing the prescribed Q terminal slots whenever they occur in W and enforcing B nonadjacency against z. Let `U(t,u,v;zeta)` count admissible original Q suffix completions h+1..n with exactly zeta B defects, with ending Q[n]=A and terminal slots u,v enforced whenever those slots occur in the suffix. Because Q[m-2..m] lies in the paired prefix, overlaps are checked for consistency exactly once.

The **population of every individual** supported key with these aggregates is
\[
M(a,b,c,u,v,W)=\sum_{j=0}^{k_Q}
 T(a,b,c,x,y,z;j)\,U(t,u,v;k_Q-j-s).
\]
For incompatible overlap assignments set M=0. In particular M depends on W only through its first three prescribed symbols, its total B count s, and its last symbol t. Therefore

\[
q_F=\sum_{a,b,c,x,y,z,u,v,s,t} C(x,y,z,u,v;s,t)\,[M>0],\qquad
|F|=\sum C\,M.
\]
The sums include only compatible boundary assignments. The count `C` counts different keys, while M counts raw ordered provenance-preserving histories *inside* one key. This is the Boolean-support/positive-integer-population distinction used by BRC; no signed cancellation is introduced.

All transfers use integer additions and a final nonnegative convolution. The number of boundary bits is constant (three P, three Q paired, two Q terminal, last W); each transfer has polynomially many indices/counters bounded by N=max(m,n), and each exact count needs at most O(m+n) bits. A conservative implementation bound for grouped support and total population is O(N^5) arbitrary-precision integer operations and polynomial memory, without explicitly listing q_F keys. Enumerating all keys or returning their individual populations has an unavoidable output-size cost. This bound is for the described grouped transfer; the attached executable finite checker verifies the *classification* on small fibers and does not benchmark that grouped large-N implementation.

## A general, not necessarily minimal, sufficient repair for arbitrary budgets

For any nonnegative pP,pQ (POP always conditioned on legal nonempty words) set
\[
c=\min(\max(0,m-p_P),\max(0,n-p_Q)).
\]
Store the original predecessor tails `P[max(1,m-pP)..m-1]`, `Q[max(1,n-pQ)..n-1]`, and the indexed cross-match exposure windows
\[
P_{c+1..\min(m,n+r_Q)},\qquad Q_{c+1..\min(n,m+r_P)}.
\]
Retain initial O and the literal indexed directions, coalescing duplicates. This **suffices** to reconstruct the full observer after every admissible interleaved future operation: the original joint prefix through c always survives, its aggregate K is obtained by subtracting the known exposed matches from original K, and every comparison beyond c plus every original edge deletion is determined by the stored coordinates. For arbitrary budgets this is a finite exact *sufficient* key; minimality and a uniformly small representation are separate questions. When `pP=3,pQ=2,m<n` it reduces, after fixed A endpoints and duplicate removal, to the key in Theorem 452.1.

## Concrete minimality witnesses against Stage451 key

(1) New cross-source direction `Q[m-2]`: let m=6,n=10, P=`AAAAAA`. Set Q1 to ten A's except B at one-based position 4, Q2 to ten A's except B at position 2. Both have kP=0,kQ=1,d=1, equal full initial O, equal Stage451 key and distinct R452. Three P POPs leave K=3 and K=2 respectively. Thus `Q[m-2]` is observable and cannot generally be omitted.

(2) New P predecessor `P[m-3]`: let m=7,n=10, Q=`AAAAAAAAAA`. Let P1 be seven A's except B at one-based position 4, P2 be seven A's except B at position 2. Both have kP=1,kQ=0,d=1, equal full initial O, equal Stage451 key and distinct R452. Three P POPs produce distinct P directed adjacency histograms: one contains A->A:2 and A->B:1, the other A->A:1,A->B:1,B->A:1. Thus the third predecessor is genuinely visible.

## Executed finite crosscheck

Executed the self-contained standard JavaScript verifier `STAGE452B.js` (no external libraries, exact integer labels) and saved the actual JSON output. It independently enumerates 8 fixed parameter configurations, 26 nonempty fixed-O fibers, 243 source-distinct initial history pairs, and 1,804 unordered pair comparisons. For every history it recursively interns the entire labeled legal operation tree using all 12 signed X6 APPEND labels and all POP/APPEND interleavings; 28,059 memoized future states and 16,173 different observation-subtree signatures. Repair-key equality and full-future-signature equality agree for every tested pair. Both minimality witnesses pass. Test budgets are pP=3,pQ=2, rP,rQ in {0,1}, with precise m,n,kP,kQ values in the executed JSON. This finite test is a crosscheck, not the logical basis of the general theorem.

## Next exact open unit

Stage453-B: construct a minimal key and grouped exact-support integer transfer for arbitrary (pP,pQ) even when `n-pQ < m-pP`; test the new P-side cross-alignment window and give the shortest small-fiber witness to any proposed omission. Preserve the same original science pins and current normative routes. Independent review and formal Source Result remain distinct from this author-side proof.
