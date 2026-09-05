# Viète rotation precision pro-state: fixed profinite address, scale-root readouts, and first-winding selection

Status: `FREE_RESEARCH / EXACT PRO-OBSERVER THEOREM / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent: `#1158`

## 1. Why a pro-state is the correct deep-precision type

Current project substrate explicitly treats finite resolution/precision as endogenous to the research ontology. P000 separately types time as the trace/order of relational change.

Therefore deeper dyadic refinement should not be forced into either of two false types:

- a new spatial Cell at every level;
- a metric midpoint of native time.

Instead use the finite observer tower itself.

Let

\[
N_m=6\cdot2^m,
\qquad
\Gamma_m=C_{N_m},
\]

with precision-collapse maps

\[
p_m:\Gamma_{m+1}\to\Gamma_m,
\qquad
p_m([k])=[k]\pmod{N_m}.
\]

Define the exact precision pro-state carrier

\[
\boxed{
\mathcal P_{\rm rot}:=\varprojlim_m\Gamma_m.
}
\]

By the Chinese remainder decomposition,

\[
\boxed{
\mathcal P_{\rm rot}\cong C_3\times\mathbf Z_2.
}
\]

This is a derived precision carrier, not an extra spatial or temporal dimension.

## 2. One pro-state, many finite observers

A point

\[
x=(x_m)_{m\ge0}\in\mathcal P_{\rm rot}
\]

satisfies

\[
p_m(x_{m+1})=x_m.
\]

The level-`m` observer is simply

\[
O_m(x)=x_m\in\Gamma_m.
\]

Finite equality is therefore observer-relative:

\[
O_m(x)=O_m(y)
\]

may hold even when a finer observer separates `x` and `y`.

No physical time evolution is asserted when `m` changes. `m` is resolution depth.

## 3. Scale-dependent character readout automatically gives square roots

Choose compatible faithful finite characters

\[
\chi_m:\Gamma_m\to\mu_{N_m}
\]

whose generators satisfy

\[
\zeta_{m+1}^2=\zeta_m.
\]

For a fixed pro-state `x`, define

\[
z_m(x)=\chi_m(x_m).
\]

Because

\[
x_{m+1}\equiv x_m\pmod{N_m},
\]

one has exactly

\[
\begin{aligned}
z_{m+1}(x)^2
&=\zeta_{m+1}^{2x_{m+1}}\\
&=\zeta_m^{x_{m+1}}\\
&=\zeta_m^{x_m}\\
&=z_m(x).
\end{aligned}
\]

Thus

\[
\boxed{
z_{m+1}(x)^2=z_m(x)
}
\]

is not a temporal midpoint law. It is the relation between character readouts of the **same pro-state at adjacent precision scales**.

The Viète half-trace recurrence follows from this identity on the selected pro-state.

## 4. Normalized phase distance on a pro-state

For each finite observer define

\[
\delta_m(x)
=\frac{d_{N_m}(x_m,0)}{N_m},
\]

where `d_N` is cyclic Cayley distance.

Choose the least signed integer representative `r_m` of `x_m`:

\[
|r_m|\le\frac{N_m}{2}.
\]

Then

\[
\delta_m(x)=\frac{|r_m|}{N_m}.
\]

Compatibility gives

\[
r_{m+1}=r_m
\quad\text{or}\quad
r_{m+1}=r_m\pm N_m.
\]

If a jump occurs, then

\[
|r_{m+1}|
\ge N_m-|r_m|
\ge\frac{N_m}{2},
\]

and since `N_(m+1)=2N_m`,

\[
\boxed{
\delta_{m+1}(x)\ge\frac14.
}
\]

## 5. Archimedean-germ theorem

Suppose

\[
\delta_m(x)\to0.
\]

Then the jump alternative can occur only finitely often. Hence the least signed representatives eventually stabilize:

\[
r_m=n\in\mathbf Z
\]

for all sufficiently large `m`.

Therefore `x` is exactly the diagonal image of the ordinary integer `n` in every finite quotient.

Conversely, if `x` is the diagonal image of an ordinary integer `n`, then for sufficiently large `m` the least representative is `n`, so

\[
\delta_m(x)=\frac{|n|}{N_m}\to0.
\]

Hence

\[
\boxed{
\delta_m(x)\to0
\iff
x\in\mathbf Z\subset C_3\times\mathbf Z_2.
}
\]

The ordinary integers are exactly the pro-states possessing an Archimedean near-identity germ under the normalized cyclic observers.

This is stronger than merely saying the profinite and Archimedean completions differ: it identifies the exact subset of profinite states on which the finite character samples can approach identity in this normalization.

