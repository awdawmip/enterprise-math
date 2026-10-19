# P022 Franel Rank-Two Discriminant Bridge — Research Return

Status: `PASS / MINIMAL_EXACT_MATRIX_OBSTRUCTION_FROZEN / DETERMINANT_ONLY_ROUTE_KILLED / ALL-M IMPLICATION OPEN`

Task: `RS-P022-FRANEL-RANK2-DISCRIMINANT-BRIDGE`  
Publication: `TP2-59CF7A99F7C9755E4561`  
Claim: `chatgpt-p022r2d-20260829-1915-6f2a91`  
Researcher: `EM-P022R2D-6F2A91`  
Execution branch: `research/p022-franel-rank2-discriminant-bridge-em-p022r2d-6f2a91`

Hard target:

`P022_RANK2_DISCRIMINANT_BRIDGE_PROVED_OR_REFUTED_OR_MINIMAL_EXACT_MATRIX_OBSTRUCTION_FROZEN`

Disposition:

`MINIMAL_EXACT_MATRIX_OBSTRUCTION_FROZEN / MET`

The original implication

\[
q\mid F_{6m}\Longrightarrow \left(\frac{-2}{q}\right)=-1
\]

is **not** claimed proved or refuted. What is closed here is the determinant-only route: the same quadratic square class already occurs on the Franel coefficient-transfer side, and after composing coefficient transfer with the frozen cusp transfer it cancels exactly. The remaining boundary-zero condition is a genuinely independent projective incidence for a canonically normalized \(\mathrm{SL}_2(\mathbf F_q)\) connection.

---

## 1. Frozen inputs consumed

The return uses only exact material already exposed by the taskbook and its released parent lineage.

1. Frozen rank-two Franel equation:
\[
x(x+1)(8x-1)h''+(24x^2+14x-1)h'+(8x+2)h=0,
\qquad
h(x)=\sum_{n\ge0}F_nx^n.
\]

2. Frozen cusp state and Apéry-side cusp transfer:
\[
v_0=\binom{1}{2},
\qquad
v_{1/8}=\binom{-1}{8/3},
\qquad
v_0=A_0v_{1/8},
\]
with
\[
A_0=
\begin{pmatrix}
-1&0\\
1&9/8
\end{pmatrix},
\qquad
\det A_0=-\frac98.
\]

3. Frozen accepted Hahn boundary equivalence and centered transfer from the released parent:
\[
p\mid F_{2n}
\iff
Q_n(n;-3n,n-1,3n)=0
\qquad (p=6n-1),
\]
and
\[
(s-\tfrac13)(s+\tfrac23)Y_{s+1}
+(\tfrac13-2s^2)Y_s
+(s-\tfrac12)(s+\tfrac16)Y_{s-1}=0.
\]

4. Frozen task specialization:
\[
q=18m-1,\qquad n=3m,\qquad k=6m=\frac{q+1}{3},
\]
with \(q,12m-1,12m+1\) prime.

No scalar dual-Hasse first-jet condition is treated as independent; the parent already proved that route formally adjoint/redundant.

---

## 2. Rank-two Franel coefficient transfer derived directly from the ODE

Taking the coefficient of \(x^n\) in the frozen second-order Franel equation gives, for every \(n\ge1\),

\[
\boxed{
(n+1)^2F_{n+1}
=
\bigl(7n(n+1)+2\bigr)F_n
+
8n^2F_{n-1}.
}
\]

This is derived here from the frozen mother equation rather than imported as an extra arithmetic premise.

For a prime \(p=6M-1>3\), put

\[
k=\frac{p+1}{3}=2M.
\]

For \(1\le j\le k-1\), define

\[
S_j=
\begin{pmatrix}
0&1\\[2mm]
\dfrac{8j^2}{(j+1)^2}
&
\dfrac{7j(j+1)+2}{(j+1)^2}
\end{pmatrix}
\in \operatorname{GL}_2(\mathbf F_p).
\]

All denominators are nonzero because \(j+1\le k<p\), and

\[
\det S_j=-\frac{8j^2}{(j+1)^2}\ne0.
\]

With

\[
W_j=\binom{F_{j-1}}{F_j},
\]

the coefficient recurrence is exactly

\[
W_{j+1}=S_jW_j.
\]

Hence, defining

\[
K_k=S_{k-1}\cdots S_2S_1,
\]

we get the exact connection

\[
\boxed{
K_kv_0
=
K_k\binom{1}{2}
=
\binom{F_{k-1}}{F_k}.
}
\]

Thus the same two-dimensional space that carries the cusp first-jet state also carries a completely explicit coefficient-extraction transfer.

---

## 3. The coefficient-transfer determinant has the same quadratic character as the cusp determinant

The determinant telescopes:

\[
\det K_k
=
\prod_{j=1}^{k-1}
\left(-8\frac{j^2}{(j+1)^2}\right)
=
\boxed{
\frac{(-8)^{k-1}}{k^2}.
}
\]

Because \(k=2M\) is even, \(k-1\) is odd, so

