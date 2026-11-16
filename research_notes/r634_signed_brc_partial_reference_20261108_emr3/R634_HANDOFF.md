# R634 handoff — partial matched references and depth-precision tradeoff

2026-11-08; frozen science R462@18783e01e3646c72b7aab3b16d3f565e83e6446f, original K generator blob 7fa7a762f758b30c6090468ac43487daa34abad8; R633 parent 1cc630a021e9870ab15f95c0e9acb2f7698de962. P000 unchanged; author side, unreviewed.

Model: unknown S6 orientation of signed six-axis BRC P_j=K_(2j-1), M_j=K_(2j); two responses per axis with the same arbitrary axis-specific additive background. Known a>=1, first gain t-order a and mod-5 unit; second gain t-order >=a-1; exactly r axes receive matched background reference. Observe mod-5 d-jets.

Proved exact minimax orientation fiber F=(h)!/(h-min(r,h))!*(6-r)!, with h=6-min(6,max(0,floor((d-a)/2)+1)). At d=a+8 the fiber counts for r=0..6 are 720,120,24,6,2,1,1. Thus five references (not six) are necessary and sufficient; d=a+8 is the uniform minimum depth when r=5. The positive readout minus its matched baseline supplies a label via BRC valuation; uncalibrated channels can still be made identically zero by the R633 independent-gain/full-background construction.

Verifier R634_VERIFY.py regenerates frozen K and verifies the complete 720-permutation × seven-budget × twelve-depth × three-a grid, plus witness and background checks (196746 exact checks); R634_EVIDENCE.json retains formula, representative matrix and count evidence. No native operator equivalence is claimed.

Next unfinished question: Source X6 joint-field operator that admits five matched-background references or a provable cross-axis nuisance coupling achieving the same orientation separation with fewer calibration channels. Preserve source and branch histories and independent time typing. Formal Owner/CLAIM/Driver disposition requires current native Source gates.
