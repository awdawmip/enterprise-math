# Free Research — Pi-to-Prime Geometry Frontier V5

Status: `FREE_RESEARCH_CURRENT_FRONTIER / PNT_NORMALIZATION_CLOSED_AT_REAL_SMOOTHING_STRENGTH / PAIR_SIMPLEX_VARIANCE_CARRIER_FOUND / NATIVE_REMAINDER_THEORY_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION / EXTERNAL_NOVELTY_PARTITIONED`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V4_20260904.md`

## 1. Current strongest interpretation

The extension of the endogenous full-turn constant `tau` to prime geometry now has four exact finite layers and one completed asymptotic layer.

### Full-turn completion

At the existing completion strength,

\[
\boxed{
\tau^2
=3!\lim_{M\to\infty}
\det(I-B_M^{-2})^{-1},
}
\]

where `B_M` is the arithmetic prime-birth block of the genuine finite Hamming/Krawtchouk integer spectrum.

The factor `3!` is the ordered three-history provenance fiber over a common shell-3 endpoint.

### Prime births and windings

A prime `p` is the first appearance of an irreducible multiplicative mode; `p^a` is the birth of winding layer `a` in that same direction. The saturated finite tower satisfies

\[
\boxed{
\det\mathcal W_M
=\operatorname{lcm}(1,\ldots,M)=L_M,
}
\]

so

\[
\boxed{
\psi(M)=\log\det\mathcal W_M.
}
\]

The von Mangoldt function is the discrete trace-log jump current of this tower.

### Native `120 degree` chirality

For the three-sector cycle matrix `P` and `J=P^2-P`,

\[
\chi_3(p)=\frac13\operatorname{Tr}(JP^p).
\]

Thus the same prime birth has a magnitude/winding coordinate and a native orientation coordinate.

### Prime distribution

The positive degree-two provenance energy and real smoothing now yield

\[
\boxed{
\psi(x)\sim x,
\qquad
\pi(x)\sim\frac{x}{\log x}.
}
\]

The prime-number-theorem normalization is therefore no longer merely quoted as an external fact in this research line; it is reached from the prime-winding carrier through a classical real-variable smoothing closure.

---

## 2. Why the macroscopic constant is `1`

The finite harmonic history volumes

\[
\mathcal H_r(N)
=\sum_{n_1\cdots n_r\le N}
\frac1{n_1\cdots n_r}
\]

obey exact Möbius recoalescence:

\[
\sum_{d\le N}\frac{\mu(d)}d
\mathcal H_r(\lfloor N/d\rfloor)
=\mathcal H_{r-1}(N).
\]

For `r=2`, the logarithmic simplex has leading area

\[
\frac12(\log N)^2.
\]

Recoalescing one history must leave a one-dimensional logarithmic length `log N`; this forces the inverse coefficient `2` and hence

\[
\boxed{
\Psi_2(N)
=\sum_{n\le N}
\bigl(\Lambda(n)\log n+(\Lambda*\Lambda)(n)\bigr)
=2N\log N+O(N).
}
\]

Writing

\[
V(T)=e^{-T}(\psi(e^T)-e^T),
\]

the positive energy gives the triangular averaging inequality

\[
T^2|V(T)|
\le2\int_0^T(T-u)|V(u)|du+O(T).
\]

Therefore the pointwise upper amplitude cannot exceed its long average. Bounded signed transport, one-way prime-power birth jumps, and the local post-zero triangular deficit imply that any positive limiting amplitude would make the long average strictly smaller. The contradiction forces

\[
V(T)\to0.
\]

Geometrically:

> density `1` is the unique stable fixed normalization because every persistent centered winding defect would have to be simultaneously supported by and strictly depleted by its own recoalesced history average.

---

## 3. Exact finite support gap

For every action label `a>=1`, define

\[
q_a(n)=\lfloor n/a\rfloor,
\qquad
\delta_a f(n)=f(n)+f(q_a(n)).
\]

The quotient maps compose exactly:

\[
q_bq_a=q_{ab}.
\]

Every ordered pair of histories therefore forms an odd quotient 2-simplex:

\[
\boxed{
2f(n)
=\delta_a f(n)+\delta_{ab}f(n)-\delta_bf(q_a(n)).
}
\]

and

\[
\boxed{
4|f(n)|^2
\le3\left(
|\delta_a f(n)|^2
+|\delta_{ab}f(n)|^2
+|\delta_bf(q_a(n))|^2
\right).
}
\]

This is now formalized for arbitrary `a,b` in Lean. The earlier `2-2-4` triangle is only the smallest instance.

---

## 4. Macroscopic pair-simplex gap

Let `S_Y` contain all prime powers up to `Y`, with weights

\[
u_a=\frac{\Lambda(a)}a,
\qquad
U_Y=\sum_{a\le Y}u_a=\log Y+O(1).
\]

Summing the odd-triangle inequality over ordered pairs gives

\[
\boxed{
4U_Y^2|f(n)|^2
\le3\left(
U_YE_1+E_{\rm dir}+E_{\rm tr}
\right).
}
\]

Here:

- `E_1` is one-step signless edge energy;
- `E_dir` is the direct `ab` edge energy;
- `E_tr` is the degree-two packet transported to the intermediate quotient vertex.

The direct coefficient groups as

\[
\sum_{ab=c}
\frac{\Lambda(a)\Lambda(b)}{ab}
=rac{(\Lambda*\Lambda)(c)}c.
\]

Thus the full odd-simplex family has gap mass of order `(log Y)^2`, exactly matching the degree-two collision sector. Unlike a single fixed-prime triangle, it survives normalization with a constant gap.

---

## 5. Canonical finite fluctuation form

For any finite positive action weights, let

\[
y_a=f(q_a(n)),
\qquad
\bar y=U^{-1}\sum_a u_a y_a.
\]

Then

\[
\boxed{
\sum_a u_a|f(n)+y_a|^2
=U|f(n)+\bar y|^2
+\sum_a u_a|y_a-\bar y|^2.
}
\]

The quotient-cloud variance has the exact pairwise representation

\[
\boxed{
2U\sum_a u_a|y_a-\bar y|^2
=\sum_{a,b}u_au_b|y_a-y_b|^2.
}
\]

This is the first canonical finite quadratic fluctuation carrier for the prime-winding geometry. The scalar return equation controls the mean term. The pairwise graph Laplacian is the remaining roughness term.

Accordingly, the old open phrase “find the energy-to-defect transfer” is now sharpened to:

\[
\boxed{
\text{control the weighted quotient-cloud variance by a positive provenance energy.}
}
\]

---

## 6. Provenance degree alignment

Define

\[
\Lambda_r:=\mu*\log^r.
\]

Then

\[
\Lambda_{r+1}=D\Lambda_r+\Lambda*\Lambda_r,
\]

so every degree is nonnegative and consists of ordered collision/transport channels. In particular,

\[
\Lambda_3=D\Lambda_2+\Lambda*\Lambda_2.
\]

The term `Lambda*Lambda_2` has exactly the provenance type of `E_tr`: one prime-power history transports a complete degree-two packet to an intermediate quotient vertex.

Therefore degree three is the first natural source for a carré-du-champ comparison with the pair-simplex variance.

---

## 7. Current status table

| Statement | Status |
|---|---|
| Prime = irreducible finite spectral birth | exact finite |
| Prime power = new winding layer | exact finite |
| `det W_M=lcm(1,...,M)` | exact finite |
| `psi=log det W` | exact finite/readout |
| Native mod-3 chirality trace | exact finite local readout |
| `tau^2/3!` prime-winding completion | existing analytic completion strength |
| Harmonic recoalescence hierarchy | exact finite |
| `Psi_2=2x log x+O(x)` | proved, elementary asymptotic |
| `psi(x)~x` | proved by real Selberg smoothing |
| `pi(x)~x/log x` | proved by standard transfer |
| Universal quotient odd triangle | exact finite, Lean formalized |
| Weighted pair-simplex gap | exact finite |
| Quotient-cloud Gram variance | exact finite |
| Native quantitative remainder for `psi-x` | open |
| RH-scale remainder | not claimed |
| Working Truth / Foundation promotion | no |

---

## 8. Novelty partition

The following ingredients are classical mathematics and are not claimed as externally novel:

- Kummer/Farhi/Nair binomial-LCM identities;
- Selberg's symmetry formula;
- the real-variable elementary smoothing proof of the prime number theorem;
- the PNT itself.

The project-specific research contribution lies in the integrated carrier and typing:

1. arithmetic primes selected inside the genuine Krawtchouk integer spectrum;
2. prime powers interpreted as winding-layer births of a finite determinant tower;
3. `psi` identified with its trace-log;
4. Selberg's coefficient `2` derived as harmonic history-simplex recoalescence;
5. quotient histories organized as finite odd 2-simplices;
6. the centered remainder typed as a weighted quotient-cloud variance problem.

External novelty of this integrated formulation remains unverified.

---

## 9. Current artifacts

Current theorem packets:

- `FREE_RESEARCH_PRIME_WINDING_HARMONIC_RECOALESCENCE_GAP_20260904.md`;
- `FREE_RESEARCH_PRIME_WINDING_PNT_SMOOTHING_CLOSURE_20260904.md`;
- `FREE_RESEARCH_PRIME_WINDING_PAIR_SIMPLEX_VARIANCE_20260904.md`.

Formal finite core:

- `EnterpriseMath/Relation/PrimePowerQuotientTriangle.lean`.

Exact regression checkers:

- `check_free_research_prime_winding_harmonic_gap.py`;
- `check_free_research_prime_winding_pair_simplex_variance.py`.

---

## 10. Next mother question

The first-order distribution problem is closed. The next genuinely discriminating target is:

> Can the positive degree-three provenance packet be polarized into a finite carré-du-champ form that dominates the pairwise quotient-cloud variance, uniformly at the natural cutoff `Y=sqrt(n)`?

A successful comparison would turn the current real-smoothing PNT proof into a native finite-RG remainder mechanism. It would not automatically imply the Riemann hypothesis; it would first need to produce and quantify a decay rate for

\[
\psi(x)-x.
\]
