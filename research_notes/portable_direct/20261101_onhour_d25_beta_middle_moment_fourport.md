# D25 SECOND-DIGIT-LIFT — original beta signed middle/middle port and four-source budget

2026-11-01 · TASK_RESEARCH · AUTHOR-SIDE EXACT PROOF · FINITE EXACT CHECK · **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN**.

Mother: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; original publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Research lane `chatgpt-research-onhour-enterprise-math-20260923`, never the separate maintenance conversation. Earlier source-specific high/low result: commit `e5f31bafe2c7dd421430023f4d717013c424525f` (consumed, not recredited).

## All-prime arithmetic theorem (p ≡ 5 mod 8)

Take any prime p≥13 with p≡5 (mod 8), and set
[
a=(5p-1)/8,quad b=(7p-3)/8,quad m=b-a=(p-1)/4.
]
Retain the **original** beta coefficient and signed clipped square:
[
eta_k=rac{(1/8)_k(3/8)_k}{9^k(k!)^2}
=rac{prod_{j=0}^{k-1}(8j+1)(8j+3)}{576^k(k!)^2},
qquad
T_{eta,p}=sum_{substack{0le i,j<p\i+jge p}}(8(i+j)+1)eta_ieta_j.
]
Work in the p-local integers; all divisions by p below are exact. The valuation bands are L=[0,a] (valuation 0), M=[a+1,b] (valuation 1), H=[b+1,p−1] (valuation 2). Put
[
s_r=eta_{a+1+r}/ppmod p quad(0le r<m).
]

**Theorem A, new middle-band seed and recurrence:**
[
oxed{quad s_0=rac{10}{441}inom ba9^{-a}pmod p,qquad
s_{r+1}=s_r,rac{(8r+8)(8r+10)}{9(8r+15)^2}pmod pquad(0le r<m-1).quad}
]
All modular denominators are units in the stated range.

**Proof.** The transition from beta_a to beta_(a+1) contains the *single* factor 8a+1=5p, while 8a+3=5p+2 and a+1≡7/8 (mod p). Thus beta_(a+1)/p≡beta_a·10/(576(a+1)^2)≡(10/441)binom(b,a)9^(−a) (mod p). The exact recurrence
[
eta_{k+1}/eta_k={(8k+1)(8k+3)}/{(576(k+1)^2)}
]
at k=a+1+r, reducing the p-unit factor after dividing both sides by p, gives the claimed recurrence. QED.

Define
[
S=sum_{r=0}^{m-1}s_r,qquad W=sum_{r=0}^{m-1}(a+1+r)s_rpmod p
]
and retain the **original signed ordered** middle/middle component
[
T^{MM}_{eta,p}=sum_{substack{i,jin M\i+jge p}}(8(i+j)+1)eta_ieta_j.
]
**Theorem B, new complete p² middle/middle port:**
[
oxed{quad T^{MM}_{eta,p}equiv p^2 S(S+16W)pmod{p^3}.quad}
]
**Proof.** Every pair in M² is clipped because 2(a+1)>p. Each beta in M has valuation one, so divide the product by p² and reduce mod p. The original signed coefficient expands as 1+8i+8j; summing over the **ordered** square gives S²+16SW. This factorization only preserves the declared signed scalar observer mod p³, not native H0/B0, derivative, Green/Hesse or other observers. QED.

**Theorem C, exhaustive four-port budget:** writing T^LL,T^LM,T^LH,T^MM for the original weighted clipped ordered pair sources, where unequal bands count both orientations,
[
oxed{quad T_{eta,p}equiv T^{LL}+T^{LM}+T^{LH}+T^{MM}pmod{p^3}.quad}
]
The omitted MH/HH pair classes have valuation≥3. In this decomposition LL requires full mod p³ precision and LM retains its mod p² normalized carry. The existing high/low port T^LH is reused from the preceding proof. Nothing equates p²-valued MM or LH to the original 216 Delta−R observer.

