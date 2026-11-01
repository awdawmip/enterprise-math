# D25 SECOND-DIGIT-LIFT — exact original beta low/low first-carry, binomial–harmonic ports

Date: 2026-11-01 Asia/Hong_Kong. **AUTHOR-SIDE PROVED ARITHMETIC IDENTITY / EXECUTED EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN**.

Mother `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Research lane `chatgpt-research-onhour-enterprise-math-20260923` distinct from maintenance. Consume previous signed beta LM/MM/LH ports (fba1062e, 3cc0aede, e5f31baf) and exact low Pochhammer deformation (f8cc8141), without recredit.

## New all-prime arithmetic theorem

Let p>=13 be prime, p≡5 (mod8); a=(5p−1)/8, b=(7p−3)/8. In Z_(p), for 0<=i<=a put

`beta_i = ((1/8)_i(3/8)_i)/(9^i(i!)²)`,
`c_i = binom(a,i)binom(b,i)9^(−i)`,
`e_i = −[5(H_a−H_(a−i))+7(H_b−H_(b−i))]/8 (mod p)`.

Here H_n=sum_{j=1}^n 1/j and all denominator factors in these expressions are p-units. Let `C(z)=sum_{i=0}^a c_i z^i` over Z_(p), `E(z)=sum_{i=0}^a (c_i mod p)e_i z^i` over F_p. For degree <=2a define the *original signed high-degree readout* `L_p(U)=sum_{s=p}^{2a}(8s+1)[z^s]U`, reduced at the precision of U.

Define the exact clipped, both-ordered-orientations original low/low source:

`T_LL = sum_{0<=i,j<=a; i+j>=p} (8(i+j)+1) beta_i beta_j`.

**Theorem LL-2PORT (for every specified p):**

```text
T_LL = L_p(C²) + 2p L_p(C E)     (mod p²).
```

In particular, whenever p divides `L_p(C²)`, taking the p-local quotient before reduction gives

```text
T_LL/p = L_p(C²)/p + 2 L_p(C E)   (mod p).
```

The two terms are respectively the *original integer-binomial high-degree carry* and the *separately labeled first-order Pochhammer/harmonic port*, not one unlabelled number.

**Proof.** The exact identities `1/8=−a+5p/8`, `3/8=−b+7p/8` and invertibility of every denominator for i<=a yield the previously established one-index Taylor expansion
`beta_i ≡ c_i(1+p e_i) (mod p²)`. For each allowed original ordered pair, multiply:
`beta_i beta_j ≡ c_i c_j [1+p(e_i+e_j)] (mod p²)`.
Summing the unchanged signed weight `8(i+j)+1` over exactly `i+j>=p` gives `L_p(C²)`. Swapping `(i,j)↔(j,i)` preserves both the cut and signed weight, hence the two deformation terms coincide and equal `p L_p(C E)`. No infinite-prime CM cancellation was assumed. QED.

## Exact p≡13(mod24) residual obligation, not its proof

Set `G_p=sum_{k=0}^{p−1} beta_k`. On the original p≡13(mod24) branch, *conditional on the explicitly reused* author-side mod-p CM selection `G_p≡0(mod p)` and p-unit `H_p`, the published Guo–Zudilin 2304 supercongruence `B_p≡p χ_(−3)(p) (mod p³)` (Adv. Math. 346, 2019, arXiv:1803.01830), and exact weighted Clausen identity `B_p=G_p H_p−T_beta`, the four band ports imply `p | T_LL` and `p | L_p(C²)`: other ports have p-adic order >=1. The previously proved low/middle first-carry port `C_LM = T_LM/p (mod p)` is retained. It follows strictly that

```text
G_p ≡ 0 (mod p²)
  iff [L_p(C²)/p + 2 L_p(C E) + C_LM] ≡ −χ_(−3)(p) (mod p),
  for p≡13 (mod24), subject to the stated reused inputs.
```

The right-hand *universal cancellation is OPEN*. This theorem decomposes the remaining opaque LL source into two exact original signed ports; it does not complete the 216 LIFT or native experiment.

## Reproducible exact certificate and scope

Executable **actually run**: `research_notes/portable_direct/d25_ll_first_carry_brc_port_20261101.py`, Git blob `996434eac0a356b8b485bb675b2b194a77413574`. Imports preceding author-side source-port programs `d25_beta_middle_moment_fourport_20261101.py` and `d25_beta_lowmiddle_signed_carry_20261101.py`. Uses standard-library integer modular arithmetic, no floating point. The program forms `c_i mod p²`, `e_i mod p`, evaluates the whole LL signed pair readout using *four original-index suffix moments in O(p)*, and independently recomputes every original beta coefficient and LL contribution from the separate Pochhammer recurrence. At p=13,29,37,53,61,109,373 it compares to the original signed double-index source checker. It also checks the still-open target identity empirically, without promoting it.

All **109 primes 13<=p<=3000, p≡5(mod8)** passed; **53** are p≡13(mod24). In this finite domain the harmonic first-carry port is nonzero in **all 109 cases**, and the integer-binomial first carry is nonzero in **108**; neither source can be silently discarded. This finite calculation does not prove infinite-prime CM cancellation.

| p | base L_p(C²)/p | harmonic 2L_p(C E) | LL/p | LM/p | joint (LL+LM)/p | 
|--:|--:|--:|--:|--:|--:|
| 13 | 10 | 12 | 9 | 3 | 12 |
| 29 | 0 | 1 | 1 | 0 | 1 |
| 37 | 25 | 5 | 30 | 6 | 36 |
| 53 | 35 | 7 | 42 | 12 | 1 |
| 61 | 50 | 10 | 60 | 0 | 60 |
| 109 | 50 | 22 | 72 | 36 | 108 |
| 373 | 282 | 260 | 169 | 203 | 372 |

At p=373, `282+260 ≡169 (mod373)`, `169+203=372≡−1 (mod373)`; this is the original beta signed scalar, **not** native H0/B0 Frobenius or `Delta_373=R_373=196`.

**BRC COMPOSE_APPLIED:** retain two original indices, both orientations, signs, clipping, p-adic valuation, integer-binomial and harmonic provenance. The suffix-moment quotient is certified only for this signed scalar observer mod p²; it is not lossless for a changed cut, derivative, Green/Hesse or native semilinear Frobenius.

**Next scientific action:** prove/refute the displayed p13 LL+LM congruence via source-faithful Jacobi/CM/Frobenius moment algebra at the *rational lift 1/9*; then reconnect original weighted216 `Delta_p−R_p`. Do not redo completed LH/MM/LM seeds. The exact native fixed-p373 original H0/B0 divided-power `[X]U mod139129`, rank, semilinear Frobenius eta, odd signed Green/Hesse, kappa and independently replicated output remain **NOT_RUN/PENDING_OWNER**, existing support issue #1559. Portable beta scalar is not a substitute.

**Control:** gateway 0.6.11 observed 2026-11-01T05:02Z `research_authority_granted=false`, `executor_binding_configured=false`, quota active 5/5. Previous request `research-onhour-20261031-0205-dispatch-r15` read returned client-scoped `CONTROL_REQUEST_NOT_FOUND` (global state unknown), own checkpoint `ACCESS_DENIED`. No new native CLAIM/OPEN/Source checkpoint/Result or session registration is asserted; previous staging is separate. This is author-side repo research persistence, **UNREVIEWED/NOT_ADMITTED**, not a formal Source checkpoint. Research/maintenance identity separation, frozen pin, P000/ACTIVE worldview and existing scheduler settings preserved.
