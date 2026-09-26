# A finite cyclotomic exclusion obligation for fixed K33

Status: DIRECTED AUTHOR SYMBOLIC DERIVATION / SHARED CONTEXT / UNREVIEWED / NOT ADMITTED.

Researcher: `EM-DIRECT-C6438C`; activity: `RA-CAAAC604CB513AEA8BBC1DFC`.
Registration Source: `f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf`.
Pinned bank payload SHA256: `feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c`.

This note constructs a finite sufficient certificate for all-history primitive-component invertibility. It does not assert that its remaining determinants were evaluated. It uses no new ideal or numerical reference propagation. The separate `ROOT_CF_ALL_WIDTH_SUCCESS.md` now proves original CF-only positive success by a chosen-history argument, without requiring this stronger certificate.

## 1. Why the family of phase products is finite

At a streaming round `i`, the previous control bit at position `c` activates phase index `m=i-c+1`. Each index occurs at most once. Under K33, every `m>=33` is the identity on the entire retained carrier. The original execution orders the remaining maps from high `m` to low `m` in time; the usual right-to-left matrix convention therefore writes every possible product as

`T_epsilon = V_2^epsilon_2 V_3^epsilon_3 ... V_32^epsilon_32`,

`epsilon_m in {0,1}`.

There are at most `2^31` products. At small rounds some high-index bits are necessarily zero; including them all is a safe superset. At larger rounds each formal mask is a possible history label, without asserting that each such history has positive probability for a specific input. The order of factors is fixed; arbitrary permutations, repetitions, or independently chosen inverses are not added.

The mask family, the native phase bank, and the finite tests below are independent of `N`, the unknown order, and the control width `t`.

The common rational invariant space is

`A=span_Q(e0,e1,z_3,...,z_32)`, with `R=dim_Q A<=32`.

All products are identity on `A^perp`. This is a proof property of the full 61-mode execution, not a proposal to discard those coordinates.

## 2. Complete original list of low-degree odd parts and orders

A primitive work component can be killed only if a product has eigenvalue `-sigma mu^(-1)`, where the order of `mu` has the same odd part `d` as the unknown work order. A rational restriction of degree at most 32 cannot have a primitive root whose cyclotomic degree exceeds 32.

Every odd prime `p` dividing an odd `d` with `phi(d)<=32` must satisfy `p-1<=32`. Thus the only possible primes are `3,5,7,11,13,17,19,23,29,31`. The prime-power formula bounds the exponents, and multiplicativity bounds their combinations. It gives exactly the following 20 nontrivial odd parts:

`D_low={3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,39,45,51}`.

For a transparent exhaustiveness check: the only prime powers beyond first powers are `9,27,25`; combinations of distinct primes with totient at most 32 are `15,21,33,39,51,35`; multiplying `9` by `5` also gives `45`; no triple of distinct odd primes qualifies because `phi(3*5*7)=48` already exceeds 32. Higher prime-power combinations exceed the budget. Hence no omitted odd `d>51` qualifies.

For each listed `d`, the possible root orders are

`L=2^v d`, with `0<=v<=1+floor(log2(32/phi(d)))`.

This follows from `phi(2^v d)=phi(d)` for `v=0,1`, and `phi(2^v d)=2^(v-1) phi(d)` for `v>=2`. Grouping the complete list by the maximum exponent gives:

| Odd parts `d` | Allowed `v` | Number of orders |
| --- | --- | --- |
| `3` | `0,...,5` | 6 |
| `5` | `0,...,4` | 5 |
| `7,9,15` | `0,...,3` | 12 |
| `11,13,17,21` | `0,...,2` | 12 |
| `19,23,25,27,29,31,33,35,39,45,51` | `0,1` | 22 |

There are **57 distinct orders** in total. Multiplication by the sign in `-sigma mu^(-1)` exchanges the orders `d` and `2d` when the two-adic exponent is zero or one, and preserves the exponent when it is at least two. Thus both `d` and `2d` are needed; they must not be silently identified.

The odd part `d=1` is intentionally absent. Identity has eigenvalue one and the exact quarter-turn has eigenvalues `+i,-i`, so a claim excluding all roots of unity would already be false. Pure power-of-two orders are handled by the separate exact `1/2` factor-event proof.

## 3. An exact finite certificate and its logical strength

Let `L_low` be the 57-order set just constructed. The initial sufficient certificate is

`det(Phi_L(T_epsilon|A)) != 0`

