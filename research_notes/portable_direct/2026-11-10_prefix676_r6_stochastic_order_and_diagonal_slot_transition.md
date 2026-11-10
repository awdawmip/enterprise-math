# PREFIX-676-R6 — Exact stochastic order and a diagonal slot-phase transition in the frozen BRC observer

Date: 2026-11-10 (Asia/Shanghai). Mode: independent portable TASK_RESEARCH. Source execution identity: Researcher-ID `EM-DIRECT-1659EA`; Research-Activity-ID `RA-467440BA332695697F2EBC2F`.

Scientific input is fixed at `f42f2906d77f24085c123f3ccfe9667d41caa96d`. The model is the **189-survivor-layer, two-informative-direction, first-stop statistical observer** of Heartbeat World X6. Its two observer probabilities `p,z` are not primitive space axes or a two-dimensional native plane. The results below concern the declared stochastic observation, not an unperformed physical-dynamics experiment.

Status: `AUTHOR_DERIVED / EXACT_INTEGER_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## Question and two results

PREFIX-675 solved the complete one-dimensional edge `p=0`. An efficient global two-variable exclusion still needs to understand how variance behaves when one observer probability is increased. This note establishes a useful ordered carrier and an exact counterexample to a tempting coordinate-monotonicity shortcut.

Let `A_n(k)` denote the original frozen signed-path survivor multiplicity at depth `n`, with `A_n(k)=0` outside its surviving indices. Define

[
s_n(x)=sum_{k=0}^{n}A_n(k)x^k(1-x)^{n-k},quad 0le xle 1/2,quad n=0,ldots,188.
]

Let `Y_x` denote the associated first-stop Poissonized time, and for **independent** clocks `Y_p,Y_z` let

[
Y(p,z)=max(Y_p,Y_z),quad
mu(p,z)=E[Y(p,z)],quad W(p,z)=mathrm{Var}(Y(p,z)),
]
[
V_q(p,z)=q^2W(p,z)-qmu(p,z),qquad 12le qle24.
]

**Theorem 676.1 (stochastic order of the marginal first-stop clock).**
For every real `0<=x<=y<=1/2` and every `t>=0`,

[
Pr(Y_x>t)lePr(Y_y>t).
]

Consequently, for fixed `z`, the distribution of `Y(p,z)` is stochastically nondecreasing in `p` on `[0,1/2]`, and its mean is nondecreasing. The same holds with the two parameters exchanged. This property is established for the exact finite frozen model, by 8,836 integer coefficient comparisons.

**Theorem 676.2 (exact change of the diagonal-vs-edge variance ordering).**
Define

[
Deltamu(z)=mu(z,z)-mu(0,z),quad
Delta W(z)=W(z,z)-W(0,z),
]
[
D_q(z)=V_q(z,z)-V_q(0,z)=q(qDelta W(z)-Deltamu(z)).
]

Set `a=13/250=0.052`, `b=53/1000=0.053`, `c=27/500=0.054`. Exact rational computation proves

[
egin{array}{c|rr}
z & lfloor D_{12}(z)floor & lfloor D_{24}(z)floor\
hline
a &207&1015\
b &-32&63\
c &-280&-927
end{array}
]

and, at `z=b`,

[
Delta W(b)>0,qquad 17Delta W(b)<Deltamu(b)<18Delta W(b).
]

There is therefore an exact, well-defined slot threshold

[
q_0=rac{Deltamu(b)}{Delta W(b)},qquad oxed{17<q_0<18},
]

such that `D_q(b)<0` for `12<=q<q_0`, `D_{q_0}(b)=0`, and `D_q(b)>0` for `q_0<q<=24`.

For **every real** `q in [12,24]`, the continuous function `z -> D_q(z)` has at least one zero in `(a,c)`. For the two actual slot schemes this sharpens to

[
exists z_{12}in(a,b):D_{12}(z_{12})=0,
qquad
exists z_{24}in(b,c):D_{24}(z_{24})=0.
]

This is an existence statement; it does not assume uniqueness of those zeros. The positive signs at `a` and negative signs at `c` hold **uniformly** for all real `q in [12,24]`.

## Proof of Theorem 676.1

Define normalized Bernstein coefficients

[
c_{n,k}=A_n(k)/inom nk.
]

Rebuild the exact 190 rows `n=0,dots,189` from the frozen decision predicate of PREFIX-675. The row at `n=189` is empty and all earlier rows satisfy reflection symmetry. Integer cross-products check

[
A_n(k+1)inom nk geA_n(k)inom n{k+1},
quad 0le k<lfloor n/2floor,
]

for every `1<=n<=188`. These 8,836 inequalities exactly establish that `c_{n,k}` is nondecreasing toward the center and symmetric; the first 25 rows are identically full. All tests use integers with no rounding.

Since `s_n(x)` is the Bernstein polynomial with coefficients `c_{n,k}`, differentiating yields

[
s_n'(x)=nsum_{k=0}^{n-1}inom{n-1}{k}
(c_{n,k+1}-c_{n,k})x^k(1-x)^{n-1-k}.
]

Pair `k` with `n-1-k`. Symmetry changes the coefficient difference's sign, while for `0<=x<=1/2` the Bernstein weight at the smaller index is at least the reflected weight. Each paired contribution is nonnegative, and any central unpaired term vanishes. Hence `s_n'(x)>=0`.

