# Orientation-resolved primitive spectral factors and resultants for odd denominators

Status: `FREE_RESEARCH / EXACT FINITE-ALGEBRA THEOREM-CANDIDATE / NOT_FOUNDATION`
Date: `2026-09-05`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on:
- finite midpoint-reflection factorization of Dirichlet continuants;
- primitive divisor factorization;
- phase-multiplication polynomial cocycle;
- native full primitive resultant law.

## 1. Full reflection factors at odd length

Let

\[
M=2h+1
\]

be odd.  The addition identity gives

\[
D_{2h}=D_h^2-D_{h-1}^2.
\]

Define monic reflection factors

\[
\boxed{
E_M(u):=(-1)^h(D_h(u)+D_{h-1}(u)),
}
\]

\[
\boxed{
O_M(u):=(-1)^h(D_h(u)-D_{h-1}(u)).
}
\]

Then

\[
\boxed{Q_M(u)=E_M(u)O_M(u),}
\tag{ORS-1}
\]

with each factor of degree `h`.

Under the internal phase readout, `E_M` contains the even mode indices and `O_M` the odd mode indices in the canonical interval `1,...,M-1`.

## 2. Endpoint orientation localization

Using `D_j(0)=j+1` and `D_j(4)=(-1)^j(j+1)`, one gets

\[
|E_M(0)|=M,
\qquad
|O_M(0)|=1,
\]

\[
|E_M(4)|=1,
\qquad
|O_M(4)|=M.
\tag{ORS-2}
\]

Thus the two reflection channels exchange the full endpoint mass under `u -> 4-u`.

## 3. Primitive orientation factors

All divisors of an odd `M` are odd.  Reflection parity is compatible with denominator reduction, so the full factors decompose divisorwise:

\[
\boxed{
E_M=\prod_{\substack{d\mid M\\d>1}}\Psi_d^E,
\qquad
O_M=\prod_{\substack{d\mid M\\d>1}}\Psi_d^O.
}
\tag{ORS-3}
\]

The primitive factors are monic integral and

\[
\boxed{
\Psi_d=\Psi_d^E\Psi_d^O,
\qquad
\deg\Psi_d^E=\deg\Psi_d^O=\frac{\varphi(d)}2.
}
\tag{ORS-4}
\]

Complement symmetry exchanges them:

\[
\boxed{
\Psi_d^O(u)=(-1)^{\varphi(d)/2}\Psi_d^E(4-u).
}
\tag{ORS-5}
\]

## 4. Primitive endpoint mass lives in one orientation channel

From (ORS-2) and divisor Möbius inversion,

\[
\boxed{
|\Psi_d^E(0)|=P_d,
\qquad
|\Psi_d^O(0)|=1,
}
\tag{ORS-6}
\]

where

\[
P_d=\begin{cases}p,&d=p^a,\\1,&\omega(d)\ge2.\end{cases}
\]

At the complementary endpoint,

\[
\boxed{
|\Psi_d^E(4)|=1,
\qquad
|\Psi_d^O(4)|=P_d.
}
\tag{ORS-7}
\]

Thus the prime-power primitive endpoint mass is orientation-localized before the two channels are recoalesced into `Psi_d`.

## 5. Odd-scale orientation cocycle

Let `m,t` be odd.  The reflection factors satisfy the exact scale cocycles

\[
\boxed{
E_{mt}(u)=E_m(u)E_t(R_m(u)),
}
\tag{ORS-8}
\]

\[
\boxed{
O_{mt}(u)=O_m(u)O_t(R_m(u)).
}
\tag{ORS-9}
\]

This is the reflection-resolved form of the normalized scale cocycle.  It can be read from the finite recurrence or from the internal half-phase identities; no continuous Fourier spectrum is required.

At an `E_m` primitive root, `R_m(alpha)=0`, while at an `O_m` primitive root, `R_m(alpha)=4`.

Using the endpoint values of `E_t,O_t`, the same-orientation quotient has magnitude `t` at every primitive root, whereas the opposite-orientation quotient has magnitude one.