For **p≡13 (mod24)**, *conditional on the previously established* p-local unit H_p, the original Clausen identity B_p=G_pH_p−T_beta and the external 2304 supercongruence B_p≡pχ_(−3)(p) mod p³, the still-unproved p13 lift is equivalent to the narrower signed problem
[
oxed{quad G_pequiv0pmod{p^2}iff T^{LL}+T^{LM}equiv-pchi_{-3}(p)pmod{p^2}.quad}
]
Neither side is proved for all p≡13 mod24 by this report. The prior Jacobi divided-Frobenius target 8J/p=5C1+7C_lambda mod p likewise remains OPEN. Original 216 A_p≡p mod p³ remains OPEN.

## Actual exact computations

Executed Python standard library checker `d25_beta_middle_moment_fourport_20261101.py`: **109/109** primes 13≤p≤3000 with p≡5 mod8, including **53 p≡13 mod24**. Each prime independently checks all beta recurrence terms modulo p³, the three valuation bands and every middle s_r against the new recurrence. Seven selected primes also independently form all original signed ordered pair sums, verify MM/p²=S(S+16W), check MH/HH vanish, and reconstruct full T with a separate suffix-sum path. All assertions PASSED.

| p | S | W | MM/p² mod p | previous LH/p² mod p | full T mod p³ | LL+LM mod p² |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 12 | 3 | 5 | 8 | 1170 | 156 |
| 29 | 17 | 5 | 25 | 11 | 17690 | 29 |
| 37 | 25 | 34 | 17 | 28 | 13653 | 1332 |
| 53 | 30 | 4 | 11 | 42 | 61851 | 53 |
| 61 | 6 | 26 | 31 | 11 | 44591 | 3660 |
| 109 | 1 | 20 | 103 | 65 | 974133 | 11772 |
| 373 | 232 | 195 | 332 | 111 | 29773233 | 138756 |

For p=373, the **distinct** new MM quotient 332 and earlier LH quotient 111 sum to 70 mod373; their combined contribution is p²·70 mod p³. Lower-valuation LL and LM remain nonzero and must not be dropped. This is a finite exact certificate plus the displayed elementary all-p proof, **not** an independently admitted result.

## BRC, checkpoint, recovery

BRC COMPOSE_APPLIED: origin labels LL/LM/LH/MM, signed ordered indices, clipping predicate, valuations, original modulus and observer are conserved. Reducing MM to two moments is proven safe *only* for this specified mod-p³ signed scalar; cannot be transferred to semilinear Frobenius/rank/native operator.

Next smallest scientific unit: consume finished LH and MM, derive a **joint LL+LM mod p² cancellation** for p≡13 mod24 (or counterexample); then couple with original 216 Delta−R. Do not add yet another already-settled high-band terminal lemma.

The original-class p=373 **native H0/B0 divided-power** with [X]U mod139129, true rank, semilinear Frobenius/eta, odd signed Green/Hesse, kappa, independent reproduction still belongs to existing support **#1559**, NOT_RUN/PENDING_OWNER. Actual responsible path: authenticated Source task owner, designated native evaluator or project maintainer; required acceptance is original-class raw reproducible benchmark and independent validation. This work did not execute that experiment.

Control status in this turn: authenticated Gateway 0.6.11 reported research_authority_granted=false, executor_binding_configured=false, active native-job quota full; original target_request_id `research-onhour-20261031-0205-dispatch-r15` read returned scope-local CONTROL_REQUEST_NOT_FOUND, **not proof of a global empty request**. No current own authenticated Source session, winning CLAIM, opened run, checkpoint, freeze or admission was established. No attempt to replay denied mutations or borrow maintenance identity. Existing three neutral staging sources remain separate. No scheduling, P000/ACTIVE worldview or frozen science pin changes.

**Program**: `research_notes/portable_direct/d25_beta_middle_moment_fourport_20261101.py`; `AUTHOR_PROVED_ELEMENTARY / EXACT_FINITE_CHECK_PASSED / UNREVIEWED / NOT_ADMITTED`.
