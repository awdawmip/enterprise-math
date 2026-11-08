# R5 follow-up — full physical five-parameter Blackwell prism now t ≤ 1/13

Date: 2026-11-08. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Frozen scientific pins inherited unchanged (GLOBAL_KNOWLEDGE a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e). P000/ACTIVE worldview unchanged; this is the seven-node P/Q-BRC statistical observer model.

## Extended real theorem

For **every real** t,p,q,theta,kappa with

\[
0\le t\le\frac1{13},\qquad 0\le p,q,\theta,\kappa\le1,
\]

and lawful FULL_HIST source

\[
x=(1,t,1,(\frac{13t}{40}+\frac1{80})p,\;
  \frac{9\kappa}{40}+\frac{t\theta}{10},\;
  (\frac{3t}{40}+\frac{21}{80})q,\;\frac{t\theta}{10}),
\]

there exists a lawful seedless LR target and a nonnegative declaration-independent 7-by-7 Blackwell martingale transport preserving all seven terminal Q/P contributions and both stop times \(T_P,T_Q\); in particular it preserves the entire \((e_P,e_Q,T_P,T_Q)\) observer for every randomized terminal declaration. The calibrated masses, time functionals, and finite Strassen/convex-order bridge are those stated precisely in adjacent RESEARCH.md and VERIFY.py.

## New exact two-chart seam

This stronger result uses a different **bilinear seam**. Let \(S(p,q)\) interpolate the rational corners

\[
S(0,0)=\frac35,\quad S(0,1)=\frac7{10},\quad
S(1,0)=\frac1{20},\quad S(1,1)=\frac25,
\]

and put

\[
\boxed{h(t,p,q)=1-13t(1-S(p,q)),\quad 1/20\le h\le1}.
\]

For \(0\le\kappa\le h\), set \(\lambda=\kappa/h\) and use the **G** seedless face \(a'=z'=0\). For \(h\le\kappa\le1\) and \(h<1\), set \(\lambda=(\kappa-h)/(1-h)\) and use the **F** face \(z'=a'/10,\ v'-z'=9b'/40\). At \(t=0\), \(h=1\), and the source itself is seedless, so identity transport suffices.

The new rational vertex data in VERIFY_T1OVER13.py include precisely 16 G and 16 F targets at \(t=1/13\), each indexed by \((p,q,\theta,\lambda)\in\{0,1\}^4\). All are lawful, satisfy exactly the two stop-time equalities and all five hinge convex-order inequalities; targets are on their declared common linear seedless face. The same checker verifies 32 \(t=0\) identity endpoints. Every numerical comparison is exact fractions.Fraction, without tolerances or floating-point search in the verifier. Earlier floating LP was used for discovery, not proof.

For any fixed chart, source and target are separately affine in \(t,p,q,\theta,\lambda\). The 32 multiaffine product weights are nonnegative and sum to one. Thus all capacity/normalization inequalities, five hinge inequalities and time equations persist under their convex interpolation, and the target remains on the same seedless face. Finite-support Strassen supplies the required nonnegative Blackwell matrix at each real point. G and F cover the full parameter box, including irrational values and all boundaries. This establishes the extended theorem.

## Exact local execution

On 2026-11-08, using Python 3 standard library, executing VERIFY_T1OVER13.py returned (recorded in EXACT_OUTPUT_T1OVER13.txt):

    PASS_EXACT_ENDPOINT_VERTICES 64
    PASS_EXACT_INTERIOR 251
    PASS_PHYSICAL_BOUNDARY 32
    ALL_REAL_FIVE_PARAMETER_BOX_T_LE_1_OVER_13_AUTHOR_CERTIFICATE

The first number consists of 32 exact rational nontrivial target vertices and 32 exact identity vertices. The 251 samples independently check interpolation implementation; the general real proof is the algebraic multiaffine argument and Strassen's finite theorem.

## Next experiment

Try \(t=1/12\) with \(p=1,q=0,\theta=1\). One floating LP experiment found **the selected G chart infeasible across a scanned \(\kappa\) range**; this is a chart-local exploratory diagnostic, not a model-wide no-go. Test new seam values, variable \(g',b'\), intermediate \(C_c\) seedless faces and/or a triangular partition of the parameter box. Seek exact rational counter-certificates or rational positive transport certificates. A separate independent direction is to construct an analytic sparse martingale kernel from the five-hinge proof to improve execution/verification cost.

Native Task CLAIM/Result, source activity checkpoint and independent mathematical review remain outside this author-side proof.
