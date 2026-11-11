# R82 — Persistent dual-index separation of source-time GCD and absolute phase groups

Status: exact mathematical result and author-side validation in the **auxiliary rational circular-source observer** only. Source predecessor R81: 1d7e851e4caa3d4319fb8f574a2900df6fd0e23f (research_notes/brc_s23_av_persistent_observer_gcd_20261111_r81/PROOF.md). Frozen original S23/AV science pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged). Not a heartbeat/native BRC theorem, formal shared CLAIM, Result, independent review or P000 update.

## Exact definitions

Let E be a finite set of independent source identities (t,branch), t an integer. Fix integer observer time j, integer original labels a,b, rational observer phase x, real parameter theta. Set A(theta)=fractional_part(a theta), B(theta)=fractional_part(b theta), S_t(theta)=fractional_part(x+(t-j)theta). Target membership uses the directed half-open circular arc from A to B, with lower endpoint included and upper excluded; when A=B the target is empty. If A>B it wraps through zero. W_E(theta) is the lexicographically greatest qualifying (t,branch), or NONE.

Define g(E,j,a,b)=gcd(|a|,|b|, {|t-j| : (t,branch) in E}), with the empty-source definition gcd(|a|,|b|). R81 proves that if tau is the smallest distinct time and D(E) the gcd of consecutive gaps among sorted distinct times (zero for a singleton), then g=gcd(|a|,|b|,D(E),|tau-j|). For g>0, shift theta by 1/g preserves every labelled phase and W_E.

Independently choose a fixed reduced rational anchor theta0=p/q, q>0. Group identities by their **absolute raw** residue r_t=tp mod q into exact classes C_r. The class index depends on times and the anchor, not on g, observer j, or original label values.

## Theorem A: fully persistent three-index representation

Maintain (1) an immutable augmented AVL T keyed by each distinct integer time and storing its branch set, subtree time minima/maxima, gap gcd and counts; (2) an immutable outer AVL P keyed by residue r with each payload a persistent per-class time/branch AVL; and (3) an immutable ordered AVL M holding one key (max_time(C_r),r) per nonempty class.

Insert or delete one identity (t,branch). Exactly one class r=tp mod q changes. Every other class's inner AVL root is identical by object identity to its previous root, regardless of the new global g. M changes only when that class's maximum time changes; an unchanged maximum retains M itself. Every old version retains its precise source identities, extrema, class groups, gap gcd and M.

Proof: a sorted time subtree's adjacent gaps consist of left gaps, an optional gap from max(left) to t, an optional gap t to min(right), and right gaps. Therefore its exact gap summary is gcd(G_left,G_right,t-max(left) if left,min(right)-t if right). Structural induction and local recalculation after AVL rotations preserve the summary. For phase grouping, residue depends only on unchanged t and fixed p/q; path-copy insertion can affect only one inner group. The M key set is exactly the class maxima, so conditional deletion/reinsertion maintains it. Path copying never mutates an old root. QED.

With m distinct global times, h nonempty classes and m_r distinct times in the affected class, this construction visits O(log(m+1)+log(h+1)+log(m_r+1)) AVL nodes for the time/class indexes, and at most two O(log(h+1)) max-index edits. The Python demonstration copies branch sets and can incur O(b_t) for b_t branches at a changed time. Each visited time node also performs exact gcd arithmetic with nonconstant integer bit cost. Persistent live storage is proportional to retained identities and class/index keys; historical updates allocate touched paths and branch-set copies. This is not a generic constant-bit-time assertion.

## Theorem B: lazy normalization under GCD changes

For a fixed source version with g>0, set eta=g theta. Because g divides a,b and every (t-j), we have the exact, all-real identities:

  fractional_part(a theta)=fractional_part((a/g)eta)
  fractional_part(b theta)=fractional_part((b/g)eta)
  fractional_part(x+(t-j)theta)=fractional_part(x+((t-j)/g)eta).

