# R5 continuation — extending the four-parameter Blackwell lifting cone

Frozen scientific pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568` / EM `86149263e38c22292c9def1e0f69092efa1be77e`. Reuse the exact 4-corner source/certificates and standalone `VERIFY.py` from this folder.

Confirmed: for `x=(1,1,1,27p/80,9/40,27q/80,0)` and all real `p,q in [0,1]`, all seven real terminal declarations lift to one seedless LR flow with a calibrated Blackwell kernel; both stopping times are preserved.

Next discriminating unit: broaden `v` and `z` beyond `9/40,0` while permitting simultaneous `u,w>0`. Search for 4 or 8 compatible seedless corner lifts belonging to one *affine seedless face*, e.g., shared endpoint splitting ratio `theta` with `z=theta*a/10, v-z=theta*9b/40`, so convex interpolation remains seedless. Maintain `u<=13a/40+b/80`, `w<=3a/40+21b/80`, and the frozen full seven-key stopping masses. Check all seven calibrated transport column equations, not only a scalar convex-order direction. If one face fails, distinguish failure of the proposed common-theta construction from nonexistence over the full seedless set.

Control: native status/task lookup on 2026-11-07 returned `BACKEND_IDENTITY_OR_VERSION_MISMATCH`, `STATUS_DATABASE_UNAVAILABLE`, `operation_sent=false`; no live R5 Owner/CLAIM was verified. The research evidence is author-side and awaits independent review.

## Strongest latest frontier (2026-11-07)

The rectangle result above has been extended to the full four-parameter cone: `0<=s<=g<=1`, `p,q in [0,1]`, source flow `x=(g,s,s,27sp/80,9s/40,27sq/80,0)` and all real terminal declarations. Exact proof is `CONE_EXTENSION.md`; 108 additional rational tests and source code in `VERIFY_CONE.py` / `EXACT_CONE_OUTPUT.txt`. The next question below remains to vary `v` and `z` while retaining both side flows; preserve this stronger source frontier.
