# PREFIX-695-R6 — Exact BRC jet reconciliation and uniform safeguarded Newton certificate

Date: 2026-11-11 (Asia/Shanghai). Science pinned to `enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Direct independent research unit, without taking a shared Task CLAIM. Researcher `EM-DIRECT-192A00`, activity `RA-FEED90A8D5CFD47BD62B4CDB`.

Status: **AUTHOR_RECOMPUTED / EXACT_189_ROW_INTEGER_KERNEL_REPLAY + EXACT_FRACTION_IMPLICATION_CHECK / UNREVIEWED / NOT_ADMITTED**.

## 1. Frozen observer and exact discrepancy

The frozen BRC model uses 189 first-stop survival levels and retains 9,529 nonzero ordered survivor count cells. Its two separately labelled joint-clock observation branches are `Y(z,z)` and `Y(0,z)`. Let

\[
A(z)=\mathrm{Var}(Y(z,z))-\mathrm{Var}(Y(0,z)),\quad
B(z)=E[Y(z,z)]-E[Y(0,z)],\quad
F_q(z)=qA(z)-B(z).
\]

These \(z,q\) values are parameters of a *typed auxiliary readout*, not native spatial coordinates or native heartbeat ticks. The update and survivor predicate remain the pinned exact BRC model; the algebra below certifies properties of its already-defined readout.

PREFIX-693's paper and Python assertion report
\[
\left\lfloor 10^8 A^{(5)}(53/1000)\right\rfloor=-36266294695911132.
\]
Its earlier `PREFIX693_R6_RESULTS.json` instead contained `-36266294695911140`. We independently recomputed all orders \(0\) through \(5\) using a different exact moment-accumulation method. The exact answer is **\(-36266294695911132\)**. The mismatch was an evidence-recording error, not a change to the model or input pin.

All recomputed integer floors of \(10^8 A^{(j)}\), \(j=0,\ldots,5\), are

```text
[44000296, -168056589514, -6667624082229,
 39352687679231, 3189837819999830, -36266294695911132]
```

and of \(10^8 B^{(j)}\):

```text
[789752024, 12845959424, -99127959112,
 -1326952329685, -14895243921676, -1960958310350017]
