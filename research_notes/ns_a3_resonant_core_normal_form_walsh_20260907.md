# A3/FCC root-ray quadratic normal form: only the 90-degree opposite-edge resonance survives

Status: `RESEARCH_NOTE / DURABLE_FRONTIER / EXACT_RESONANCE_CLASSIFICATION + GENERALIZED_WALSH_FACTORIZATION / NORMAL_FORM_TARGET / NOT_PROMOTED / NOT_MILLENNIUM_PROOF`
Researcher-ID: `EM-FREE-7N3K2A`
At: `2026-09-07T17:22:00+08:00`
Parents:
- global `knowledge/projects/enterprise-math/pde-opposite-edge-90deg-multipath-resonance-frontier-20260906.md`
- global `knowledge/projects/enterprise-math/pde-90deg-fourpath-walsh-exact-upgrade-20260906.md`
- `research_notes/ns_a3_root_pair_low_derivative_transfer_20260907.md`
Authority immediately before write: `enterprise-math main@0b4f92a828ad4a1053e241c485fc1b3459fe4aaf`.

## 1. Root-ray parabolic resonance classification at all radii

For a quadratic heat/Stokes Duhamel branch with `k=p+q`, the homological denominator is

`Omega(p,q)=nu(|k|^2-|p|^2-|q|^2)=2nu p·q`.

Let `p=m alpha`, `q=n beta` be exact A3 root-ray inputs. Distinct nonparallel normalized A3 root directions have cosine `-1/2,0,+1/2`, equivalently primitive root dot products `-1,0,+1`.

Therefore:

- STAR/120-degree line pair: `Omega=-2nu mn !=0`;
- opposite-edge/90-degree line pair: `Omega=0`;
- acute/60-degree line pair: `Omega=+2nu mn !=0`.

Same-line pairs have zero A3 output defect, and opposite vectors require separate zero/collinear treatment.

Thus, at **every radial scale**, not only the primitive shell,

`boxed: A3 ROOT-ROOT QUADRATIC PARABOLIC RESONANCE`
`       = K4 OPPOSITE-EDGE / 90-DEGREE PAIRS.`

There is no small-divisor sequence on the nonresonant A3 pair classes: the nonzero denominator has exact magnitude `2nu mn` in primitive radial coordinates.

## 2. Nonresonant normal-form order

The raw Navier–Stokes quadratic coefficient carries one derivative, schematically of size `O(max(|p|,|q|))` times the two amplitudes.

On the 60/120-degree root-pair classes,

`|Omega| ~ nu |p||q|`.

Dividing by the homological denominator therefore produces a bilinear correction of schematic order

`O(1/(nu min(|p|,|q|)))`.

So the nonorthogonal root-pair leakage is one derivative smoother at the quadratic normal-form level. Differentiating this correction in time replaces the eliminated nonresonant quadratic term by cubic/higher terms involving the decimated/root dynamics.

This does not by itself prove a global normal-form theorem, but it identifies the exact quadratic resonant kernel that cannot be removed in this way.

## 3. General unequal-radius 90-degree Leray output

Let `e,f,z` be an orthonormal right-handed frame with `z=e x f`. Take

`p=P e`, `q=Q f`, `P,Q>0`,
`k=P e+Q f`, `L=sqrt(P^2+Q^2)`.

Divergence-free polarizations have the form

`u_p=A f+B z`,
`u_q=C e+D z`.

The symmetrized raw convective pair is

`R=Q A u_q + P C u_p`
` = AC(Q e+P f) + (QAD+PCB) z`.

Let

`ell=(Q e-P f)/L`,

which is the unit in-plane vector orthogonal to `k`. Leray projection gives exactly

`boxed:`

`P_k R`
`= AC (Q^2-P^2)/L * ell`
` + (QAD+PCB) z.`

At `P=Q`, the in-plane term vanishes because `Qe+Pf` is longitudinal; this recovers the equal-shell result from the parent Walsh note.

For unequal radii the resonant 90-degree output has two transverse pieces:

1. an in-plane shell-mismatch component;
2. an out-of-plane polarization/helicity component.

## 4. Generalized four-path Walsh formula

For the four STAR-mediated paths between the opposite K4 edges, let the path products have Walsh transform `(W0,W1,W2,W3)` in the convention of the parent note, where

`W0=2BD`,
`W1=AC`,
`W2=sqrt(2)BC`,
`W3=sqrt(2)AD`.

Then the unequal-radius resonant output is exactly

`boxed:`