\[
\boxed{
\left(\frac{\det K_k}{p}\right)
=
\left(\frac{-8}{p}\right)
=
\left(\frac{-2}{p}\right).
}
\]

The frozen cusp transfer has

\[
\left(\frac{\det A_0}{p}\right)
=
\left(\frac{-9/8}{p}\right)
=
\left(\frac{-2}{p}\right).
\]

Therefore the two independent-looking rank-two transports carry **the same square class**.

More strongly,

\[
\frac{\det K_k}{\det A_0}
=
\frac{(-8)^k}{9k^2}
=
\boxed{
\left(\frac{(-8)^{k/2}}{3k}\right)^2
},
\]

and

\[
\det(K_kA_0)
=
\frac{9(-8)^k}{64k^2}
=
\boxed{
\left(\frac{3(-8)^{k/2}}{8k}\right)^2
}.
\]

This is exact in \(\mathbf F_p\); no Legendre-symbol heuristic is being used.

---

## 4. Canonical normalized cusp-to-boundary connection

Define the explicit nonzero scalar

\[
\nu_k=\frac{3(-8)^{k/2}}{8k}\in\mathbf F_p^\times
\]

and the normalized connection

\[
\boxed{
J_k=\nu_k^{-1}K_kA_0.
}
\]

Then

\[
\boxed{\det J_k=1,}
\qquad
J_k\in\mathrm{SL}_2(\mathbf F_p).
\]

Since \(A_0v_{1/8}=v_0\),

\[
\boxed{
J_kv_{1/8}
=
\nu_k^{-1}
\binom{F_{k-1}}{F_k}.
}
\]

Define the single projective boundary coefficient

\[
\Xi_p
:=
e_2^TJ_kv_{1/8}.
\]

Then

\[
\boxed{
p\mid F_k
\iff
\Xi_p=0.
}
\]

Because every \(S_j\) is invertible, \(K_k\) is invertible. Therefore \(F_{k-1}\) and \(F_k\) cannot both vanish modulo \(p\). On the zero locus,

\[
p\mid F_k
\quad\Longleftrightarrow\quad
J_k[v_{1/8}]=[1:0]
\quad\text{in }\mathbf P^1(\mathbf F_p).
\]

This is the promised strictly smaller named matrix obstruction:

\[
\boxed{
\texttt{NORMALIZED\_CUSP\_TO\_BOUNDARY\_PROJECTIVE\_CONNECTION}
}
\]

with residual scalar/projective condition \(\Xi_p=0\).

---

## 5. Consequence for the requested discriminant implication

Now specialize to the task:

\[
q=18m-1,\qquad k=6m.
\]

The desired implication becomes

\[
\Xi_q=0
\Longrightarrow
\left(\frac{-2}{q}\right)=-1.
\]

Equivalently, since

\[
q\equiv2m-1\pmod8,
\]

the still-open load-bearing statement is

\[
\boxed{
m\equiv1,2\pmod4
\ \text{and the admissible prime-triple gate holds}
\Longrightarrow
\Xi_q\ne0.
}
\]

The crucial boundary is now exact:

- \(\det A_0\) has square class \((-2/q)\);
- \(\det K_{6m}\) has the **same** square class;
- their composition has square determinant;
- after the explicit normalization above, \(\det J_{6m}=1\) in **every** residue sector.

Therefore a proof based only on the square class of \(\det A_0\), or on determinant data that does not distinguish the specific projective orbit of \(J_{6m}\), cannot close the theorem.

This is not merely a failure to find a determinant proof. Abstractly,
\(\mathrm{SL}_2(\mathbf F_q)\) acts transitively on
\(\mathbf P^1(\mathbf F_q)\). Hence determinant \(1\) alone places no
projective restriction preventing

\[
J_{6m}[v_{1/8}]=[1:0].
\]

The arithmetic content must therefore constrain the **specific transfer
product** \(J_{6m}\), not merely its determinant.

This kills the determinant-only discriminant route without changing the
problem's definitions and without refuting the actual arithmetic implication.

---

## 6. Exact three-step Hahn transfer reaches conductor 18

For the released parent's centered Hahn recurrence, write

\[
M_s=
\begin{pmatrix}
-\dfrac{B_s}{A_s}&-\dfrac{C_s}{A_s}\\
1&0
\end{pmatrix},
\]

where

\[
A_s=(s-\tfrac13)(s+\tfrac23),\qquad
B_s=\tfrac13-2s^2,\qquad
C_s=(s-\tfrac12)(s+\tfrac16).
\]

Then

\[
\det M_s
=
\frac{(s-\tfrac12)(s+\tfrac16)}
     {(s-\tfrac13)(s+\tfrac23)}.
\]

Block three consecutive steps:

\[
B_t=M_{3t+2}M_{3t+1}M_{3t}.
\]

Direct multiplication of the three exact determinants gives

\[
\boxed{
\det B_t
=
\frac{
(t+\tfrac12)(t-\tfrac16)(t+\tfrac16)
(t+\tfrac1{18})(t+\tfrac7{18})(t+\tfrac{13}{18})
}{
(t-\tfrac19)
(t+\tfrac29)^2
(t+\tfrac59)^2
(t+\tfrac89)
}.
}
\]

