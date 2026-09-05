# Viète X6 trajectory precision: periodicity obstruction, exact memory lower bound, and horizon-stratified BRC quotient

Status: `FREE_RESEARCH / EXACT RELEVANT-SCOPE NO-GO + QUOTIENT CERTIFICATES / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1255`
Parent line: `#1158`
Depends on:
- `research_notes/VIETE_X6_FIXED_RADIUS_MICROTRACE_C12_20260905.md`
- `research_notes/VIETE_2ADIC_ROOT_GAUGE_ARCHIMEDEAN_SELECTION_20260905.md`
Checker: `experiments/viete_x6_prostate_memory_obstruction_20260905/check_prostate_memory_obstruction.py`
Checker source commit: `feb6320cf3f4382b94480817ad624c14dd0b4dfa`

## 1. Question sharpened after the native C12 lift

The centered-X6 analysis produced an actual 12-Cell primitive outer microcycle

\[
\mathcal O_{12}
=
(a_0,m_0,a_1,m_1,\ldots,a_5,m_5),
\qquad m_k=a_k+a_{k+1},
\]

with native successor `F` satisfying

\[
F^{12}=1,
\qquad
F^6(z)=-z,
\]

and an exact local phase semiconjugacy onto the already-proved C12 successor.

This raises the next exact question in #1255:

> can this actual native Cell trajectory, or any fixed finite-memory augmentation of a fixed-radius Cell trajectory, intertwine the **full** rotation precision pro-state
> \(\mathcal P_{\rm rot}=\varprojlim_m C_{6\cdot2^m}\)?

The answer is no.

The obstruction is not geometric approximation. It is finite-period versus aperiodic successor dynamics.

## 2. Finite target levels and their successor

Write

\[
M_m=6\cdot2^m,
\qquad
\Gamma_m=C_{M_m}.
\]

Let

\[
Q_m([k])=[k+1]
\]

be the one-step phase successor.

The precision projections commute with successor, so the inverse limit carries the compatible successor

\[
Q:\mathcal P_{\rm rot}\to\mathcal P_{\rm rot},
\qquad
Q((z_m)_m)=(z_m+1)_m.
\]

This is the successor that a full trajectory-to-pro-state factorization must intertwine if one native transition is declared to represent one precision-phase successor.

## 3. Lemma: cyclic source criterion at finite precision

Let `X_N` be one source orbit of exact period `N` under `T`:

\[
T^N x=x.
\]

Suppose there is a map

\[
\Phi_m:X_N\to C_{M_m}
\]

satisfying

\[
\Phi_m(Tx)=Q_m(\Phi_m(x)).
\]

Iterating `N` times gives

\[
\Phi_m(x)
=
\Phi_m(T^N x)
=
Q_m^N(\Phi_m(x))
=
\Phi_m(x)+N.
\]

Hence

\[
N\equiv0\pmod{M_m}.
\]

Conversely, if `M_m | N`, then after choosing an origin on the source cycle,

\[
\Phi_m(T^k x_0)=[k]_{M_m}
\]

is well-defined and intertwines the successors.

Therefore

\[
\boxed{
X_N\text{ factors to }(C_{M_m},+1)
\iff
M_m\mid N.
}
\]

This is exact and requires no analytic completion.

## 4. Corollary: the native outer C12 cycle cannot reach C24+

For the actual native outer cycle,

\[
N=12.
\]

Therefore

\[
6\mid12,
\qquad
12\mid12,
\]

so its exact semiconjugacies to C6 and C12 are allowed.

But

\[
24\nmid12.
\]

Hence there is no map

\[
\Phi_2:\mathcal O_{12}\to C_{24}
\]

with

\[
\Phi_2F=Q_2\Phi_2.
\]

A fortiori there is no such factorization to any deeper C48, C96, ... level.

Thus

\[
\boxed{
\text{ACTUAL NATIVE OUTER 12-CELL CYCLE}
\to C_{12}
\text{ EXACTLY, BUT NOT TO }C_{24+}
}
\]

under one-step successor intertwining.

This dynamically explains why the prior C24 result had to leave the single spatial Cell-ray category and use a richer typed realization.

