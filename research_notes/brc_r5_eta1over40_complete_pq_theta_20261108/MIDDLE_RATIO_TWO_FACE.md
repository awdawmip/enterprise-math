# R5 exact middle-ratio mixed point — simultaneous G and F lifts

Date: 2026-11-08 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**. Scientific pins global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`, unchanged. Model and 7-node mass/observer definitions are given in this folder's `RESEARCH.md`.

This is a new **exact positive example** in the previously open middle-ratio interval `1/40<eta<46/705`. Set eta=1/30, theta=p=q=1/2, g=s=1, giving
```text
x=(1,1,1/30,781/4800,23/400,67/1600,1/20).
M_Q(x)=(234569/2160000,781/4800,0,58327/360000,
         29/60,67/1600,89569/2160000).
(TP,TQ)=(1039/400,2223/800).
```

**Two separate exact rational seven-node Blackwell witnesses exist for this same source**:

G-face target (`b=0,v=z`):
```text
y_G=(637111/641580,637111/641580,0,254017/1509600,
     1716979/25663200,462163/8554400,1716979/25663200).
```

F-face target (`z=a/10,v-z=9b/40`):
```text
y_F=(44147/56400,44147/56400,10399/28200,19477/75200,
     36377/225600,0,44147/564000).
```

Full nonnegative rational matrices Q_G (10 nonzero entries) and Q_F (12 nonzero entries) are in `MIDDLE_RATIO_EXACT.json`, orientation Q[target_node,source_node]. `VERIFY_MIDDLE_RATIO.py` imports the standard-library seven-node checker `VERIFY.py` and exactly verifies: lawfulness, seedless equation and face, row Q masses, column Q masses, likelihood-weighted P column masses, measure normalizations, and both stopping times. Actual executed output in `EXACT_MIDDLE_OUTPUT.txt`: `EXACT_MIDDLE_FACE_PASS G SPARSE_EDGES 10`, `EXACT_MIDDLE_FACE_PASS F SPARSE_EDGES 12`, `PASS_R5_MIDDLE_ETA_1_OVER_30_THETA_P_Q_HALF_TWO_FACES`. All computations use exact rational arithmetic in the frozen R5 finite statistical BRC model.

For every `h in [0,1]`, use `x_h=(1-h)x+h*y_G` and `Q_h=(1-h)Q_G+h*diag(M(y_G))` (and likewise F). The same exact calibration identities imply preservation of `(eP,eQ,TP,TQ)` for **all seven-node terminal declarations** via the row-normalized kernel. Thus the single positive example yields two nontrivial continuous **real line segments** in the middle-ratio region. This is a scoped result; no conclusion is claimed for the whole middle-ratio rectangle.

The two distinct seedless target faces at this one source provide a bridge design opportunity: seek a same-face positive-volume neighborhood, then an overlapping G/F cover along `eta` from 1/40 to 46/705. Distinguish arbitrary FULL_HIST mother problem and native-X6 physics from the finite R5 observer equivalence. Native role/Owner/CLAIM was unavailable; this file is author-side source evidence pending independent mathematical review.
