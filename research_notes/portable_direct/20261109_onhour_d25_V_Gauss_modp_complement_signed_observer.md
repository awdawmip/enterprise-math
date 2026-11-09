# D25 AF4 — finite-field complementary Gauss compression and signed derivative observer

Date: 2026-11-09. Scope: AUTHOR-SIDE EXACT ALGEBRA / TESTED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0.
Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen science pin `c47e13e4aba0e006366f989d6334d443f6333ae3` is unchanged.
Consumes the exact earlier Gauss affine first-jet `research_notes/portable_direct/20261109_onhour_d25_V_Gauss_affine_firstjet_p13_certificate.md`. The current operational Source was read separately.

## Theorem 1 (exact polynomial identity in finite characteristic)

Let `p` be prime, `0<=a<=b<=p-1` and `a+b>=p-1`. Put
`h=a+b-(p-1)`, `u=p-1-b`, `v=p-1-a`. In `F_p[z]`:

```text
P_ab(z)=sum_{k=0}^a C(a,k)C(b,k)z^k
       =(1-z)^h sum_{k=0}^u C(u,k)C(v,k)z^k
       =(1-z)^h Q_uv(z).
```

**Proof.** Over the rationals, the classical Euler transformation gives the formal identity
`2F1(-a,-b;1;z)=(1-z)^(1+a+b)2F1(1+a,1+b;1;z)`.
Compare coefficients of degrees `k<p`: their denominators `(k!)^2` are units modulo `p`. Moreover `1+a=p-v` and `1+b=p-u`, so the second hypergeometric factor is coefficientwise congruent modulo `(p,z^p)` to the terminating `2F1(-v,-u;1;z)=Q_uv(z)`. Because `1+a+b=p+h`, the prefactor becomes `(1-z)^(p+h)=(1-z)^h(1-z^p)` in characteristic p. Reducing modulo `z^p` gives `P_ab=(1-z)^hQ_uv` through degree `p-1`. Both are polynomials of degree at most `a=h+u<p`, so equality is global. This does not use a conjecture about their value at a special argument.

## Theorem 2 (direct p=13 mod24 original-observer port)

For every prime `p=13 (mod24)`, put
`a=(5p-1)/8`, `b=(7p-3)/8`, `u=(p-5)/8`, `h=(p+1)/2`. Then `v=3u+1` and

```text
P_p(z) = sum_{k=0}^a C(a,k)C(b,k)z^k
Q_p(z) = sum_{k=0}^u C(u,k)C(3u+1,k)z^k
P_p(z) = (1-z)^h Q_p(z)  in F_p[z].
```

Let `z0=1/9` in `F_p` and use the original Clausen Gauss factors
`M_p=sum_{k=0}^{p-1}(1/8)_k(3/8)_k z0^k/(k!)^2`,
`N_p=sum_{k=0}^{p-1}k (1/8)_k(3/8)_k z0^k/(k!)^2`.
Then, with `H_p=M_p+16N_p` (this `H` is only a Gauss scalar, NOT a native H0/B0 matrix),

```text
M_p = -(8/9) Q_p(1/9)           (mod p)
H_p = -(128/81) Q_p'(1/9)        (mod p).
```

**Proof.** Reduction of the exact finite affine first-jet at `X=p` gives `M_p=P_p(z0)`, `N_p=z0 P_p'(z0)` modulo `p`, including derivative and all original `k<p` terms. Since `p=5 mod8`, the Legendre symbol `(8/p)=-1`; thus `(1-z0)^h=-(1-z0)=-8/9` in F_p. Differentiate Theorem 1:
`P+16zP'=(1-z)^(h-1)[(1-(1+16h)z)Q+16z(1-z)Q']`.
Here `1+16h=9 mod p`. At `z=z0=1/9` the coefficient of `Q` vanishes **without assuming Q(z0)=0**, leaving `16z0(1-z0)^h Q'(z0)=-128/81 Q'(z0)`. QED.

This preserves the two signed observer ports `(M,H)` under a degree reduction from `a~5p/8` to `u~p/8`, rather than collapsing the derivative observer. In BRC-style typed carrier terms this is a `FINITE_FIELD_SIGNED_PAIR` with proven exact readout; it is not a positivity/mass claim. To lift to mod p^2, the difference `P-(1-z)^h Q` divided by p and the previously proved first-jet middle-band T must be retained. No mod-p compression silently completes the p^2 cancellation.

## Executed reproducible checks (integer modular arithmetic)

Checker: `research_notes/portable_direct/d25_V_Gauss_complement_observer_20261109.py`.
For all 157 primes `p<=10000, p=13(mod24)`, directly computed P,Q and derivatives using modular binomial recurrences and separately computed full original Gauss M,N via Pochhammer recurrence modulo p. Both claimed port identities agreed exactly, with no floating-point arithmetic. For the six p in `{13,37,61,109,157,181}`, the full polynomial identity (every coefficient) was also checked independently by convolution. Additional observations, **not a universal theorem**, in all 157 primes: `Q(1/9)=0` and `Q'(1/9)!=0`.

| p | u | Q(1/9) | Q'(1/9) | M mod p | H=M+16N mod p |
|---:|---:|---:|---:|---:|---:|
| 13 | 1 | 0 | 4 | 0 | 7 |
| 37 | 4 | 0 | 11 | 0 | 5 |
| 61 | 7 | 0 | 27 | 0 | 59 |
| 109 | 13 | 0 | 14 | 0 | 64 |
| 157 | 19 | 0 | 154 | 0 | 28 |
| 181 | 22 | 0 | 124 | 0 | 137 |
| 373 | 46 | 0 | 369 | 0 | 80 |
| 9973 | 1246 | 0 | 9056 | 0 | 8344 |

## Exact remaining step and benchmark distinction

Smallest algebraic open unit: prove `Q_u(1/9)=0 mod p` uniformly when `p=8u+5=13(mod24)`; then complete the previously recorded p^2 relation `P/p+L+T=0 mod p`, explicitly retaining the quotient/defect and original middle-band T. The `Q'` port supplies a short exact observable to connect to the original signed Clausen cutoff Q and 216 source. Do not reprove the completed Euler factor theorem as another research unit.

Highest original-native outstanding experiment: issue #1559, same-original-class p=373 H0/B0 divided-power `[X]U mod139129`, module rank, semilinear direction/eta, native κ and Delta-R, odd observer and independent reproduction. This finite Gauss lemma does NOT execute or substitute that experiment.

Formal Source continuation: read-only request `onhour11-20261109-2003-fresh-continuation`, latest source `c8664d5335ac245d0ba711f00d5003ad4c2cabc9`, no live winning claim. Historical Research lane service-issued researcher `EM-ENTERPRISE-F0B4A2`/session `MCP-b2108cf3e4614e26b52719f13f8e334c` is not a present capability; no claim/run/native checkpoint asserted. Maintenance lane is separate.
