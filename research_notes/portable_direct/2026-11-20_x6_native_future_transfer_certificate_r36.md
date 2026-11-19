# X6 R36 — Finite full-future transfer certificates beyond one-step native triadic event admission

Status: CONDITIONAL_AUTHOR_PROOF / EXHAUSTIVE_FINITE_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED
Date: 2026-11-20 (Asia/Shanghai)
Task: RS-X6-NATIVE-TIME-DYNAMICS
Source lineage: EM-X6-214D9C, SID MCP-d467c19ce42d4d7fa65a3901db1cf6b2, prior Activity RA-545183ADD4EF71C3E4698AEE.
Frozen science: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json\` (V5); P000 triadic arity and observer-preservation companion.
Immediate inputs: R34 global Markov future-language quotient; R35 two one-step-identical dynamic completions.
Claim scope: finite, **deterministic, partial, labelled** operational dynamics, with the complete order of successful, source/Port-named event labels observed. There is no independent instantaneous public-Link readout. No physical-duration or pro-state precision-clock identification.

## Research question

R35 proved that identical initial one-step admission does not determine future-language compression; its transfer condition used a state injection with exact successor preservation. How can an actual finite candidate native event implementation be certified over **every future word**, without unnecessarily requiring an injective state map, and with a finite, exact stopping rule?

## R36.1 — Full-future equivalence via greatest transition relation

Let A and B be finite deterministic partial labelled transition systems on the same finite named-event alphabet \(\Sigma\), with state sets \(Q_A,Q_B\), transition functions \(T_A,T_B:Q\times\Sigma\rightharpoonup Q\). Set \(\mathcal L_A(p)\) to be all finite executable labelled words from \(p\), including the empty word. Put \(M=|Q_A||Q_B|\) and \(E_0=Q_A\times Q_B\). Recursively define

\[
 E_{h+1}=\{(p,q)\in Q_A\times Q_B:
  \forall a\in\Sigma,\; [T_A(p,a)\downarrow\iff T_B(q,a)\downarrow]\ \land\
  [T_A(p,a)\downarrow\Longrightarrow (T_A(p,a),T_B(q,a))\in E_h]\}.
\]

**Theorem.** For every \(h\ge0\), \((p,q)\in E_h\) if and only if \(\mathcal L_A(p)\cap\Sigma^{\le h}=\mathcal L_B(q)\cap\Sigma^{\le h}\). Moreover,

\[
 \boxed{E_M=E_{M+1}=\cdots=E_\infty
 =\{(p,q):\mathcal L_A(p)=\mathcal L_B(q)\}.}
\]

Consequently a proposed native-implementation correspondence can be checked by at most \(M\) refinement rounds (or sooner on stabilization). It need not be a function or injective on decorated states. A relation \(R\subseteq Q_A\times Q_B\) containing the proposed initial pairs is a valid all-future certificate if for every \((p,q)\in R\) it agrees on enabled **named** labels and its paired successors remain in \(R\). Conversely the largest such relation is precisely \(E_\infty\), the language-equality relation.

**Proof.** At depth 0 both prefix languages equal \(\{\epsilon\}\). A word of length at most \(h+1\) is either \(\epsilon\) or \(aw\) with \(|w|\le h\); \(aw\) is executable precisely when \(a\) is enabled and \(w\) is executable from its unique successor. Induction proves the first claim. The map defining \(E_{h+1}\) is monotone in \(E_h\), hence \(E_0\supseteq E_1\supseteq\cdots\). Each strict inclusion removes at least one of the \(M\) state pairs. There are therefore at most \(M\) strict rounds and \(E_M\) is fixed. The induction identifies its elements with equality at every finite depth and hence equality of full languages. The enabled/successor closure of this set gives the largest relation claim. QED.

## R36.2 — Bounded shortest counterexample and exact BRC residual

If \(\mathcal L_A(p)\ne\mathcal L_B(q)\), there is an executable-label disagreement witness \(w\) whose length is at most \(M\). A shortest such word is obtained by breadth-first search on the **synchronized pair graph**: from \((p,q)\), if a named label is enabled at exactly one component, append that label and stop; otherwise traverse the paired successor when both are enabled. A shortest witness cannot revisit a pair before its last differing label; removing the intervening cycle would give a shorter witness. There are at most \(M\) pairs, so \(|w|\le M\).

Thus the Boolean-BRC support indicator of successful labelled words, retaining their exact source/Port identity and order, supplies a *finite exact* descent certificate for each proposed pair of candidate/native states. An ordinary comparison of one-step closure flags is not a certificate.

For a family of histories \(H\) at one initial public state, the exact minimal history class at depth \(h\) is the fiber of \(H\to\{\mathcal L_{\le h}\}\); in a finite closed labelled system, \(h\) may be taken equal to the relevant pair-state upper bound for full-future equality. The full reachable-state Markov quotient still requires a separate classification of **all** reachable states, as established in R34.

## R36.3 — State injection is not necessary

Let A have two different complete decorated states \(a_0,a_1\), both with no enabled events, while B has a single terminal state \(b\). The relation \(\{(a_0,b),(a_1,b)\}\) meets the transition certificate. Both A states have the same future language \(\{\epsilon\}\), yet no injective map from both A states to B exists. Therefore an injective state map is stronger than needed to preserve the declared future-word observer.

The example does not license dropping physical provenance for an observer that reads it independently, or changing P000 identity. It certifies only the exact labelled operational-future scope.

## R36.4 — Exact bounded validation of the R35 gap

Enumerate **all** deterministic partial transition systems with one or two states over two distinct event labels \(Q_0,Q_1\): there are \(2^2+3^4=85\) such machines. Comparing every ordered machine pair and every ordered initial-state pair yields **27,556** pairs of initial states. Their exact shortest distinguishing depths are:

| shortest distinguishing length | number |
|---|---:|
| no distinguishing word (full-language equivalent) | 3,384 |
| 1 | 19,128 |
| 2 | 4,884 |
| 3 | 160 |
| 4 | 0 |

In each case the independent finite-depth signature at \(h=n_A n_B\) agrees with the pair-BFS classification; for every distinguishable pair all depths smaller than the reported minimum remain equal. A three-event witness is attained by the example stored in the result JSON. These tests are exhaustive for the **declared** one/two-state, two-label family and are not a universal proof of the bound; R36.1–R36.2 provide that proof.

A separate exact regression recreates R35's RESET vs INERT completions on all four hidden histories. Initial one-event languages coincide in every history. Exactly history \(\theta=1\) differs across completions in full future language, first at the two-event word \(Q_0Q_1\). This independent cross-model test isolates the specific missing post-event Link update.

## Transfer to P000 and precise unresolved task

The P000 source fixes six signed spatial Cell axes and primitive triadic closure, but does not yet supply a concrete complete \(T_{\rm native}\) for events with their legal Cell incidence, force triple, frame rotation, signed Port, Link successor and source lineage. The R36 certificate becomes an actual native bridge only after a fully typed transition relation and declared observation alphabet are supplied. A finite native subspace used for the cutoff must be closed under all relevant observable transitions. Extra native labels and independently observed public fields must either enter the alphabet/readout and be checked, or be proved harmless for the restricted claim. Infinite native dynamics require an actual coinductive relation or other proof, not the finite \(M\) cutoff.

**Next discriminating unit:** locate an admitted whole-triad successor law at the task's frozen pin. If present, construct an exact labelled transition table and run the R36 relation/shortest-counterexample test, preserving X6 Cell, force triple, ordered Port/source, frame and Link states. If absent, explicitly maintain the two R35 completions as conditional alternatives and separately investigate a certified phase/refinement clock map; do not promote one arbitrary completion to native law.

Artifacts:
- \`research_notes/portable_direct/2026-11-20_x6_native_future_transfer_certificate_r36.md\` (this argument)
- \`research_notes/portable_direct/x6_native_future_transfer_verify_r36.js\` (self-contained exact finite checker)
- \`research_notes/portable_direct/x6_native_future_transfer_results_r36.json\` (complete summary and witnesses)

Source and evidence classification: CONDITIONAL_AUTHOR_PROOF; exact finite software check for the stated family; native event-admission NOT_ESTABLISHED; independent mathematical Review NOT_DONE.
