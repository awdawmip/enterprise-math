# RH / X6 / Factor-BRC transport frontier

Status: `RESEARCH FRONTIER / MIXED EXACT + PRIOR-ART-DEPENDENT + EMPIRICAL / NOT FOUNDATION`
Date: `2026-09-06`
Project: `Enterprise Math / 进取数论`
Research scope: `Riemann hypothesis / Möbius / Riesz-Báez-Duarte / X6 / Factor-BRC / provenance-preserving transport`

## 0. Purpose and typing guard

This note records the current RH research frontier reached on 2026-09-06 and prevents later work from re-entering routes already ruled out.

Project foundation remains P000:

- native space is signed discrete X6;
- six native axes are the spatial primitive directions;
- primitive straight support is one native axis;
- primitive stable nonzero force semantics are triadic;
- a three-axis slice is only a slice of X6;
- arithmetic factor directions and prime labels are NOT additional native spatial axes.

All factor/RH constructions below are arithmetic relation fibers, observers, or X6 local ports. They do not alter P000.

BRC discipline remains mandatory:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

Positive mass and signed Möbius orientation must not be conflated.

---

## 1. Factor fiber and X6 local port

For

\[
n=\prod_p p^{e_p},
\]

the factor fiber is the finite exponent lattice

\[
F(n)=\prod_{p\mid n}\{0,1,\ldots,e_p\}.
\]

For \(r=\omega(n)\le6\), choose a local injection of the active prime labels into X6 slots. The exponent endpoint becomes

\[
(e_1,\ldots,e_r,0,\ldots,0).
\]

This preserves exactly:

\[
N_{\min}=\Omega(n),
\]

\[
L_E^2=\sum_p e_p^2,
\]

and

\[
B_{\min}=\frac{\Omega(n)!}{\prod_p e_p!}=B_{\rm fact}(n).
\]

For squarefree \(n\) with \(r\le6\), the endpoint lies in \(\{0,1\}^6\) and the shortest factor-path multiplicity is \(r!\).

Freeze:

`X6_FACTOR_PORT = LOCAL_GEOMETRY`

`PRIME_LABEL_PROVENANCE = RETAINED_FIBER`

`X6_PORT != GLOBAL_INTEGER_IDENTITY`

---

## 2. Riesz/Báez-Duarte positive BRC scale

Use the classical Riesz-type Möbius observable

\[
P_2(x)=\sum_{n\ge1}\frac{\mu(n)}{n^2}e^{-x/n^2}.
\]

Define the positive squarefree shell weight

\[
W_x(n)=\mu(n)^2n^{-2}e^{-x/n^2}.
\]

Let

\[
A_x=\sum_n W_x(n),
\qquad
V_x=\sum_n W_x(n)^2.
\]

The positive asymptotic scales are

\[
A_x\asymp x^{-1/2},
\qquad
V_x\asymp x^{-3/2},
\]

with the more precise constants derived in the research session

\[
A_x\sim \frac{3}{\pi^{3/2}}x^{-1/2},
\]

\[
V_x\sim \frac{3\sqrt2}{8\pi^{3/2}}x^{-3/2}.
\]

Hence

\[
\sqrt{V_x}\asymp x^{-3/4}.
\]

The natural effective Cell count is

\[
N_{\rm eff}=\frac{A_x^2}{V_x}\asymp \sqrt x.
\]

Thus the classical RH exponent \(3/4\) coincides with the intrinsic positive BRC RMS/collision scale.

Define coherence

\[
\mathcal C_x=\frac{|P_2(x)|}{\sqrt{V_x}}.
\]

Within the classical Riesz/Báez-Duarte equivalence framework, RH is equivalent to subpolynomial growth of this normalized coherence.

Important boundary:

`RMS_SCALE_IS_POSITIVE_BRC`

`SIGNED_CANCELLATION_IS_FINAL_OBSERVER`

`RMS_INTERPRETATION != RH_PROOF`

---

## 3. Pair-BRC distance histogram

For two positive squarefree Cells \(m,n\), let \(S_m,S_n\) be their prime-support sets. Define

