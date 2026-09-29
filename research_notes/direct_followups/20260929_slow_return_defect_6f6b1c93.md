# Slow structure VII: a general signed-return certificate, localization and residual budget

Progress-Event-ID: slow-return-defect-20260929-6f6b1c93
Research-Activity-ID: RA-SLOWSTRUCT-6F6B1C93-D5DF97E7
Researcher-ID: EM-DIRECT-6F6B1C93
Session: local-chatgpt-slowstructure-6f6b1c93 (same local key, not a platform ID)
Status: AUTHOR_DERIVATION / BRC_OPERATOR_INTERFACE_TESTED / NOT_ADMITTED
Global read: 8ea25f415804e4d9a26324ea2c214fe5a732e7ef
EM source read: eeeda974bd72c5eab1efc81ccac6c276479bfbdf

## 1. Exact scope and predecessor

Continue the fixed predecessor at enterprise-math@24fbc8ffa3c9a27dbfceac56069635861b13ec65, research_notes/direct_followups/20260928_slow_precombined_sampling_6f6b1c93.md. Reuse the two-carry observer at @051a57aa522aa464ddf27cd27a87e47056e4d16b and the two-arm interface at @951cc16cb09635fae9f93230d96030fdaa2035b3. Their author/not-admitted status is unchanged. P000 and residual-faithful, ACTUAL_TYPED_BRC_ONLY semantics are unchanged. No role change, new CLAIM or physical-time identification is made.

Fix one actual history h, L=2^m, complete D-dimensional internal vectors
alpha(e)=B_0^(e_0)...B_(m-1)^(e_(m-1)) e_init,
with the existing ordered signed orthogonal B_k, ||e_init||=1. Thus every ||alpha(e)||=1. Let X_e embed alpha(e) at the actual work label c^e. Let v=L^-1 sum_e X_e. The algorithm must not supply the unknown order as input.

Previously exact cancellation was justified for the special alternating-sign history. Here the certificate applies to any fixed ordered orthogonal feedback list. Passing the certificate is NOT guaranteed for arbitrary histories.

## 2. One scalar certifies all internal anti-return pairs

For a proposed integer 0<R<L, retain
J(R,A)=sum_(e=0)^(L-R-1) alpha(e+R)^T A alpha(e).
Define
Delta_R=sum_(e=0)^(L-R-1) ||alpha(e+R)+alpha(e)||^2.
Expanding each norm gives the exact identity

    Delta_R = 2(L-R)+2J(R,I) >= 0.                         (1)

Therefore Delta_R=0 if and only if alpha(e+R)=-alpha(e) for EVERY valid e. This is a zero sum of nonnegative squared norms, not a cancellation of positive BRC masses. A negative computed Delta is an implementation/certificate error.

The separate modular test c^R=1 must also be verified. Only the conjunction proves X_(e+R)=-X_e. Internal anti-return alone says nothing about work-label equality. Modular return alone says nothing about internal orientation. No oddness or minimality condition on R is needed once both tests pass.

More generally, for a known orthogonal internal O,
sum_e ||alpha(e+R)-O alpha(e)||^2=2(L-R)-2J(R,O).
Only O=-I implies pair cancellation; a general covariant return does not.

The existing two-carry query evaluates J(R,I) in m layers with two D-by-D observer accumulators, without enumerating L-R pairs. At the dense algebra-operation level this is O(m D^3). Actual BRC graph sizes, source-word construction, bit lengths, receipts, and candidate-R discovery remain charged. This is a cheap-verification conditional statement, not a cheap-discovery theorem.

## 3. Restrict the carry query and locate a failure