The Poissonized survival function is exactly

[
Pr(Y_x>t)=e^{-t}sum_{n=0}^{188}s_n(x)rac{t^n}{n!}.
]

Its summands are nonnegative and all `s_n` are nondecreasing on the interval, proving first-order stochastic dominance. The independent maximum has survival `1-(1-S_p(t))(1-S_z(t))`, which is also nondecreasing in either marginal survival. QED.

## Exact finite proof of Theorem 676.2

All calculations use `fractions.Fraction` and the original 189-layer survivor histograms, not floating point comparisons. For rational `x=a/d`, the exact survival probabilities are

[
s_n(a/d)=d^{-n}sum_k A_n(k)a^k(d-a)^{n-k}.
]

For independent clocks, define the exact minimum-time kernels

[
w_{nm}=rac{inom{n+m}{n}}{2^{n+m+1}},qquad
g_{nm}=rac{n+m+1}{2}w_{nm}.
]

Their exact first two maximum moments obey

[
mu(p,z)=sum_{n=0}^{188}{s_n(p)+s_n(z)}
-sum_{n,m=0}^{188}w_{nm}s_n(p)s_m(z),
]

[
rac{E[Y(p,z)^2]}2
=sum_{n=0}^{188}(n+1){s_n(p)+s_n(z)}
-sum_{n,m=0}^{188}g_{nm}s_n(p)s_m(z).
]

The script evaluates these finite sums for `(0,a),(a,a),(0,b),(b,b),(0,c),(c,c)`. Exact numerator/denominator comparisons establish all six signs and the two strict threshold inequalities in Theorem 676.2. The companion JSON records floors at scale `10^6` for `Delta mu`/`Delta W`, integer floors of each signed `D_q`, and exact numerator/denominator bit lengths. The floors are summaries of **exact** fractions, not the basis of the comparisons.

For each fixed `z`, `D_q(z)/q=qDelta W(z)-Deltamu(z)` is affine in `q`. Its signs at `q=12,24` therefore determine the same strict signs for all intervening real `q` at `a` and `c`. The exact inequalities at `b` give the unique threshold `q_0` for this fixed comparison. Continuity in `z` and the intermediate value theorem yield the asserted crossing existence and the disjoint brackets for `q=12,24`. QED.

## Execution, interpretation and next discriminating step

Run `python research_notes/portable_direct/PREFIX676_R6_STOCHASTIC_ORDER_AND_DIAGONAL_CROSSING.py` and capture its stdout as the companion JSON. The author run passed all **8,836 exact unimodality comparisons**, checked reflection, extinction at 189, 9,529 nonzero histogram cells and the strict rational slot-comparison inequalities. Exact reconstruction follows the frozen decision predicate in PREFIX-675. Numerical decimal impressions are ancillary only.

**Research consequence:** the first-stop clocks, and their independent maximum, have a monotone stochastic/mean carrier, but the **variance objective** `V_q` reverses a natural diagonal-versus-edge comparison near `z≈0.053`. Thus a proposed all-domain pruning rule that treats `V_q` as coordinatewise nonincreasing cannot be justified by marginal stochastic order alone. The proved transition brackets may instead be used to split a rigorous two-dimensional branch-and-bound search without making that shortcut.

**Next frontier:** use the complete edge certificate from PREFIX-675 as the strict global competitor; introduce joint Bernstein/interval bounds for cells with `p>=1/64` and for `z` outside the previously certified band; preserve the new crossing signs as regression tests for interval exclusion logic. The parent target remains the global maximum over full `[0,1]^2`, while the present theorem is a scoped exact stochastic-geometry result.

References: frozen scientific pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`; predecessor source `research_notes/portable_direct/2026-11-10_prefix675_r6_complete_global_edge_maxima.md` at `c8d034bda669497d88a53ecf4cae67d6bff4ff76`; current applicable Source continuation protocol `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`. No shared CLAIM, Result or Review is created by this independent artifact.