\[
r=|S_m\triangle S_n|.
\]

Aggregate the positive pair mass

\[
H_r(x)=\sum_{|S_m\triangle S_n|=r}W_x(m)W_x(n),
\]

and

\[
\mathcal H_x(z)=\sum_{r\ge0}H_r(x)z^r.
\]

Then exactly

\[
\mathcal H_x(1)=A_x^2,
\]

\[
\mathcal H_x(0)=V_x,
\]

and

\[
\mathcal H_x(-1)=P_2(x)^2.
\]

Therefore the RH problem can be expressed as comparison of one signed parity readout of a completely positive pair-BRC histogram against its zero-distance collision mass.

This is currently the preferred positive-carrier formulation.

---

## 4. Collision-capacity no-go for fixed finite quotient

Suppose a coarse observer collapses the positive shell into only \(M_x\) output states, with coarse masses \(U_j\). By Cauchy,

\[
\sum_jU_j^2\ge \frac{A_x^2}{M_x}.
\]

Relative to the true collision energy,

\[
\frac{\|U\|_2^2}{V_x}\ge \frac{N_{\rm eff}}{M_x}.
\]

Since \(N_{\rm eff}\asymp\sqrt x\), retaining the RH collision scale up to \(x^{o(1)}\) loss requires

\[
M_x\ge x^{1/2-o(1)},
\]

unless the quotient retains an additional orthogonal/provenance fiber.

Consequences:

- collapsing arithmetic identity to the 64 Boolean X6 endpoints is insufficient;
- exponent shape alone is insufficient;
- any fixed finite-state summary that merges positive weights inside fibers suffers polynomial collision inflation.

Freeze:

`X6_LOCAL_PORT = ALLOWED`

`FIXED_FINITE_GLOBAL_IDENTITY_QUOTIENT = FORBIDDEN_FOR_RH_COLLISION_SCALE`

`PRIME/INTEGER_PROVENANCE_MUST_NOT_BE_COLLAPSED`

---

## 5. Shape-only no-go

On an effective range \(n\le x^C\), the total exponent mass satisfies \(\Omega(n)=O(\log x)\). The number of unlabeled exponent partitions is

\[
\exp(O(\sqrt{\log x}))=x^{o(1)}.
\]

Therefore all unlabeled factor-shape statistics together — including \(\Omega,\omega,\tau,B_{\rm fact},\kappa_F\), the sorted exponent partition, etc. — have only subpolynomial state complexity on this range.

This is far below the \(x^{1/2-o(1)}\) collision-resolution requirement.

Freeze:

`FACTOR_SHAPE_GEOMETRY_ALONE != RH_SUFFICIENT_INFORMATION`

---

## 6. Gram-energy formulation

Define for \(\sigma>1/2\)

\[
\mathcal E_\sigma=\int_0^\infty |P_2(x)|^2x^{1-\sigma}\,dx.
\]

Within the classical Riesz/Mellin framework, finiteness across every \(\sigma>1/2\) is an RH-equivalent energy formulation.

The pair kernel integrates exactly to

\[
K_\sigma(m,n)
=2^{\sigma-2}\Gamma(2-\sigma)
(mn)^{-\sigma}
\operatorname{sech}^{2-\sigma}\!\left(\log\frac mn\right).
\]

At the critical boundary \(\sigma=1/2\),

\[
K_{1/2}(m,n)
=\frac{\sqrt\pi}{2^{5/2}}
\frac1{\sqrt{mn}}
\operatorname{sech}^{3/2}\!\left(\log\frac mn\right).
\]

Thus the RH energy is a positive-semidefinite Cell-Cell interaction with a log-balance penalty.

---

## 7. Exact gcd CORE / LEFT / RIGHT decomposition

For squarefree pair \((m,n)\), uniquely write

\[
m=ga,\qquad n=gb,\qquad g=\gcd(m,n),
\]

with \(g,a,b\) pairwise coprime.

Prime provenance splits exactly into three roles:

