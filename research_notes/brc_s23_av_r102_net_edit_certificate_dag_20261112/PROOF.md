# R102 — Persistent net-edit certificate DAG: source-set branches, local exact queries, and OUT reuse

Date: 2026-11-12. Author-side mathematical proof and exact finite audit. Independent review pending.

**Scientific predecessor:** R101 at commit fb4776ca9a53ca42ceaf16d09aeb54cd73509773, research_notes/brc_s23_av_r101_lazy_topk_period_20261112/PROOF.md. **Frozen scientific pin:** 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Scope: R101's auxiliary finite rational circular-source model; no new P000 / native X6 theorem, formal task CLAIM, Result or independent admission is implied.

## Exact source model

Fix observer signature sigma=(j,x,a,b), where j,a,b are integers and x is rational. Each source u=(t,branch) has an integer time and complete branch identity; identities rank descending lexicographically. For any real parameter theta, define s_t={x+(t-j)theta}, A={a theta}, B={b theta}, where braces denote fractional part in [0,1). Eligibility M_u(theta) means that s_t belongs to the directed *half-open* circular arc [A,B); if A=B the arc is empty. Sources with the same time have the same eligibility, but are not identical ranked sources. Top_k(S,theta) gives the first k eligible identities from finite S. The eligibility predicate is independent of which version contains u.

Source-version edits are finite identity sets (D,A) acting by T_(D,A)(S)=(S\D) union A. A version DAG keeps immutable parent links for provenance and additionally caches a terminal edit normal form relative to a fixed base E.

## R102.1 — Composition and canonical terminal overlays

For two edits applied in order (D1,A1) then (D2,A2), with each pair normalized so its addition and deletion sets are disjoint, put:

    A' = (A1 \ D2) union A2
    D' = (D1 union D2) \ A'.

**Theorem.** T_(D2,A2)(T_(D1,A1)(S))=T_(D',A')(S) for *every* finite S, and D' intersect A' is empty. Hence any finite edit history can be represented by one pair regardless of path depth.

**Proof.** Distribute set difference over the union:
((S\D1) union A1)\D2 union A2
= (S\(D1 union D2)) union ((A1\D2) union A2).
The final added set is A'. Removing elements of A' from the accumulated deletion set changes nothing because they are reintroduced on the right. This gives the stated normalized pair. Apply induction along the ancestor path. QED.

Given a *fixed* base E and terminal version F, the unique minimal base-relative pair is D_E=E\F, A_E=F\E. Then D_E is a subset of E; A_E is disjoint from E; and F=(E\D_E) union A_E. Necessity follows by inspecting membership separately on E and outside E; sufficiency follows by direct substitution.

Repeated insertion/deletion toggles can cancel in the terminal overlay even when all parent edit edges are retained as provenance. This is safe for the declared terminal *source-set* observer: it is not permission to discard path histories needed by a different provenance-sensitive or native X6 observer.

## R102.2 — Exact source-version branch union and intersection

Let F_i=(E\D_i) union A_i, with D_i subset E and A_i disjoint E, i=1,2. Their exact base-relative normal forms are:

    union:         (D1 intersect D2, A1 union A2)
    intersection:  (D1 union D2,     A1 intersect A2).

Also F1\F2=(D2\D1) union (A1\A2).

**Proof.** Within E, version i retains precisely E\D_i. A base element is present in the union unless both histories deleted it, and present in the intersection only if neither deleted it. Outside E, version i has exactly A_i, so normal union and intersection rules apply. The difference equation follows by the same partition into base and nonbase identities. The two parts are disjoint. QED.

The equations merge source-set branches using only overlays, without iterating through E or expanding any theta period. They preserve source identities even when different branches share a time. For persistent balanced-set maps, modifying one identity costs O(log(m+1)) new tree nodes at overlay size m, plus exact-key comparison and allocator costs; old roots may be retained. Query costs below depend on the *net* overlay size, not the number of historical edit edges, once canonical overlays are built.

## R102.3 — Exact point Top-k and rational interval certificates

For a canonical overlay (D_E,A_E), write d=|D_E|. Then for every real theta and k>=1,

    Top_k(F,theta)
      = Top_k((Top_(k+d)(E,theta) \ D_E)
               union {u in A_E : M_u(theta)}).

**Proof.** Any eligible base source omitted from Top_(k+d)(E,theta) has at least k+d higher-ranked eligible base sources; deleting no more than d leaves at least k higher-ranked eligible survivors. Such an omitted source cannot enter the edited top k. All possible new eligible identities are explicitly included. Complete identities resolve equal-time branch ties. This is the R101 argument applied to the terminal net edit, and is valid for *all real theta*. QED.