for every mask `epsilon` and every `L in L_low`. Equivalently, the characteristic polynomial of the restriction is coprime to every indicated cyclotomic polynomial. Because products are identity on `A^perp` and `Phi_L(1)!=0`, it is equivalent to test the full-dimensional matrix `Phi_L(T_epsilon)`; no rational basis extraction or coordinate deletion is required.

This condition is **necessary and sufficient for the stated algebraic property**: none of these finitely many products has any nontrivial-odd-part root of unity as an eigenvalue. Higher-degree roots have already been excluded by the rational dimension bound.

If the certificate holds, every primitive-component branch matrix is invertible for every work order with odd part greater than one. Hence every terminal history has positive mass. Together with the pure-two-power result, this is sufficient to close CF-only positive factor support.

It is **not necessary for positive factor success**, and failure of an individual determinant test is not an algorithmic counterexample. A singular eigenspace might not contain the actual prefix vector; a formal history mask might be unreachable for the input; a killed primitive component need not kill every work component; and other CF-successful histories may remain. Even showing a zero-probability history would not establish that all successful readouts have zero probability.

## 4. Certified near-rank-two structure removes 55 of the 57 orders

For each retained nonexact phase, the existing full-space bound is `w_m+4 delta`, with `delta=2^-32`. Summing `m=3,...,32` gives `177 delta`. This exact constant is inherited from the stored K33 affine slope `185 delta` after subtracting `4u33=8 delta`, where the actual endpoint certificate has `u33=2 delta`. Even the coarser `30*(4+4)delta=240 delta` bound suffices for this section.

Replace only the retained phases by their ideal principal-plane rotations and leave the omitted tail as identity. The resulting product is `R_theta direct_sum I`, and

`||T_epsilon-(R_theta direct_sum I)|| <= eta=177 delta<1/2`.

The comparison minus identity has rank at most two. Hence `T_epsilon-I` has at most two singular values greater than `eta`. Since `T_epsilon` is normal, those singular values are precisely its eigenvalue distances from one.

If a cyclotomic factor `Phi_L` of degree `f>=4` occurred, rationality would supply all of its primitive roots as eigenvalues. At most two have distance from one greater than `eta`; each of these two distances is at most two. Therefore the nonzero integer

`|Phi_L(1)| = product_(zeta primitive L) |1-zeta|`

would satisfy `|Phi_L(1)|<=4 eta^(f-2)<1`, a contradiction.

Only root orders `1,2,3,4,6` remain possible. Therefore the nontrivial-odd-part finite obligation reduces to **`Phi_3` and `Phi_6` only**. This bound uses the truncated ideal comparison; no arbitrary all-width ideal QFT accuracy is claimed.

## 5. Exactly 176 mask/order pairs remain after a symbolic angle window

Put `M=2^32` and encode a mask uniquely by

`j=sum_(m=2)^32 epsilon_m 2^(32-m)`, with `0<=j<2^31`.

Its truncated comparison has angle magnitude `theta=2 pi j/M`, lying in `[0,pi)`. This is an exact symbolic encoding of the chosen factors, not a computed ideal trajectory.

If `T_epsilon` has a primitive cube root, take its eigenvalue `exp(2 pi i/3)` and put `alpha=2 pi/3`. If it has a primitive sixth root, take `exp(pi i/3)` and put `alpha=pi/3`. Spectral inclusion for a norm perturbation of a normal matrix gives distance at most `eta` from this eigenvalue to the comparison spectrum `{1,exp(i theta),exp(-i theta)}`. One direct proof is that a point farther than `eta` from that spectrum has an inverse resolvent of norm less than `1/eta`, so the perturbed matrix cannot be singular there.

For either value of `alpha`, the distances from `exp(i alpha)` to `1` and to `exp(-i theta)` are at least one for `0<=theta<=pi`. Since `eta<1`, the close comparison eigenvalue must be `exp(i theta)`. Thus

`2 |sin((theta-alpha)/2)| <= eta`.

Here `|theta-alpha|<=pi`. Concavity of sine on `[0,pi/2]` gives the standard chord bound `sin x>=2x/pi`, yielding

`2 |sin((theta-alpha)/2)| >= 2 |theta-alpha|/pi`.

Substitution cancels pi completely:

- for `Phi_3`, `|j-M/3|<=eta M/4=177/4`;
- for `Phi_6`, `|j-M/6|<=eta M/4=177/4`.