1. `CORE`: primes shared by both Cells, carried by \(g\);
2. `LEFT`: primes unique to \(m\), carried by \(a\);
3. `RIGHT`: primes unique to \(n\), carried by \(b\).

Moreover

\[
\mu(m)\mu(n)=\mu(a)\mu(b).
\]

The Gram kernel becomes

\[
K_\sigma(ga,gb)
=C_\sigma g^{-2\sigma}(ab)^{-\sigma}
\operatorname{sech}^{2-\sigma}\!\left(\log\frac ab\right).
\]

At \(\sigma=1/2\), the common core has harmonic weight \(g^{-1}\). All sign/orientation information is in the two arms.

This is a mathematically forced three-role decomposition and is preferred over artificial grouping of primes in triples.

Typing guard:

`CORE_LEFT_RIGHT = ARITHMETIC_PAIR_RELATION_TRIAD`

`CORE_LEFT_RIGHT != THREE_NEW_SPATIAL_AXES`

---

## 8. P2 carrier versus P1 divergence

The positive squarefree P2 mass satisfies

\[
\sum_n\frac{\mu(n)^2}{n^{2\sigma}}
=\frac{\zeta(2\sigma)}{\zeta(4\sigma)},
\]

which converges for \(\sigma>1/2\).

But the absolute P1 mass

\[
\sum_n\frac{|\mu(n)|}{n^\sigma}
\]

requires \(\sigma>1\).

Therefore the critical strip \(1/2<\sigma<1\) is exactly the range in which the positive P2/Hilbert carrier is already finite while absolute P1 control has failed.

Research interpretation:

`RH_CRITICAL_STRIP = P2_CARRIER_AVAILABLE_BUT_P1_UNAVAILABLE`

This does not prove RH; it locates the correct norm layer.

---

## 9. Generic observer restriction loses one half power

The Bohr/Hardy Dirichlet-series picture supplies a positive global/Haar P2 model for the prime phases. The arithmetic one-parameter orbit \(p^{-it}\) is a much thinner observer.

Generic local embedding/control from the global P2 coefficient norm requires a stronger weighted coefficient sum corresponding to a one-half-derivative loss; for the Möbius coefficients this pushes the generic threshold back to \(\sigma>1\).

Hence a universal P2-to-local-observer inequality cannot prove RH. Any recovery of the lost half power must be Möbius/prime-provenance specific.

Freeze:

`GENERIC_HILBERT_EMBEDDING != RH_MECHANISM`

`MOBIUS_SPECIFIC_HALF_DERIVATIVE_RECOVERY = OPEN_TARGET`

---

## 10. Local triadic transport pilot

A natural sign-flip move on squarefree factor provenance is

\[
pq\leftrightarrow r,
\]

or with a common core

\[
gpq\leftrightarrow gr.
\]

It changes \(\omega\) parity once and involves three prime labels. This is a genuine minimal parity-flip factor move, unlike mechanically grouping three sieve differences.

Finite dyadic-interval experiments during the research session produced high local matching coverage at distance about \(\sqrt N\), suggesting that the large-prime sector is highly connected under such moves.

However this route has two hard limitations below.

### 10.1 Net-charge obstruction

For any matching confined to one dyadic shell, the number of unmatched vertices is at least

\[
|M(2N)-M(N-1)|.
\]

Thus local graph connectivity does not remove the global Möbius discrepancy.

### 10.2 Smooth-cell obstruction

For any fixed \(K\), consider a rule that may alter at most \(K\) prime labels in one local move. Let a squarefree \(n\in[N,2N]\) be \(y\)-smooth. Any old arm using at most \(K\) labels has size at most \(y^K\); hence its common core has size at least \(N/y^K\). Any distinct endpoint therefore moves by at least this core size.

Choosing \(y\) so that \(y^K\ll\sqrt N\) gives a positive-density family of squarefree smooth Cells for which every such bounded-label move has displacement \(\gg\sqrt N\).

Therefore:

`FIXED_K_LABEL_LOCAL_TRANSPORT -> NO_GLOBAL_RH_SCALE_COVERAGE`.

