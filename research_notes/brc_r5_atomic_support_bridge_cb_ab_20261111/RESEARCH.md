# R5 — One-atom C→B and three-atom A→B support bridges

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact theorem with explicit Fraction witness; formal Source Result admission and independent review pending.

## Scientific object (pins preserved)

Continue the frozen seven-ratio P/Q–BRC Blackwell auxiliary observation fiber from prior R5 commit 9708a8b5ba1870bb423577c50144c1acfa7606dd (R5 PR #2072), which records the original global scientific pin a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math scientific pin 86149263e38c22292c9def1e0f69092efa1be77e. This research does not update either scientific pin.

There are 28 dynamic labeled arcs (i,j) for seven targets i=0,...,6 and source ports j∈{1,2,3,5}, with two unchanged strictly positive singleton arcs (0,0) and (6,6). The integer ratio vector is R=(2,10,15,20,25,30,38). The observation fiber is

\[
\mathcal F=\{x\in\mathbb Q_{\ge0}^{28}:Ax=b\}.
\]

The 15 observer rows comprise seven dynamic target totals, four source totals and four source ratio-weighted first moments; rank(A)=13. The right-hand side b is generated exactly from the original 30-arc strictly positive reference E0 in VERIFY_BRIDGES.py.

For source port 3 the three previously established four-support masks are

\[
A=\{1,3,4,6\},\quad C=\{2,3,4,6\},\quad B=\{2,3,4,5\}.
\]

A primitive operation is a signed six-arc K(2,3) kernel residual on a source pair {3,j}, j∈{1,2,5}, and three explicitly labeled targets, traversed along a nonnegative line segment. Peak support always counts positive **source-3 targets**, rather than total arc count.

## Exact result 1 — C→B atomic distance is 1 at peak 5

Use source pair {3,5} and target triple {2,5,6}, with source-3 residual entries

\[
h_{2,3}=-8/15,\qquad h_{5,3}=23/15,\qquad h_{6,3}=-1.
\]

Put the opposite coefficients at the matching source-5 targets and zeros elsewhere. Indeed

\[
-8/15+23/15-1=0,\qquad
15(-8/15)+30(23/15)+38(-1)=0,
\]

so this residual H preserves the full labeled observation system: AH=0.

The exact rational transfer XC in VERIFY_BRIDGES.py has support C and satisfies AXC=b with all 28 masses nonnegative. Let

\[
t=\frac{226755}{8493961}>0,\qquad YC=XC+tH.
\]

Direct Fraction calculation verifies YC≥0, AYC=b, and source-3 support B. Convexity certifies the whole segment, with interior source-3 support C∪B={2,3,4,5,6} of size five. Distinct endpoint masks require at least one operation. Consequently,

\[
\boxed{N_{\mathrm{atomic}}(C,B;\;\mathrm{peak}_3\le5)=1}.
\]

This contrasts with the preceding exact A→C theorem, in which one atom was excluded by nine integer Farkas certificates and two atoms were required.

## Exact result 2 — A→B has a single compatible three-operation path

Use source-3 triple {1,2,6} with residual coefficients (-23,28,-5). Let H1 compensate on source 1 and H2 on source 2; take H3=H above, compensating on source 5.

The exact starting transfer XA is specified as 28 rational numbers in VERIFY_BRIDGES.py. Define

\[
t_1=\frac{1544855}{475661816},\quad
t_2=\frac{196521}{67951688},\quad
t_3=\frac{226755}{8493961},
\]

and

\[
W_1=XA+t_1H_1,\quad
W_2=W_1+t_2H_2,\quad
YA=W_2+t_3H_3.
\]

All four states are nonnegative and satisfy the same 15 observation equations. Their source-3 support sequence is exactly

\[
\{1,3,4,6\}\longrightarrow\{1,2,3,4,6\}
\longrightarrow\{2,3,4,6\}
\longrightarrow\{2,3,4,5\}.
\]

The successive unions all have size five, so all open segments satisfy peak support at most five. The previously established support-filtration result proves this peak is optimal for movement between A and B. The four labels in the symmetric difference A△B={1,2,5,6} cannot all change in a single triple-supported primitive residual, so at least two primitive operations are needed. The present exact conclusion is therefore

\[
\boxed{2\le N_{\mathrm{atomic}}(A,B;\;\mathrm{peak}_3\le5)\le3}.
\]

This construction is a **compatible** three-atom path: the transfer at intermediate mask C simultaneously belongs to the first two-move bridge and to the final one-move bridge. Merely concatenating two unrelated existence theorems would not suffice.

## Actual computation and verification scope

Run: python3 VERIFY_BRIDGES.py. Standard-library fractions.Fraction verifies E0 positivity, all 15 exact observer equations at all states, every atom kernel identity, all nonnegativity inequalities, all four labeled support masks, and positive step coefficients. The console output from the actual local exact run is included as EXACT_OUTPUT.txt.

Terminal line: PASS_EXACT_R5_C_B_ONE_ATOM_AND_A_B_THREE_ATOM_WITNESSES.

Independent mathematical review and formal Source scientific Result acceptance remain pending.

## Next specific problem

Establish the exact atomic distance for A→B. The present exact interval is {2,3}. An exploratory finite linear-programming screen of ordered two-atom source-3 sign patterns narrowed the candidate family but supplies **no exact two-atom exclusion proof**. A next useful unit is complete bounded enumeration of target triples, compensator source ports and mid-state support patterns, and exact rational Farkas dual certificates for the nonnegative fiber feasibility problems that remain. If a feasible two-atom rational witness is instead found, it establishes distance two immediately.

The underlying residuals retain target labels, signed amplitudes and compensator port identities. This is an auxiliary observation-fiber result and does not retype the frozen native X6 world or dynamics.
