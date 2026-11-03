# PREFIX-460 — Sparse exact certificates for native X6 BRC moment ranks in degrees 11–14

2026-11-03, Asia/Shanghai. **Author-side exact computer-assisted proof; independent review and native task admission not obtained.**

## Frozen inputs and exact claim

Scientific input remains pinned to `f42f2906d77f24085c123f3ccfe9667d41caa96d`. This follows PREFIX-459 (`d814e4a60f6cdb36a8c5a1ed4da83446d1fe45e8`) and uses its explicit all-degree kernel construction. The governing rules were read separately at Enterprise Math `main@f12541ee71e77f200608fed40ba445faaf642dae` and GLOBAL_KNOWLEDGE_V1 `main@b9206b383039edd2d197bb0f7d0bb7918e01ea73`. P000 and the ACTIVE native X6/Heartbeat/residual-fidelity worldview are retained.

Take ordered length-N paths of signed native X6 unit steps. The history port records the number of negative first-axis steps modulo q. For each residue, observe all endpoint polynomial moments up to total degree d. Define B_d=binom(d+6,6) and let R_d(q) be the rational rank of this observer at N=q+d-2, q>=d. The result is:

| d | q range | B_d | last history-sector rank | defect | full rank R_d(q) |
|---:|---:|---:|---:|---:|---|
| 11 | q>=11 | 12376 | 12216 | 160 | 12376q-160 |
| 12 | q>=12 | 18564 | 18388 | 176 | 18564q-176 |
| 13 | q>=13 | 27132 | 26940 | 192 | 27132q-192 |
| 14 | q>=14 | 38760 | 38552 | 208 | 38760q-208 |

All quantifiers here are exact. The conclusion concerns this fixed native path model and polynomial observer, not reconstruction of all ordered-path provenance.

## Proof and checkable finite evidence

Put m=d-1. PREFIX-459 proved that the first q-1 history sectors individually have rank B_d, and that the last sector is the evaluation matrix of degree <=m+1 polynomials on

W_m={(s,y) in Z_nonnegative x Z^5 : s+sum_i |y_i|<=m and m-s-sum_i |y_i| is even}.

Under the 32 independent sign flips of y_1,...,y_5, the rational polynomial space decomposes into characters T subset {1,...,5}; write t=|T|. For T, take columns indexed by b,c_i>=0 with b+2sum c_i+t<=m+1 and basis y_T*s^b*product_i(y_i^2)^c_i. Rows are indexed by s>=0 and five a_i>=0, with a_i>0 for i<=t, s+sum a_i<=m and m-s-sum a_i even. Dividing each evaluation row by its nonzero factor product_{i<=t}a_i yields integer entries

A_(m,t)[(s,a),(b,c)] = s^b * product_i(a_i^(2c_i)).

The original and divided matrices have equal rational rank. The character of cardinality t occurs binom(5,t) times. PREFIX-459 constructed independently vanishing polynomials giving the rational upper bound

rank_Q(A_(m,t)) <= C_(m,t)-delta_(m,t), where
C_(m,t)=number of columns and delta_(m,t)=max(0,floor((m-t+3)/2)).

For every m=10,11,12,13 and every t=0,...,5, the companion exact program first enumerates all support rows. It groups rows by (s,sum(a)), sorts each group deterministically by SHA-256 of (m,t,s,a), then selects rows cyclically. The number selected is min(full_rows,max(C+25,ceil(1.01 C))). On this fixed near-square row subset it constructs exact matrices modulo both 32003 and 32009; these are primes by integer trial division. Full modular Gaussian elimination obtains rank C-delta in all 48 cases (24 blocks x 2 primes). A nonzero determinant minor modulo p gives a nonzero integer minor, hence rank_Q >= rank_Fp = C-delta. The universal rational kernel gives the opposite inequality. Thus the character rank is *exactly* C-delta.

Summing binom(5,t)(C-delta) equals B_(m+1)-16m. Earlier sectors contribute (q-1)B_(m+1), yielding all four formulas for every integer q>=d. No floating-point rank threshold is used; the program performs integer products and residues within signed 64-bit range.

The six character ranks per m, agreeing across both primes, are:

| m | t=0 | t=1 | t=2 | t=3 | t=4 | t=5 |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 918 | 666 | 415 | 289 | 164 | 108 |
| 11 | 1379 | 918 | 666 | 415 | 289 | 164 |
| 12 | 1841 | 1379 | 918 | 666 | 415 | 289 |
| 13 | 2632 | 1841 | 1379 | 918 | 666 | 415 |

The exact last-sector support sizes are 53834, 88166, 139139 and 212681. In the m=13 certificate, character-weighted selected row slots total 39562, compared to 212681 full support points. These are *certificate* row counts, not JSON storage measurements.

### Additional all-m counting lemma

For each m>=0 and t in {0,...,5}, the number L_(m,t) of unsigned character row labels satisfies

sum_{m>=0} L_(m,t) z^m = z^t / ((1-z)^6 (1-z^2)).

Indeed, s and the five a_i are nonnegative, t of the a_i are positive, and the remaining even slack is 2k>=0. Likewise C_(m,t) = [z^(m+1-t)] (1-z)^(-2) (1-z^2)^(-5) for m+1>=t. Consequently L_(m+1,t+1)=L_(m,t) and C_(m+1,t+1)=C_(m,t), whenever t<=4. These equalities of *counts* do not by themselves assert equality of evaluation ranks after translating a positive coordinate.

## Reuse, verification, provenance and next question

**BRC reuse: REUSE_APPLIED.** The carrier is a positive-rational weighted native path histogram with sector history, and the observer is the exact endpoint moment map. Sign-character projection is a proof technique, not an identification of positive branch masses with signed or complex amplitudes. The result certifies recoverability of the full standard degree-d moment tuple from a rational basis of the claimed rank. A concrete rational pivot decoder remains an engineering deliverable.

Evidence files: `prefix460_sparse_rank_certificate.py` and `PREFIX460_SPARSE_RANK_EXECUTION.log`. Python 3.13.5 and NumPy 2.3.5 were used with exact modular arithmetic. The 48 checks were completed in bounded invocations: a monolithic four-degree invocation was time-limited on reaching m=13, after which the m=13 blocks were individually executed and the execution log transparently consolidated. This certificate proves only the four stated degrees via the earlier all-degree analytic upper bound; arbitrary-degree exactness remains a research question.

**Next PREFIX-461:** Establish or disprove the all-degree matching equality dim ker_(m,t)=max(0,floor((m-t+3)/2)) using a parity-restricted Newton/border basis, testing the shifted-square interpolation step rather than inferring rank from cardinality. A separate implementation route constructs explicit rational pivot decoders in degrees 11–14 and benchmarks coefficient bit lengths and streaming native BRC propagation.

Current GitHub authentication: `awdawmip` with admin permission. The native task inventory call returned `CONTROL_QUOTA`; native researcher session registration returned `STATIC_READONLY_SCOPE_DENIED` with operation_sent=false. Current active owner is unconfirmed. No native Researcher-ID, formal CLAIM, independent review or admission is asserted. This is stored as independent author-side work.