The same circular half-open membership and the same lexicographic winner therefore result. On changing g, compute the new divisor from the global T summary at query time and generate reduced slopes only for visited candidates. There is **no requirement to rewrite all retained raw source identities or rebuild P after a one-identity update**. This avoids a potentially linear eager normalization rewrite, not necessarily a linear query or certificate cost. For g=0, the positive-period and division formulation is not invoked.

## Theorem C: raw-phase group certificates are invariant under unrelated GCD changes

Fix the same original-coordinate query signature (theta0,j,a,b,x,I), where I=[L,U] is a rational closed interval containing theta0 and the target original arc is nonempty, nonwrapping, with constant boundary floors on I. For one unchanged class root, the R71 exact sufficient exclusion applies without reference to global g.

Indeed, for r=tp mod q, beta_r=fractional_part(r/q+x-j theta0), and for every t in class r,

  S_t(theta)=fractional_part(beta_r+(t-j)(theta-theta0)).

The four products from d in [t_min-j,t_max-j] and delta in [L-theta0,U-theta0] bound the complete lifted class phases in [s_-,s_+]. With boundary floors k_a,k_b constant, let q_-=min(aL-k_a,aU-k_a) and q_+=max(bL-k_b,bU-k_b). If

  ceil(s_--q_+) > floor(s_+-q_-),

then there is no integer translate of the closed phase envelope meeting the closed target envelope. Consequently, NO source in this class can qualify for ANY real theta in I. Unchanged class root and query signature preserve the proof verbatim even if global g changes. This does not license copying an entire old-version winner result without checking changed/new classes.

## Infinite exact separation family

For every integer N>=1 choose theta0=1/16, a=4, b=8, j=x=0, and

  E_N={(16k,0),(16k-4,1): 1<=k<=N},
  I_N=[1/16-1/(1000N),1/16+1/(1000N)].

There are 2N sources but only two classes r=0,12. Global g=4. Across I_N, target boundary phases are approximately [1/4,1/2] and never wrap; group-0 lifts lie in [-0.016,0.016] and group-12 lifts in [0.734,0.766]. Each satisfies the exact integer exclusion condition, so W_E(theta)=NONE throughout I_N.

Insert e*=(16N+5,2). The new divisor is g=1, all 2N old normalized nonzero slopes change from t/4 to t, and a third phase class r=5 appears. BOTH old immutable class roots and both old all-interval exclusion certificates survive. At theta0, S_e*=5/16 is inside [1/4,1/2), and e* has the greatest time; hence W_new(theta0)=e* rather than NONE. This simultaneously exhibits a linear eager table rewrite, logarithmic path-copy updates, safe per-class certificate reuse, and the failure of whole-winner certificate reuse. It proves the claimed local separation only.

## Executed exact verification

Full local immutable Python AVL checker: seed 8220261112, 722 effective random insert/delete updates, 2166 historical-version reconstruction checks, 8664 direct-GCD matches, 8664 normalized-versus-original winner matches, 8664 exact period-shift checks, and 9538 object-identity reuse observations for unaffected class roots. Nine directed sizes N=1,2,4,8,16,32,64,128,256 tested exact R71 certificates, g=4 to g=1, and winner changes. All full-checker assertions passed: R82_PASS 722 2166 8664 8664 9538 9. A concise independent reproducible checker checked 2500 random configurations and all nine directed sizes: R82_MIN_PASS 2500 9. Exact arithmetic uses integers and fractions, no floating-point thresholds.

Full local checker and raw run JSON are preserved in the companion bundle; check_r82_min.py is the standalone repository reproduction. The universal theorems follow from the proofs, not from finite random coverage.

## Next R83

Benchmark the triple-index approach against the R75 ephemeral max-heap on equal **all-real winner decision** requirements. Include original input conversion, all gcd integer-bit costs, index construction, persistent allocations across versions, group certificate construction, query counts and witness-output recovery. Separate gcd=1 adversarial cases, few-phase classes, many classes, update-heavy and read-heavy workloads. Investigate compressed periodic witness representation for the R77 explicit-output-size family. Preserve the existing S23/AV science pin and independent review boundary.
