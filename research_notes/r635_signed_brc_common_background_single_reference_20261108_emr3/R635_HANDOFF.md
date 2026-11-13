# R635 scientific handoff — shared cross-axis background

Date: 2026-11-08. Author-side proof, not reviewed/admitted.
Frozen R462 pin: 18783e01e3646c72b7aab3b16d3f565e83e6446f; K generator blob 7fa7a762f758b30c6090468ac43487daa34abad8. Immediate predecessor R634 commit 1fab59f1bb9b0d89d79baa51989aaf30cd33f35b.

Problem: R634 needed five matched references because H_x was arbitrary on each spatial axis. Replace that nuisance by a single unknown common-mode H(t) across all six native axes, still with independent ± signed K branch gains A^+ valuation a>=1 and A^- valuation >=a-1.

Proved (conditional on this exact observer law): m=clamp(floor((d-a)/2)+1,0,6), h=6-m.
Without a matched reference, exact maximal S6 orientation fiber F0=max(2,h!).
With ONE matched reference R=H, exact maximal fiber F1=h!.
At d=a+8, no reference gives twofold ambiguity, one reference uniquely recovers all 720 S6 configurations. No-reference ambiguity persists at infinite precision: choose W=product(U_j V_j), C_j=t^(a+2j-2)W, and alternate H'=C_5+C_6 with the labels 5/6 swapped. This preserves all 12 complete integer polynomial outputs.

Verification: R635_VERIFY.py regenerates frozen K, checks alternative nuisance decompositions and fiber signatures, 60,672 exact checks; see R635_EVIDENCE.json.

Source/native semantics: six axes, signed branch and source provenance unchanged. No actual X6 joint-field operation shown to implement a common H or matched reference; full future-operation quotient safety unproven. Status=AUTHOR_SIDE_PROVED_DERIVATION, Driver=UNREVIEWED, CLAIM=NOT_GRANTED. Native research activity RA-CA1F23CE9F91983A369153C9 / researcher EM-DIRECT-D51C7E (issued in this run); Source identity does not itself grant task ownership.

Next test: enumerate Source-registered joint-field operators, test whether their induced H_x are equal or related by known low-rank constraints, then demonstrate a legal single native operation/readout or a certified counterexample. If common mode fails, preserve the measured cross-axis residual and study whether rank-two backgrounds need two references.
