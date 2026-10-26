# EC48D — A two-bank seedless-memory interpolation theorem for positive BRC experiments

**Status:** author-side general mathematical proof; deterministic finite checks; not a native Enterprise Math Result, Driver review, Working Truth, Foundation admission, or native X6/Heartbeat theorem.
**Date:** 2026-10-27. **Mode:** independent mathematical continuation of EC48B/EC48C, no takeover or impersonation of an active owner.
**Sources pinned:** GLOBAL_KNOWLEDGE_V1 canonical main `bc537c4c13f8de68eda85997a26ffae60e5abee1` (00_BOOTSTRAP, OPERATING_MANUAL, Enterprise Math project router, P000_STARTUP verified canonical P000 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, ACTIVE worldview, BRC and math/code policies). Enterprise Math control read snapshot `1f07fa714735d60df7c97117875caf532e238e27`; publication branch base `d4ce578345f3690f19af0f8fe2518c251b13829a`. Research delivery: `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Immediate scientific source: [EC48C](https://github.com/awdawmip/enterprise-math/blob/d582d2bd1487446008648fe9da1fae63d2c86b9c/research_notes/r4_ec48c_encoder_quotient_20261027/EC48C_ENCODER_QUOTIENT_THEOREM.md), and its dependency [EC48B](https://github.com/awdawmip/enterprise-math/blob/91d7c15573afaf7803c62e3bbdfc0aa00e52aa73/research_notes/r4_ec48b_face_components_20261027/EC48B_FACE_COMPONENT_THEOREM.md).

## 1. Typed model and question

Fix finite nonempty source-history alphabet (H), subsequent visible-label alphabet (Y), two strictly positive separately normalized *rational* source laws (p(h,y),q(h,y)), and (K) private internal memory labels. The encoder draws (m) with law (pi_hinDelta_K); the binary terminal decoder declares P with probability (u(m,y)in[0,1]). It has no persistent public random seed, and source labels (h,y) are retained as BRC provenance. Thus
[
 w(h,y)=sum_mpi_h(m)u(m,y),quad
 alpha=sum_{h,y}p(h,y)w(h,y),quad eta=sum_{h,y}q(h,y)w(h,y).
]
Write (S_Ksubsetmathbb R^2) for this seedless attainable region and
(Z=sum_{h,y}[0,(p(h,y),q(h,y))]) for the complete-history zonotope.
The declared four-coordinate lift is ((e_P,e_Q,t_P,t_Q)=(1-alpha,eta,2,2)). No stopping/continue decision, variable depth, signed amplitudes, or native X6 dynamics is claimed.

Define (K_{m seed}=min{K:S_K=Z}), and (K_{m hull}) the minimum (K) for which (operatorname{conv}(S_K)=Z). EC47–EC48A establish (K_{m hull}) by generic-threshold sign profiles; this paper needs only their exact finite-scope statement, not the unresolved implication (K_{m seed}=K_{m hull}).

Set (Lambda={p(h,y)/q(h,y)}). At every (rinLambda) define two binary signature words in ({0,1}^Y):
[
 a_r(h)_y={f1}[p(h,y)ge r q(h,y)],
 quad b_r(h)_y={f1}[p(h,y)>r q(h,y)].
]
Let (A_r={a_r(h):hin H}), (B_r={b_r(h):hin H}) and
[
 M=max_{rinLambda}|A_rcup B_r|.
]
All sets are finite. Each binary word is a valid fixed terminal decoder across labels (y); the identical word occurring in both banks consumes only one memory label.

## 2. Theorem EC48D.1 — Two-bank construction

For every finite positive model above:
[
 oxed{K_{m hull}le K_{m seed}
       leminigl(|H|,,Migr)
       leminigl(|H|,,2K_{m hull}igr).}
]
More precisely, **for every threshold (r), its *entire exposed optimal edge* of (Z) is implementable seedlessly using at most (|A_rcup B_r|) memory states, with one explicit fixed decoder bank and private per-history encoder mixing.** Thus the possible extra seedless memory beyond convexified preservation is at most a factor two in this model, regardless of rational denominator sizes, (|H|), (|Y|) or geometry of the optimal-encoder graph. The bound is an upper bound, NOT an assertion that a factor-two separation is attained.

### Proof

**Step 1 — threshold face.** For (r>0), the support functional (F_r(w)=alpha-reta=sum_{h,y}(p-rq)w) attains its full-history maximum
(O_r=sum_{h,y}max(p(h,y)-rq(h,y),0))
exactly when every strictly positive cell is declared with probability one and every strictly negative cell with probability zero. Tied cells (T_r={(h,y):p(h,y)=rq(h,y)}) have no support constraint; writing (Q_r=sum_{T_r}q(h,y)), their total Q-mass (t) ranges across ([0,Q_r]) in the full-history face. Since tied generators all lie on slope (r), this one parameter exactly describes the entire exposed edge.

**Step 2 — a seedless implementation of every edge point.** Allocate one memory label for each *distinct* word in (A_rcup B_r), and set its decoder bit-vector equal to that word. Fix (sin[0,1]). At history (h), the encoder assigns probability (s) to memory word (a_r(h)), and (1-s) to word (b_r(h)). If they coincide, the probabilities combine at that single memory label. The resulting declaration probability is
[
 oxed{w_s(h,y)=s,a_r(h)_y+(1-s)b_r(h)_y.}
]
For (p-rq>0) both words have bit 1; for (p-rq<0) both have bit 0; for a tie, the first bit is 1 and the second 0. Therefore this is a support maximizer for every (s), with tied Q-mass (sQ_r). As (s) varies continuously, it covers **every point on the face**. This construction samples a private memory label conditional on the realized (h); no cross-episode/public/persistent mixture of whole policies is used. Its decoder bank is fixed while (s) varies.

**Step 3 — all faces imply all of (Z).** EC48B's elementary geometric argument applies verbatim: generators of (Z) are strictly positive in both coordinates, so every nontrivial exposed boundary edge has a normal ((1,-r)) or its negative with (rinLambda); the opposite edges follow by decoder complementation (umapsto1-u). The degenerate one-dimensional (Z) is directly covered by its unique tied-ratio interpolation. Further, (S_K) is star-shaped at the origin: (umapsto c u) produces (c(alpha,eta)) for every (0le cle1). Boundary coverage therefore implies (S_M=Z). Independently (K=|H|) stores the entire observed history and realizes arbitrary (w(h,y)), hence (K_{m seed}lemin(|H|,M)).

**Step 4 — the factor-two estimate.** Immediately left of (r), the generic strict-sign profile of history (h) equals (a_r(h)); immediately right it equals (b_r(h)). Therefore (|A_r|,|B_r|le K_{m hull}). Thus (|A_rcup B_r|le |A_r|+|B_r|le2K_{m hull}) for every threshold. The lower bound (K_{m hull}le K_{m seed}) follows from (S_Ksubset Z) and convexification. QED.

### Structural interpretation and finite algorithm

The previously unresolved obstruction is **not unbounded**: even without knowing whether (operatorname{conv}(S_K)=ZRightarrow S_K=Z) at equal (K), a source-preserving observer can always recover all ROC points using at most twice the hull-optimal memory. At each critical face, store the union of its two adjacent deterministic decision-signature banks, and mix *inside the conditional encoder*, never by retaining a public seed. The resulting construction preserves the exact ROC observer and both hypothesis probabilities; it need not preserve original full provenance for any unrelated future operator.

For positive rational (p,q), sort the finitely many exact ratios, form both sets of (Y)-bit words using integer cross-products, count their union sizes, and take (M). Naive implementation is finite and exact. The bit operation/arithmetic cost is distinct from the count of rational comparisons.

## 3. Auditable finite evidence (not the proof)

`EC48D_VERIFY.js` implements the exact signature-bank policy with safe integer cross-products (all generated values are small enough for exact JavaScript Number arithmetic), evaluates rational encoder probabilities (sin{0,1,2,3,5,7}/7), and checks the full support optimum and tied Q-mass identity. It also executes an adversarial, deterministically seeded positive nonuniform-weight template search for (K=2,3), (H=6,7), (Y=3,4), implementing EC48C's exact encoder-only graph and interval cover on the central face. The complete deterministic counts and zero/nonzero findings are saved in `EC48D_REPORT.json`. These generated cases are not an exhaustive proof of (K_{m hull}=K_{m seed}) and are not a new physical experiment.

Example (H=4,Y=2,Q_{hy}=1, P_{m raw}=(3,2;2,3;1,2;2,1)): at the center ratio 2 in raw units, the two adjacent binary signature sets each have three words and their union has four. Thus the construction provides at most four states, whereas the convexified sign-peak lower bound is three. This **illustrates the resource estimate, not its sharpness**.

**Reuse classification:** REUSE_APPLIED — typed positive weighted BRC provenance, EC47/EC48A threshold signatures, EC48B/C exposed-face criterion; EXTEND_EXISTING_TOOL — lightweight integer signature-bank verifier against the exact model, not a new Foundation primitive. Signed/phase interference and variable-depth four-observer or native Heartbeat X6 transfers remain unsupported.

## 4. Open obligation EC48E

The exact equality (K_{m seed}=K_{m hull}) for all fixed finite models is still **OPEN**. The factor-two certificate does not discharge it; EC48C's quotient graph can resolve individual instances. Next: search (Kge3), (Hge8), (Yge4) adversarial nonuniform positive masses with exact component-union witnesses, or prove a color-bank compression/reconfiguration lemma reducing (|A_rcup B_r|) to (K_{m hull}). A true counterexample requires a raw rational (P,Q), an exact tied ratio, all component intervals and an uncovered rational open subinterval. The separately harder variable-decision-depth four-observer problem remains independent.
