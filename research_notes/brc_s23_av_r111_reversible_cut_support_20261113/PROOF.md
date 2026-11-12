# R111 — Persistent exact crossing-support index with reversible coalescence

Date: 2026-11-13 Asia/Shanghai. Status: author-side mathematical proof, executable exact tests; independent scientific review pending.
Scope: auxiliary rational directed-circle S23 (continuing R110 at Git commit \`af0e01f2c5bdc7df994a5092c518cda06016287b\`).
Frozen scientific input remains \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. This work makes no native Heartbeat-X6 embedding claim.

## Model and exact crossing set

Fix \(\sigma=(j,x,a,c)\), where \(j,a,c\in\mathbb Z\), \(x\in\mathbb Q\), a closed rational parameter interval \(I=[L,U]\), \(L<U\), and \(k\ge1\). A complete source identity is \((t,b)\in\mathbb Z^2\), ranked in descending lexicographic order. Let \(M_t(\theta)\) be the membership predicate from R110: the fractional part of \(x+(t-j)\theta\) lies on the positively directed half-open circular arc from \(\{a\theta\}\) to \(\{c\theta\}\); identical endpoints give the empty arc. Versions \(F,G\) are finite sets of complete identities.

For a source time \(t\), define \(K_t(I)\) as all *interior* rational solutions of integer-crossing equations in the six affine forms
\[
 a\theta,\quad c\theta,\quad (a-c)\theta,\quad
 x+(t-j)\theta,\quad x+(t-j-a)\theta,\quad x+(t-j-c)\theta.
\]
For a zero-slope form, omit its crossings: it is constant and cannot introduce isolated changes. The resulting \(K_t(I)\) is finite; duplicated crossing positions within a single time are counted once. Let
\[
S(F,G)=\{t:(t,b)\in F\cup G\text{ for some }b\},
\qquad n(q)=\#\{t\in S(F,G):q\in K_t(I)\}.
\]
The **generator-supported partition** is induced by \(C(F,G)=\{q:n(q)>0\}\), together with endpoints \(L,U\). It contains every cut singleton and each intervening open gap. Its crossings need not be the semantically minimal discontinuities; the definition gives a canonical sufficient cut set for the chosen six forms.

## R111.1 — Exact reversible cut transport

If exactly one complete identity \((s,b)\) is toggled in only F or only G, put \(S=S(F,G)\) before and \(S'=S(F',G')\) afterwards.

- When \(s\in S\cap S'\) (the time remains represented), \(n'=n\): the complete cut index is reused *without modification*, even though ranking and discrepancy identities may have changed.
- When \(s\notin S\) but \(s\in S'\), \(n'(q)=n(q)+1[q\in K_s(I)]\).
- When \(s\in S\) but \(s\notin S'\), \(n'(q)=n(q)-1[q\in K_s(I)]\).

Remove a crossing precisely when its new support count becomes zero. The new support-index set and every surviving point count are exactly the ones computed from scratch from \(S'\).

**Proof.** By definition \(n(q)\) is a finite sum of one indicator for each distinct active time. A one-identity toggle can change this summation index only through the first entrance or last departure of its time s. The three cases follow by subtraction of the sums. No information from other times is modified. Repeated additions and deletions preserve the invariant inductively, including arbitrary forks of immutable historical roots. QED.

## R111.2 — Sound coalescence and exact witness recovery

The parameter predicate \(M_t\), for each active \(t\in S'\), is constant on each open gap of the updated partition. At every cut singleton its exact half-open membership is separately evaluated. Therefore on each updated atom all eligibility predicates and all ordered Top-k outputs of F' and G' are constant; checking the exact singleton or a rational midpoint for each open gap is equivalent to checking all real \(\theta\in I\).

If deleting the last active identity at time s removes an interior crossing q because its support count becomes zero, all *remaining* \(M_t\) are constant across the merged open gap containing q. Merging the former adjacent open gaps and q's singleton is exact after the edit. If any updated atom violates the R108 rank-shield inequalities, its singleton or midpoint is an exact rational Top-k disagreement witness.

**Proof.** The six-affine crossing set contains every wrap or equality capable of changing a directed fractional-arc membership comparison. On a gap free of those crossings, the floor values and strict comparison signs are locally constant, so membership is constant. Every active time has all its crossings in the new support index. A formerly stored q with zero support is not a crossing of any remaining active time; the same argument extends across q. Top-k selection uses a fixed finite lexicographic identity order applied to those constant predicates. Finally apply the R108 pointwise rank-shield characterization. QED.

This proves **safe coalescence**, not that a stored margin for a removed time can be reused: the discrepancy-time row for the edited time and affected common-rank contributions must be updated according to R110 before certifying the new version.

## R111.3 — Persistent ordered-index implementation and cost

Maintain support counts in an immutable, path-copy AVL tree keyed by normalized exact rational numbers. For an event at s, insert, adjust, or delete each key in \(K_s(I)\). Retain the previous root so older historical versions remain independently queryable. A time-preserving branch edit directly reuses the old tree root.

Let \(N\) be the current number of distinct supported interior cuts and \(r=|K_s(I)|\). A single time-entry/exit costs \(O(r\log(N+r+1))\) *rational comparisons and tree-node allocations* in a persistent AVL representation. Additional costs include enumerating the r candidate cut values (which may dominate for high-frequency time parameters), arbitrary-precision arithmetic and comparing rational numerators/denominators. This bound concerns the ordered crossing index, not total history/source-set copying or construction of all Top-k margins.

For affine \(m\theta+d\) with integer nonzero slope m and rational d, its next integer crossing strictly after q is
\[
\mathrm{Next}_{m,d}(q)=
\begin{cases}
(\lfloor mq+d\rfloor+1-d)/m,&m>0,\\
(\lceil mq+d\rceil-1-d)/m,&m<0.
\end{cases}
\]
The minimum of six such next crossings gives an exact output-sensitive \(K_s(I)\) iterator. A local query window J may use \(K_s(J)\) rather than a full global period. For an explicit full-interval list with N supported cuts, exactly \(2N+3\) point/gap atoms arise when L<U; the enumeration of those atoms requires \(\Omega(N)\) output work, whereas point queries can use a balanced-key predecessor/successor traversal.

## Reproduction and evidence

The attached self-contained JavaScript program \`check_r111.mjs\` uses exact rational arithmetic from native BigInt (no floating-point values in eligibility, cut coordinates or comparisons). Run \`node check_r111.mjs\` with a modern Node.js runtime. A deterministic seeded test suite tests 510 one-sided branch edits in 3 independently seeded histories, randomly forks earlier immutable roots, compares every incremental AVL support count to a full regeneration, verifies AVL invariants, checks each cut singleton and gap midpoint for k=1,2,3 against both independent direct Top-k sorting and the R108 shield criterion, and validates exact forward-crossing streams for t=-9..9. Test model is \(I=[0,1]\), \(j=0,x=1/4,a=0,c=1\), source times -4..4 and branch labels 0..3 (additional stream checks use -9..9).

Validation is finite executable evidence for the algorithm and the stated example range; the general statement rests on the set-sum and phase-cut proofs above. The persistence implementation shares AVL nodes but copies JavaScript Set objects for F,G, so the reported index-complexity bound is not a whole-program runtime claim.

## Next frontier R112

Combine the event-support AVL index with a lazy, versioned rank-shield margin index so that edits visit only affected time buckets and required local windows; derive explicit bit-operation, memory, and witness-recovery cost models. Compare sparse-window versus full-interval queries, first/last-time edits versus branch-only edits, and the zero-phase certificates from R108. Preserve full source/branch identity and distinguish auxiliary S23 parameters from Heartbeat native time and X6 coordinates.
