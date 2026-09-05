# p-adic valuation from primitive decimation traces and primitive resultants

Status: `FREE_RESEARCH / EXACT FINITE-ARITHMETIC CONSISTENCY THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- primitive trace law `T_d(q)=2(phi(d)-c_d(q))`;
- native primitive resultant prime-ray law.

## 1. Prime-power trace response

For `d=p^a`, the Ramanujan sum is

\[
c_{p^a}(q)=
\begin{cases}
\varphi(p^a),&p^a\mid q,\\
-p^{a-1},&p^{a-1}\mid q\text{ but }p^a\nmid q,\\
0,&p^{a-1}\nmid q.
\end{cases}
\]

Substitute into

\[
\mathcal T_d(q)=2(\varphi(d)-c_d(q)).
\]

Then

\[
\boxed{
\mathcal T_{p^a}(q)=
\begin{cases}
0,&p^a\mid q,\\
2p^a,&v_p(q)=a-1,\\
2\varphi(p^a),&v_p(q)\le a-2.
\end{cases}}
\tag{PVT-1}
\]

So one primitive prime-power denominator channel is a finite three-level p-adic threshold detector.

## 2. Valuation as trace-zero depth

The zero condition is exact:

\[
\boxed{\mathcal T_{p^a}(q)=0\iff p^a\mid q.}
\tag{PVT-2}
\]

Hence

\[
\boxed{
v_p(q)=\max\{a\ge1:\mathcal T_{p^a}(q)=0\},
}
\tag{PVT-3}
\]

with the maximum understood as zero when there is no vanishing prime-power channel.

Therefore ordinary prime factorization can be reconstructed dynamically from primitive decimation traces:

\[
\boxed{
q=\prod_p p^{\max\{a:\mathcal T_{p^a}(q)=0\}}.
}
\tag{PVT-4}
\]

Only finitely many primes/channels contribute for fixed `q`.

## 3. Gcd from trace-zero support

For fixed `N,q`, among the divisor channels of `N`,

\[
\mathcal T_d(q)=0\iff d\mid q.
\]

Thus

\[
\boxed{
\{d:d\mid N,\ \mathcal T_d(q)=0\}
=\{d:d\mid(N,q)\}.
}
\tag{PVT-5}
\]

The gcd is therefore the largest divisor channel of `N` whose primitive decimation trace vanishes.

This is a finite spectral divisibility observer.

## 4. Independent resultant reconstruction of the same valuation

The native resultant prime-ray law gives

\[
\frac1{\varphi(m)}
 v_p|\operatorname{Res}(\Psi_m,\Psi_n)|
=\mathbf 1_{\{n=mp^a,\ a\ge1\}}.
\]

The endpoint boundary contributes

\[
v_p|\Psi_n(0)|=\mathbf 1_{\{n=p^a\}}.
\]

Summing all lower prime-ray hits into `n` gives

\[
\boxed{
 v_p(n)
= v_p|\Psi_n(0)|
+\sum_{\substack{m\mid n\\2\le m<n}}
\frac1{\varphi(m)}
 v_p|\operatorname{Res}(\Psi_m,\Psi_n)|.
}
\tag{PVT-6}
\]

This derivation uses static pairwise primitive spectral coupling rather than phase-decimation traces.

## 5. Cross-observer valuation identity

Combining the two independent finite reconstructions,

\[
\boxed{
\max\{a:\mathcal T_{p^a}(n)=0\}
=
 v_p|\Psi_n(0)|
+\sum_{\substack{m\mid n\\2\le m<n}}
\frac1{\varphi(m)}
 v_p|\operatorname{Res}(\Psi_m,\Psi_n)|.
}
\tag{PVT-7}
\]

Thus one and the same `p`-adic coordinate is encoded by:

```text
DYNAMIC CHANNEL:
prime-power primitive spectrum
 -> phase multiplication R_(2n)
 -> trace-zero depth
 -> v_p(n)

STATIC CHANNEL:
endpoint primitive mass + pairwise primitive resultants
 -> p-adic normalized coupling count
 -> v_p(n)
```

The two carriers remain distinct; their valuation readouts coincide.

Freeze:

`P_ADIC_VALUATION = PRIME_POWER_DECIMATION_ZERO_DEPTH`.

`P_ADIC_VALUATION = ENDPOINT_PLUS_RESULTANT_P_RAY_COUNT`.

`DYNAMIC_AND_STATIC_SPECTRAL_VALUATIONS_COINCIDE`.
