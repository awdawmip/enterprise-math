# POWER feedback research: witness-preserving Smith certificate

Research-Activity-ID: `RA-POWER-REVIEW-16243626C61A`  
Researcher-ID: `EM-DIRECT-16243626C61A`  
Status: `EXECUTABLE_CERTIFICATE_EXTENSION_CANDIDATE / NOT_DRIVER_ACCEPTED / NOT_FOUNDATION`  
POWER source stimulus: `awdawmip/power@6d784d3990afae602a03745173c3f2a16a076b0c:src/power/algebra/smith_normal_form.py`.

## Selected positive reuse question

POWER's Smith implementation returns not only invariant factors but integer transition witnesses

\[
U A V = S.
\]

Can that witness-preserving interface strengthen existing Enterprise exact cokernel/chain surfaces without importing POWER's weak verifier or creating a duplicate top-level family?

## Existing Enterprise interfaces and reuse resolution

### T10 Local Redistribution / Toppling / Potential — `EXTEND_EXISTING_TOOL`

Current Enterprise source `src/enterprise_math/discrete_laplacian_chip_firing.py` already provides exact integer matrices, Bareiss determinant, firing-lattice membership, reduced Laplacians and cokernel order. What it does not expose is a generic Smith certificate that decomposes the cokernel and preserves the left/right integer coordinate transformations.

The new candidate therefore reuses T10's exact determinant/cokernel substrate and adds a verifier-only Smith witness surface. It does **not** add a competing determinant or graph-Laplacian implementation.

### T11 Discrete Morse / Chain Reduction — `REUSE_APPLIED / SEMANTIC_BOUNDARY_PRESERVED`

T11 already treats a reduction as a certificate with explicit projection/lift/homotopy maps and verifies those maps by exact replay. The useful design lesson transfers: a canonical form should not be accepted merely because its summary invariants look plausible; the transition witnesses themselves must be checked.

Smith equivalence is not chain-homotopy equivalence, so this candidate does not claim to replace or subsume T11.

## New candidate interface

`src/enterprise_math/smith_certificate.py` verifies a proposed integer certificate rather than computing one. For an `m x n` integer matrix it checks:

1. matrix dimensions;
2. `det(U), det(V) in {+1,-1}`;
3. exact integer identity `U*A*V == S`;
4. S is diagonal;
5. positive nonzero Smith diagonal precedes all zeros;
6. divisibility chain `d_i | d_(i+1)`;
7. rank and free-rank consistency.

It then returns exact cokernel summary data while preserving U,V outside the summary for provenance/coordinate transport.

This closes the specific POWER verifier defect where a forged `U=((0,),)` could certify `A=((7,),)` against `S=((0,),)`.

## Validation

Local candidate source SHA256:
`5b2fdd7f6466b7b8f59336bf87b8dc27116ff9eb8440aac06314b6583420cfc1`.

Local self-contained publication tests: **5/5 PASS**, including a nontrivial 3x3 certificate emitted by POWER's frozen generator and explicit rejection of the forged zero-transform pattern.

Separately, before publication, the unchanged POWER Smith generator from the frozen audited blob was exercised on **160 random matrices** (all shapes 1..4 by 1..4, ten matrices per shape, entries -15..15). Every generated certificate passed the stronger candidate verifier and the verified rank matched POWER's returned rank. This is bounded compatibility evidence, not an unrestricted proof that the POWER generator is correct.

The earlier POWER audit had independently checked another 200 matrices against transform, unimodularity, diagonal/divisibility and reference invariant factors. Those earlier checks remain provenance; they are not re-counted as this candidate's tests.

## BRC / information-preservation interpretation

Invariant factors alone preserve the isomorphism class of the presented abelian group but erase how source and target integer coordinates map into the canonical presentation. When later operations care about named generators, ports, coordinates or provenance, this erased information can matter.

The U,V witnesses are therefore retained as a richer carrier. Compression to invariant factors is safe only for observers proven to factor through the isomorphism-class summary. This is the same information-discipline principle used in the lift-safe sieve, now applied to integer linear relations.

## Scope and nonclaims

- no claim that Smith normal form is new mathematics;
- no new top-level Enterprise tool family is claimed;
- no claim that POWER's generator is universally correct or high performance;
- no use of floating determinant/rank;
- no claim that Smith equivalence preserves arbitrary future operations;
- no Foundation, Working Truth, Driver acceptance or theorem promotion.

## Next positive POWER reuse target

The group-ring collision mass interface is the next high-value research target. Its exact second moment can be treated through T4 finite-fiber collision calculus plus T6 observer-safe quotienting. The substantive question is whether the identity-coefficient observer under the remaining group-ring multipliers admits a strictly smaller future-safe state than explicit subgroup support, with bit/state cost accounted for. No speedup is assumed.
