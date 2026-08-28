# Enterprise BRC Half-Coupling Inert Minus Unit-Tail Block Cancellation Bridge — Research Return

Status: `FINAL_FROZEN / PROOF_NOT_CLOSED_WITH_SMALLER_CANCELLATION_IDENTITY / EXACT_SECOND_ORDER_REDUCTION`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-UNIT-TAIL-BLOCK-CANCELLATION-BRIDGE`  
Publication: `TP2-1D36A3FD357DED15E27B`  
Claim: `chatgpt-ebp4m-20260827-2236`  
Researcher-ID: `EM-EBP4M-7C31D2`  
Execution: `ER-7C31D2A4F8E19B506D23`

## Frozen verdict

`PRIMARY_VERDICT = PROOF_NOT_CLOSED_WITH_SMALLER_CANCELLATION_IDENTITY`.

For every prime \(p\equiv17,23\pmod{24}\), this execution proves the full first cancellation layer:
\[
p\mid T_{00},\qquad p\mid T_{01},\qquad p^2\mid T_{02},\qquad p^2\mid T_{11},
\]
and also proves \(p\mid G_p\). The original derivative-weighted target
\[
G_pH_p-T_p\equiv-p\pmod{p^3}
\]
is not claimed proved or refuted. It is reduced exactly to two explicit finite congruences modulo \(p\), denoted `(R0-)` and `(R1-)`.

## Frozen parent inputs

Let
\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}2^{-k},\qquad
G_p=\sum_{k=0}^{p-1}B_k,\qquad
H_p=\sum_{k=0}^{p-1}(12k+1)B_k,
\]
and
\[
T_p=\sum_{\substack{0\le i,j<p\\i+j\ge p}}
(1+6(i+j))B_iB_j.
\]
The parent proved the exact finite identity \(S_p=G_pH_p-T_p\).

For \(p=6m+5\), it also proved
\[
v_p(B_k)=
\begin{cases}
0,&0\le k\le4m+3,\\
1,&4m+4\le k\le5m+4,\\
2,&5m+5\le k\le p-1.
\end{cases}
\]
Call these blocks \(I_0,I_1,I_2\). Modulo \(p^3\), only `00`, two-sided `01`, two-sided `02`, and `11` survive.

## 1. Three block divisibilities are termwise

From the valuation split alone,
\[
\boxed{p\mid T_{01}},\qquad
\boxed{p^2\mid T_{02}},\qquad
\boxed{p^2\mid T_{11}}.
\]
Thus the only genuine aggregate-cancellation problem is \(p\mid T_{00}\).

## 2. Exact factorization of the unit tail

Put
\[
A=5m+4,\qquad B=4m+3.
\]
Modulo \(p\),
\[
B_k\equiv w_k:=\binom Ak\binom Bk2^{-k}\qquad(0\le k\le B).
\]
Reverse the `00` tail by \(i=B-u,\ j=B-v\). The condition \(i+j\ge p\) becomes
\[
u,v\ge0,\qquad u+v\le2m+1.
\]
With \(C_m=\binom{2m+1}{m}\),
\[
w_{B-u}\equiv(-1)^{m+1}2^{-B}C_m\,r_u\,2^u\pmod p,
\qquad
r_u=\frac{(2m+2)_u^2}{(m+2)_u\,u!}.
\]
Also
\[
1+6(i+j)\equiv-3(2(u+v)+1)\pmod p.
\]

Define
\[
R_m(x)={}_2F_1(2m+2,2m+2;m+2;x),
\qquad
Q_m(x)={}_2F_1(-m,-m;m+2;x).
\]
Euler transformation gives
\[
R_m(x)=(1-x)^{-3m-2}Q_m(x),
\]
hence
\[
R_m(x)^2=(1-x)^{-(p-1)}Q_m(x)^2.
\]
For \(0\le s<p\),
\[
[x^s](1-x)^{-(p-1)}\equiv
\begin{cases}
1,&s=0,\\
-1,&s=1,\\
0,&2\le s<p
\end{cases}
\pmod p.
\]
Since the reversed triangle stops at degree \(2m+1<p\), applying \(1+2x\,d/dx\) at \(x=2\) yields
\[
\boxed{
T_{00}\equiv
3\,2^{-2B}C_m^2Q_m(2)\bigl(5Q_m(2)+8Q_m'(2)\bigr)
\pmod p.
}
\tag{F00}
\]

## 3. Legendre/CM vanishing proves \(p\mid T_{00}\) and \(p\mid G_p\)

Define
\[
\mathcal A_m=C_mQ_m(2).
\]
Pfaff transformation gives the exact finite identity
\[
\mathcal A_m
={}_2F_1(-m,2m+2;1;-1)
=\sum_{k=0}^{m}2^{m-k}\binom mk\binom{2m+1}{k}.
\tag{A}
\]

Let \(P_n(x)\) be the ordinary Legendre polynomial and choose \(t^2=1/2\). The odd-degree hypergeometric representation gives
\[
2^m\frac{P_{2m+1}(t)}{t}
={}_2F_1\!\left(-m,-m-\frac12;1;-1\right).
\]
The second upper parameters differ by
\[
(2m+2)-\left(-m-\frac12\right)=\frac p2,
\]
so the terminating series are termwise congruent modulo \(p\):
\[
\boxed{
\mathcal A_m\equiv
2^m\frac{P_{2m+1}(t)}{t}\pmod p.
}
\tag{AL}
\]

For \(p\equiv17,23\pmod{24}\), \(\lfloor p/3\rfloor=2m+1\), and \(2\) is a quadratic residue modulo \(p\). Zhi-Hong Sun, *Congruences involving* \(\binom{2k}{k}^2\binom{3k}{k}m^{-k}\), arXiv:1104.2789v3, Theorem 4.5, proves
\[
P_{\lfloor p/3\rfloor}\!\left(\frac{\sqrt2}{2}\right)\equiv0\pmod p
\]
for exactly these two residue classes. Therefore
\[
p\mid\mathcal A_m,\qquad p\mid Q_m(2).
\]
Since \(C_m\) is a \(p\)-unit, `(F00)` gives
\[
\boxed{p\mid T_{00}}.
\]
Together with the termwise results, all four parent candidate block divisibilities are now proved.

The same \(\mathcal A_m\) also controls \(G_p\). Modulo \(p\),
\[
G_p\equiv
2^{-B}{}_2F_1(-B,A+1;1;-1)
\equiv2^{-B}\mathcal A_m,
\]
because \(-B\equiv2m+2\pmod p\), \(A+1\equiv-m\pmod p\), and the terminating terms beyond \(k=m\) vanish. Hence
\[
\boxed{p\mid G_p}
\qquad(p\equiv17,23\pmod{24}).
\]

## 4. Exact two-rate deformation

Set
\[
b_{m,k}(\varepsilon)=
\frac{(-A+5\varepsilon/6)_k(-B+2\varepsilon/3)_k}
{(k!)^2 2^k}.
\]
Then \(B_k=b_{m,k}(p)\) exactly. Its Taylor vanishing orders are \(0,1,2\) on \(I_0,I_1,I_2\).

For \(k\in I_0\), write
\[
b_{m,k}(\varepsilon)
=w_k(1+L_k\varepsilon+Q_k\varepsilon^2)+O(\varepsilon^3),
\]
where
\[
L_k=-\frac56(H_A-H_{A-k})-\frac23(H_B-H_{B-k}),
\]
\[
Q_k=\frac12\!\left[
L_k^2-\frac{25}{36}(H_A^{(2)}-H_{A-k}^{(2)})
-\frac49(H_B^{(2)}-H_{B-k}^{(2)})
\right].
\]
For \(B<k\le A\),
\[
b_{m,k}(\varepsilon)=d_k\varepsilon+d_kM_k\varepsilon^2+O(\varepsilon^3),
\]
with
\[
d_k=\frac{2(-1)^{B+k}}3
\frac{A!B!(k-B-1)!}{(A-k)!(k!)^2 2^k},
\qquad
M_k=-\frac56(H_A-H_{A-k})+\frac23(H_{k-B-1}-H_B).
\]
For \(A<k<p\),
\[
b_{m,k}(\varepsilon)=v_k\varepsilon^2+O(\varepsilon^3),
\]
where
\[
v_k=\frac{5(-1)^{A+B}}9
\frac{A!B!(k-A-1)!(k-B-1)!}{(k!)^2 2^k}.
\]

Define
\[
F_0=\sum_{I_0}w_k,\quad
F_1=\sum_{I_0}w_kL_k+\sum_{I_1}d_k,\quad
F_2=\sum_{I_0}w_kQ_k+\sum_{I_1}d_kM_k+\sum_{I_2}v_k,
\]
\[
J_0=\sum_{I_0}(12k+1)w_k,\qquad
J_1=\sum_{I_0}(12k+1)w_kL_k+\sum_{I_1}(12k+1)d_k.
\]
Then
\[
G_p\equiv F_0+pF_1+p^2F_2\pmod{p^3},
\qquad
H_p\equiv J_0+pJ_1\pmod{p^2}.
\]

For the tail, retaining \(i+j\ge p\) and \(W_{ij}=1+6(i+j)\), define
\[
T_{00}^{(0)}=\sum_{I_0I_0}W_{ij}w_iw_j,
\]
\[
T_{00}^{(1)}=\sum_{I_0I_0}W_{ij}w_iw_j(L_i+L_j),
\]
\[
T_{00}^{(2)}=\sum_{I_0I_0}W_{ij}w_iw_j(Q_i+Q_j+L_iL_j),
\]
\[
U_{01}^{(0)}=2\sum_{I_0I_1}W_{ij}w_id_j,\quad
U_{01}^{(1)}=2\sum_{I_0I_1}W_{ij}w_id_j(L_i+M_j),
\]
\[
U_{02}^{(0)}=2\sum_{I_0I_2}W_{ij}w_iv_j,\qquad
U_{11}^{(0)}=\sum_{I_1I_1}W_{ij}d_id_j.
\]
Then
\[
T_p\equiv
T_{00}^{(0)}
+p(T_{00}^{(1)}+U_{01}^{(0)})
+p^2(T_{00}^{(2)}+U_{01}^{(1)}+U_{02}^{(0)}+U_{11}^{(0)})
\pmod{p^3}.
\tag{T2-}
\]

The proved divisibilities imply \(p\mid F_0\) and \(p\mid T_{00}^{(0)}\). Set
\[
g_0=\frac{F_0}{p}+F_1,\qquad g_1=F_2,
\]
\[
\tau_0=\frac{T_{00}^{(0)}}p+T_{00}^{(1)}+U_{01}^{(0)},
\qquad
\tau_1=T_{00}^{(2)}+U_{01}^{(1)}+U_{02}^{(0)}+U_{11}^{(0)}.
\]
Then the original target is exactly equivalent to
\[
\boxed{
(g_0+pg_1)(J_0+pJ_1)-(\tau_0+p\tau_1)\equiv-1\pmod{p^2}.
}
\tag{R2-}
\]
Equivalently:
\[
\boxed{g_0J_0-\tau_0\equiv-1\pmod p,}
\tag{R0-}
\]
\[
\boxed{
\frac{g_0J_0-\tau_0+1}{p}
+g_0J_1+g_1J_0-\tau_1\equiv0\pmod p.
}
\tag{R1-}
\]
`(R0-)` and `(R1-)` remain unproved all-prime; they are the smallest exact residue.

## 5. Independent routes and regression

Three distinct exact routes were used:

1. reverse-tail generating-function factorization, producing `(F00)`;
2. Pfaff + Legendre/CM vanishing, proving \(p\mid T_{00}\) and \(p\mid G_p\);
3. two-rate \(p\)-adic parameter deformation, producing `(R0-)` and `(R1-)`.

Checker:
`scripts/check_enterprise_brc_half_coupling_inert_minus_unit_tail_block_cancellation_bridge.py`.

Frozen finite regression:
- all primes \(p=6m+5\le300\): `32`;
- target primes \(p\equiv17,23\pmod{24}\): `15`;
- failures: `0`.

This regression is falsification evidence only. The imported Sun theorem, not the scan, proves the all-prime CM vanishing used above.

## Final boundary

Closed:
- all four parent block divisibilities;
- unit-tail cancellation modulo \(p\);
- \(p\mid G_p\) in both minus classes;
- exact reduction of the mod-\(p^3\) target to `(R0-) + (R1-)`.

Not closed:
- all-prime proofs of `(R0-)` and `(R1-)`;
- therefore the full derivative-weighted supercongruence.

`HARD_TARGET = ACHIEVED_AT_EXACT_REDUCTION_STRENGTH`.  
`MINUS_TARGET = UNPROVED_UNREFUTED`.  
`SMALLEST_EXACT_REMAINING_IDENTITY = (R0-) + (R1-)`.  
`FOUNDATION_MUTATION = NONE`.  
`WORKING_TRUTH = NOT_GRANTED`.  
`NOVELTY_OR_PRIORITY_CLAIM = NONE`.

Recommended Driver action: accept this strict exact reduction; if continuation remains valuable, publish only one narrow successor for the second-order CM/Jacobi lift `(R0-) + (R1-)`. Do not reopen the closed unit-tail mod-\(p\) cancellation layer.