```

The two resulting finite jets match the original PREFIX-693 checker and paper. The old JSON cell was corrected on canonical `main`, with the previous literal value retained in provenance. PREFIX-694's result metadata was also corrected to distinguish the earlier paper/checker value from the earlier JSON value. Its conservative Taylor envelope remains valid.

### Integer-kernel identity and reproducibility

For the frozen rational center \(b=53/1000\), put \(D=1000\), \(N=189\), \(P=2D\). Each derivative of the survivor polynomial \(s_n\) has an exact integral normalization
\[
u_n^{(j)}=D^n s_n^{(j)}(b)\in\mathbb Z.
\]
The preserved joint-clock moment kernels are
\[
K_{nm}=\frac{\binom{n+m}{n}}{2^{n+m+1}},
\qquad J_{nm}=\frac{n+m+1}{2}K_{nm}.
\]
Let \(H=2P^{2(N-1)}\) and
\[
W_{nm}=\binom{n+m}{n}P^{2(N-1)-n-m}\in\mathbb Z.
\]
For rational derivative arrays \(x,y\), let \(u_n=D^n x_n\), \(v_m=D^m y_m\). Direct cancellation of denominators gives the **exact identities**
\[
\sum_{nm} x_n y_m K_{nm}
=\frac{\sum_{nm}u_nv_m W_{nm}}{H},\qquad
\sum_{nm} x_n y_m J_{nm}
=\frac{\sum_{nm}(n+m+1)u_nv_m W_{nm}}{2H}.
\]
Thus the two joint moments can be accumulated in one integer sweep, and \(\mathrm{Fraction}\) normalization is needed only at the final division. This is an algebraically identical yet operationally distinct replay of PREFIX-693's per-addend rational summation. The local equivalent implementation completed all six derivative orders and checked all twelve floor values in approximately 3.6 seconds on this run. The published self-contained verifier uses the same exact integer-kernel algorithm and strict assertions; there is no floating-point input to the proofs.

## 2. Certified derivative and residual-to-root envelope

Reuse the predecessor certificates only on the closed bridge
\[
I=[L,R]=[0.0528706,0.0530659],\qquad W=R-L=1953/10^7
\]
and parameter band
\[
Q=[q_-,q_+]=\left[\frac{63055771}{5256000},\frac{660614143}{27500000}\right].
\]
PREFIX-690/693 provide exactly one root \(z_q\in(L,R)\) of \(F_q\) for every real \(q\in Q\), together with
\[
-1751<A'(z)<-1611,\quad 128<B'(z)<129,
\]
throughout \(I\). PREFIX-694 supplies
\[
|A''(z)|<2500000,\qquad |B''(z)|<1500.
\]

**Theorem 695.1 (uniform a posteriori error conversion).** For every \(q\in Q\), \(x\in I\), and \(x\ne z_q\), put
\[
d_-:=128+1611q_- =\frac{11361735009}{584000},\qquad
d_+:=129+1751q_+=\frac{1160282864393}{27500000}.
\]
Then
\[
\boxed{\frac{|F_q(x)|}{d_+}<|x-z_q|<\frac{|F_q(x)|}{d_-}.}
\]
In particular, an exact evaluated residual immediately gives a rigorous root enclosure centered at \(x\). If a certified approximate readout \(\tilde F_q(x)\) obeys \(|\tilde F_q(x)-F_q(x)|\le\varepsilon\), then
\[
\boxed{|x-z_q|\le\frac{|\tilde F_q(x)|+\varepsilon}{d_-}.}
\]

*Proof.* \(F'_q=qA'-B'\), so for each \(q\in Q,z\in I\), \(-d_+<F'_q(z)<-d_-<0\). Apply the mean-value theorem between \(x\) and the unique root \(z_q\), then the triangle inequality for the certified residual. This also proves the direction of each sign comparison on the bridge.

## 3. A uniform five-step certified Newton solver

Define \(\Pi_I(t)=\min(R,\max(L,t))\). For any real \(q\in Q\) and any starting \(x_0\in I\), consider the *auxiliary readout root solver*
\[
\boxed{x_{n+1}=\Pi_I\left(x_n-\frac{F_q(x_n)}{F'_q(x_n)}\right).}
\]
This is a proof/analysis operation on the exact readout polynomial, **not** a substitution for a native BRC state update.

**Theorem 695.2 (global safeguarded Newton convergence on the certified bridge).** Put
\[
M:=2500000q_++1500=\frac{660630643}{11},\qquad
C:=\frac M{2d_-}=\frac{192904147756000}{124979085099}.
\]
For all real \(q\in Q\) and all starting \(x_0\in I\), the sequence is well-defined, stays in \(I\), and satisfies
\[
\boxed{|x_{n+1}-z_q|\le C|x_n-z_q|^2.}
\]
In particular, set \(e_0=W\), \(e_{n+1}=Ce_n^2\). Then \(|x_n-z_q|\le e_n\) and the exact rational comparisons give
\[
CW=\frac{10465050015763}{34716412527500}<\frac{31}{100}<1,
\]
\[
\boxed{e_4<\frac{31}{10^{13}}=3.1\times10^{-12},\qquad
e_5<\frac2{10^{20}}=2\times10^{-20}.}
\]
The bounds cover **every real** \(q\) in the certified band, including \(12,18,24\), from **any** initialization in the bridge.

*Proof.* Throughout \(Q\times I\),
\[
|F''_q|=|qA''-B''|<M,\qquad |F'_q|>d_-.
\]
Taylor's theorem for \(F_q(z_q)=0\) about \(x\) gives
\[
\left|x-\frac{F_q(x)}{F'_q(x)}-z_q\right|
\le\frac{M}{2d_-}|x-z_q|^2.
\]
Metric projection onto the closed interval \(I\) is nonexpansive with respect to every point in \(I\), in particular \(z_q\). Hence the same quadratic bound holds for the clipped iterate. Induction starts from \(|x_0-z_q|\le W\). The rational inequalities above establish the explicit steps. This is a constructive uniformly convergent root solver for the entire low-slot crossing family.

## 4. Evidence, scope, and next unit

- Frozen science: `f42f2906d77f24085c123f3ccfe9667d41caa96d`; exact 189-level survival predicate, 9,529 live row cells, joint-clock labelled branches and kernels are preserved.
- Exact local re-execution: independent integer-accumulation kernel agrees with all twelve PREFIX-693 derivative floors. The 5th-jet JSON mismatch is resolved; no independent blinded mathematical review is asserted.
- Proof dependencies: certified signs/uniqueness from PREFIX-690/693 and second-derivative envelopes from PREFIX-694. All newly derived numerical inequalities are exact integer or rational comparisons. An executable, self-contained 189-row verifier accompanies this note; its remote source was read back after publication.
- Status: `AUTHOR_RECOMPUTED / EXACT_189_ROW_INTEGER_KERNEL_REPLAY + EXACT_FRACTION_IMPLICATION_CHECK / UNREVIEWED / NOT_ADMITTED`.

**Next discriminating unit.** Use the rigorous residual-to-root bound to build a small batch certificate for \(q=12,18,24\), and compare the newly certified Newton intervals against PREFIX-688/691. Then subdivide \(0.052\le z\le0.054\) to attempt exact sign certification of \(Q''\) outside \(I\). Feed the resulting branch/variance sign structure into PREFIX-675's full triangular auxiliary parameter domain \(0\le p\le z\le\frac12\).

## Published companion paths

- `research_notes/portable_direct/PREFIX695_R6_FAST_INTEGER_KERNEL_AND_NEWTON_CERTIFICATE.py`
- `research_notes/portable_direct/PREFIX695_R6_RESULTS.json`
- Corrected predecessor records: `PREFIX693_R6_RESULTS.json` and `PREFIX694_R6_RESULTS.json`.

No shared task claim, Driver review, or Foundation theorem promotion is inferred from this direct scientific contribution.
