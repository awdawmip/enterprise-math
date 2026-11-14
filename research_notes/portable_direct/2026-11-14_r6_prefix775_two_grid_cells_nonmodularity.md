# PREFIX-775 / R6 — Opposite exact mixed signs on the same 1/768 Gamma lattice

Date: 2026-11-14 (Asia/Shanghai). Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Status: `AUTHOR_EXACT_INTEGER_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED`.

## 1. Problem and model

Continue PREFIX-774's **external auxiliary** 189-layer killed-Pascal first-stop model. Let `T_x≤189` be its first-stop layer; conditioned on `T_x=m`, sample an independent unit-scale Gamma(m,1) clock `C_x`. Two clocks are independent, conditional on their respective layers. Define

\[
Y(p,z)=\max(C_p,C_z),\quad
\mu(p,z)=\mathbb E Y,\quad
W(p,z)=\operatorname{Var}(Y),\quad
V_q(p,z)=q^2W(p,z)-q\mu(p,z).
\]

This is an explicitly two-parameter auxiliary model, not native X6 or a physical-clock transfer. The `1/768` lattice here consists of parameter pairs `(k/768,\ell/768)`.

For any unit grid cell `R=[a,b]\times[c,d]`, put

\[
\Delta_R F=F(b,d)-F(b,c)-F(a,d)+F(a,c).
\]

The new question is whether both signs of `Δ_R V_q` can be certified **within the same lattice**, with exact arithmetic and a uniform range of `q`, rather than combining continuous witnesses and discrete examples.

## 2. Exact moment identities

Use `S_i(x)=Pr(T_x>i)`, `0≤i≤188`, and `s(x)=(S_i(x))`. Let

\[
K_{ij}=\binom{i+j}{i}/2^{i+j+1},\qquad L_{ij}=(i+j+1)K_{ij}.
\]

The finite Erlang-survival expansion gives

\[
\begin{aligned}
\mu(p,z)&=\sum_i S_i(p)+\sum_iS_i(z)-s(p)^\top K s(z),\\
M_2(p,z)&=2\sum_i(i+1)[S_i(p)+S_i(z)]-s(p)^\top Ls(z),\\
W(p,z)&=M_2(p,z)-\mu(p,z)^2.
\end{aligned}
\]

The same killed-Pascal survivor predicate as PREFIX-774 is reconstructed exactly:

\[
40(n+1)\binom nk x^k(2^{18}-x)^{n-k}>(2^{18})^n,
\]

together with the frozen quartile-width rule. The 189 retained rows contain 9,529 nonzero survivor positions; row 189 is empty. These counts are checked, not assumed, by the attached script.

## 3. Theorem 775.1: exact two-cell lattice nonmodularity

Consider two *distinct* cells of the same `1/768` grid:

\[
R_+=[12/768,13/768]\times[760/768,761/768],\qquad
R_-=[38/768,39/768]^2.
\]

For these exact cells, the signed moment differences obey

\[
\boxed{\Delta_{R_+}\mu>0,\quad\Delta_{R_+}W>0},
\qquad
\boxed{\Delta_{R_-}\mu<0,\quad\Delta_{R_-}W<0}.
\]

Define `r_\pm=(\Delta_{R_\pm}\mu)/(\Delta_{R_\pm}W)`; both are positive. Integer cross-products establish the strict rational enclosures

\[
\boxed{
0.033661560<r_+<0.033661562,\qquad
0.028520342<r_-<0.028520343.}
\]

For every real `q>0` the exact identity

\[
\Delta_R V_q=q\,\Delta_R W\,(q-r_R)
\]

holds. Since `r_-<r_+<0.033662`, it follows *simultaneously* that

\[
\boxed{\forall q\in\mathbb R,\ q\ge 0.033662:
\quad\Delta_{R_+}V_q>0,\qquad\Delta_{R_-}V_q<0.}
\]

In particular, the sampled `1/768` lattice function `(p,z)\mapsto V_q(p,z)` is neither supermodular nor submodular for every `q≥0.033662`, by the definitions of those properties on a rectangular grid. At `q=2`, the exact signs are opposite, with display-only decimals

\[
\Delta_{R_+}V_2\approx +0.46832464480101176013,\qquad
\Delta_{R_-}V_2\approx -0.68198303964111198330.
\]

### Proof of the numerical claims

Let `E=768^{188}`, `T=2^{377}`, `H=E^2T>0`. The recurrence produces each rational survivor vector over denominator `E`. The integers `K_{ij}T=\binom{i+j}i2^{376-i-j}` give both moment numerators `U=H\mu`, `B=HM_2`. Thus `Z=HB-U^2=H^2W` is integral. For each cell, compute signed corner differences `dU=ΔU`, `dZ=ΔZ`, giving `Δ\mu=dU/H`, `ΔW=dZ/H^2`, and the *exact* switch `r_R=H\,dU/dZ`. The program checks every stated sign and rational bound using signed integer multiplications, with the denominator sign handled explicitly. The theorem then follows algebraically, including the closed lower endpoint `q=0.033662` because both switch inequalities are strict.

The positive cell is a new off-diagonal witness; the negative cell reuses and independently checks the PREFIX-774 cell. The candidate search used an exploratory floating-point scan of 441 selected cells; only the two exact cells above constitute this theorem's certified finite domain. Float values did not decide any rigorous sign or bound.

## 4. Reproduction, scope and next question

Run:

```bash
python3 research_notes/portable_direct/PREFIX775_R6_TWO_GRID_CELLS_EXACT_CHECK.py
```

The program uses only Python's standard library, writes `PREFIX775_R6_TWO_GRID_CELLS_RESULTS.json`, and prints `ALL_CHECKS_PASS PREFIX775 TWO_GRID_CELL_SIGN` in its result field. It checks both cells at `q=0.033662` and `q=2`.

This gives a finite two-cell sign obstruction for the **external Gamma auxiliary lattice**; it does not add original-comparator `1/768` exclusion cells. The continuous global threshold `q_c` studied in PREFIX-773 remains a distinct question. Next: certify a *complete* low-cost region or optimize the positive-grid witness's switch threshold; compare exact off-diagonal/edge cells with the pointwise diagonal candidate and assess a native-source bridge only with its typed observer/port requirements. No independent review or formal Result admission is claimed.

Provenance: PREFIX-774 exact moment identities and frozen survivor recurrence; PREFIX-773 pointwise Gamma critical ratio.