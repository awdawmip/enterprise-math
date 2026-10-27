# D25 / SECOND-DIGIT-LIFT — Original W/S midpoint p-adic two-port exact certificate

Date: 2026-10-27. Logical researcher conversation: chatgpt-research-onhour-enterprise-math-20260923 (separate from maintenance). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Immutable scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.

**AUTHOR-SIDE / PROVED ALGEBRAIC IDENTITIES / EXACT INTEGER CROSSCHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_H0B0_NOT_EXECUTED.**

## Scope and prior results consumed

Retain the unchanged rational sources

$$w_k=\frac{(6k+1)(2k)!(3k)!}{(k!)^5 216^k},\qquad
s_k=\frac{(8k+1)(4k)!}{(k!)^4 2304^k},\qquad d_k=w_k-s_k.$$

Consume the already proved Guo–Zudilin companion half-truncation, the frozen D24 UR, the actual original source-port alignment and the separately authored R47 exact source-labelled W/S adjacent-rank recurrence in research_notes/portable_direct/20261027_hourly_d25_rank2_additive_and_highhigh_pole_r47_r48.md. The present theorem concerns the original midpoint rank and its next rank, not any native H0/B0 calculation. All fractions below are divided in Z_(p) *before* reduction.

## Theorem A: uniform exact units at the half-length seam

For every prime p=6m+1>=7, put h=(p-1)/2=3m and epsilon=(6/p), the actual Legendre symbol. Then

$$v_p(w_h)=v_p(s_h)=1,\qquad v_p(w_{h+1})=v_p(s_{h+1})=2,$$

$$\boxed{w_h/p\equiv4\epsilon,\quad s_h/p\equiv3\pmod p,}\tag{A1}$$

$$\boxed{w_{h+1}/p^2\equiv(4/9)\epsilon,\quad s_{h+1}/p^2\equiv5/36\pmod p.}\tag{A2}$$

**Proof.** The exact factorial arguments at h are 2h=p-1, 3h=p+h-1 and 4h=2p-2, so Legendre's formula gives v_p(w_h)=v_p(s_h)=1. The original weights are 6h+1=3p-2 and 8h+1=4p-3, both units. Wilson reflection gives

$$(2h)!\equiv-1,\quad(3h)!/p\equiv-(h-1)!,\quad
(4h)!/p\equiv-(p-2)!\equiv-1\pmod p.$$

Pairing terms in Wilson also gives (h!)^2=(-1)^(h+1), hence (h!)^4=1 mod p, while h=-1/2 mod p. Thus substitution in the unchanged sources gives

$$w_h/p\equiv4\cdot216^{-h}=4(216/p)=4(6/p),\qquad
s_h/p\equiv3\cdot2304^{-h}=3,$$

using 216=6^3 and 2304=48^2. For the successor consume the exact R47 source ratios

$$a_k=w_{k+1}/w_k=
\frac{(6k+7)(2k+1)(3k+1)(3k+2)}{36(6k+1)(k+1)^3},$$

$$b_k=s_{k+1}/s_k=
\frac{(8k+9)(2k+1)(4k+1)(4k+3)}{288(8k+1)(k+1)^3}.$$

At k=h the common factor 2h+1 is exactly p, all remaining factors are p-units, and h=-1/2 mod p yields a_h/p=1/9 and b_h/p=5/108. Multiply by (A1) to obtain (A2). All displayed leading residues are units for p>=7, so both valuations are exact. QED.

## Theorem B: source-labelled additive boundary and exceptional rank drop

Define the original signed observations D0=d_h/p mod p and D1=d_(h+1)/p^2 mod p. Theorem A yields

$$\boxed{D0=4\epsilon-3,\quad D1=(16\epsilon-5)/36\pmod p.}\tag{B1}$$

For the explicitly declared *free* source-labelled input (u,v)=(w_h/p,s_h/p) mod p, the two-port linear observation matrix is

