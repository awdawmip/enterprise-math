# X6 R14 — full signed-Port two-source radius theorem and factorial hidden source order

Date: 2026-11-19 (Asia/Shanghai). Status: **new author-side exact conditional proof with finite typed Boolean-BRC tests; NOT_REVIEWED**. Research line: RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3. Scientific input remains the frozen \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`; do not replace that pin with current control files. Earlier fronts: R11 two-source fixed *positive* axis Port collision cone; R12 blocker identity alias; R13 exact clipped gaps on fixed one-axis lanes. This R14 studies a different, fully signed six-axis **conditional vacancy-only** event alphabet.

## Carrier, native typing, and observer

Let the Cell chart be the six-component signed relative integer torsor Z^6, with **six native axes and twelve signed directions**, not twelve spatial dimensions. Time is ordered source-labelled events, not an additional spatial step or measured physical duration. A finite set of labelled triad *carriers* occupies distinct Cells. For each label s and signed Port v in {+e_1,-e_1,...,+e_6,-e_6}, one conditional primitive event \`(s,v)\` advances this source by exactly v **if and only if** the target Cell is vacant. Its old Cell becomes vacant. A word is legal iff every prefix event is permitted. The labelled Boolean BRC carrier retains each ordered successful source/Port branch; \`L_h(S)\` is the prefix-closed set of legal words with at most h events, including empty. Rejected-event blocker identity is not returned. No source weight or signed amplitude is assigned.

This is a fully specified conditional Port operator; **TRIADIC_CLOSURE_E force admission, native Link permission and actual time dynamics remain unverified**. It is not an assertion that every offered Port step is an admissible native physical triad action. A selected axis or coordinate projection is not an independent native plane or a complete three-dimensional research slice.

## R14.1: two-body exact minimum state for all twelve signed Ports

For two labelled sources A and B, let d=position(B)-position(A), d≠0, and \|d\|_1=Σ_{i=1}^6 |d_i|, an **event-graph** path length for the declared signed Port moves (not an assertion about the native enterprise metric L_E). For h≥0 define

    rho_h(d) = d                 when 0 < ||d||_1 ≤ h;
               FAR              when ||d||_1 > h.

Then the exact observational equivalence is

    L_h(d)=L_h(d')  ⇔  rho_h(d)=rho_h(d').

**Sufficiency.** At each event, two sources can first collide only if their initial displacement can be closed by at most the number of attempted unit events, as each event changes their relative position by one signed native axis. If \|d\|_1>h, all words of length at most h are legal; therefore all FAR configurations have the same language. The exact d cases have the same allowed guards and successor transitions.

**Necessity.** Take distinct d,d' with 0<\|d\|_1≤h and either d' different within that range or d' FAR. Select any shortest axis-step sequence that moves A from 0 towards stationary B at d; its length is r=\|d\|_1≤h. Every proper prefix is legal at d and its final step is illegal (it would enter B's Cell). In the d' configuration, either the same sequence has a blocked **earlier** prefix (when d' lies on the chosen path), which witnesses different languages, or all r steps are legal (when d' does not lie on that path), again distinguishing the languages. The case d'=d is trivial. Thus no two distinct non-FAR displacement classes coincide.

**Exact class count.** For unrestricted nonzero relative displacements, the possible near vectors are all nonzero integer points of the six-dimensional signed coordinate \ell_1 ball of radius h, and there is one pooled FAR class. Their total is

    C_6(h) = 1 + #{d∈Z^6\{0}: ||d||_1 ≤ h}
           = Σ_{j=0}^{min(6,h)} 2^j binom(6,j) binom(h,j).

To count a vector with precisely j nonzero components: choose their axes, their signs, and a j-tuple of strictly positive magnitudes whose sum is at most h (binom(h,j) choices). In particular h=0..6 gives

    C_6(h) = 1,13,85,377,1289,3653,8989.

For this explicit two-source observation fiber the minimal fixed-length supplementary label is exactly

    b_h = ceil(log_2 C_6(h)).

This is a **state-class code** within the family of all valid relative displacements, not a claim that all six integers can physically be observed with one finite-resolution instrument. If an observer already reports d or constrains its distribution, the *additional* coding requirement must be recomputed in that observer fiber.

**Future-safe graded update.** For a legal A event +v, d changes to d-v; for a legal B event +v, d changes to d+v. Given rho_h(d) at h≥1, both step permission and rho_(h-1)(d') are determined: exact near vectors update exactly; FAR stays FAR because \|d'\|_1≥\|d\|_1-1≥h>h-1. Thus rho_h is an exact horizon-decreasing Markov quotient for the full successful labelled Port language.

## R14.2: many sources — sufficient joint quotient, not necessarily minimal

For n≥2 distinctly labelled occupied Cells, retain rho_h(position(j)-position(i)) for each ordered/unordered pair consistently with a signed orientation. The tuple determines every offered immediate vacancy guard (a target collision is a unit displacement with an occupied other label). The graded two-body update applies to the pairs incident to the moving source and leaves all other pairs unchanged. By induction on horizon, this tuple determines the full joint L_h. It is therefore a **correct sufficient Boolean BRC quotient** for any finite n under this exact vacancy operator. The pair-product need not be minimal, as R12 already warns for restricted Port sets; the next theorem gives a stronger full-signed-Port failure.

## R14.3: factorial hidden ordering at horizon one, fully revealed at two

For every integer q≥1, take q+2 labelled sources \`LEFT, RIGHT, M_0,...,M_(q-1)\`. Place LEFT at (0,0,0,0,0,0), RIGHT at (q+1,0,0,0,0,0), and arrange the q middle labels arbitrarily at the intermediate Cells (1,0,0,0,0,0),...,(q,0,0,0,0,0). There are q! different initial placements, all with one occupied contiguous line segment. The *model still has all twelve signed X6 Port directions available*. We have deliberately chosen a one-axis embedded configuration, **not** a native two-dimensional plane or a replacement of six-dimensional space.

For all q! permutations, every middle label has blocked ±e_1 moves; LEFT has blocked +e_1 but free -e_1; RIGHT has blocked -e_1 but free +e_1. All labels have free ±e_i, i=2,..,6. Therefore their full one-step successful-event languages are identical:

    # { L_1(S_pi) : pi ∈ Sym(q) } = 1.

However, their two-step languages are pairwise distinct. If placements pi and pi' differ, their ordered adjacent-pair sets differ. Choose a directed adjacent edge (t,s) that occurs in pi but not pi', where t is the immediate left neighbor of s and s is one of the middle labels (there is at least one, because LEFT and RIGHT fix the ends). Consider the labelled two-event word

    ((s,+e_2),(t,+e_1)).

In pi, s moves transversely to a free Cell, vacating its original position, and t then advances into that vacancy: both events are legal. In pi', after s steps transversely, t is *not* immediately left of s, so its +e_1 target remains occupied (t is never RIGHT here), and the second event is illegal. This is a source- and Port-labelled two-step distinguishing witness. The edge-set uniqueness holds for a line whose endpoints and all labels are fixed. Hence

    # { L_2(S_pi) : pi ∈ Sym(q) } = q!,
    b_1=0,  b_2=ceil(log_2(q!)).

The bound is attained for every integer q, and for q≥2 the information jump grows superlinearly with the number of inner labels. The future observation is **successful** source/Port labels, not the identities of blockers returned after a rejected attempt. If blocker IDs or exact positions are already exposed, these equivalence claims refer to a different observation fiber and the bit cost changes.

This sharp contrast identifies a genuine **joint permutation residual**: retaining only the one-event allowed Port mask loses up to log2(q!) bits of information needed to predict a two-event successful source-labelled future. No finite-dimensional ambient-cell count alone bounds the resource history bits when the number of distinguishable sources may grow.

## Exact reproducible checks and limits

Run \`python3 research_notes/portable_direct/x6_full_signed_port_r14_brc_verify.py\` and compare the companion JSON \`x6_full_signed_port_r14_brc_results.json\`. This checker independently enumerates full **labelled Boolean branch languages**, not merely the claimed signatures. Two-body exhaustive near-vector checks were run for dimensions 2 with horizons 0..3 (typed auxiliary projection) and actual X6 6-component vectors with horizons 0..2, with three distinct FAR representatives each. They produced exactly 1,5,13,25 classes in the auxiliary projection and 1,13,85 classes in X6. The q! family was checked completely for q=1..5, giving one one-step class and respectively 1,2,6,24,120 two-step classes. All assertions PASS. Counts C_6(h) for h>2, the all-q factorial claim and the general-n graded sufficiency are consequences of the proofs, **not** extrapolations from those tests.

## Preserved provenance and next research question

Source predecessors R11, R12, R13 remain unchanged. This R14 is an extension from **fixed positive signed-axis masks/fixed-lane order** to **full twelve-direction vacancy offers**, not an accepted native kinetic law. The finite BRC carrier preserves branch order, source/Port identity and exact joint occupancy; it does not claim positive branch weights equal signed amplitudes or any physical period.

Next: derive an exact compact joint horizon-2 signature from the directed source/Port enabling structure and conditional successor language, then ask whether actual P000 \`TRIADIC_CLOSURE_E\` admits a source-signed move along either direction under explicit force/Link/Port constraints. A counterexample to correspondence must be preserved rather than declaring conditional closure a native proof. Neither current GitHub publication nor optional Activity linkage establishes independent Result/Review acceptance or a live formal CLAIM.
