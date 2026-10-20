# R005-A — p=2 Repair–Gap Multiplicity Checkpoint

Status: `PROVED R005 STRUCTURE + INDEPENDENT FINITE AUDIT / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-30`  
Researcher-ID: `R005A-7C2`  
Task: `RS-R005-PRIME-ALGORITHM-LAB`  
Owner generation: existing `research/r005a-prime-algorithm-lab-20260810`

## 1. Scope

This checkpoint continues the existing square-basin branch without changing task, theorem ownership, Prime Toolkit status, or canonical/Foundation status.

Set

\[
A=k^2,\qquad U=k^2+2k,
\]

and assume the established R005 p=2 theorem slice on which the fourth-root core

\[
C_4=\lfloor U^{1/4}\rfloor
\]

is forced. Let `NF_k` be the non-forced candidate-prime field and let `R_k` be the residual support hypergraph from the existing closure-shadow factorization.

The purpose here is to connect **repair number** directly to **multiplicity of prime-gap obstructions** before full pair closure is constructed.

No new generic hypergraph or prime-gap machinery is introduced. The existing Prime Toolkit / R005 next-prime and witness-forcedness surfaces are the intended reusable mechanism.

---

## 2. P2-GM1 — small-NF transversal theorem

Define the repair-relevant small non-forced set

\[
S_k
=
NF_k\cap
\left(
C_4,\,\lfloor A^{1/3}\rfloor
\right].
\]

Then

\[
\boxed{S_k\text{ is a transversal of }\mathcal R_k.}
\]

Consequently

\[
\boxed{
\tau(\mathcal R_k)\le |S_k|.
}
\]

### Proof

Take any residual block. By the already-proved p=2 three-factor normal form, its residual integer can be written

\[
N=abc,\qquad a\le b\le c,
\]

with `Omega(N)=3`, every distinct factor non-forced, and

\[
C_4<a\le \lfloor A^{1/3}\rfloor.
\]

Therefore every residual block contains at least one vertex in `S_k`. Hence `S_k` hits every residual block.

### Immediate consequences

If `R_k` is nonempty and

\[
|S_k|=1,
\]

then

\[
\boxed{\tau(\mathcal R_k)=1.}
\]

More generally,

\[
\boxed{
\tau(\mathcal R_k)\ge t
\Longrightarrow
|S_k|\ge t.
}
\]

Thus the search for the first basin with repair number at least two has an exact prefilter:

\[
\boxed{
\tau\ge2
\Longrightarrow
\text{at least two small non-forced coordinates.}
}
\]

This precedes pair closure, repeated-forest construction, and squarefree-triangle branching.

---

## 3. P2-GM2 — exact quarter-power gap at every small repair coordinate

Fix

\[
q\in S_k,
\qquad
x=\frac{A}{q}.
\]

Because `q>C_4`, the established local forcedness classifier applies. Because also

\[
q\le A^{1/3},
\]

we have

\[
q^3\le A,
\]

so pure-cube forcing is absent from the basin. Non-forcedness therefore implies that the eligible cofactor interval

\[
\left(\frac Aq,\frac Uq\right]
\]

contains no prime.

Let `alpha<beta` be the consecutive cofactor primes surrounding `x`, and let

\[
g=\beta-\alpha.
\]

Then

\[
g>\frac{U-A}{q}=\frac{2k}{q}.
\]

Since `q^3<=A=k^2`,

\[
q^{3/4}\le k^{1/2},
\]

and hence

\[
\frac{2k/q}{x^{1/4}}
=
2k^{1/2}q^{-3/4}
\ge2.
\]

Therefore every small repair-relevant non-forced coordinate satisfies the exact bound

\[
\boxed{
g>2x^{1/4}.}
\]

Equivalently, without floating-point quantities,

\[
\boxed{
qg^4>16A.
}
\]

### Relation to the earlier T-A46 obstruction

T-A46 used the looser cube-root condition `q^3<=U`, producing a finite-k constant

\[
2\left(\frac{k}{k+2}\right)^{1/4}
\to2.
\]

For the coordinates that actually hit every p=2 residual block, the stronger fact `q^3<=A` is available. The asymptotic loss disappears:

\[
\boxed{
\text{repair-relevant small NF coordinate}
\Longrightarrow
\text{gap ratio strictly greater than }2.
}
\]

---

## 4. P2-GM3 — shared-gap occupancy amplification

Several small non-forced coordinates could, a priori, be pulled back from the same consecutive cofactor prime gap.

Suppose one cofactor gap `(alpha,beta)` contains the reciprocal points

\[
x_i=\frac{A}{q_i},
\qquad
q_1<q_2<\cdots<q_m,
\qquad
q_i\in S_k.
\]

Because all `q_i>C_4>=2` on the theorem slice, the `q_i` are odd primes and

\[
q_m-q_1\ge2(m-1).
\]

All `x_i` lie in the same prime gap, so

\[
g> x_1-x_m
=
A\frac{q_m-q_1}{q_1q_m}.
\]

Also

\[
q_1q_m\le A^{2/3}.
\]

Therefore

\[
\boxed{
 g>2(m-1)A^{1/3}
 =2(m-1)k^{2/3}.
}
\]

An exact integer form is

\[
\boxed{
 g^3>8(m-1)^3A.
}
\]

So repeated occupancy of one reciprocal prime-gap strip is much more expensive than a single quarter-power obstruction.

For `m=2`:

\[
\boxed{
\text{two small NF coordinates from one cofactor gap}
\Longrightarrow
g>2k^{2/3}.
}
\]

At the minimal cofactor scale `x~k^{4/3}`, this is a square-root-scale gap condition.

---

## 5. Repair–gap multiplicity theorem

Combine P2-GM1, P2-GM2 and P2-GM3.

If

\[
\tau(\mathcal R_k)\ge t,
\]

then there exist at least `t` distinct small non-forced coordinates

\[
q\in\left(C_4,A^{1/3}\right].
\]

Each coordinate forces a cofactor prime gap satisfying

\[
g>2x^{1/4}.
\]

Group the selected coordinates by their containing cofactor prime gaps. If one gap receives multiplicity `m>=2`, that gap is amplified to

\[
g>2(m-1)k^{2/3}.
\]

In particular:

\[
\boxed{
\tau(\mathcal R_k)\ge2
}
\]

forces the following dichotomy:

1. **two distinct cofactor gaps**, each carrying an exact quarter-power obstruction `g>2x^(1/4)`; or
2. **one shared cofactor gap** containing two small reciprocal coordinates, with the much stronger bound
   \[
   g>2k^{2/3}.
   \]

This turns the earlier local hypergraph obstruction target into a prime-gap multiplicity target.

---

## 6. Search compression

The previous exact route for p=2 was

`NF field -> pair closure -> residual hypergraph -> transversal number`.

For searching the first basin with `tau>=2`, the new safe route is

`reciprocal prime gaps -> S_k -> cardinality gate -> pair closure only if |S_k|>=2`.

Thus:

- `|S_k|=0` implies no residual block on the fourth-root-forced slice;
- `|S_k|=1` and nonempty residual implies `tau=1` immediately;
- only `|S_k|>=2` can possibly produce `tau>=2`.

The new gate does not replace pair closure. It removes basins that cannot possibly have higher repair complexity before the more expensive closure step.

---

## 7. Independent finite audit on the current exact family

An independent exact audit was run against the existing 49-basin / 50-residual certificate family from

`experiments/r005a_p2_exact_residual_family.py`.

Results:

- verified no-least basins: `49`;
- verified residual composites: `50`;
- total small non-forced coordinates across those basins: `56`;
- small-NF count histogram:
  - `|S_k|=1`: `42` basins;
  - `|S_k|=2`: `7` basins;
- the seven two-small-NF basins are
  \[
  308,\ 888,\ 1162,\ 1290,\ 1345,\ 1679,\ 1781;
  \]
- every certified residual support intersects `S_k`;
- every basin satisfies `tau(R_k)<=|S_k|`;
- all 49 current no-least basins still have `tau=1`;
- therefore **42 of the 49 `tau=1` results follow before full residual-hypergraph construction**, solely from `|S_k|=1` plus residual nonemptiness;
- all `56` small coordinates satisfy the exact integer quarter-power certificate
  \[
  qg^4>16A;
  \]
- minimum observed normalized ratio remains approximately
  \[
  2.2515411161,
  \]
  at
  \[
  k=5833,\ q=281,
  \]
  with cofactor primes
  \[
  121081<121123
  \]
  and gap `42`;
- no two of the 56 current small coordinates occupy the same cofactor prime gap, so the shared-gap amplification branch is not exercised by the current certificate family.

This finite audit is not an exhaustiveness claim in `k` and is not evidence that shared-gap occupancy is impossible.

---

## 8. Prior-art boundary

Standard ingredients remain prior mathematics:

- hypergraph transversals / hitting sets;
- consecutive-prime gaps;
- reciprocal inequalities;
- almost-primes between consecutive squares.

Peter J. Campbell's 2026 result proves that every interval between consecutive squares contains an integer with at most three prime factors and uses explicit finite prime-gap input in its computational range. That is adjacent prior art for the ambient three-factor shell, not the R005 forced/non-forced repair semantics.

Banks–Ford–Tao's probabilistic large-gap model is relevant only to the plausibility of polynomial-scale gap obstructions; it does not supply the repair/transversal multiplicity theorem above.

No historical novelty claim is made for P2-GM1–P2-GM3. The candidate Enterprise-specific content is the exact composition

`forced/non-forced witness semantics -> small-NF transversal -> reciprocal gap obstruction -> repair-number multiplicity`.

Novelty remains `UNVERIFIED`.

---

## 9. Tool-reuse disposition

Current toolbox lookup identifies the accepted domain facade

`D1_PRIME_TOOLKIT`.

This checkpoint does not create a new tool family. It reuses the existing R005 exact witness-forcedness / next-prime / pair-closure semantics. The new contribution is a theorem-level compression and a search gate.

Disposition:

`REUSE_APPLIED / NO_NEW_TOOL_FAMILY`.

---

## 10. Next frontier

The next exact target is no longer "find another residual".

Search directly for

\[
|S_k|\ge2,
\]

using reciprocal prime-gap strips, then classify those candidate basins by:

1. distinct-gap versus shared-gap occupancy;
2. pair closure / repeated-forest / squarefree-triangle formation;
3. the first actual `tau>=2` obstruction, if one exists.

A shared-gap candidate is especially rigid because it must already satisfy

\[
g>2k^{2/3}.
\]

Status remains:

`PROVED R005 STRUCTURAL CHECKPOINT / FINITE AUDIT PASSED / PRIOR-ART NOVELTY UNVERIFIED / NOT CANONICAL / LEAN PENDING`.