$$\binom{D0}{D1}=
\begin{pmatrix}1&-1\\1/9&-5/108\end{pmatrix}
\binom uv,\qquad \det=7/108.$$

For every p>=13 with p=1 mod6, the exact inverse is

$$\boxed{u=(108D1-5D0)/7,\quad v=(108D1-12D0)/7\pmod p.}\tag{B2}$$

At p=7 this *free-amplitude* observer has rank one. The actual original values are (u,v)=(3,3), D0=D1=0. This is a scoped information-loss witness, not an assertion that the fixed factorial sources are unknown. On the frozen D25 classes:

| p mod24 | epsilon | D0 | D1 |
|---:|---:|---:|---:|
| 13 | -1 | -7 | -7/12 |
| 19 | +1 | 1 | 11/36 |

These are exact signed boundary inputs, not a proof of full W_p=S_p mod p^3 or LIFT.

## Native-priority p=373 original-source certificate

For p=373, h=186, p^2=139129 and p^3=51895117, all residues were obtained independently from the original integer factorials:

| Quantity | Normalized residue mod373 | Original rational term modulo indicated power |
|---|---:|---|
| w_186/373 | 369 = -4 | w_186=137637 mod139129 |
| s_186/373 | 3 | s_186=1119 mod139129 |
| w_187/373^2 | 41 | w_187=5704289 mod51895117 |
| s_187/373^2 | 197 | s_187=27408413 mod51895117 |
| D0 | 366 = -7 | d_186=136518 mod139129 |
| D1 | 217 = -7/12 | d_187=30190993 mod51895117 |

**Actual execution:** Python 3 standard-library checker d25_original_midpoint_two_port_guard_20261027.py used an independent p-free-factorial modular path on all 80 primes 7<=p<1000 with p=1 mod6 and a separate exact rational Fraction/factorial path at p=7,13,19,37,43,211,373. All asserted source valuations, residues, inverse boundary conditions, p=7 exception and the p=373 table passed. The theorem is proved algebraically above; the finite checks validate implementation and arithmetic, not the infinite statement by extrapolation.

## BRC, source authority and continuation

BRC resolution: COMPOSE_APPLIED. Carrier: prime and Legendre branch, ordered original W/S source labels, exact midpoint ranks h/h+1, distinct valuations, normalized residues, signed D0/D1 and future original low-half/Green/WZ source reconstruction. The determinant is the exact condition for source-observer factorization; reducing both original terms to zero before p-division would lose required information. These indices are auxiliary arithmetic ranks, not native X6 Cell axes; P000 and the ACTIVE residual-faithful discrete worldview are unchanged.

Mother D25/LIFT/JT2 remains OPEN. Required highest-priority original fixed H0/B0 divided-power benchmark at p=373 is still [X]U mod139129, actual module rank and semilinear Frobenius orientation/eta, signed Green/Hesse, original kappa and Delta_p-R_p. On 2026-10-27 support Issue awdawmip/enterprise-math#1559 was OPEN/PENDING_OWNER/NOT_EXECUTED. The author calculation does not substitute that original native experiment.

Historical same-lane recovery request research-onhour-20261027-0501-recovery-r13 has a verified read-only success receipt reporting an ACTIVE but unbound Researcher session MCP-de3e5bafb24f43f4a5e6285e7601676a, with no own claims/runs; dispatch request research-onhour-20261027-0507-dispatch-r13 is terminal FAILED/TimeoutExpired. The 2026-10-27 Site gateway reports research_authority_granted=false and quota 5/5. No alternate-identity mutation, source CLAIM, Source-native checkpoint, or other lane execution occurred. The three neutral staging sources retain independent provenance.

**Next exact action:** after current Source authorization/quota resolution, use this real Research lane for lawful continuation and await a verified original H0/B0 native executor on #1559. Use (A1)–(B2) only as original W/S signed low-half seam inputs when investigating the still-open all-prime source-labelled cancellation; retain the p=7 exceptional boundary outside the target classes. Frozen science source pin is unchanged.
