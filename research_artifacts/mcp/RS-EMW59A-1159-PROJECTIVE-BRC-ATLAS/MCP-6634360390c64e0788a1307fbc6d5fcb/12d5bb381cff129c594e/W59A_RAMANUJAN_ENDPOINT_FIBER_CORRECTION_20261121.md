# W59A Ramanujan spectral trace: exact endpoint-fiber correction
Status: TASK_RESEARCH / independently checked correction to a FREE_RESEARCH theorem-candidate proof / NOT_REVIEWED
Date: 2026-11-21
Task: RS-EMW59A-1159-PROJECTIVE-BRC-ATLAS
Affected frozen source: enterprise-math@9e6e9abe813aa17a7eff1ee8278e2f0e9f73312c:research_notes/RAMANUJAN_SUMS_AS_PROJECTIVE_SPECTRAL_GALOIS_TRACES_20260905.md, especially RA-6–RA-8.
No change to the historical source bytes or its author attribution.

## Exact local issue
For d>2 let E_d be the primitive projective spectral root set with |E_d|=h_d=φ(d)/2, and let R_n be the finite decimation polynomial. Put e=d/gcd(d,n). The source states in RA-6 that every root of E_e has φ(d)/φ(e) preimages under E_d→E_e, with a 'natural endpoint interpretation' for e=1,2. This ratio is correct for e>2, because h_e=φ(e)/2. At e=1 or e=2 there is ONE critical endpoint root, while φ(1)=φ(2)=1. Its actual fiber size is h_d=φ(d)/2, not φ(d)/φ(e)=φ(d). Thus the literal uniform-fiber assertion cannot hold at the endpoints.

Smallest explicit witness: d=6,n=3 => e=2. E_6={1} because Ω_6(v)=v-1, and R_3(v)=v(3-v)^2. Hence R_3(1)=4, the only denominator-2 endpoint root. The actual fiber contains 1 element, while φ(6)/φ(2)=2. The source's RA-1 formula S_e=φ(e)-μ(e) is stated for e>2; substituting e=2 would give S_2=2, whereas the actual endpoint root sum is S_2=4. Two incorrect endpoint extrapolations can accidentally cancel in the final trace identity. The theorem's correct endpoint proof must be explicit.

## Corrected exact statement and case-split proof
Keep d>2 and h_d=φ(d)/2. Let
  T_d(n)=Tr_{K_d/Q}(C_n(2-α_d))
         =Σ_{v∈E_d}(2-R_n(v)).
Here the trace expansion uses the proposed projective spectral Galois orbit, so its algebraic/Galois identification is an explicit hypothesis to audit separately.

Case e>2: E_e has h_e=φ(e)/2 elements; the constant fiber size is h_d/h_e=φ(d)/φ(e). If the independently stated root-sum theorem S_e=φ(e)-μ(e) holds, then
  T_d(n)=φ(d)-[φ(d)/φ(e)]·S_e
        =μ(e) φ(d)/φ(e).

Case e=1: all R_n(v)=0 (critical spectral endpoint). Thus T_d(n)=2h_d=φ(d), agreeing with μ(1)φ(d)/φ(1).

Case e=2: all R_n(v)=4 (the other critical endpoint). Thus T_d(n)=-2h_d=-φ(d), agreeing with μ(2)φ(d)/φ(2).

Consequently the advertised identity
  T_d(n)=μ(e)φ(d)/φ(e)=c_d(n)
survives **with corrected endpoint fiber accounting**, provided the spectral denominator-transition and Galois-orbit hypotheses are satisfied. The endpoints are not instances of RA-6 with the ordinary φ-ratio.

## Independent compatibility audit
In the external finite root-of-unity presentation α_{r,d}=2-(ζ_d^r+ζ_d^{-r}), r ranges over units mod d up to ±; C_n(ζ+ζ^{-1})=ζ^n+ζ^{-n}. Summing over ±-pairs gives T_d(n)=Σ_{r∈(Z/d)×}ζ_d^{nr}=c_d(n). This supplies an independent algebraic compatibility check of the corrected result, not an intrinsic P000-native BRC carrier map.
For the d=6,n=3 witness, E_6={1} and C_3(2-1)=1³-3·1=-2=c_6(3). For d=3,n=3, E_3={3}, R_3(3)=0 and T_3(3)=2=c_3(3).

## Scope and practical consequence
Retain RA-8 as a finite spectral arithmetic trace statement with its Galois inputs, while marking RA-6's endpoint wording and the RA-7 proof's e=1,2 substitutions as requiring this correction. Do not infer a native BRC or X6 state correspondence from matching cyclotomic traces. The exact native-integration problem remains open, as does an independent Driver mathematical review.

Next: verify the actual finite decimation/root transitions for e>2 and the rooted projective Galois orbit with exact source paths. Preserve the 2026-09-05 FREE research provenance and all existing task ownership.
