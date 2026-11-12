# R109 — Persistent exact rank-shield certificates on a frozen rational phase partition

Research date: 2026-11-13 (Asia/Shanghai). Scientific scope: auxiliary BRC S23 finite rational directed-circle model, extending R108 proof at immutable enterprise-math commit `0a8aab1f555e282f342448dc71ac07af3e17e3d0`. Frozen scientific pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`, unchanged. Author-side theorem and finite validation; independent review pending. No formal RS-S23-AV CLAIM (exact native task query returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION`).

## Model and notation

A complete source is u=(t,b)∈Z², ranked in descending lexicographic order. Fix sigma=(j,x,a,c), with j,a,c integers and x rational; choose rational closed I=[L,U]. M_t(theta) means that the fractional part of x+(t-j)theta belongs to the half-open, positively directed circular arc from {a theta} to {c theta}. Equal endpoints mean an empty arc. All branches at a time have the same M_t, but full (t,b) rank and identity are retained.

For finite versions F,G and k>=1, put C=F∩G, Delta=F△G, T_Delta={t:(t,b)∈Delta}, and d_t=max{b:(t,b)∈Delta}. Define

    r_t(C)=#{(t,b)∈C: b>d_t}
    H_t(C,theta)=sum_{(s,b)∈C,s>t} 1[M_s(theta)].

The R108 time-bucket lemma proves pointwise equality of the ordered Top-k lists exactly when every t∈T_Delta obeys M_t(theta) => H_t(C,theta)+r_t(C)>=k.

## R109.1 — Exact phase-atom margin certificate (necessary and sufficient)

Freeze a finite *time universe* S containing every current source time and the times of all future edits covered by this particular index. On rational closed I, collect all rational integer crossings of the six affine forms

    a theta; c theta; (t-j)theta+x; (t-j-a)theta+x;
    (t-j-c)theta+x; (a-c)theta       (t∈S),

plus L and U. Partition I into singleton crossing points and the open gaps between consecutive points. Choose rho_i as the rational crossing itself on singleton atoms and the exact rational midpoint on open atoms. Let q be the number of atoms.

For t∈T_Delta and each atom i set

    B(t,i)=H_t(C,rho_i)+r_t(C)-k   if M_t(rho_i) holds,
           +∞                    otherwise.

**Theorem.** The Top-k outputs of F,G coincide for **all real theta in I** iff every B(t,i) is nonnegative (the minimum over an empty set is +∞). If some B(t,i)<0, rho_i is an exact rational witness of different ordered Top-k lists.

**Proof.** The six affine forms contain every fractional-part wrap or equality modulo 1 that can change any of the circular-membership comparisons. On an open gap between consecutive crossings all membership predicates are constant; singleton cutpoints are treated separately, retaining the half-open endpoint convention. H_t and r_t are constant on these atoms. Apply the exact R108 rank-shield iff on every atom. A negative B entails a live discrepancy with fewer than k higher-ranked eligible common identities, so the ordered lists differ at its rational representative. Conversely nonnegative margins shield every live discrepancy on the entire interval. QED.

## R109.2 — Common-edit rectangle law and persistent segment trees

Freeze Delta, sigma, k, I and S. Permitted edits simultaneously add an identity u=(s,b) to both F and G when u is not in Delta and not already present, or simultaneously remove an identity common to both. Consequently Delta and all d_t remain fixed. Let eps=+1 on insertion and -1 on removal; E_s={i:M_s(rho_i)}.

**Exact update law.** All margins in rows t<s change by eps on E_s. The t=s row changes by eps on E_s only when it exists and b>d_s. All other rows are unchanged; +∞ inactive entries stay +∞. This holds for every atom and across arbitrarily many permitted edits and historical forks.

**Proof.** A common identity u contributes to H_t exactly when its time s>t and M_s holds; for s=t, it contributes to r_t exactly when its branch b>d_t, with eligibility M_t=M_s. All lower-ranked rows t>s are unaffected. The common-set change is one identity, so deletion applies the inverse signed update. Delta does not change under the declared edits. QED.

For each t∈T_Delta, store B(t,.) as a persistent balanced binary segment tree over the ordered atoms. Its nodes carry the minimum finite margin or +∞ and a lazy integer add. Since E_s is a union of p_s maximal contiguous index ranges, apply p_s lazy range additions to each affected row by copying only touched nodes; all older roots remain immutable.

Put d=|T_Delta| and h_s=#{t∈T_Delta:t<s}+1[s∈T_Delta and b>d_s]. The provided implementation copies a d-entry root dictionary and makes O(h_s p_s log(q+1)) structural node copies, with O(d) comparisons of root minima and O(log(q+1)) descent to a negative witness. Its extra root-table references require O(d) per edit. Initial row trees use O(dq) nodes, in addition to generating exact rational cuts and margins. These are tree-operation bounds: Fraction numerator/denominator bit costs, phase partition generation, representation size and oracle recovery are charged separately. If h_s=0 or p_s=0, no segment roots need changing.

The exact rational rho_i and complete source identities are retained for independent witness recomputation; the tree is a sufficient answer certificate, not a destructive quotient of the model's provenance.

## R109.3 — Scope and zero-phase fast path

This result is a persistent certificate for histories with a fixed Delta and fixed time universe. Asymmetric changes that alter Delta, a new time outside S, or a changed sigma/k/I require refinement or a new tree. In particular the method is not yet an automatic fully general dynamic cut partition.

Before building phase atoms, test R108's stronger same-time condition r_t>=k for all discrepant times. If satisfied, equality holds on **all R** for all permissible observation signatures, without enumerating any phase cut. R109 supplies an exact reusable index for the phase-dependent cases.

## Executable and verification evidence

`check_r109.py.gz.b64` is gzip+base64 encoding of the standard-library Python source (original SHA256 `0e1aeaaf44a5dd8ee079c5e6fed3d6fbfffcff1d58485d324ffef9ec656055d5`). Decode via `base64 -d | gzip -d` and execute with Python 3. Its oracle sorts all eligible complete identities directly; the certificate implementation uses separately constructed exact phase cuts and persistent tree updates. It verifies all finite/inactive margins, the whole-interval decision, rational counter-witnesses, and all retained historical roots after later edits. Exact arithmetic is Python `fractions.Fraction`.

Seed 109: `R109_PASS`, 48 cases, 240 shared common edits, 17,795 directly checked atom-row margins, 191 valid exact inequality witnesses, 240 historical-version checks, 3,896 copied nodes, 558 nontrivial row-range updates, 103 no-op edits, 3 zero-phase large-time examples. Independent seeds 110 and 111 also passed (15,240 and 16,865 margin checks; 170 and 192 inequality witnesses; 240 edits each). `verification_r109.json` retains seed 109 data. Exact finite tests support implementation correctness on their specified samples; R109.1–R109.3 are derived above.

## R110 frontier

Generalize to *changing Delta* and *new time buckets* by persistent exact split/merge/refinement of the rational cut partition, including singleton half-open endpoints. Measure full rational bit operations, persistent history memory and witness restoration, and compare against R103 net-change overlays and R107 full atom refinement. Auxiliary theta is not native Heartbeat time or an X6 spatial coordinate: any physical/native transfer needs its own typed observer/embedding proof.