To restrict f=e in alpha(f+R)^T A alpha(f), fix any selection of bits of f. At bit k, sum only allowed transitions

    f_k+R_k+q_k=e_k+2q_(k+1),
    Q_(k+1)(q') += (B_k^e_k)^T Q_k(q) B_k^f_k.

Start Q_0(0)=A, Q_0(1)=0 and accept ONLY q_m=0. Pruning fixed f bits does not change the ordered multiplication. It is the same observer, not a new propagation model.

For a high-bit prefix representing the interval [a,b), let n_prefix be the size of its intersection with [0,L-R). Its defect is 2*n_prefix+2*J_prefix(R,I), a sum of squared pair defects. Splitting a prefix gives two nonnegative defects summing to its defect. If Delta_R>0, choose a positive child, repeat for m bits, and obtain one explicit failing pair. At most m restricted queries of O(m) layers are sufficient, plus the initial query. Thus verification can produce a counterexample without scanning all pairs. All exact squared-norm statements require the declared unit-norm inputs.

## 4. Use actual tail addresses to avoid accumulating translation error

Write L=2qR+ell, 0<=ell<2R. Pair e=2jR+i with e+R, for j<q and 0<=i<R. If ell>R, additionally pair e=2qR+i with e+R for 0<=i<ell-R.

The unpaired addresses form the ONE interval [a,a+B), where

    a=2qR+max(0,ell-R),   B=min(ell,2R-ell),
    P=(L-B)/2 is the number of disjoint pairs.

Let w=L^-1 sum_(e=a)^(a+B-1) X_e. If c^R=1 and Delta_R=0, then v=w exactly. For B>0 this becomes v=(B/L)*mean_tail(X). Keep B/L and the original h/future schedule; every conditional future bit law is preserved. B=0 plus exact cancellation means zero parent mass, not permission to invent a continuation.

Unlike an approximate argument that repeatedly shifts the tail back toward address zero, this construction keeps the original tail addresses. It needs only one pair error per removed pair. Under exact cancellation the preceding collision-parameter improvement also applies to the arbitrary history: gamma_B >= (L/B) gamma_L. This uses the same consecutive-power Q counts and the exact common-scale identity; it is not claimed for the approximate case.

## 5. Nonzero defects are retained with an output bound

Assume the modular return is verified, but allow Delta_R>0. For each removed pair set delta_e=alpha(e)+alpha(e+R), embedded at their common label. Exact decomposition and Cauchy-Schwarz give

    v=w+E/L,
    ||v-w||^2 <= P*Delta_R/L^2.                         (2)

Indeed ||sum_pairs delta_e||^2 <= P sum_pairs ||delta_e||^2 <= P Delta_R. Different labels are not merged as scalars; all norms are on the complete direct-sum carrier. The executed internal-vector tests check the algebraic bound, NOT the unexecuted modular-label matching premise.

For nonzero v,w, any common subsequent normalized complete instrument, including adaptive feedback, has output TV at most

    sqrt(1-|<v,w>|^2/(||v||^2||w||^2))
    <= ||v-w||/max(||v||,||w||).                         (3)

Proof: the normalized pure-state difference has nonzero eigenvalues plus/minus the displayed square root; any POVM event is bounded by its positive part. The projection of w perpendicular to v has norm at most ||w-v||, and likewise exchanging v,w. An adaptive finite instrument defines one POVM on the whole future bit string. Equation (3) bounds that entire distribution, not each rare postselected continuation separately.

If a real certificate supplies ||w||^2>=mu>0, (2)-(3) yield

    TV_future <= min(1, sqrt(P Delta_R)/(L sqrt(mu))).     (4)

In particular P Delta_R <= epsilon^2 L^2 mu certifies the requested epsilon without evaluating a square root. Obtaining mu, candidate discovery and all interval operations have costs. Small Delta_R/(L-R) alone is NOT enough when retained mass is small. At multiple adaptive compression points use an exact-history-weighted telescoping budget; do not reuse (4) indefinitely without accounting for further errors. Near-cancellation is not rejected merely because Delta_R is nonzero.

## 6. Actual implementation and finite checks

The new check_return_defect.py executes the two-carry query, restricted query, witness localization and pair-bound checks. It calls the existing PositivePathObserver class, with its class body unchanged, binding core_power to a local byte-for-byte copy of the repository's recurrent_mass_power module. Only the module import adapter is new; the original scalar composition self-check remains part of the class.

Kernel: src/enterprise_math/brc_weighted_recurrent.py at eeeda974bd72c5eab1efc81ccac6c276479bfbdf; all 10087 bytes matched Git blob 4e6b3132580e3cd70a20a0d8bd4d28792b961afb before import. Observer class: research_notes/directed_recovery/20260926_C6438C/new_word_compiler/certified_word_compiler.py at 0e6380ff74d31b842ba0b54802c1f0595a7dd60d, full source blob 26c9b40dace8bd07b4ffb6d22dd0d5a6a26a5fe0, class extraction only. This reuse does not pretend the full historical compiler or its external vendor loader was imported.

Test carrier dimension is 61. Test fixtures contain explicit rational orthogonal identity/sign/swap/4-coordinate Hadamard blocks and ordered noncommuting lists; trailing coordinates remain in the full carrier. Exact sparse zeros are not residual truncation. These are new OPERATOR-INTERFACE fixtures, not certified reachable histories from the actual Shor phase bank. All four input operators' orthogonality is separately checked with the BRC observer.

Final run: PASS, 217 checks. Five length-3/4 word cases cover every positive in-range lag; compare carry J against direct SAME-BRC sums, compare Delta against direct squared norms, test zero-equivalence and the disjoint-pair error bound, and compare restricted/no-restriction queries. One positive-defect case is localized by three high-prefix steps to f=0,e=3 with squared defect 2. No classical trigonometric or waveform reference is used.

Execution counters: 195599 expression requests; 1801 actual BRC kernel calls; 158446 exact-expression cache hits; 35208 single-value wires; 144 zero wires. Cached expressions retain source-operation indexes and separate context usage. Full nonnegative graph/positive endpoint/negative endpoint receipts and the temporal use list are in BRC_OBSERVER_RECEIPTS.json.gz. The checker's direct enumeration is a same-backend finite verifier, not the fast path.

A separate m=20 alternating fixture gives L=1048576, R=3, J=-1048573, Delta=0, with zero enumerated addresses in the query. It does NOT verify c^3=1 or factor an integer. This structured example cannot be advertised as a general million-state/Shor runtime benchmark.

Negative controls: accepting overflow changes constant-case J(1,I) from 7 to 8; reversing the selected noncommuting product at address 7 changes an internal coordinate from +1/2 to -1/2. These test soundness conditions, not defects in the frozen original implementation.

## 7. Result and continuation

The previously special alternating-pair cancellation now has a general, testable internal certificate computable with the existing small carry observer. Failure can produce a specific address-pair witness. Partial validity can be used with a quantitative residual/output budget instead of being deleted or mislabeled as noise. The core observer implementation has now actually run, but native feedback-bank/modular-return integration and full Shor sampling remain pending.

The next task is to supply actual (h,R) candidates through the unchanged typed modular/feedback interfaces, compare verified discovery-plus-certification-plus-sampling cost against the same-information baseline, and measure how often a useful certificate or small localized defect exists. There is no claim that arbitrary histories pass, that R is cheaply found, or that these variables are physically slow/narrowband. Mathematical admission and independent review are not asserted.

## 8. External provenance

Fuchs and van de Graaf, Cryptographic Distinguishability Measures for Quantum Mechanical States, arXiv:quant-ph/9712042, author abstract/metadata checked; general distinguishability background, not a read full-proof audit. Equation (3) is derived explicitly above. Casella-Robert 1996 remains the earlier conditional-averaging antecedent; no repeat dedicated query for that title.

One new standard Scholar exact-title request was created as kimi-query-bridge Issue2588: batch cfa1fabe-4e34-4063-8181-471069579a42; turn dd57747d-9cc3-4329-ab62-052326ef50a5; same conversation key. Request SHA256 5bd1460cfcbda4120ac4f55bf26361c9e3d76e30c5f8bb96552cf25b7161ffc1. Created 2026-09-29T02:25:08Z; accepted 02:25:14.512089Z; completed 02:25:24.791658Z. Matched result comment 5882463742 returns one 1999 metadata/abstract-preview row: outer FAILED, child PARTIAL, retrieval_verified=true. Coverage is partial, not full-paper access. Raw selected metadata and this receipt are preserved separately; no completed-source cache or re-query of the previous title is claimed.