## 6. Cross-orientation resultants are units

For distinct odd `m,n>1`,

\[
\boxed{
|\operatorname{Res}(\Psi_m^E,\Psi_n^O)|
=|\operatorname{Res}(\Psi_m^O,\Psi_n^E)|
=1.
}
\tag{ORS-10}
\]

For incomparable indices this follows immediately because the full resultant is one and all four orientation-resolved resultants are nonzero integers.

For `n=mt`, the quotient cocycles (ORS-8)--(ORS-9) give aggregate opposite-orientation product one over every new divisor level, forcing each nonzero integer cross-resultant to be a unit.

## 7. Same-orientation prime-power resultant law

Let `2<m<n` be odd.  The same quotient cocycle gives, for one orientation channel with `h_m=phi(m)/2`,

\[
 t^{h_m}
=\prod_{\substack{s\mid t\\s>1}}
|\operatorname{Res}(\Psi_m^E,\Psi_{ms}^E)|.
\]

Divisor Möbius inversion in `t` yields

\[
\boxed{
|\operatorname{Res}(\Psi_m^E,\Psi_n^E)|
=\begin{cases}
p^{\varphi(m)/2},&n/m=p^a,\\1,&\text{otherwise}.
\end{cases}}
\tag{ORS-11}
\]

The complementary channel has the identical law:

\[
\boxed{
|\operatorname{Res}(\Psi_m^O,\Psi_n^O)|
=\begin{cases}
p^{\varphi(m)/2},&n/m=p^a,\\1,&\text{otherwise}.
\end{cases}}
\tag{ORS-12}
\]

The full primitive resultant recoalesces the two equal same-orientation contributions, while the cross channels contribute units:

\[
p^{\varphi(m)/2}\cdot p^{\varphi(m)/2}=p^{\varphi(m)}.
\]

## 8. Same-denominator orientation coupling

The full odd-length reflection factors have exact resultant

\[
\boxed{
|\operatorname{Res}(E_M,O_M)|=2^{(M-1)/2}.
}
\tag{ORS-13}
\]

Proof kernel: if `F=D_h-D_(h-1)` and `G=D_h+D_(h-1)`, then at every root of `F`, `G=2D_h`.  Consecutive continuants have unit resultant by the Euclidean recurrence

\[
D_h=(2-u)D_{h-1}-D_{h-2},
\]

so the remaining product is a unit and only `2^h` remains.

Factor (ORS-13) over primitive odd divisors.  Since all cross-denominator opposite-orientation resultants are units by (ORS-10), divisor Möbius inversion gives

\[
\boxed{
|\operatorname{Res}(\Psi_d^E,\Psi_d^O)|
=2^{\varphi(d)/2}.
}
\tag{ORS-14}
\]

This coupling is independent of the odd prime-power endpoint mass.

## 9. Interpretation

Before orientation recoalescence, an odd primitive denominator has two finite channels:

```text
E-channel:
endpoint u=0 carries primitive prime-power mass P_d
same-orientation scale resultants carry p^(phi/2)

O-channel:
endpoint u=4 carries primitive prime-power mass P_d
same-orientation scale resultants carry p^(phi/2)

E <-> O cross-denominator resultants = units
E <-> O same-denominator coupling = 2^(phi/2)
```

The full primitive factor `Psi_d=Psi_d^E Psi_d^O` multiplies the two same-orientation arithmetic channels together.  Therefore full positive resultant data is correct but strictly less typed than the orientation-resolved algebra.

Freeze:

`ODD_PRIMITIVE_SPECTRUM = TWO_REFLECTION_ORIENTATION_CHANNELS`.

`FULL_RESULTANT_PRIME_POWER_LAW = RECOALESCED_PAIR_OF_SAME_ORIENTATION_LAWS`.

`CROSS_ORIENTATION_SCALE_RESULTANTS = UNITS`.

`SAME_DENOMINATOR_ORIENTATION_COUPLING = 2^(phi/2)`.