## 5. The full pro-state successor has no finite-period points

Suppose for some positive integer `p` that

\[
Q^p(z)=z
\]

in

\[
\mathcal P_{\rm rot}=\varprojlim_m C_{6\cdot2^m}.
\]

Project to every finite level. Then

\[
p\equiv0\pmod{6\cdot2^m}
\]

for every `m`.

No positive integer is divisible by arbitrarily large powers of two. Therefore no such `p` exists.

Hence

\[
\boxed{
Q\text{ has no finite-period point on }\mathcal P_{\rm rot}.
}
\]

Equivalently, in the already-established identification

\[
\mathcal P_{\rm rot}\cong C_3\times\mathbf Z_2,
\]

the precision successor contains an aperiodic `Z_2` translation direction.

## 6. Main no-go: no finite-period native state can intertwine the full pro-state

Let `(X,T)` contain a periodic point `x` of positive period `N`.

If

\[
\Phi:X\to\mathcal P_{\rm rot}
\]

satisfied

\[
\Phi\circ T=Q\circ\Phi,
\]

then

\[
\Phi(x)
=
\Phi(T^N x)
=
Q^N(\Phi(x)),
\]

contradicting the aperiodicity theorem above.

Therefore

\[
\boxed{
\text{NO POSITIVE-PERIOD SOURCE ORBIT CAN SEMICONJUGATE TO FULL }(\mathcal P_{\rm rot},Q).
}
\]

This applies immediately to the 12-Cell outer microcycle.

## 7. Fixed-radius finite-memory no-go

For any fixed integer native squared radius `R`, the centered-X6 shell

\[
\Sigma_R=\{x\in\mathbf Z^6:\|x\|_E^2=R\}
\]

is finite.

Now augment a shell trajectory state by any **fixed finite** amount of local memory, for example:

- previous `k` Cells for fixed `k`;
- incoming edge from a finite alphabet;
- STAR frame;
- sweep/chirality bit;
- finitely many BRC branch bits;
- any other finite label set.

The resulting state space remains finite.

Any deterministic self-transition on a finite state space is eventually periodic. If the transition is reversible/permutation-like, every orbit is periodic from the start.

Suppose an eventually periodic source state satisfied a full pro-state semiconjugacy. If

\[
T^{r+p}x=T^r x,
\qquad p>0,
\]

then

\[
Q^{r+p}\Phi(x)=Q^r\Phi(x),
\]

and cancellation of the bijection `Q^r` gives

\[
Q^p\Phi(x)=\Phi(x),
\]

again impossible.

Therefore

\[
\boxed{
\text{FIXED RADIUS + ANY FIXED FINITE LOCAL MEMORY}
\not\to
\text{FULL ROTATION PRECISION PRO-STATE}
}
\]

under exact one-step successor intertwining.

This is a relevant-scope `NO_GO` for the local-state strategy posed in #1255.

## 8. Exact finite-level memory lower bound

The obstruction is quantitative.

At precision level `m`, the target cycle has

\[
M_m=6\cdot2^m
\]

distinct phases and `Q_m` acts transitively on all of them.

If a nonempty source orbit factors equivariantly to this target, its image is `Q_m`-invariant. Since the `+1` action is transitive, the image must be all of `C_{M_m}`.

Thus the source needs at least

\[
6\cdot2^m
\]

distinguishable states on the relevant orbit.

If the state architecture is explicitly

\[
\text{C6 coarse phase}\times\text{binary memory of }b\text{ bits},
\]

it has at most

\[
6\cdot2^b
\]

states. Therefore

\[
6\cdot2^b\ge6\cdot2^m
\]

and hence

\[
\boxed{b\ge m.}
\]

So each added dyadic precision level requires at least one additional binary distinction beyond the coarse C6 phase.

In particular:

\[
\boxed{
\text{UNBOUNDED DYADIC PRECISION}
\Longrightarrow
\text{UNBOUNDED BINARY STATE INFORMATION}.
}
\]

This gives a direct dynamical interpretation of the `Z_2` factor in

\[
C_3\times\mathbf Z_2.
\]

It is not merely an algebraic completion artifact: an exact all-level successor factorization requires an unbounded compatible binary address.

