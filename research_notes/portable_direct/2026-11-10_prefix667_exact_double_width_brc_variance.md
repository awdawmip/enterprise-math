# PREFIX-667 — Exact double-width native BRC variance strip

Date: 2026-11-10 (Asia/Shanghai). Status: author-side proof and exact finite certificate; independent review pending. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d. Inherited frozen model: 189-layer first-stop native BRC survivor recurrence, available in PREFIX-666 PR #1971 (https://github.com/awdawmip/enterprise-math/pull/1971). This result continues the PREFIX-659/660/661/665/666 observation line.

## Theorem

Let \(J=[607/4096,609/4096]\), \(Q=19/128\), and \(R=[0,1/64]\times J\). For \(12\le q\le24\), define \(\mu(p,z)=\mathbb E[Y]\), \(H(p,z)=\mathbb E[Y^2]/2\), \(W=2H-\mu^2\), \(V_q=q^2W-q\mu\) in the *same frozen first-stop BRC observer*. The exact 16-subinterval Fraction certificate proves on all of \(R\):

\[
\boxed{\mu>88,\qquad \mu_{pp}>200,\qquad H_{pp}<24000,\qquad W_{pp}<-8000.}
\]

Consequently \(V_{q,pp}<-8000q^2\). Using PREFIX-661's boundary derivative \(V_{q,p}(0,z)<-76650\) and PREFIX-660's edge gap \(V_q(0,z_*(q))-V_q(0,z)\ge6400000(z-z_*(q))^2\) and unique \(z_*(q)\in J\), integration proves

\[
\boxed{M_q-V_q(p,z)\ge76650p+4000q^2p^2+6400000(z-z_*(q))^2}
\]

throughout \(R\), where \(M_q=V_q(0,z_*(q))\). Equality can occur only at \(p=0,z=z_*(q)\), the unique maximizer on \(R\). The certified p-width \(1/64\) is twice PREFIX-666's \(1/128\), and 64 times PREFIX-665's \(1/4096\).

The strict curvature bounds are proved here; the stated global-on-R optimum additionally depends on the exact previously published PREFIX-660/661 edge lemmas, which await their respective independent review.

## Frozen BRC observer and algebra

The native integer recurrence has \(A_0(0)=1\); step \(n\) generates \(A_n(k)=A_{n-1}(k)+A_{n-1}(k-1)\), retaining only the native frozen integer threshold predicate \(\operatorname{wide}(n,k)\) in PREFIX666_experiment.py. \(A_{189}=\varnothing\). Set \(f_n(k)=A_n(k)/\binom nk\in[0,1]\), \(s_n(u)=\sum_k A_n(k)u^k(1-u)^{n-k}\), \(t_m(z)=s_m(z)\), and \(w_{nm}=2^{-(n+m+1)}\binom{n+m}n\).

\[
a_n(z)=1-\sum_{m=0}^{188}w_{nm}t_m(z),\quad
b_n(z)=n+1-\sum_{m=0}^{188}(n+m+1)w_{nm}t_m(z)/2.
\]
\[
\mu(p,z)=\sum_{n=0}^{188}a_n(z)s_n(p)+\sum_{m=0}^{188}t_m(z),\quad
H(p,z)=\sum_{n=0}^{188}b_n(z)s_n(p)+\sum_{m=0}^{188}(m+1)t_m(z).
\]

The BRC native branch counts/threshold and two-clock observer are unchanged. Fraction arithmetic is used only for exact evaluation of those native algebraic readouts.

## Exact finite covering argument

Split \([0,1/64]\) into 16 *closed* intervals \(I_j=[j/1024,(j+1)/1024]\). Let \(I=[a,b]\), \(c=(a+b)/2\), \(r=(b-a)/2\), and \(\delta=1/4096\). With \(\Delta\) the forward difference of \(f_n\), the exact Bernstein identity is

\[
s_n^{(d)}(u)=n^{\underline d}\sum_{k=0}^{n-d}\binom{n-d}k \Delta^df_n(k)u^k(1-u)^{n-d-k},\quad d=1,2,3.
\]

The rational bound, valid for *every* \(u\in[a,b]\), is
\[
B_{n,d}(a,b)=n^{\underline d}\sum_{k=0}^{n-d}\binom{n-d}k|\Delta^df_n(k)|b^k(1-a)^{n-d-k}.
\]
This is justified termwise by \(u^k\le b^k\) and \((1-u)^{n-d-k}\le(1-a)^{n-d-k}\). There is no truncated Taylor series or numerical rounding in the proof.