This fixed-K statement is regarded as an exact structural no-go once the declared move model is fixed.

---

## 11. Smooth sector cannot simply be discarded

The research session checked the known friable Möbius asymptotic literature (de la Bretèche-Tenenbaum / related Buchstab formulations). In the regime \(y\asymp N^{1/4}\), the smooth squarefree sector has a nonzero signed main term of order

\[
\frac{N}{\log^2N},
\]

not merely \(O(\sqrt N)\).

Therefore the strategy

`LARGE-ARM_LOCAL_TRANSPORT + SMOOTH_SIGNED_REMAINDER`

cannot reach RH scale. Smooth and nonsmooth sectors must exchange mass/orientation in any successful global transport mechanism.

Prior-art-dependent numerical constants or the precise Buchstab specialization should be rechecked before theorem promotion; the order-of-magnitude obstruction is the durable research point.

---

## 12. Canonical Möbius quantile/interlacing formulation

Let

\[
a_1<a_2<\cdots
\]

be the positive squarefree integers with \(\mu(a_j)=+1\), and

\[
b_1<b_2<\cdots
\]

be the negative squarefree integers with \(\mu(b_j)=-1\).

Define same-rank monotone transport

\[
a_j\leftrightarrow b_j.
\]

Using

\[
A(x)-B(x)=M(x)
\]

and

\[
A(x)+B(x)=\sum_{n\le x}\mu(n)^2
=\frac6{\pi^2}x+O(\sqrt x),
\]

one obtains the exact equivalence

\[
\boxed{
RH\iff |a_j-b_j|=O_\varepsilon(j^{1/2+\varepsilon})
}
\]

for every \(\varepsilon>0\).

Interpretation:

RH is equivalent to square-root-scale interlacing of the positive and negative Möbius Cell streams under canonical rank-preserving transport.

This formulation automatically allows prime-label symmetric-difference arity to grow with scale, so it avoids the fixed-K smooth-cell obstruction.

Freeze:

`RH = SQUARE_ROOT_MOBIUS_QUANTILE_INTERLACING`

`LOCAL_OPPOSITE_SIGN_EXISTENCE != MASS_BALANCE`

---

## 13. Boolean sign change is weaker than mass transport

Known short-interval sign-change results for real multiplicative functions, including Möbius, establish strong local existence of both signs on sufficiently long short intervals.

That is a Boolean/support statement:

`IS_THERE_AN_OPPOSITE_SIGN_CELL_NEARBY?`

RH requires the stronger count/provenance statement:

`DO_POSITIVE_AND_NEGATIVE_CELL_MASSES_INTERLACE_IN_RANK_AT_SQRT_SCALE?`

A sequence can have both signs in every local window and still sustain a persistent count bias, causing same-rank transport to drift.

BRC hierarchy:

`BOOLEAN_REACHABILITY < COUNT < RANK/PROVENANCE_TRANSPORT`.

---

## 14. Growing provenance-depth requirement

The fixed-K no-go implies immediately that a fixed-depth X6 transport circuit cannot be the complete RH mechanism if each local stage exposes only finitely many new prime labels.

A stronger construction developed in the research session suggests a lower bound of order

\[
K(N)=\Omega\!\left(\frac{\log N}{\log\log N}\right)
\]

for a broad class of local prime-label-edit transports at \(\sqrt N\) displacement scale.

Current status of the stronger constant-level claim:

`CANDIDATE THEOREM / FORMAL PROOF STILL REQUIRED`.

A construction using many primes in a narrow interval suggested the explicit necessary scale

\[
K(N)\ge \left(\frac18-o(1)\right)\frac{\log N}{\log\log N},
\]

but the constant \(1/8\) is not claimed optimal and must not be treated as foundation until the short-interval-prime input and model quantifiers are formally written and independently checked.

Durable machine conclusion already safe:

`X6_DIMENSION_STAYS_FIXED`

`COMPOSITE_BRC_PROVENANCE_DEPTH_MUST_GROW_WITH_SCALE`

---

## 15. No-go registry for this RH branch

