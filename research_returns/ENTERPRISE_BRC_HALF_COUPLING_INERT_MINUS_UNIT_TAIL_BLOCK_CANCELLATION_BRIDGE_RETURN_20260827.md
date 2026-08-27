# Enterprise BRC Half-Coupling Inert Minus Unit-Tail Block Cancellation Bridge — Research Return

Status: `FINAL_FROZEN / PROOF_NOT_CLOSED_WITH_SMALLER_CANCELLATION_IDENTITY / EXACT_SECOND_ORDER_REDUCTION`

Date: `2026-08-27`

Researcher-ID: `EM-EBP4M-7C31D2`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-UNIT-TAIL-BLOCK-CANCELLATION-BRIDGE`

Publication: `TP2-1D36A3FD357DED15E27B`

Claim: `chatgpt-ebp4m-20260827-2236`

Execution: `ER-7C31D2A4F8E19B506D23`

## 1. Frozen verdict

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_SMALLER_CANCELLATION_IDENTITY`.

`HARD_TARGET_DISPOSITION = ACHIEVED_AT_EXACT_REDUCTION_STRENGTH`.

The original all-prime minus target

\[
G_pH_p-T_p\equiv-p\pmod{p^3},
\qquad p\equiv17,23\pmod{24},
\]

is **not** claimed proved here and no counterexample was found.

The execution does close the first genuinely missing cancellation layer from the parent. In particular, the parent only had bounded evidence for

\[
p\mid T_{00},\qquad p\mid T_{01},\qquad p^2\mid T_{02},\qquad p^2\mid T_{11}.
\]

This task proves all four divisibilities uniformly for the two requested residue classes. More sharply:

- `T01` is termwise divisible by `p` from the already-proved valuation split;
- `T02` and `T11` are termwise divisible by `p^2`;
- **only `T00` requires genuine aggregate cancellation**;
- `T00 mod p` admits an exact one-variable factorization;
- the required vanishing factor is identified with a Legendre/CM value covered by Zhi-Hong Sun's proved Theorem 4.5;
- the same CM bridge also proves `p | G_p` in the minus classes;
- after these divisibilities are proved, the full mod-`p^3` target is exactly normalized to one mod-`p^2` finite certificate, equivalently two explicit scalar congruences `(R0-)` and `(R1-)` modulo `p`.

Thus the former four-block cancellation problem has been reduced to one second-order finite identity. The target remains unproved/unrefuted only at that second p-adic digit.

## 2. Frozen parent inputs

For

\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}\,2^{-k},
\qquad
G_p=\sum_{k=0}^{p-1}B_k,
\qquad
H_p=\sum_{k=0}^{p-1}(12k+1)B_k,
\]

the parent proved the exact finite Clausen identity

\[
S_p=G_pH_p-T_p,
\]

where

\[
T_p=
\sum_{\substack{0\le i,j<p\\i+j\ge p}}
(1+6(i+j))B_iB_j.
\]

For `p=6m+5`, the parent also proved

\[
v_p(B_k)=
\begin{cases}
0,&0\le k\le 4m+3,\\
1,&4m+4\le k\le 5m+4,\\
2,&5m+5\le k\le 6m+4.
\end{cases}
\tag{V}
\]

Write the corresponding index blocks as `I0,I1,I2`. Modulo `p^3` only

\[
00,\quad 01+10,\quad 02+20,\quad 11
\]

survive; `12+21` and `22` vanish termwise.

## 3. First correction: three of the four candidate divisibilities are immediate

The parent correctly identified a valuation-zero `I0 x I0` triangle, but the bounded divisibility pattern should be split more sharply.

From `(V)` alone, every term in the two-sided `01` block has valuation at least one, hence

\[
\boxed{p\mid T_{01}.}
\]

Every term in the two-sided `02` block and every term in the `11` block has valuation at least two, hence

\[
\boxed{p^2\mid T_{02},\qquad p^2\mid T_{11}.}
\]

Therefore the **only** candidate divisibility requiring cancellation is

\[
\boxed{p\mid T_{00}.}
\]

This removes three unnecessary cancellation obligations before any new machinery is introduced.

## 4. Exact reverse-tail factorization of the unit block

Put

\[
A=5m+4,\qquad B=4m+3,
\]

so `p=6m+5`. Modulo `p`, the low coefficients are

