# Free Research — Hamming–Chebyshev Synchronization Bridge

Status: `FREE_RESEARCH_FRONTIER / EXACT_FINITE_CORE / NOT_WORKING_TRUTH / NOT_FOUNDATION / PRIOR_ART_SEPARATED`
Date: `2026-09-04`
Parent: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V2_20260904.md`

## Executive advance

The saturated prime-winding envelope from the previous frontier is already encoded by one finite Hamming/Krawtchouk carrier.

For `N >= 1`, define

\[
L_N:=\operatorname{lcm}(1,2,\ldots,N),
\]

and define the Hamming synchronization clock

\[
\mathcal C_m:=\operatorname{lcm}_{0\le k\le m}\binom{m}{k}.
\]

On the current #1159 Krawtchouk carrier, the shell-zero amplitude of mode `k` is exactly

\[
g_{m,k}(0)=\binom{m}{k}.
\]

Hence `C_m` is equivalently the least common synchronization period of all shell-zero amplitudes of the genuine integer-spectrum eigenmodes.

The exact bridge is

\[
\boxed{L_N=N\,\mathcal C_{N-1}.}
\]

Consequently

\[
\boxed{\psi(N)=\log N+\log \mathcal C_{N-1}.}
\]

This answers the previous mother question at the finite-invariant level: the Chebyshev saturated-winding observable is the logarithm of a Hamming/Krawtchouk synchronization clock. The remaining PNT problem is no longer to locate a carrier; it is to prove the asymptotic growth law of this exact carrier.

---

## PHC-T01 — Prime-direction carry envelope of one Hamming row

Let `p` be prime, let `N=m+1`, and write

\[
q_p(N):=\lfloor\log_p N\rfloor,
\qquad
 a_p(N):=v_p(N).
\]

Define the maximal shell carry depth

\[
h_p(N):=\max_{0\le k\le N-1}v_p\binom{N-1}{k}.
\]

Then

\[
\boxed{h_p(N)=q_p(N)-a_p(N).}
\]

### Proof

Kummer's theorem identifies `v_p(binomial(N-1,k))` with the number of base-`p` carries in the addition

\[
k+(N-1-k)=N-1.
\]

For every `r <= a_p(N)`, one has

\[
N-1\equiv -1\pmod{p^r},
\]

so the lower `a_p(N)` digit positions are all `p-1` and no carry can occur there. No carry can occur above `q_p(N)` because `N-1<p^{q_p(N)+1}`. Therefore every shell has at most `q_p(N)-a_p(N)` carries.

This upper bound is attained explicitly. If `q>a`, take

\[
\boxed{k_*=p^q-p^a.}
\]

For every `a<r\le q`,

\[
k_*\bmod p^r=p^r-p^a.
\]

Writing `s_r=N mod p^r`, the assumption `v_p(N)=a<r` gives

\[
p^a\le s_r\le p^r-p^a,
\]

and

\[
(N-1-k_*)\bmod p^r=s_r+p^a-1.
\]

The two residues therefore sum to

\[
p^r+s_r-1\ge p^r,
\]

so a carry occurs at every level `r=a+1,...,q`. If `q=a`, take `k_*=0`; the maximum is zero. This proves the formula.

### Interpretation

The total admissible winding capacity in prime direction `p` splits exactly into

\[
\boxed{
q_p(N)=v_p(N)+h_p(N).
}
\]

The current top state `N` occupies `v_p(N)` windings, while the remaining capacity is stored as maximal Hamming branch-recoalescence carry depth across the row `N-1`.

---

## PHC-T02 — Exact Hamming synchronization identity

Taking the maximum `p`-adic valuation over the row gives

\[
v_p(\mathcal C_{N-1})
=q_p(N)-v_p(N).
\]

Therefore

\[
v_p(N\mathcal C_{N-1})=q_p(N).
\]

But the exponent of `p` in `L_N` is exactly the largest `a` with `p^a<=N`, namely `q_p(N)`. Equality at every prime yields

\[
\boxed{
N\operatorname{lcm}_{0\le k<N}\binom{N-1}{k}
=\operatorname{lcm}(1,2,\ldots,N).
}
\]

Equivalently, in current Krawtchouk notation,

\[
\boxed{
L_N
=N\operatorname{lcm}_{0\le k<N}g_{N-1,k}(0).
}
\]

### Prior-art boundary

The binomial-row LCM identity itself is classical: it is Farhi's 2009 identity, and Hong showed its equivalence to an earlier identity of Nair. Kummer's carry theorem is also classical. The project-specific advance here is the exact embedding into the current genuine Hamming/Krawtchouk spectral carrier and the winding/carry complementarity interpretation. No external novelty claim is made for the number-theoretic identity.

---

## PHC-T03 — Prime powers are the jump set of the normalized Hamming clock

Define

\[
\mathcal S_N:=N\mathcal C_{N-1}=L_N.
\]

Then

\[
\boxed{
\frac{\mathcal S_N}{\mathcal S_{N-1}}
=
\begin{cases}
 p,&N=p^a\text{ for a prime }p\text{ and }a\ge1,\\
 1,&\text{otherwise}.
\end{cases}}
\]

Indeed, moving from `N-1` to `N` increases exactly one saturated prime exponent iff `N` itself is a prime power.

Hence the von Mangoldt flux is exactly the logarithmic scale derivative of the finite Hamming synchronization invariant:

\[
\boxed{
\Lambda(N)=\log\frac{N\mathcal C_{N-1}}{(N-1)\mathcal C_{N-2}}.
}
\]

Summing gives

\[
\boxed{
\psi(N)=\sum_{n\le N}\Lambda(n)
=\log\bigl(N\mathcal C_{N-1}\bigr).
}
\]

This is a finite prime-power detector using only the change in the normalized Hamming row clock.

---

## PHC-T04 — Dyadic Hamming renormalization sandwich

For every `n>=1`,

\[
\boxed{
\frac{L_{2n}}{L_n}
\mid
\binom{2n}{n}
\mid
L_{2n}.
}
\]

The left divisibility says that every new prime-power winding appearing between scales `n` and `2n` is absorbed by the single central Hamming return amplitude. The right divisibility says that this central amplitude does not use any winding depth beyond the full saturated envelope at scale `2n`.

Taking logarithms,

\[
\boxed{
\psi(2n)-\psi(n)
\le \log\binom{2n}{n}
\le \psi(2n).
}
\]

Since

\[
\frac{4^n}{2n+1}\le\binom{2n}{n}<4^n,
\]

the Hamming carrier immediately yields nondegenerate linear Chebyshev-scale bounds. In particular,

\[
\psi(N)\ge (N-1)\log2,
\]

because the largest row entry is at least the row average `2^(N-1)/N` and every row entry divides `C_(N-1)`.

The exact constant `1` in `psi(N)~N` is not supplied by this single-scale sandwich; it requires cross-scale cancellation or a stronger positive energy law.

---

## PHC-T05 — Opposite-corner path Möbius reconstruction

For `r>=0`, the integer `r!` is the number of shortest ordered coordinate-flip histories from one corner of the `r`-cube to the opposite corner.

The saturated winding envelope has the exact signed path-volume representation

\[
\boxed{
L_N
=
\prod_{d=1}^{N}
\left(\left\lfloor\frac Nd\right\rfloor!\right)^{\mu(d)}.
}
\]

### Prime-exponent proof

Fix a prime `p`. By Legendre's formula, the exponent of `p` on the right is

\[
\sum_{d\le N}\mu(d)
\sum_{a\ge1}
\left\lfloor\frac{N}{dp^a}\right\rfloor.
\]

For each `p^a<=N`, set `X=floor(N/p^a)`. Then

\[
\sum_{d\le X}\mu(d)\left\lfloor\frac Xd\right\rfloor=1.
\]

Thus every admissible winding level `p^a<=N` survives exactly once and all composite repetitions cancel. The resulting exponent is `q_p(N)`, the exponent of `p` in `L_N`.

Taking logarithms,

\[
\boxed{
\psi(N)
=
\sum_{d\le N}\mu(d)
\log\left(\left\lfloor\frac Nd\right\rfloor!\right).
}
\]

This retypes `psi` as the Möbius-renormalized entropy of opposite-corner Hamming path fibers.

---

## PHC-T06 — Positive one/two-winding energy carrier

Let `D` be the logarithmic derivation on arithmetic functions,

\[
(Df)(n)=f(n)\log n,
\]

and let `*` denote Dirichlet convolution. Since

\[
\Lambda=\mu*\log,
\]

the exact local Selberg identity is

\[
\boxed{
\mu*\log^2
=
\Lambda\log+\Lambda*\Lambda.
}
\]

Summing to `N` gives the finite energy identity

\[
\boxed{
\sum_{n\le N}\Lambda(n)\log n
+
\sum_{ab\le N}\Lambda(a)\Lambda(b)
=
\sum_{d\le N}\mu(d)
\sum_{m\le N/d}(\log m)^2.
}
\]

The left side is positive and has an exact occupation meaning:

- `Lambda(n) log n` is the weighted one-winding/self-energy channel;
- `Lambda(a)Lambda(b)` is the ordered two-direction collision channel.

The classical Selberg symmetry estimate says that this energy is `2N log N + O(N)`. The new project route is therefore:

\[
\boxed{
\text{Hamming synchronization clock}
\to
\text{prime-power jump flux }\Lambda
\to
\text{one/two-winding positive energy}
\to
\text{PNT stability}.
}
\]

The first three arrows now have exact finite formulas. The final stability step is the next open theorem.

---

## What is solved and what remains open

### Solved at exact finite strength

1. `psi(N)` is the log of a normalized Hamming/Krawtchouk zero-shell synchronization clock.
2. Each prime-direction winding capacity splits exactly into current-state valuation plus maximal row carry depth.
3. Prime powers are exactly the jump set of the normalized clock, and the jump label is the underlying prime.
4. The dyadic new-winding envelope is contained in one central Hamming return amplitude.
5. `L_N` is the Möbius-renormalized product of opposite-corner Hamming path counts.
6. The Selberg one/two-winding energy identity is an exact finite convolution law.

### Not solved

- No proof of `psi(N)~N` has yet been obtained from current Enterprise axioms.
- The Farhi/Nair/Kummer and Selberg arithmetic identities are prior mathematics; only their exact carrier identification and typed geometric interpretation are project-specific here.
- The Hamming synchronization clock is a derived finite invariant. It is not yet shown to be preserved or contracted by a primitive G0 rotation/branch RG.
- No zeta-zero or RH claim follows.

## Next discriminating theorem

The next target is a finite stability theorem for the Hamming jump flux. One useful form would be:

> derive the Selberg symmetry estimate, and then prove that any nonnegative jump flux satisfying the exact Hamming clock identities, the dyadic renormalization sandwich, and the one/two-winding energy law must obey `psi(N)=N+o(N)`.

A stronger genuinely Enterprise-specific route would exhibit a primitive finite branch operator whose quadratic energy is exactly the left side of PHC-T06 and whose spectral gap forces the required stability.