Do not spend further research budget on the following as standalone RH mechanisms:

1. endpoint-only additive X6 encoding of all prime factorizations;
2. fixed 64-state X6 Boolean compression;
3. unlabeled factor-shape statistics alone;
4. positive BRC mass interpreted as signed cancellation;
5. Z6 character triad closure by itself;
6. equal-phase 120-degree arithmetic character closure by itself;
7. grouping ordinary sieve differences mechanically into triples;
8. fixed-depth/fixed-K prime-label local matching;
9. large-prime transport plus an untreated smooth signed remainder;
10. local sign-change / Boolean reachability mistaken for global mass balance;
11. generic Hilbert-space observer restriction applied without Möbius-specific structure.

---

## 16. Current surviving architecture

The active RH research architecture is:

\[
\boxed{
\text{Arithmetic Cell identity}
\to
\text{X6 local factor port}
\otimes
\text{noncollapsed prime-label provenance}
\to
\text{scale-growing composite BRC transport}
\to
\text{rank-preserving parity balance}
}
\]

Preferred positive carriers:

- Riesz shell \(W_x(n)\);
- pair-distance histogram \(\mathcal H_x\);
- Gram energy \(\mathcal E_\sigma\);
- same-rank positive/negative Cell transport.

Preferred signed observer:

- Möbius parity only at the final comparison/readout.

---

## 17. Next concrete target

Do not aim immediately at full RH. The next research target is a genuinely weaker power-saving transport theorem.

Let

\[
D_j=a_j-b_j.
\]

Try to prove for some fixed \(\delta>0\)

\[
|D_j|\ll j^{1-\delta}.
\]

Any fixed \(\delta>0\) would represent a true power-scale improvement over purely logarithmic/PNT-level information.

A successful route must use more than local existence of opposite signs. Candidate ingredients:

1. multiscale mass transport rather than one-step local matching;
2. provenance-preserving decomposition into X6-sized local ports;
3. cross-smoothness transport;
4. quantitative control of count imbalance in short or mesoscopic intervals;
5. positive pair/Gram energy to avoid illegitimate signed-BRC compression;
6. scale-growing circuit depth, not fixed depth.

Long-term closure target:

\[
|D_j|\ll_\varepsilon j^{1/2+\varepsilon},
\]

which is RH-equivalent.

---

## 18. Status summary

### Exact / project-derived and retained

- Factor-X6 local port preserving \(\Omega,L_E^2,B_{\rm fact}\).
- Pair-BRC identities \(\mathcal H_x(1),\mathcal H_x(0),\mathcal H_x(-1)\).
- Collision-capacity lower bound for finite quotient state count.
- Shape-only information-capacity no-go.
- Exact Gram kernel formula.
- Exact CORE/LEFT/RIGHT gcd decomposition.
- Fixed-K smooth-cell obstruction for declared bounded-label local-move model.
- Möbius quantile/interlacing equivalence to RH.

### Prior-art-dependent but retained as route constraints

- Classical Riesz/Báez-Duarte RH equivalences.
- Squarefree counting asymptotic.
- Bohr/Hardy Dirichlet P2 framework.
- short-interval sign-change results.
- friable Möbius asymptotics showing a smooth-sector main term above square-root scale.

### Empirical only

- high finite matching coverage of the large-prime triadic graph near \(\sqrt N\) displacement;
- finite distribution of same-rank prime-support symmetric-difference arity.

These are heuristic diagnostics only and are not theorem inputs.

### Candidate theorem requiring formal proof

- quantitative lower bound \(K(N)\gtrsim (1/8)\log N/\log\log N\) for broad scale-growing local label-edit transports.

---

## 19. Repository policy for this branch of research

Future substantive RH/X6/Factor-BRC progress must be recorded in the `awdawmip/enterprise-math` repository, not only in cross-project/global journals.

When a claim advances from heuristic to exact theorem, create a dedicated research note or definition/tool artifact rather than silently upgrading this frontier file.

When a route is falsified, append or create a no-go note so future research does not re-spend budget on it.