\[
w_k:=B_k\equiv
\binom Ak\binom Bk2^{-k},
\qquad 0\le k\le B.
\]

Reverse the low block by writing

\[
i=B-u,\qquad j=B-v.
\]

The tail condition becomes

\[
u,v\ge0,\qquad u+v\le 2m+1.
\]

Using

\[
\binom{p-r}{k}\equiv(-1)^k\binom{r+k-1}{k}\pmod p,
\]

one obtains, for every relevant `u`,

\[
w_{B-u}\equiv
(-1)^{m+1}2^{-B}inom{2m+1}{m}\,r_u\,2^u\pmod p,
\]

where

\[
r_u=\frac{(2m+2)_u^2}{(m+2)_u\,u!}.
\]

Also

\[
1+6(i+j)\equiv-3\bigl(2(u+v)+1\bigr)\pmod p.
\]

Define

\[
R_m(x)=\sum_{u\ge0}r_ux^u
={}_2F_1(2m+2,2m+2;m+2;x)
\]

and

\[
Q_m(x)={}_2F_1(-m,-m;m+2;x).
\]

Euler's transformation gives

\[
R_m(x)=(1-x)^{-3m-2}Q_m(x),
\]

hence

\[
R_m(x)^2=(1-x)^{-(6m+4)}Q_m(x)^2
=(1-x)^{-(p-1)}Q_m(x)^2.
\]

For degrees `0<=s<p`,

\[
[x^s](1-x)^{-(p-1)}\equiv
\begin{cases}
1,&s=0,\\
-1,&s=1,\\
0,&2\le s<p
\end{cases}
\pmod p.
\]

Since the unit triangle stops at degree `2m+1<p`, its entire convolution is therefore governed modulo `p` by

\[
(1-x)Q_m(x)^2.
\]

Applying the weight operator `1+2 theta`, with `theta=x d/dx`, and evaluating at `x=2` yields

