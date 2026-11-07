# Next R5 unit — negative-residual interior flow lifting or exact separation

Frozen science pins: Global a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. Source parent R5 four-observer pointwise equivalence remains OPEN.

Completed at this frontier:
- All legal FULL_HIST flows with R=9*b*z−4*a*(v−z)>=0 have a single seedless-LR four-observer lift for every real declaration vector by explicit 7x7 Q/P transport (RESEARCH.md).
- Entire two-real-parameter negative-residual face (g,a,b,u,w)=(1,1,1,0,0) is similarly liftable, together with R>=0 part of that face (RESEARCH.md).
- Exactly all eight FULL-only deterministic flow corners admit single-process lifts for all their declarations: four R>=0, one negative corner covered in RESEARCH.md, and three remaining negative corners with rational 7x7 matrices in CORNER_ADDENDUM.md; exact checked in THREE_CORNERS_VERIFY.py.
- Predecessor f20b9a0bdc8c1fc8f69a2abeb7c231181d1a0d27 had proved conv(K_FULL)=conv(K_SEEDLESS) for all four-dimensional linear observers; this is now upgraded pointwise on specified regions but NOT yet globally.

Smallest unfinished unit: FULL_HIST flow with R<0 and arbitrary internal parameters g,a,b,u,w (especially non-extreme ones). Attempt a single seedless flow y preserving TP,TQ and a nonnegative 7x7 two-measure joint mass matrix J with row sums M_i(y), Q column sums M_j(x), P column sums r_j M_j(x). This is a sufficient uniform lift for EVERY declaration d, making it more reusable than solving one d.

Suggested discriminating tests: work on the continuous face g=a=b=1, v=9/40,z=0, u,w varying in [0,27/80]; interpolate or algebraically extend the three exact corner matrices while keeping y seedless and both times fixed. Then reduce g,a,b and vary z/v. If global garbling fails, exact test individual observer fibers (e_P,e_Q,TP,TQ) under bilinear seedless feasibility; nonexistence of one garbling does not establish four-observer separation.

Verification: base VERIFY.py and THREE_CORNERS_VERIFY.py use exact Fraction; outputs in EXACT_OUTPUT.txt and THREE_CORNERS_EXACT_OUTPUT.txt. Native Source owner/CLAIM remains unconfirmed due to BACKEND_IDENTITY_OR_VERSION_MISMATCH (operation_sent=false). Retain author proof status; independent review pending.