## 9. Important distinction: precision bits are not automatically BRC branch bits

At the first refinement, the C12 outer native cycle has two temporal phase types:

\[
E_k\quad\text{and}\quad G_k.
\]

This is the first binary precision distinction beyond C6.

Separately, the native shortest path from one C6 shell phase to the next has two BRC branches:

\[
\beta\in\{\mathrm{INNER},\mathrm{OUTER}\}.
\]

These are not the same binary variable.

Freeze:

\[
\boxed{
\text{DYADIC PRECISION BIT}
\neq
\text{BRC INNER/OUTER PATH-PROVENANCE BIT}.
}
\]

If the domain is restricted to the selected OUTER branch, the BRC branch bit becomes constant and the remaining C12 binary distinction is the Cell/gate-or-microtime precision parity.

If both shortest native branches are retained and future operations can inspect path provenance, then the branch bit is additional information beyond the precision bit.

## 10. Horizon-stratified quotient theorem for the BRC branch bit

Let a local macro state record an ordered adjacent C6 phase pair and the branch by which that macro edge was realized:

\[
D
=
\{(p,c,\beta):p\sim c,\ \beta\in\{I,O\}\}.
\]

Because an ordered adjacent pair identifies its unique STAR frame and sweep direction, define

\[
S(p,c)=(c,n(p,c)),
\]

where `n(p,c)` is the unique C6 neighbor of `c` different from `p` in that recovered STAR.

Define the branch-forgetting map

\[
q_6(p,c,\beta)=(p,c).
\]

Allow any lifted next branch `beta'`:

\[
T_{\beta'}(p,c,\beta)
=(c,n(p,c),\beta').
\]

Then for every current and next branch choice,

\[
\boxed{
q_6\circ T_{\beta'}
=
S\circ q_6.
}
\]

Therefore the INNER/OUTER branch bit is safely erasable for the exact future-operation lease generated only by:

- ordered macro C6 successor iteration;
- macro predecessor/reversal of the ordered phase edge;
- STAR-frame recovery from the ordered adjacent pair;
- common translation of the local configuration;
- carrier-phase operations that do not inspect microtime/path data.

This is a positive, scope-typed operation-safe quotient certificate.

## 11. The same quotient fails as soon as midpoint/C12 precision is observed

Take the two matched native states with the same macro endpoints `(p,c)`:

\[
X_I=(p,c,I),
\qquad
X_O=(p,c,O).
\]

They satisfy

\[
q_6(X_I)=q_6(X_O).
\]

But the native midpoint/intermediate observation differs:

\[
M(X_I)=0,
\]

while

\[
M(X_O)=p+c\neq0.
\]

At the phase-readout level:

- the INNER midpoint has no nonzero radial phase;
- the OUTER midpoint has exactly the C12 half-angle/gate phase.

Thus

\[
M(X_I)\neq M(X_O),
\]

and no operation on the branch-forgotten fiber can reconstruct the C12 intermediate observation.

Therefore

\[
\boxed{
\text{DROP }\beta
\text{ IS UNSAFE FOR A HORIZON CONTAINING C12 MIDPHASE OBSERVATION.}
}
\]

This is an exact matched-fiber BRC counterexample of the form required by #1255.

## 12. Full native path/provenance horizon also forces the branch bit

The two shortest traces are

\[
p\to0\to c
\]

and

\[
p\to p+c\to c.
\]

They differ in:

- intermediate Cell;
- intermediate radius;
- ordered signed-axis word;
- pivot visitation;
- BRC branch identity.

Any future-operation horizon containing one of those observations distinguishes the two matched states.

Because there are exactly two shortest branches, at this local scope:

- at least one bit is necessary to preserve full branch provenance;
- one bit `beta` is sufficient.

Hence

\[
\boxed{
\beta\text{ IS INFORMATION-THEORETICALLY MINIMAL FOR THE TWO-SHORTEST-PATH PROVENANCE HORIZON.}
}
\]

This is a local minimality theorem, not a claim about arbitrary longer native paths.

## 13. Sweep reversal behavior

Reverse a realized shortest macro edge.

The INNER trace

\[
p\to0\to c
\]

reverses to

\[
c\to0\to p,
\]

which is still INNER.

The OUTER trace

\[
p\to p+c\to c
\]

reverses to

\[
c\to p+c\to p,
\]

which is still OUTER.

Thus branch type is reversal-even:

\[
\boxed{
\beta(RX)=\beta(X).
}
\]

By contrast, the ordered macro phase edge reverses its sweep direction.

So once again:

\[
\boxed{
\text{SWEEP REVERSAL}
\neq
\text{BRC BRANCH FLIP}.
}
\]

This also remains distinct from endpoint half-turn.

## 14. Why old R059D fixed-length turn results do not canonically select the new OUTER branch

Historical Driver material contains accepted R059D fixed-length turn-orbit theorems, including Stage AK. However that theorem used the older state machine

\[
S=(O,r,\mathrm{sector},\mathrm{phase},a,b,z),
\qquad
R(a,b)=(-b,a+b),
\]

and explicitly retained the boundary that unique canonical resolver selection among all admissible target resolvers was not proved at that stage.

The current 2026-09-05 spatial Foundation has since rebased native Cell identity to the centered signed-X6 torsor and retyped prior plane constructions as carrier/readout material unless rederived.

No current preservation theorem was found that identifies the old R059D resolver with the centered-X6 INNER/OUTER BRC split.

Therefore this research freezes:

`LEGACY_R059D_OUTWARD/FIXED_LENGTH_RESOLVER -> NOT_PORTABLE_AS_X6_OUTER_BRANCH_SELECTION_WITHOUT_REPROOF`.

The currently proved branch selection remains only the scope-typed theorem:

`DEFINED_NONZERO_INTERMEDIATE_PHASE WITHIN TWO SHORTEST PATHS -> OUTER`.

## 15. Strongest answer now available for #1255

The state question separates into three exact layers.

### Layer A — finite C6 macro dynamics

`previous phase + current phase` is enough to recover local STAR frame and sweep.

The BRC INNER/OUTER branch may be safely forgotten if the declared horizon never inspects microtime, C12 midpoint, or path provenance.

### Layer B — first C12 native precision

To realize the C12 intermediate phase by native Cells, the OUTER branch gives the exact 12-Cell lift.

If both shortest branches remain admissible, their provenance must be retained for any horizon that can inspect the intermediate state or path.

### Layer C — full pro-state

No fixed finite local-memory augmentation of a fixed-radius Cell trajectory can intertwine the full successor on

\[
\mathcal P_{\rm rot}\cong C_3\times\mathbf Z_2.
\]

At level `m`, at least `m` binary distinctions beyond C6 are required. All levels require unbounded compatible state information.

Thus

\[
\boxed{
\text{PREVIOUS CELL IS ENOUGH FOR LOCAL FRAME,}
\quad
\text{BUT NO FIXED FINITE HISTORY IS ENOUGH FOR FULL }\mathcal P_{\rm rot}.
}
\]

## 16. #1255 disposition

At the resolution bar stated by the issue, the finite-local-state strategy has now reached a typed negative result:

\[
\boxed{
\texttt{NO_GO__FIXED_RADIUS_FINITE_LOCAL_STATE_TO_FULL_PROSTATE}
}
\]

with two independent witnesses:

1. **periodicity witness:** the actual native outer 12-Cell cycle factors to C12 but fails already at C24;
2. **matched-fiber witness:** INNER and OUTER shortest paths share the same C6 macro endpoints but differ under C12 midpoint/native path future operations.

What remains open is a stronger construction problem, not the rejected finite-state one:

> augment the actual trajectory with an **unbounded compatible precision/history state** and determine whether that enlarged object admits a canonical operation-safe map to the principal `Z_2` precision tower.

The natural candidate architecture is therefore not `current Cell + previous Cell + a few bits`, but a hybrid state of the form

\[
\boxed{
\text{native local trajectory state}
\times
\text{compatible unbounded dyadic precision address},
}
\]

with an explicit proof that the second factor is generated by or legitimately attached to native trajectory history rather than imported from the target by definition.

That is the next hard frontier.