\[
(1+2\theta)\bigl((1-x)Q_m(x)^2\bigr)\big|_{x=2}
=-Q_m(2)\bigl(5Q_m(2)+8Q_m'(2)\bigr).
\]

Consequently, with

\[
C_m=\binom{2m+1}{m},
\]

we obtain the exact factorization

\[
\boxed{
T_{00}\equiv
3\,2^{-2B}C_m^2\,
Q_m(2)\bigl(5Q_m(2)+8Q_m'(2)\bigr)
\pmod p.
}
\tag{F00}
\]

This is the first main theorem of the execution: a double triangular unit-tail cancellation problem has become a product of two one-variable finite hypergeometric values.

## 5. The vanishing factor is a proved CM/Legendre value

Define

\[
\mathcal A_m:=C_mQ_m(2).
\]

A direct Pfaff transformation gives the exact finite identity

\[
\mathcal A_m
=
{}_2F_1(-m,2m+2;1;-1)
=
\sum_{k=0}^{m}2^{m-k}inom mk\binom{2m+1}{k}.
\tag{A}
\]

Now let `L_n(x)` denote the ordinary Legendre polynomial. The standard odd-degree hypergeometric representation at `t^2=1/2` gives

\[
2^m\frac{L_{2m+1}(t)}{t}
={}_2F_1\left(-m,-m-\frac12;1;-1\right),
\qquad t^2=\frac12.
\tag{L}
\]

But

\[
(2m+2)-\left(-m-\frac12\right)
=3m+\frac52
=\frac p2.
\]

Therefore the two terminating series in `(A)` and `(L)` are termwise congruent modulo `p`:

\[
\boxed{
\mathcal A_m
\equiv
2^m\frac{L_{2m+1}(t)}{t}
\pmod p,
\qquad t^2=\frac12.
}
\tag{AL}
\]

For `p≡17,23 (mod24)`, one has `p≡1,7 (mod8)`, so `2` is a quadratic residue modulo `p`. Moreover

\[
\left\lfloor\frac p3\right\rfloor=2m+1.
\]

Zhi-Hong Sun, *Congruences involving* `binom(2k,k)^2 binom(3k,k) m^{-k}`, arXiv:1104.2789v3, Theorem 4.5, proves

\[
L_{\lfloor p/3\rfloor}\left(\frac{\sqrt2}{2}\right)
\equiv0\pmod p
\]

for exactly `p≡17,23 (mod24)`.

Combining this theorem with `(AL)` gives

\[
\boxed{p\mid\mathcal A_m,\qquad p\mid Q_m(2).}
\tag{CM}
\]

Since `C_m` is a `p`-unit, `(F00)` now yields the desired all-prime cancellation theorem

\[
\boxed{p\mid T_{00}}
\qquad(p\equiv17,23\pmod{24}).
\tag{D00}
\]

Thus all four parent candidate block divisibilities are proved.

### 5.1 The same bridge proves `p | G_p`

Modulo `p`, the full `G_p` truncation stops at `B=4m+3`. Pfaff gives

\[
G_p
\equiv
2^{-B}
{}_2F_1(-B,A+1;1;-1)
\pmod p.
\]

Because

\[
-B\equiv2m+2\pmod p,
\qquad
A+1=5m+5\equiv-m\pmod p,
\]

the terms after `k=m` vanish and

\[
\boxed{G_p\equiv2^{-B}\mathcal A_m\pmod p.}
\tag{GA}
\]

Hence `(CM)` also gives

\[
\boxed{p\mid G_p}
\qquad(p\equiv17,23\pmod{24}).
\tag{DG}
\]

This divisibility is independent of the still-conjectural derivative-weighted mod-`p^3` target.

## 6. Exact minus-class parameter deformation

The minus classes admit a two-rate deformation that makes the parent `0/1/2` valuation split structural.

Put

\[
b_{m,k}(\varepsilon)=
\frac{(-A+5\varepsilon/6)_k(-B+2\varepsilon/3)_k}
{(k!)^2 2^k}.
\]

Since

\[
-A+\frac{5p}{6}=\frac16,
\qquad
-B+\frac{2p}{3}=\frac13,
\]

we have the exact identity

\[
\boxed{B_k=b_{m,k}(p).}
\]

The zero positions at `B` and `A` immediately reproduce the three Taylor orders:

- `0<=k<=B`: order `0`;
- `B<k<=A`: order `1`;
- `A<k<p`: order `2`.

For the low block define

\[
w_k=\binom Ak\binom Bk2^{-k},
\]

\[
L_k=-\frac56(H_A-H_{A-k})-\frac23(H_B-H_{B-k}),
\]

\[
Q_k=\frac12\left(
L_k^2
-\frac{25}{36}(H_A^{(2)}-H_{A-k}^{(2)})
-\frac49(H_B^{(2)}-H_{B-k}^{(2)})
\right).
\]

Then

\[
b_{m,k}(\varepsilon)
=w_k(1+L_k\varepsilon+Q_k\varepsilon^2)+O(\varepsilon^3).
\tag{E0}
\]

For `B<k<=A`, put

\[
d_k=
\frac{2(-1)^{B+k}}3
\frac{A!B!(k-B-1)!}{(A-k)!(k!)^2 2^k},
\]

\[
M_k=-\frac56(H_A-H_{A-k})
+\frac23(H_{k-B-1}-H_B),
\]

so

\[
b_{m,k}(\varepsilon)
=d_k\varepsilon+d_kM_k\varepsilon^2+O(\varepsilon^3).
\tag{E1}
\]

For `A<k<p`, put

\[
v_k=
\frac{5(-1)^{A+B}}9
\frac{A!B!(k-A-1)!(k-B-1)!}{(k!)^2 2^k},
\]

so

\[
b_{m,k}(\varepsilon)=v_k\varepsilon^2+O(\varepsilon^3).
\tag{E2}
\]

All denominators are `p`-adic units.

Define

\[
F_0=\sum_{I_0}w_k,
\]

\[
F_1=\sum_{I_0}w_kL_k+\sum_{I_1}d_k,
\]

\[
F_2=\sum_{I_0}w_kQ_k+\sum_{I_1}d_kM_k+\sum_{I_2}v_k,
\]

and

\[
J_0=\sum_{I_0}(12k+1)w_k,
\]

\[
J_1=\sum_{I_0}(12k+1)w_kL_k+
\sum_{I_1}(12k+1)d_k.
\]

Then

\[
\boxed{G_p\equiv F_0+pF_1+p^2F_2\pmod{p^3},}
\tag{G2-}
\]

\[
\boxed{H_p\equiv J_0+pJ_1\pmod{p^2}.}
\tag{H1-}
\]

By `(DG)`, `F_0` is divisible by `p` in `Z_p`.

## 7. Exact first-two-digit tail expansion

Let every sum below retain the tail condition `i+j>=p` and the weight

\[
W_{ij}=1+6(i+j).
\]

Define the ordered low-low coefficients

\[
T_{00}^{(0)}=\sum_{I_0I_0}W_{ij}w_iw_j,
\]

\[
T_{00}^{(1)}=\sum_{I_0I_0}W_{ij}w_iw_j(L_i+L_j),
\]

\[
T_{00}^{(2)}=\sum_{I_0I_0}W_{ij}w_iw_j(Q_i+Q_j+L_iL_j).
\]

For the two-sided mixed blocks define

\[
U_{01}^{(0)}=2\sum_{I_0I_1}W_{ij}w_id_j,
\]

\[
U_{01}^{(1)}=2\sum_{I_0I_1}W_{ij}w_id_j(L_i+M_j),
\]

\[
U_{02}^{(0)}=2\sum_{I_0I_2}W_{ij}w_iv_j,
\]

and

\[
U_{11}^{(0)}=\sum_{I_1I_1}W_{ij}d_id_j.
\]

Substituting `epsilon=p` into `(E0)-(E2)` gives the exact reconstruction

\[
\boxed{
T_p\equiv
T_{00}^{(0)}
+p\bigl(T_{00}^{(1)}+U_{01}^{(0)}\bigr)
+p^2\bigl(T_{00}^{(2)}+U_{01}^{(1)}+U_{02}^{(0)}+U_{11}^{(0)}\bigr)
\pmod{p^3}.
}
\tag{T2-}
\]

The proved `(D00)` says `T_{00}^{(0)}` is divisible by `p` in `Z_p`. Therefore all normalizations below are legitimate.

Set

\[
g_0=\frac{F_0}{p}+F_1,
\qquad g_1=F_2,
\]

\[
\tau_0=
\frac{T_{00}^{(0)}}p+T_{00}^{(1)}+U_{01}^{(0)},
\]

\[
\tau_1=
T_{00}^{(2)}+U_{01}^{(1)}+U_{02}^{(0)}+U_{11}^{(0)}.
\]

Then

\[
\frac{G_p}{p}\equiv g_0+pg_1\pmod{p^2},
\qquad
\frac{T_p}{p}\equiv\tau_0+p\tau_1\pmod{p^2}.
\]

The original minus target is therefore **exactly equivalent** to the single second-order certificate

\[
\boxed{
(g_0+pg_1)(J_0+pJ_1)-(\tau_0+p\tau_1)
\equiv-1\pmod{p^2}.
}
\tag{R2-}
\]

Splitting into p-adic digits gives

\[
\boxed{g_0J_0-\tau_0\equiv-1\pmod p,}
\tag{R0-}
\]

and

\[
\boxed{
\frac{g_0J_0-\tau_0+1}{p}
+g_0J_1+g_1J_0-\tau_1
\equiv0\pmod p.
}
\tag{R1-}
\]

This is the terminal exact reduction of this execution.

The all-prime truth of `(R0-)` and `(R1-)` is **not proved here**. They are strictly smaller than the parent problem because the valuation-zero tail has already been proved to cancel modulo `p`, every remaining quantity is normalized, and only two scalar p-adic digits remain.

## 8. Two distinct exact routes were used

The task required at least two structurally distinct exact routes before returning unclosed.

### Route A — reverse-tail generating-function factorization

The `I0 x I0` triangle was reversed, converted to a low-degree convolution of

\[
{}_2F_1(2m+2,2m+2;m+2;x)^2,
\]

then collapsed modulo `p` through Euler transformation and the coefficient degeneration of `(1-x)^{-(p-1)}`. This produces `(F00)` directly from the tail geometry.

### Route B — Pfaff/Legendre/CM bridge

Independently, the low finite hypergeometric sum was transformed to `A_m`; a termwise parameter congruence identifies `A_m` with a Legendre value; Zhi-Hong Sun's proved CM theorem forces that value to vanish in the two requested residue classes. This gives `(CM)`, `(D00)`, and `(DG)`.

### Route C — two-rate p-adic parameter deformation

A third exact mechanism then reconstructs the first two p-adic digits of `G_p,H_p,T_p` and yields `(R0-)+(R1-)`. It does not assume the target sign.

The three routes agree on their overlaps but have different algebraic inputs and failure modes.

## 9. Deterministic checker and bounded falsification

Task-local checker:

`scripts/check_enterprise_brc_half_coupling_inert_minus_unit_tail_block_cancellation_bridge.py`

Frozen certificate:

`research_artifacts/ENTERPRISE_BRC_HALF_COUPLING_INERT_MINUS_UNIT_TAIL_BLOCK_CANCELLATION_BRIDGE/reduction_certificate_20260827.json`

The checker independently verifies on the finite test set:

1. direct `B_k` recurrence and block decomposition;
2. the reverse-tail factor `(F00)`;
3. the finite `A_m`/Legendre bridge `(AL)`;
4. the `G_p`/`A_m` bridge `(GA)`;
5. all four block divisibilities in the target classes;
6. the exact deformation reconstructions `(G2-)`, `(H1-)`, `(T2-)`;
7. normalized `(R0-)`, `(R1-)`, and `(R2-)`;
8. the original target as a regression guard only.

Frozen run:

- all primes `p=6m+5 <= 300`: `32`;
- target primes `p≡17,23 (mod24)`: `15`;
- class `17`: `8` primes;
- class `23`: `7` primes;
- failures: `0`.

This is `FINITE_REGRESSION_ONLY_NOT_A_PROOF`.

The imported Sun theorem, not the finite scan, is what upgrades `p|T00` and `p|G_p` to all-prime statements in the requested classes.

## 10. Prior-art and theorem boundary

The CM zero used here is imported from:

Zhi-Hong Sun, *Congruences involving* `binom(2k,k)^2 binom(3k,k) m^{-k}`, arXiv:1104.2789v3, Theorem 4.5.

That theorem proves the needed Legendre zero for `p≡17,23 (mod24)` and also a related unweighted mod-`p^2` congruence. Only the Legendre-zero statement is load-bearing here.

The derivative-weighted target remains the `a=1` specialization of Zhi-Wei Sun's Conjecture A14(ii). No all-prime proof of that conjectural mod-`p^3` target is imported or claimed.

No novelty or priority claim is made for the imported CM theorem or for the original supercongruence statement.

## 11. What is now closed

Closed exactly for every prime `p≡17,23 (mod24)`:

1. `T01` is divisible by `p` termwise;
2. `T02` and `T11` are divisible by `p^2` termwise;
3. the unit block has the one-variable factorization `(F00)`;
4. the CM/Legendre bridge forces `p|T00`;
5. the same bridge forces `p|G_p`;
6. the full tail is divisible by `p`;
7. the first two p-adic digits of the target are represented by the explicit finite deformation quantities above;
8. the original target is exactly equivalent to `(R0-)+(R1-)`.

Not closed:

1. an all-prime proof of `(R0-)`;
2. an all-prime proof of `(R1-)`;
3. therefore the full derivative-weighted `S_p≡-p mod p^3` theorem.

No exact counterexample was found.

## 12. Smallest unresolved identity and recommendation

The smallest remaining unit is no longer a four-block cancellation theorem. It is:

> Prove `(R0-)` and `(R1-)` uniformly for `p≡17,23 (mod24)`, equivalently obtain a `p^2` lift of the CM/reverse-tail factorization together with the first p-adic digits of the middle/high deformation blocks.

A useful next proof should target a terminating creative-microscoping/WZ certificate, a finite-field/Jacobi-sum lift of `(AL)`, or a Dwork/Cartier first-derivative lift. Broadening the prime scan is not successor-worthy.

## 13. Final freeze

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_SMALLER_CANCELLATION_IDENTITY`.

`HARD_TARGET = ACHIEVED_AT_EXACT_REDUCTION_STRENGTH`.

`UNIT_TAIL_MOD_P_CANCELLATION = PROVED`.

`ALL_FOUR_PARENT_BLOCK_DIVISIBILITIES = PROVED`.

`G_P_DIVISIBILITY = PROVED_FOR_17_23_MOD24`.

`MINUS_TARGET = UNPROVED_UNREFUTED`.

`SMALLEST_EXACT_REMAINING_IDENTITY = (R0-)+(R1-)`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH = NOT_GRANTED`.

`NOVELTY_OR_PRIORITY_CLAIM = NONE`.

Recommended Driver action: accept the return as a strict exact reduction and, only if continuation value remains high, publish one narrow successor for the second-order CM/Jacobi lift `(R0-)+(R1-)`. Do not reopen the already-closed unit-tail mod-`p` cancellation layer.
