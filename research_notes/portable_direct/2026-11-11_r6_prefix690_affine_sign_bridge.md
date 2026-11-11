# PREFIX-690-R6 — Affine sign bridge for the low-slot BRC variance crossover

Date: 2026-11-11 (Asia/Shanghai). Mode: independent author-side TASK_RESEARCH.
Science pin (unchanged): `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Frozen mathematical object and source

The object is the exact 189-level independent-Poissonized first-stop maximum observer `Y(p,z)` with its provenance-preserving survivor counts and two-clock joint moment kernels. Source dependencies (immutable):
- PREFIX-688: `awdawmip/enterprise-math@2b0f18fe26a276a45d8860b0d9f4ab029a0afea7`, files `research_notes/portable_direct/2026-11-11_r6_prefix688_low_slot_exact_local_crossover.md`, `PREFIX688_R6_RESULTS.json`, `PREFIX688_R6_CROSSING_BRACKETS.py`.
- PREFIX-689: `awdawmip/enterprise-math@101bab720ef0173eed1b517fcb491e11e54ebed1`, files `research_notes/portable_direct/2026-11-11_r6_prefix689_continuous_q_crossover_collars.md` and `PREFIX689_R6_PARAMETER_COLLAR_CERTIFICATE.py`.
- PREFIX-680 global third-derivative certificate is inherited via the above verified predecessor statements; not recomputed here.

Write
\[
 A(z)=\operatorname{Var}(Y(z,z))-\operatorname{Var}(Y(0,z)),\quad
 B(z)=E[Y(z,z)]-E[Y(0,z)],\quad F_q(z)=q A(z)-B(z).
\]
For q>0, `V_q(z,z)-V_q(0,z)=qF_q(z)`, with `V_q=q² Var(Y)-q E[Y]`.
The declared readout is the comparison of these two observers; no native Heartbeat physical-time or X6 dynamics is being inferred.

Set `L=0.0528706` and `R=0.0530659`. Pinned exact certificate data provide
\[
F_{12}(L)\ge2028625/10^9>0,\qquad F_{24}(R)<-7369716/10^9<0,
\]
\[
0.656<A(L)<0.657,\qquad0.329<A(R)<0.330.
\]
For the right upper bound: `floor(10^9 F_24(R))=-7369717`.

Define the following exact rational q endpoints:
\[
q_-:=12-\frac{2028625/10^9}{657/1000}=\frac{63055771}{5256000}
\approx11.996912290715374,
\]
\[
q_+:=24+\frac{7369716/10^9}{330/1000}=\frac{660614143}{27500000}
\approx24.02233247272727.
\]

## Theorem 690.1 (one crossing for every real q across the full bridge)

For **every real** `q ∈ [q_-,q_+]`, there is at least one real `z ∈ (L,R)` satisfying `F_q(z)=0`, hence `V_q(z,z)=V_q(0,z)`.

**Proof.** For `q<=12`, affineness in q and `A(L)<657/1000` give
\[
F_q(L)=F_{12}(L)-(12-q)A(L)
>2028625/10^9-(12-q)657/1000\ge0
\]
for all `q>=q_-`. Strictness also holds at `q=q_-`. For `q>=12`, `A(L)>0` immediately implies `F_q(L)>0`. Similarly, if `q<=24`, `A(R)>0` implies `F_q(R)<0`; for `q>=24`,
\[
F_q(R)=F_{24}(R)+(q-24)A(R)
<-7369716/10^9+(q-24)330/1000\le0
\]
for `q<=q_+`, also strict at the endpoint. As the finite observer yields polynomial A,B, `F_q` is continuous in z. Apply the intermediate value theorem. QED.

This establishes an exact q-width `434538558277/36135000000` (about 12.02542), covering every intermediate real q rather than just the two earlier collars. For the concrete internal sample `q=18`, the exact strict endpoint margins are
\[
F_{18}(L)>31504229/8000000=3.938028625,\qquad
F_{18}(R)<-495342429/250000000=-1.981369716.
\]

## Theorem 690.2 (ordered interpolation between the two earlier roots)

Let `z_12∈(0.0528706,0.0528708)` and `z_24∈(0.0530655,0.0530659)` be the individually certified unique local roots of PREFIX-688. For each **real** `12<q<24`, there is a zero of `F_q` **strictly between `z_12` and `z_24`**.

Indeed `F_q(z_12)=(q-12)A(z_12)>0` and `F_q(z_24)=(q-24)A(z_24)<0` because PREFIX-689 proved strict positivity of A on both corresponding spatial windows. Intermediate value gives the claim. At q=12 and 24 the respective original root is certified.

## Theorem 690.3 (odd crossing-parity invariant)

For every q in the certified closed interval, the number of **distinct roots of odd multiplicity** of the real polynomial `F_q(z)` in `(L,R)` is odd. The frozen survivor `S_n(z)` is a finite integer-coefficient polynomial, and the exact joint-clock kernels are rational; hence B is a polynomial of degree at most 376, A is of degree at most 752, and F_q is a polynomial. Strict endpoint signs show it is nonzero as a polynomial and has no boundary zeros. The overall sign change from positive to negative requires an odd number of odd-multiplicity roots. QED.

The theorem establishes existence and odd sign-crossing parity, leaving the exact root count/uniqueness over the full spatial bridge for the next certificate.

## Reproducibility and next frontier

The companion `PREFIX690_R6_AFFINE_BRIDGE_CERTIFICATE.py` executes the new exact rational implications with standard Python `Fraction` and produces `PREFIX690_R6_RESULTS.json`. The original 189-row recurrence is **inherited** from PREFIX-688, not rerun in this installment; mathematical admission and independent review remain open. The observer carrier is the pinned 189-row count population, with its two-clock kernels; only after forming the declared mean/variance readout is it reduced to A,B.

Next: construct a signed Bernstein/Sturm root-count certificate for `[L,R]`, perhaps first at q=12,18,24 followed by a q-cell continuation proof. Determine whether the certified odd number equals one, then use the crossing topology together with PREFIX-675's two-parameter variance-boundary comparison.