**Query-local exact classification theorem.** Let I=[L,U] be a bounded rational interval, L<=U. For every distinct source time t in E union A_E, consider six integer-slope affine phases:

    a*theta; b*theta; (t-j)*theta+x;
    (t-j-a)*theta+x; (t-j-b)*theta+x; (a-b)*theta.

Construct C_I from L,U and every rational theta in I where any one of these expressions with nonzero slope becomes an integer. Evaluate the above point formula at every cut and at one rational midpoint of each consecutive open gap. On each gap the circular phase discontinuities and phase-order crossings are absent, so every membership predicate and the ranked Top-k are constant. Thus the resulting finite set is a complete certificate on I, including the half-open endpoints and isolated equalities. For *two* history versions, construct cuts from their combined source times, check the two winners at every representative, and return an exact rational mismatch witness whenever their winner functions differ somewhere in I.

If w=U-L, one nonzero slope c has at most floor(|c|w)+1 crossings. Consequently

    |C_I| <= 2 + sum_over_distinct_times_t
                  sum_over_nonzero_six_slopes_c (floor(|c|w)+1).

The algorithm depends on the actual query interval I, not the entirety of the R99/R100 enlarged global safe period. An interval with many real transitions still costs at least its explicit output size; the R101 Omega(N) full-profile lower bound remains in force.

Given an exact base Top-prefix oracle, a point query takes one prefix of length k+d, checks at most q=|A_E| new eligibility predicates, filters deleted identities and selects k of at most k+d+q candidates. A simple sort uses O((k+d+q)log(k+d+q+1)) identity comparisons, in addition to base-oracle, rational bit arithmetic, membership checks and set lookup costs. Query depth is independent of edit path length after normal-form construction. Building/maintaining the overlay and retaining version histories cost extra space/time and are not hidden in this claim.

## R102.4 — Source-version-independent OUT certificates

A genuinely certified R93 OUT box keyed by the exact signature sigma, time-residue class, time range and closed parameter interval J asserts M_t(theta)=false over *all covered integer times and every real theta in J*. Eligibility depends on sigma and t, not on source-version identity or branch. The certified proposition therefore survives any source-set addition/deletion/branch merge. An active index version that omits a certified box must not silently behave as if it included it, although an immutable earlier index root may still retain it. Reuse requires the matching signature, residue, time and parameter ranges and original all-real certification.

For a concrete nondegenerate box take sigma=(0,1/4,0,1), 0<=t<=200, theta in [0,1/1024]. Then s_t=1/4+t*theta lies in [1/4,1/4+200/1024] (strictly below 1) and exceeds theta. The arc [0,theta) therefore never contains s_t; at theta=0 it is empty. This proves the OUT status for all these *real* parameters and for any branch. The recorded rational grid checks only audit the implementation, not the mathematical all-real proof.

## Implementation, verification and limits

The original complete proof is also preserved in the local R102 bundle. The Python source is saved here as a lossless gzip/base64 text file; decode to check_r102.py, then run with standard Python to regenerate verification_r102.json. It uses fractions.Fraction for exact source predicates and all mathematical assertions. Seed 10220261112.

The reproduction built 60 base histories with 12 branching updates each (720 edited versions), 23,040 direct-versus-overlay Top-k point checks, 95,310 exact cut/midpoint Top-k checks, 480 branch-union/intersection operations with 2,400 direct checks, 240 cross-history comparisons with 127 rational difference witnesses, 200 independent arbitrary-source-set edit replay checks, and 39,975 rational-grid membership checks against an analytically certified OUT box. A 2,001-toggle history reduced to one net insertion. In the N=509 period-expansion family the interval [0,1/1018] required only 3 exact cuts versus 1,527 cuts over the whole new period [0,1]. These are finite reproducibility checks; no universal CPU speedup, mathematical independence or formal Result is asserted.

The relevant R101/R93 statements and source versions remain pinned as described above; no native X6 primitive, P000 or frozen science input is modified.

## Next frontier R103

Implement the canonical overlay with persistent balanced maps and a stored exact base Top-prefix oracle; integrate the R93 certified OUT interval index for demand-driven local eligibility pruning. Measure actual retained bytes, rational integer-bit arithmetic, update costs, candidate scans and exact witness restoration for (1) raw lazy DAG, (2) net-overlay checkpoint, and (3) explicit profile materialization. In particular, test whether narrower parameter queries justify structural checkpointing even when whole-period expansion is provably expensive.