At \(z=Q\), evaluate the exact midpoints \(\mu,\mu_{pp},H_{pp},\mu_{ppz},H_{ppz}\). The NB kernel has \(\sum_{m\ge0}w_{nm}=1\) and \(\sum_{m\ge0}m(m-1)w_{nm}=(n+1)(n+2)\). Because \(0\le f_m(k)\le1\), \(|t_m''(z)|\le2m(m-1)\). This gives the following *all-z* bounds:

\[
Z_\mu(I)=2\sum_n(n+1)(n+2)B_{n,2}(a,b)\ge|\mu_{ppzz}|,
\]
\[
Z_H(I)=2\sum_n(n+1)(n+2)(n+3)B_{n,2}(a,b)\ge|H_{ppzz}|.
\]

The inherited score estimate \(|t_m'(z)|<21\) on \(J\) implies \(|a_n'(z)|\le21\), \(|b_n'(z)|\le21(n+1)\). Define

\[
E_{\mu,3}=r\sum_n a_n(Q)B_{n,3},\quad E_{H,3}=r\sum_n b_n(Q)B_{n,3},\quad
E_{\mu z,3}=r\sum_n|a'_n(Q)|B_{n,3},\quad E_{Hz,3}=r\sum_n|b'_n(Q)|B_{n,3}.
\]

The computed exact bounds for all \(I\times J\) are

\[
L_{\mu pp}=\mu_{pp}(c,Q)-E_{\mu,3}-\delta(|\mu_{ppz}(c,Q)|+E_{\mu z,3})-\delta^2Z_\mu(I)/2,
\]
\[
U_{Hpp}=H_{pp}(c,Q)+E_{H,3}+\delta(|H_{ppz}(c,Q)|+E_{Hz,3})+\delta^2Z_H(I)/2.
\]

For \(\mu\), reuse the edge fact \(|\mu_z(0,z)|<3969\) on \(J\), and \(|\mu_{pz}(u,z)|\le21\sum_n |s'_n(u)|\) throughout \(0\le u\le1/64\). **The integration from 0 requires the full-range bound** \(C_1=\sum_nB_{n,1}(0,1/64)\), not an interval-local bound. Therefore

\[
L_\mu=\mu(c,Q)-r\sum_na_n(Q)B_{n,1}(a,b)-\delta(3969+21b C_1).
\]

Evaluate \(U_{Wpp}=2U_{Hpp}-2L_\mu L_{\mu pp}\). The Python program checks the exact rational assertions \(L_\mu>88\), \(L_{\mu pp}>200\), \(U_{Hpp}<24000\), \(U_{Wpp}<-8000\) in all 16 intervals. These imply the theorem via \(W_{pp}=2H_{pp}-2\mu_p^2-2\mu\mu_{pp}\).

## Execution and evidence

Command: run the published PREFIX667 certificate alongside the frozen PREFIX666_experiment.py and PREFIX666_certificate.py (the Python import names must be in PYTHONPATH). The executed local certificate printed **ALL_INTERVALS_CERTIFIED 16**. An independent native two-clock Fraction program checked exact \(p=0,1/128,1/64\) with \(z=Q\): **ALL_SAMPLES_PASS 3**. Samples are corroboration, not the proof of the rectangle.

Across all covering intervals, conservative float renderings of the *exactly compared* rational bounds were:

| Diagnostic | Worst certified bound |
|---|---:|
| \(\min L_\mu\) | 88.4793178420 |
| \(\min L_{\mu pp}\) | 205.0296046977 |
| \(\max U_{Hpp}\) | 23922.8712148472 |
| \(\max U_{Wpp}\) | -8580.1674357490 |

All assertions ran in Python Fraction; decimals above are output only. Exact source, original logs and a full reproducibility package are retained together with the frozen dependency sources in the conversation artifact ENTERPRISE_MATH_PREFIX667_DOUBLE_WIDE_BRC_VARIANCE_COMPLETE.tar.gz.

Scope: finite native BRC first-stop readout, not external physical validation. No change to the protected P000/X6 axioms or Source frozen science pin. The stronger full-square variance claim, independent mathematical review, formal Result and native Cell/path rotation remain open.

## Next discriminating work

Construct adaptive subdivided enclosures on \([1/64,1/32]\times J\), preferably directly bounding \(2H_{pp}-2\mu_p^2-2\mu\mu_{pp}\) to preserve cancellation, rather than broad independent H and \(\mu\) bounds. Compare the exact BRC samples and certify a further real parameter interval if the new bounds close.