## 6. Generic profinite states exhibit recurrent macroscopic readout excursions

If

\[
x\in\mathcal P_{\rm rot}\setminus\mathbf Z,
\]

then the least representatives do not stabilize. Therefore jumps occur infinitely often, and at infinitely many levels

\[
\boxed{
\delta_m(x)\ge\frac14.
}
\]

This is a normalized phase-readout statement, not a claim of physical oscillatory motion.

It gives a precise meaning to the fact that a profinite precision state can be perfectly well defined while failing to possess an Archimedean infinitesimal-phase interpretation.

## 7. Pure 2-primary fiber and winding aliases

Project to the coarse `C3` factor. The kernel is

\[
K=\ker(\mathcal P_{\rm rot}\to C_3)
\cong\mathbf Z_2.
\]

The Archimedean-germ points in this fiber are exactly

\[
K\cap\mathbf Z=3\mathbf Z.
\]

The towers rooted at the C6 half-turn must be odd multiples of three:

\[
\boxed{
\ldots,-15,-9,-3,3,9,15,\ldots
}
\]

because they reduce to `[3]` modulo six.

Under the standard Archimedean character decoder these are precisely the odd-winding aliases of the same half-turn endpoint.

No classical value of pi is required for the finite/profinite classification itself.

## 8. First winding selects ±3

Among the nonzero integer points in the pure 2-primary fiber with half-turn parity, the smallest absolute representatives are

\[
\boxed{\pm3.}
\]

They are exactly the two all-level shortest/strictly-refining towers found in the `Z_2^×` gauge classification.

Sweep chirality exchanges them. Choosing the forward orientation selects

\[
\boxed{x_{\rm Viete}=3.}
\]

Thus the principal Viète tower has an invariant pro-state characterization:

\[
\boxed{
\text{the shortest positive Archimedean-germ integer in the pure 2-primary rotation fiber.}
}
\]

Its finite projections are simply

\[
O_m(x_{\rm Viete})=[3]_{6\cdot2^m}.
\]

## 9. Viète recursion is scale readout, not pro-state motion

For the selected fixed pro-state `x_Viete=3`, write

\[
z_m=z_m(x_{\rm Viete}).
\]

Then

\[
z_{m+1}^2=z_m.
\]

The symmetric and antisymmetric traces

\[
c_m=\frac{z_m+z_m^{-1}}2,
\qquad
s_m=\frac{z_m-z_m^{-1}}{2J}
\]

therefore obey the exact Viète relations.

But the underlying pro-state has not changed:

\[
x_{\rm Viete}=3
\]

at every resolution.

What tends toward identity is the **scale-dependent Archimedean character readout**, not the profinite state itself.

This gives the precise type-safe form of the intuition that increasing precision can reveal smaller and smaller phase while the exact underlying discrete address is already fixed.

## 10. Where the completion constant lives

The rotation completion constant is not equal to the profinite coordinate `3`.

It arises from the renormalized character germ, e.g.

\[
\Pi_m=2^m s_m,
\]

and from its target-free completion limit.

Thus the roles are:

- `3`: exact selected profinite/precision address;
- `z_m,c_m,s_m`: level-dependent finite character readouts;
- `Pi_m`: renormalized finite slope/half-period readout;
- `Pi_rot=tau`: the completed generator-scale constant.

This prevents conflating state convergence with readout renormalization.

## 11. BRC observer audit

The maps

\[
O_{m+1}\to O_m
\]

are nested observer quotients. Higher 2-adic bits are provenance that a level-`m` observer erases.

Operations such as successor, inversion and finite cyclic incidence factor through the appropriate finite quotient. The future operation "refine the phase character" does not factor through a permanently fixed level, so the projective carrier retains all finite precision information.

This is exactly the observer/future-operation discipline required by the current BRC policy.

No positive branch mass is involved in defining the pro-state.

## 12. Native/process boundary

Current project substrate already allows finite resolution/precision as endogenous research ontology. Therefore `P_rot` is a legitimate derived **precision carrier** without claiming a new eighth dimension.

This does not prove that every projection state is a new physical Cell or a new native time event. The physical provenance remains layered:

- C6: ordered-neighbor Cell direction quotient;
- C12: actual Cell/gate incidence;
- distinguished C24 root: balanced native segment spinor;
- deeper levels: exact precision observers / character states unless another physical carrier is proved.

The deep Viète algebra therefore no longer requires a fictitious temporal midpoint. The remaining question, if one insists on G0 spatial realization of every precision state, is a stronger requirement than is needed for the exact precision/pro-observer derivation itself.