The resulting exact integer windows are:

| Factor | Integer mask codes `j`, inclusive | Count |
| --- | --- | --- |
| `Phi_3(x)=x^2+x+1` | `1431655722,...,1431655809` | 88 |
| `Phi_6(x)=x^2-x+1` | `715827839,...,715827926` | 88 |

For example, `M/3=1431655765+1/3` and `M/6=715827882+2/3`; subtracting or adding `177/4` and taking the exact ceiling/floor gives those endpoints. They are disjoint windows, so the stronger exclusion certificate needs only **176 mask/order tests**, not each factor for every mask. The `Phi_3` window always has `epsilon_2=1`; the `Phi_6` window has `epsilon_2=0`.

This 176 count uses the exact stored `177 delta` prefix budget. If one elects to use only the simpler `240 delta` proof bound, each radius is 60 and each window has 120 integers, for 240 tests; that conservative alternative is also finite and independent of `N,t`.

## 6. A compact exact modular witness is sufficient

Every actual full-dimensional `T_j` is dyadic. For an odd prime `p`, all its powers-of-two denominators are invertible modulo `p`. Thus a nonzero finite-field determinant of

`T_j^2+T_j+I` for the 88 `Phi_3` masks,

or `T_j^2-T_j+I` for the 88 `Phi_6` masks,

proves the corresponding rational determinant is nonzero. Different masks may use different odd primes. A determinant that is zero modulo one prime is inconclusive over the rationals; another prime or a direct exact rational calculation is needed.

For full-dimensional `Phi_3` tests, avoid `p=3`: the identity complement contributes the factor `Phi_3(1)=3`, so it makes the determinant vanish modulo three regardless of the active restriction. Choosing an odd prime different from three avoids this automatic obstruction. This is a proof-design constraint, not a newly executed modular test.

A replayable certificate should bind the pinned bank payload, the 61-dimensional actual matrices or their certified columns, the exact factor order, mask code, chosen prime, and a nonzero determinant residue. Alternatively, an explicit modular inverse of the tested matrix is a direct witness whose multiplication can be checked. The root's typed arithmetic provenance rules still apply to any actual execution. This note supplies the mathematical obligation, not a substitute source for primitive column certification.

## 7. What dyadic/native structure alone does not prove

Dyadic entries and orthogonality alone do not exclude odd-part roots: an integer three-cycle permutation has primitive cube roots. Even the single native rotor formula and positive retained completion do not by themselves exclude `Phi_3`.

For an exact symbolic counterexample to that generic structural claim, take the dyadic unit vector `w=(1,1,1,1)/2` and `D0=diag(1,-1,-1,-1)`. The same form

`V=D0(2ww^T-I)`

is dyadic, orthogonal, identity on the complement of `span(e0,w)`, and has planar rotation cosine `2w_0^2-1=-1/2`. Its nontrivial eigenvalues are the primitive cube roots. This is not one of the actual pinned small-angle words and is not a counterexample to the compiled algorithm; it shows why those broad structural labels cannot replace a bank-specific argument. No reference simulator was executed to obtain it.

The actual finite products may or may not all avoid `Phi_3,Phi_6`. Neither a genericity assertion, a near-angle estimate alone inside the remaining windows, nor a single zero residue modulo a prime settles that question.

## 8. Why the factor-support proof no longer depends on this stronger certificate

Root's separately audited argument chooses `k=nearest(Q/r)` when the order's odd part is three. Along that history the full feedback angle satisfies an exact phase-alignment identity. For work eigenvalue order three or six, the ideal branch has smallest singular value greater than `1/2`; the actual full-feedback error is at most `185 delta`, including the omitted identity tail. Thus the branch remains invertible. Early rounds are handled exactly, and orders at least twelve are already covered by the cyclotomic norm exclusion.

This establishes a supported CF-successful history for odd part three without excluding every cyclotomic eigenvalue of every mask. Together with Section 4 for odd parts greater than three and the pure-power-of-two theorem, it closes positive factor support for the original CF-only algorithm under the stated input/randomness/peripheral contracts. See `ROOT_CF_ALL_WIDTH_SUCCESS.md` for the proof, dyadic success lower bound, and finite-retry statement.

The 176-test certificate remains a finite, well-defined stronger route toward all-history support. It is optional for the completed chosen-history success proof and must not be described as already evaluated here.

Global-Knowledge-Sync: main@441ebef / GLOBAL_KNOWLEDGE_V1