`P_k R`
`= [(Q^2-P^2)/L] W1 * ell`
` + [P W2+Q W3]/sqrt(2) * z.`

The trivial/common path character `W0` is absent for all `P,Q`, not only at equal shell.

At equal shell `P=Q=K`, the `W1` coefficient is zero and

`P_kR=(K/sqrt(2))(W2+W3)z`,

recovering the earlier exact formula.

Thus the entire unequal-radius 90-degree resonant sector is carried by the three nontrivial Walsh characters; radial equality removes one of those three and leaves the two-dimensional transverse path-imbalance pair.

## 5. Helical factorization of the resonant kernel

Use helical polarizations

`h_s(e)=(f+i s z)/sqrt(2)`,
`h_t(f)=(e-i t z)/sqrt(2)`,

with `s,t in {+1,-1}`.

Then

`AC=1/2`,
`QAD+PCB=i(Ps-Qt)/2`.

Therefore

`boxed:`

`P_kR`
`= (Q^2-P^2)/(2L) * ell`
` + i(Ps-Qt)/2 * z.`

This separates the exact null coordinates.

### Same-helicity inputs `s=t`

Both transverse components contain a radial mismatch factor:

- in-plane: `Q^2-P^2=(Q-P)(Q+P)`;
- out-of-plane: `s(P-Q)`.

Hence an equal-radius homochiral opposite-edge pair is completely null, while near-equal radii give a commutator-type shell-difference defect.

### Opposite-helicity inputs `s=-t`

The out-of-plane coefficient becomes

`i s(P+Q)/2`,

which is order one in the high frequency even at `P=Q`. This is the genuinely strong quadratic resonant branch. The in-plane component remains purely shell-mismatch driven.

Therefore the root-ray quadratic resonance has the sharpened decomposition

`RESONANT 90-DEGREE OUTPUT`
`= SHELL-MISMATCH PART`
`+ CROSS-HELICITY PART`,

and the only component that survives simultaneously at exact shell equality and exact heat resonance is cross-helical.

## 6. Smallest quadratic hard kernel

Combining the normal-form and Walsh/helicity classifications:

- 60-degree acute root pairs: nonresonant -> quadratically normal-form removable / one derivative smoother;
- 120-degree STAR pairs: nonresonant unless interpreted as retained equal-shell decimated closure; off-root mismatched pairs have nonzero denominator and the cubic output defect already carries shell mismatch;
- 90-degree opposite-edge pairs: parabolically resonant;
- within that resonant class, same-helicity equal-shell pairs vanish;
- the strong surviving resonant core is opposite-edge + opposite-helicity, with shell mismatch contributing an additional secondary channel.

This is the smallest quadratic root-ray kernel that a nonperturbative proof must control before generated off-root modes are included.

## 7. Relation to the physical-space extensional obstruction

The parent work identified the same three K4 opposite-edge classes with the two-dimensional extensional/checkerboard strain sector carrying the middle-eigenvalue obstruction after rotation to the strain eigenframe.

The present formula adds a radial/helical resolution:

- `W1` is activated by radial shell mismatch;
- `W2,W3` carry the out-of-plane resonant polarization;
- at equal shell, only the `W2+W3` combination survives, and helicity decides cancellation versus reinforcement.

An explicit intertwiner from this frequency-resonant Walsh sector to the physical-space signed K4 strain-tree source is still open. That remains an Enterprise-specific high-value target.

## 8. BRC resolution

For the resonant kernel the safe branch state is

`(opposite-edge endpoints, four STAR path labels, radial pair P,Q, Walsh characters W1,W2,W3, helicity signs, complex amplitudes, output frequency)`.

`W0` may be discarded for this local effective output because its exact absence is proved.

Do not aggregate `W2,W3` before helicity projection when `P!=Q`: they carry different radial weights `P,Q`.

Positive Weighted-BRC remains inapplicable to the signed/complex cancellation.

## 9. Next executable target

Apply a quadratic Poincare-Dulac/normal-form transform to the complete root-ray skeleton forcing, eliminating the dot `±1` nonresonant pair classes with the exact denominator `2nu p·q`, and leave only the opposite-edge resonant bilinear operator.

Then test whether the remaining resonant operator admits a critical estimate in terms of

`minority helicity x opposite-edge Walsh imbalance`

that is stronger than the existing global minority-helicity criterion. If not, record that the 90-degree cross-helicity resonance is the irreducible quadratic obstruction and move to cubic resonance generated by the normal form.