Equivalently,

\[
\det B_t=
\frac{
81(2t+1)(6t-1)(6t+1)
(18t+1)(18t+7)(18t+13)
}{
64(9t-1)(9t+2)^2(9t+5)^2(9t+8)
}.
\]

This is the exact determinant-level bridge requested by the parent return.
It exposes the conductor-18 cubic orbit

\[
\left\{\frac1{18},\frac7{18},\frac{13}{18}\right\}
\]

and the repeated denominator-nine shifts already visible in the frozen
three-section packet. It does **not** identify the full rank-nine Frobenius
system and is not promoted as such.

The next structural step is therefore well-typed: lift this determinant-level
contact to the projective orbit of \(J_{6m}\), for example by an exact
Cartier/Hasse-Witt off-diagonal block, a contiguous conductor-18 transfer, or a
finite-field Frobenius invariant that constrains the \(\mathrm{SL}_2\) orbit.

---

## 7. Regression and falsification controls

The companion checker performs four independent classes of replay:

1. derives/replays the Franel recurrence against
   \(F_n=\sum_r\binom nr^3\) for low exact integer indices;
2. verifies the coefficient transfer, determinant telescoping, cusp
   normalization and \(\det J_k=1\) over several primes \(p\equiv5\pmod6\);
3. verifies the known unrestricted control \(p=149,\ k=50\), where
   \(149\mid F_{50}\), as an actual projective hit
   \(J_{50}[v_{1/8}]=[1:0]\);
4. verifies the three-step Hahn determinant formula exactly over
   \(\mathbf Q\).

A task-local finite falsification scan through \(m\le5000\) finds:

- 137 admissible prime triples
  \((18m-1,12m-1,12m+1)\);
- 72 in the \((-2/q)=+1\) sector;
- 65 in the \((-2/q)=-1\) sector;
- 0 boundary zeros \(F_{6m}\equiv0\pmod q\).

This finite scan is **regression/falsification evidence only**. It is not used
as proof of the all-\(m\) nonvanishing statement.

---

## 8. Theorem-status table

| Item | Status | Exact scope |
|---|---|---|
| Franel rank-two coefficient transfer \(K_k\) | PROVED | all primes \(p=6M-1>3\) |
| \(\det K_k=(-8)^{k-1}/k^2\) | PROVED | same scope |
| \((\det K_k/p)=(-2/p)\) | PROVED | same scope |
| determinant square-match \(K_k\) vs. \(A_0\) | PROVED | same scope |
| normalized \(J_k=\nu_k^{-1}K_kA_0\in SL_2\) | PROVED | same scope |
| \(p\mid F_k\iff J_k[v_{1/8}]=[1:0]\) | PROVED | same scope |
| determinant-only discriminant closure | KILLED | determinant cannot distinguish the projective hit |
| Hahn three-step conductor-18 determinant | PROVED | exact rational identity |
| \(q\mid F_{6m}\Rightarrow(-2/q)=-1\) | OPEN | admissible prime-triple line |
| all-\(m\) nonvanishing of \(\Xi_q\) in square sector | OPEN | \(m\equiv1,2\pmod4\) under admissibility |

---

## 9. Hard-target disposition and recommended next route

Hard target:

`P022_RANK2_DISCRIMINANT_BRIDGE_PROVED_OR_REFUTED_OR_MINIMAL_EXACT_MATRIX_OBSTRUCTION_FROZEN`

Disposition:

\[
\boxed{\texttt{MINIMAL\_EXACT\_MATRIX\_OBSTRUCTION\_FROZEN}}
\]

The surviving object is no longer a vague “matrix invariant”. It is the
explicit normalized connection

\[
J_{6m}\in\mathrm{SL}_2(\mathbf F_q)
\]

and the single projective incidence

\[
J_{6m}[v_{1/8}]=[1:0].
\]

Recommended successor, only if Driver accepts this return:

**Do not reopen determinant square-class work, scalar dual-Hasse first jets, or
larger finite scans.** Construct a conductor-18 Frobenius/Cartier or contiguous
three-section invariant that places \(J_{6m}\) in a proper arithmetic orbit or
subgroup of \(\mathrm{PSL}_2(\mathbf F_q)\), and prove that the square-sector
admissible line \(m\equiv1,2\pmod4\) cannot meet the projective target
\([1:0]\). If no such proper orbit exists, freeze that failure explicitly.

---

## 10. Files

- `research_returns/P022_FRANEL_RANK2_DISCRIMINANT_BRIDGE_RETURN_20260829.md`
- `research_checks/P022_FRANEL_RANK2_DISCRIMINANT_BRIDGE_CHECK_20260829.py`
- `research_artifacts/P022_FRANEL_RANK2_DISCRIMINANT_BRIDGE/exact_regression.json`

No Working Truth, Foundation mutation, factoring claim, or broader P022 closure is granted by this task return.
