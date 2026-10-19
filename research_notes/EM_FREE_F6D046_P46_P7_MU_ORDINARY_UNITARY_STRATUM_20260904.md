# The p=7 reduction as the inert mu-ordinary unitary stratum

Status: `FREE_RESEARCH / DERIVED PEL-NEWTON CLASSIFICATION / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research units: `R67-INERT-HODGE-COCHARACTER-AVERAGE / R68-P7-MU-ORDINARY / R69-MAXIMAL-INERT-P-RANK`.

## 1. Hodge cocharacter at an inert prime

The geometric endomorphism field is \(K=\mathbf Q(i)\), and the Hodge signature is \((3,1)\). At a prime inert in \(K\), the two embeddings of the unramified quadratic local field are exchanged by arithmetic Frobenius.

Over the unramified closure, the Hodge cocharacters on the two four-dimensional eigenspaces have dominant weight vectors

\[
\mu=(1,1,1,0),
\qquad
\sigma\mu=(1,0,0,0),
\]

where the second is the polarized conjugate signature. Averaging over the two-element Frobenius orbit gives

\[
\boxed{\bar\mu=\frac12(\mu+\sigma\mu)=(1,\tfrac12,\tfrac12,0).}
\]

On the underlying eight-dimensional rational representation, each entry occurs twice. Hence the mu-ordinary Newton polygon is

\[
\boxed{0^2,(\tfrac12)^4,1^2.}
\]

## 2. Exact match at p=7

The quartic surface polynomial

\[
h(T)=T^4+5T^3+245T+2401
\]

has p-adic root valuations

\[
0,1,1,2.
\]

Relative to \(q=49\), the absolutely simple surface \(B\) therefore has slopes

\[
0,\tfrac12,\tfrac12,1.
\]

Since

\[
f_7(X)=h(X^2),
\]

the fourfold \(P_{46,7}\) has slopes

\[
\boxed{0,0,\tfrac12,\tfrac12,\tfrac12,\tfrac12,1,1.}
\]

This agrees exactly with the inert signature-\((3,1)\) mu-average polygon. Thus

\[
\boxed{P_{46,7}\text{ lies in the mu-ordinary Newton stratum}.}
\]

## 3. Maximal inert p-rank

The p-rank is the multiplicity of slope zero, so

\[
\boxed{f(P_{46,7})=2.}
\]

For the inert unitary signature \((3,1)\), the mu-ordinary polygon is the maximal Newton polygon compatible with the Hodge cocharacter, and its p-rank two is the maximal p-rank available in that inert PEL fiber. Thus the reduction is nonordinary as an ordinary abelian fourfold, but generic at the Newton level inside the relevant unitary family.

The quadratic base-change decomposition

\[
P_{46,7,\mathbf F_{49}}\sim B^2
\]

and the mu-ordinary Newton classification are different statements: the first records the outer endomorphism character and semisimple isogeny decomposition; the second records the p-divisible isocrystal. Neither determines the integral Ekedahl--Oort type or the Prym polarization lattice by itself.

## 4. Boundary

No a-number for \(P_{46,7}\) is inferred merely from the isogeny \(B^2\), because a-number is not an isogeny invariant. Determining the integral p-torsion type requires a Dieudonne-module or Hasse--Witt calculation on the actual Prym.

Classification: `DERIVED_MU_ORDINARY_UNITARY_STRATUM / MAXIMAL_INERT_P_RANK / INTEGRAL_P_TORSION_OPEN / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.

## 5. Next frontier

Compute the Cartier--Manin/Hasse--Witt operators of \(C_{46,7}\) and \(E_7\), isolate the anti-invariant Prym block, and determine the exact Ekedahl--Oort type and a-number.
