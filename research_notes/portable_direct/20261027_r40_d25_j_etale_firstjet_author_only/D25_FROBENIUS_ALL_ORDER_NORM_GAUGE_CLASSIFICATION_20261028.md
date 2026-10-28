# D25/LIFT — all-order norm/gauge classification of pinned odd jets

2026-10-28. **AUTHOR_DERIVED / AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE**. Same shared author context as PR #1566; this is not an independent review. Extends this branch's existing second-digit even/odd gauge-fiber lemma to every finite p-adic precision. Parent `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific source pin **c47e13e4aba0e006366f989d6334d443f6333ae3**, unchanged.

## Typed population and observations

For an odd prime p and n≥2 take B=Z/p^nZ, A=B[T]/(T²−2), σ(T)=−T. Define F_η(v)=ησ(v) with η=x+yT in 1+pA (x≡1, y≡0 mod p). For D25 use p≡13,19 mod24; the algebraic theorem holds for all odd p. The **even observer** is F_η², together with tr, det and F_η mod p; the **pinned odd observer** is y=[T]F_η(1)∈pB, with the chosen generator and basis fixed. Semilinear basis changes are the explicitly declared *unmarked* future operation, not part of the pinned observer.

## Theorem

For every such p,n,η:

1. F_η²=N(η)id for N(η)=x²−2y²∈1+pB, with B-linear matrix [[x,−2y],[y,−x]], trace=0, determinant=−N(η), and F_η mod p=σ.
2. **Complete exact pinned classifier:** η↦(N(η),y) is a bijection 1+pA ≅ (1+pB)×pB. The inverse is η(z,y)=sqrt₁(z+2y²)+yT, where sqrt₁ is the unique root ≡1 mod p. Consequently N is surjective, each fixed norm/even-observation fiber contains exactly **p^(n−1)** pinned operators, and an exactly recovering pinned observer must distinguish n−1 p-adic digits. This is a cardinality lower bound relative to the specified source marking.
3. **Complete unmarked classifier:** if N(η)=N(ξ), set α=ξ/η, u=1+α. Then N(α)=1, σ(α)=α⁻¹, u≡2 mod p is invertible, and u/σ(u)=(1+α)/(1+α⁻¹)=α. Hence M_u F_η M_u⁻¹ = F_ξ. Conversely any such gauge change preserves norm. Thus an *entire pinned norm fiber is one gauge orbit*, and every F_η is conjugate to the scalar sσ with s=sqrt₁(N(η)). Even norm completely classifies this **auxiliary unmarked family**, while no nonconstant odd-only readout descends to that quotient.

## Proof

Evaluating F_η(1)=x+yT and F_η(T)=−2y−xT gives the matrix. Since σ²=id and A is commutative, F_η²(v)=ησ(η)v=(x²−2y²)v. For each z≡1 (mod p) and y≡0 (mod p), z+2y²≡1 (mod p). The polynomial X²−(z+2y²) has X=1 as a root modulo p with derivative 2X=2 a unit. Elementary digit-by-digit Hensel lifting produces a unique root x≡1 (mod p) modulo p^n, proving the asserted bijection without assuming a general Hilbert-90 theorem. There are |pB|=p^(n−1) possibilities for y and |1+pB|=p^(n−1) for z. The explicit gauge calculation in (3) proves both orbit transitivity and norm invariance. This establishes all claims for **every** odd p and n≥2.

## Exact witness and checking

A standalone standard-library Python checker and actual author-side summary accompany this note. Complete enumeration passes at (p,n)=(5,2),(5,3),(5,4),(7,2),(7,3),(13,2),(13,3),(19,2); it includes 15,625 η for (5,4) and 28,561 for (13,3). Additionally **1,365** direct exact conjugation checks passed for 7 target primes 13,19,37,43,109,211,373 at n=2,3,4,5. At p=373,n=4,m=19,356,878,641, η+=(139130,373) and η−=(139130,19356878268) have norm 1, opposite pinned odd digit modulo 373², but u=(556518,19253087661) conjugates one to the other exactly modulo 373⁴. They are *not* two inequivalent unmarked Frobenius modules.

## Meaning, provenance and unresolved native gate

The labelled BRC source space has elements (η,p,n,ordered basis,observer); projecting to norm collapses p^(n−1) exact fibres for the **marked** future odd readout. For the different *unmarked* gauge operation, that same fibre is one equivalence class. This auxiliary finite ring is **not** the Heartbeat World's native discrete six-dimensional X6 Cell space; no X6/CM embedding, original H0/B0 semilinear rank, or true Δ_p−R_p source transfer has been established. No original p373 native experiment is claimed.

Existing Issue #1559 still requires authentic same-original-class H0/B0, Frobenius, original marked section, signed Green/Hesse observation and the full native transfer. This lemma sets an **information and normalization gate** but does **not** disprove LIFT/JT2 or prove native odd-data gauge freedom. The separate UR four-file V2 bundle remains unverified as 94,687 bytes / SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; its mathematics is not re-proved.

During this author's run Source control replies CONTROL_QUOTA on task inventory, ACCESS_DENIED on own checkpoint list; status reports UPSTREAM_CODE_REVIEW_REQUIRED, 5/5 active jobs, executor_binding_configured=false and research_authority_granted=false. PR storage **does not** establish native CLAIM, OPEN, checkpoint, Result or independent admission. If continuation seed later says CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS, fully read initial artifacts then use typed continuation_prepare with completed_units=[].

**Next exact scientific action:** under #1559, establish the true original-class normalized source and its allowed gauge group, then determine whether a marked odd second digit is independently fixed or requires a separately retained native port. Only then test a strict relation to the existing finite Cauchy/Clausen observations and Δ_p−R_p.
