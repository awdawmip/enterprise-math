# PREFIX-575-GC — Rank-One Gate Channel, Exact Linear Degree 14, and Strict Perron Response

Status: AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / BRANCH-PERSISTED / PREFIX-575-COMPANION  
Research mode: unshared direct derivation; no task claim or shared task-state mutation  
Project branch base: `awdawmip/enterprise-math@b19856a1843fd120b4fccc77ed6f94b424f69225`  
Concurrent canonical main after branch creation: `61b08d67197f4422fa0d8ac1c197f608e09b69af`  
Science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`  
Prior frontier: PREFIX-574, exact result blob `359ea1417845140966a48fbe943b4ce8a8a8f363`; irreducibility checker blob `6cdf85ae5154b3f5f52bf6cab58b3a175e93dbb4`.

## 1. Question and exact scope

### Distinction from the concurrent canonical PREFIX-575 result

Canonical main now also contains `2026-11-08_prefix575_gate_frequency_and_variance_poisson.md` at `61b08d67197f4422fa0d8ac1c197f608e09b69af`. That result fixes `q1=q2=q3=q4=q5=q6=1` and studies the gate-count Poisson/martingale moments. This branch is a distinct parametric observer: `q1=q2=q3=q4=1`, `x=q5`, `y=q6`, `z=gate`, `r5=r6=0`. Both consume the same frozen science pin and the same gate-preserving 96-port/37-class source, but neither supersedes the other. This note is therefore labelled PREFIX-575-GC (gate-channel companion). The branch remains based on its recorded base commit; it was not rebased or merged after canonical main advanced, preserving owner isolation.


The PREFIX-574 frontier leaves this question: the gate-retaining 37-class quotient has an irreducible degree-14 factor Q14, but the scalar companion orthant is not invariant. Can the gate response be isolated as a smaller exact linear system, and what does that say about the positive-realization problem?

This note answers the gate-channel part. It does not yet determine the minimum positive-realization dimension.

The frozen observer is exactly the existing four-STAR native X6-BRC construction:

- 96 ordered ports, 6 labeled actions, 9 roots;
- weighted quotient growth 1, 4, 13, 21, 33, 37, giving 37 classes;
- bipartition 17/20;
- observer q1=q2=q3=q4=1, x=q5, y=q6, z=gate;
- root scope r5=r6=0.

This is a restricted observer/readout inside the native X6 carrier, not a new lower-dimensional world and not a full-X6 dynamical theorem. z is a formal gate marker, not physical time or a heartbeat interval.

BRC reuse: REUSE_APPLIED to the existing typed weighted transition rows and their verified 96-to-37 future-observer quotient; EXTEND_EXISTING_TOOL for the gate-channel certificate below. No new BRC family is claimed. No π, classical trigonometry, ordinary propagator, Taylor/Padé/Cayley or precision-escalation fallback is used.

The Q14 generic irreducibility result is reused from PREFIX-574's Rabin certificate over Q(u,v,z). This run independently reconstructed Q14 and matched its exact SHA-256, but did not rerun the prior Rabin proof.

## 2. Rank-one gate decomposition

In the 37-class quotient, the only gate-marked edges are

\[
4\to5,\qquad 15\to5,\qquad 17\to5,
\]

each with multiplicity one. The three sources lie in the 20-state right block and share the same target in the 17-state left block.

Let A be the 17×20 left-to-right weighted matrix and B(z) the 20×17 right-to-left matrix. Let u be the indicator of right-block positions 2, 8, 10, and let c=e_2^T select the left-block position corresponding to quotient class 5. Then the exact matrix identity is

\[
B(z)=B_0+zuc.
\]

Consequently the two-step operator is

\[
P(z)=AB(z)=P_0+zbc,\qquad
P_0=AB_0,\quad b=Au.
\]

Thus the gate perturbation has rank exactly one. In the 17-state realization, b has 7 nonzero entries and c has one. The identity was checked entrywise over exact symbolic polynomials.

## 3. The gate transfer function has exact McMillan degree 14

The existing characteristic factorization is

\[
\chi(\lambda,z)=\det(\lambda I-P(z))
=Q_3(\lambda;u,v)\,Q_{14}(\lambda;u,v,z),
\]

where

\[
Q_3(\lambda;u,v)
=\lambda^3+4\lambda^2-(32u+16v)\lambda+192v
\]

is independent of z, while Q14 is monic of degree 14 in λ, affine in z, and irreducible over \(\mathbb Q(u,v,z)\).

Write

\[
Q_{14}(\lambda;u,v,z)
=Q_0(\lambda;u,v)+zQ_z(\lambda;u,v),
\qquad Q_z=\partial_z Q_{14}.
\]

The matrix determinant lemma gives

\[
\chi(\lambda,z)
=\det(\lambda I-P_0)
-z\,c\,\operatorname{adj}(\lambda I-P_0)b.
\]

Comparing the constant and z coefficients with Q3 Q14 yields

\[
\det(\lambda I-P_0)=Q_3Q_0,
\qquad
c\,\operatorname{adj}(\lambda I-P_0)b=-Q_3Q_z.
\]

Therefore the scalar gate transfer function is exactly

\[
\boxed{
H(\lambda)
=c(\lambda I-P_0)^{-1}b
=-\frac{Q_z(\lambda;u,v)}{Q_0(\lambda;u,v)}
}.
\]

### Coprimality

If a nonconstant D in \(\mathbb Q(u,v)[\lambda]\) divided both Q0 and Qz, it would divide Q0+zQz=Q14 in \(\mathbb Q(u,v,z)[\lambda]\). That contradicts the irreducibility of Q14, because degλ(Qz)=12<14. Hence

\[
\gcd(Q_0,Q_z)=1.
\]

The reduced denominator Q0 is monic of degree 14. The scalar transfer function therefore has McMillan degree exactly 14 over the generic parameter field.

The exact reconstruction gives:

- degλ Q0 = 14, with 83 nonzero terms;
- degλ Qz = 12, with 76 nonzero terms;
- leading coefficient of Qz: \(-4(2u+1)\);
- SHA-256(Q0) = `1d94ddd76f887618816fad17571a6735de3514b53028f41da817c6fefb528fc6`;
- SHA-256(Qz) = `9bddcd8896a6148a108d7d29a0a98edaaa28520b9e169a7b58c57d4fed7893e4`.

The relative degree in the 17-state two-step operator is exactly two. Direct Markov-parameter checks give

\[
cb=0,\qquad cP_0b=4(2u+1),
\]

so

\[
H(\lambda)=\frac{4(2u+1)}{\lambda^2}
+O(\lambda^{-3}).
\]

### Every Q14 root is gate-sensitive

Q14 is irreducible of degree 14 and Qz is nonzero of degree 12. Therefore Qz cannot vanish at any root of Q14: otherwise the minimal polynomial Q14 would divide Qz. Characteristic zero also makes Q14 separable. For every algebraic root branch λ_i(z),

\[
\frac{d\lambda_i}{dz}
=-\frac{Q_z(\lambda_i)}{\partial_\lambda Q_{14}(\lambda_i)}
\ne0.
\]

Thus all 14 generic roots of Q14 respond to the gate parameter. The degree-3 factor Q3 cancels from this scalar gate channel; its cancellation is channel-specific, not a claim that those modes are invisible to every other observer.

## 4. Strict Perron response and location of the dominant mode

The 17-state support graph of P0 and P(z) is identical: 17 vertices and 117 directed edges. Exact forward and reverse BFS from vertex 0 reach all 17 vertices, with maximum distance 2. All matrix entries are polynomials with nonnegative coefficients in x,y,z, and the support is strongly connected. Hence P(z) is irreducible and nonnegative for x,y>0 and z≥0.

For its Perron root ρ(z), choose positive left/right Perron vectors ℓ,r. Since

\[
P(z)=P_0+zbc,\qquad b\ge0,\ b\ne0,\quad c\ge0,\ c\ne0,
\]

the simple-eigenvalue derivative is

\[
\boxed{
\rho'(z)=\frac{\ell^Tbc\,r}{\ell^Tr}
=\frac{(\ell^Tb)(cr)}{\ell^Tr}>0
}.
\]

The Perron root therefore increases strictly with the gate weight.

It must lie in Q14, not Q3, for z>0. If it were a Q3 root at some z0, simplicity would prevent it from simultaneously being a Q14 root; continuity would then force the Perron branch to remain on the z-independent Q3 root locally, contradicting ρ'(z0)>0. At z=0, the positive left/right Perron vectors and nonzero b,c give a nonzero transfer-function residue, so the Perron root is a pole of H and belongs to Q0=Q14(z=0) as well.

The dominant growth mode is therefore inside the gate-sensitive degree-14 factor.

## 5. Positive-realization bound

For x,y>0, P0 is a 17×17 nonnegative matrix, b is a nonnegative input vector, and c is a nonnegative output row. Thus (P0,b,c) is an explicit 17-state positive realization of H.

Every positive realization is also an ordinary linear realization, so its dimension is at least the McMillan degree 14. For generic positive parameters,

\[
\boxed{14\le d_+(H)\le17}.
\]

This narrows the positive-realization problem from the 37-class quotient to a gap of at most three states. It does not prove that d_+=14. The existing failure of the standard scalar companion orthant is not a proof that every 14-ray invariant cone is impossible.

## 6. Exact verification

Checker: PREFIX575_gate_channel_certificate.py  
Runtime: Python 3.13.5; SymPy 1.14.0; exact symbolic polynomial arithmetic; no floating point.

The checker independently reconstructs the frozen 96-port kernel and verifies:

- all 9 root rows agree;
- the weighted quotient has 37 classes and growth [1,4,13,21,33,37];
- the 17/20 bipartition and exactly three gate edges;
- B(z)=B0+zuc and P(z)=P0+zbc entrywise;
- P0 and P(z) have the same 117-edge strongly connected support;
- P0, b, c and the BRC block matrices have nonnegative polynomial coefficients;
- the 17×17 characteristic polynomial factors by the existing Q3;
- the reconstructed Q14 SHA-256 matches PREFIX-574 exactly;
- Q14 is affine in z, Qz has degree 12 and leading coefficient \(-4(2u+1)\);
- cb=0 and cP0b=4(2u+1).

Result: ALL_CHECKS_PASS.

The existing Rabin certificate remains the proof source for generic Q14 irreducibility; this checker does not claim to rerun that certificate. The general transfer-function, coprimality, Perron and realization conclusions are proved in Sections 3–5; finite symbolic execution checks the concrete matrix construction and identities.

## 7. Reproducibility and provenance

Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.  
Prior Q14 source: PREFIX-574 checker blob `6cdf85ae5154b3f5f52bf6cab58b3a175e93dbb4`.  
Prior exact result: PREFIX-574 result blob `359ea1417845140966a48fbe943b4ce8a8a8f363`.  
Independent reconstructed Q14 SHA-256: `d258201370bd030e081aefec6c538dbea1abfc69712798080583a842ce66643e`.  
Executed local checker source SHA-256: `1e0983012fea414bb4fcadc960a7e1b0e99e1ac2096ff51ae1a0af9c8e6a50bb`. Persisted GitHub checker blob after readback: `9d61db526095621d0545f033c5c8a2622943e6b2`.  
Canonical compact result digest: `55d29881c7d9a07467ca2b8e4bb0289fb2bc230ddd256adb7b0ac63f64523a6c`. Persisted result JSON Git blob after readback: `abe18145c2ff07610f50ea41e7c4a34b7c4e2c82`.

## 8. Identity, ownership and publication status

GitHub authentication was verified as awdawmip, repository permission admin. This is repository identity/permission, not an Enterprise Math Researcher-ID.

The native Source session-start and live task-owner query failed with BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE; operation_sent=false. No active Owner or Researcher-ID was established, no CLAIM/takeover was attempted, and no Native Result or independent review is claimed. The Source activity registration was not completed because no authenticated session was issued; no identity or unknown session was invented.

This is an owner-branch durable research artifact. It is not canonical-main integration, theorem admission, Working Truth or Foundation promotion. Canonical Owner visibility and activity registration remain pending.

## 9. Next discriminating question

Determine whether the generic gate transfer function has a 14-state positive realization. Either:

1. construct a 14-ray polyhedral cone invariant under the 14-dimensional minimal realization and compatible with nonnegative input/output; or
2. prove a positive-realization obstruction giving d_+(H)≥15 for a generic positive parameter region.

If 14 is impossible, narrow the exact minimum to 15, 16 or 17. Preserve the gate-sensitive Q14 factor, the rank-one update, the same X6-BRC observer and the existing source pin. Do not reinterpret two-step operator depth as physical heartbeat time.
