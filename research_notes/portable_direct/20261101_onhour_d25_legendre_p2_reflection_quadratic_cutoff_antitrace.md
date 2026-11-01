# D25 SECOND-DIGIT-LIFT — p² Legendre reflection and the quadratic-cutoff even port

2026-11-01 Asia/Hong_Kong. **AUTHOR-SIDE SELF-CONTAINED PROVED POLYNOMIAL IDENTITIES / EXECUTED EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN**. Scientific Source pin `c47e13e4aba0e006366f989d6334d443f6333ae3` preserved; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Research lane `chatgpt-research-onhour-enterprise-math-20260923`, distinct from maintenance. This result consumes the previous p13 signed beta/CM-moment bridge (project `f416522fd1d194a55e2bdc2cc393a887526ff979`) without recrediting it. No P000/ACTIVE worldview modification.

## 1. All-prime coefficientwise reflection theorem

Let p>=5 be odd prime, a∈Z_(p) with a≢0,1 (mod p), b=1−a, and

`U_{p,a}(t)=sum_{k=0}^{p−1} (a)_k(b)_k t^k/(k!)²`.

Let n∈{1,...,p−2} be the unique integer satisfying a≡−n (mod p). The following identity holds **coefficientwise in (Z/p²)[t]**, without a CM premise:

```
U_{p,a}(1−t) ≡ (−1)^n U_{p,a}(t) (mod p²).
```

**Proof.** Put u_k=(a)_k(b)_k/(k!)² and L=t(1−t)∂²+(1−2t)∂−ab. For 0≤k≤p−2, the exact recurrence is (k+1)²u_(k+1)=(k+a)(k+b)u_k, and every denominator is a p-unit. The (a)_(p−1) factor at j=n and the (b)_(p−1) factor at j=p−n−1 each contribute p, so p² divides u_(p−1). Thus LU_{p,a}=0 coefficientwise mod p², including the terminal coefficient. Since a+b=1, the differential operator is invariant under t↔1−t, and V(t)=U_{p,a}(1−t) also satisfies LV=0. Among polynomials of degree <p over Z/p², the recurrence uniquely determines a solution from its constant term: V=cU, c=U(1). Reflecting twice and evaluating at t=0 gives c²=1 mod p². Mod p the series terminates at n and equals the Legendre polynomial P_n(1−2t), because the two hypergeometric parameters reduce to −n and n+1. Therefore c≡P_n(−1)=(−1)^n mod p. For odd p, c²=1 mod p² has exactly the roots ±1, so c=(−1)^n mod p². QED.

The p² strength is sharp in this family: at a=1/4,p=13,n=3, exact arithmetic gives U_{13}(1)+1≡12·13² (mod13³). The theorem does not assert all-prime CM selection or native H0/B0 data.

## 2. Original p13 quadratic ring, two branch ports

Set `U_p(t)=sum_{k<p}(1/4)_k(3/4)_k t^k/(k!)²`. For p≡5(mod8), n=(p−1)/4 is odd, so U_p(1−t)=−U_p(t) mod p². Work in the **external auxiliary coefficient ring**

`R₂=(Z/p²)[s]/(s²−2)`, `t_−=1/2−s/3`, `t_+=1/2+s/3=1−t_−`.

Then 4t_−t_+=1/9. The Legendre symbol (2/p)=−1, and s↦−s is both the nontrivial residue Frobenius and the ring conjugation. Reflection gives

```
Tr(U_p(t_−))=U_p(t_−)+U_p(t_+)=0 (mod p²).
```

Therefore U_p(t_−)=s·v_p with v_p∈Z/p²: its rational/even port vanishes, while the anti-invariant/odd port is retained. This external two-coordinate ring is **not** the native P000 X6 three-dimensional slice, the original H0/B0 divided-power, or its semilinear Frobenius.

## 3. Exact finite quadratic pullback and highest-degree cutoff

Keep the original beta Gauss polynomial `F_p(z)=sum_{k=0}^{p−1} alpha_k z^k`, `alpha_k=(1/8)_k(3/8)_k/(k!)²`. The standard quadratic identity of formal series over Q is

```
₂F₁(1/8,3/8;1;4t(1−t)) = ₂F₁(1/4,3/4;1;t).
```

A direct proof is obtained from the two hypergeometric differential equations: under z=4t(1−t), the Legendre operator on the composed left side equals 4 times the Gauss operator on F; both normalized formal series have initial value one, hence coincide coefficientwise.

Define the **actual finite truncation discrepancy** `R_p(t)=F_p(4t(1−t))−U_p(t)`. Missing terms in either infinite series start at t^p, giving the following **exact rational polynomial**, not a p-adic approximation:

```
R_p(t) = sum_{j=p}^{2p−2} r_(p,j) t^j,
r_(p,j) = sum_{k=ceil(j/2)}^{p−1}
           (−1)^(j−k) 4^k alpha_k binom(k,j−k).
```

Every alpha_k is p-integral for k<p. The original high-degree index, sign and source coefficients are explicit. Since t_± are p-adic units, the factor t^p is **not** a license to discard the finite cutoff at t_±.

Combine the exact quadratic pullback at 4t_±(1−t_±)=1/9 with the proven anti-trace of U. For every p≡5(mod8),

```
F_p(1/9) ≡ [R_p(t_−)+R_p(t_+)]/2 (mod p²).
```

The open **p≡13(mod24) second-digit cancellation** becomes the precise, source-retaining obligation

```
R_p(t_−)+R_p(t_+) ≡ 0 (mod p²).
```

Thus the even observer of the original Gauss sum is supported entirely by the **quadratic transformation's explicit j≥p cutoff**, whereas the truncated Legendre period is purely odd. This narrows the next proof search to high-degree coefficient pairing and even projection. It does **not** identify this new quadratic cutoff with the separately named 2304 signed Clausen T_beta, or establish the mother weighted216 result.

## 4. Executed independent checks and negative controls

Executable: `research_notes/portable_direct/d25_legendre_p2_reflection_antitrace_20261101.py` (standard-library Python; modular arithmetic; complete source published separately). Actual run returned: **45/45 primes 5≤p≤211** passed the full coefficientwise p² reflection, and the Legendre mod-p reduction; **8 primes p≡5(mod8)** passed two-coordinate quadratic anti-trace with an independent original beta recurrence; **4 primes p=13,29,37,373** passed the **complete quadratic pullback coefficient** check, the high-degree remainder evaluation and its even trace. The finite evidence is a regression check of the preceding all-prime proofs, not their proof.

| p | U_p(t_−) (1,s) mod p² | Original F_p(1/9) mod p² | R_p(t_−) (1,s) mod p² |
|---:|---:|---:|---:|
| 13 | (0,39) | 0 | (0,130) |
| 29 | (0,836) | 287 | (287,5) |
| 37 | (0,999) | 0 | (0,370) |
| 373 | (0,42895) | 0 | (0,96234) |

**Two discriminating limits:** (i) p=13 has a nonzero odd Legendre branch 39s mod169 while the rational Gauss factor vanishes mod169, so a direct branch identification fails. (ii) p=29 has an odd Legendre branch 836s mod841, while the rational Gauss factor is 287≡26(mod29), so simply tracing the Legendre branch would incorrectly prove vanishing for a non-target prime. The high-degree cutoff's rational port is indispensable.

## 5. BRC observer discipline, remaining frontiers and control

**BRC COMPOSE_APPLIED:** exact conjugate branch identities (t_−,t_+), Z/p² coefficients, original high-degree r_(p,j), even/odd and future derivative observers are kept distinct. The even quotient may eliminate the main Legendre branch for this precise mod-p² scalar, not for derivatives, coordinate lifts, signed Clausen/Green or native H0/B0 operations.

**Next smallest scientific unit:** at p≡13(mod24), prove or refute the explicit Galois-even sum of high-degree r_(p,j) at t_± modulo p² with a finite coefficient involution/CM pairing; then compose with the prior signed beta/CM moment M_p(1/9) and the original weighted216 Delta_p−R_p. No repetition of finished LL/LM/MM/LH source algebra is required.

**Native benchmark remains prioritized and distinct:** issue #1559 requires the same-original-class fixed p=373 H0/B0 divided-power [X]U mod139129, native module rank, real semilinear Frobenius eta/direction, original signed odd Hesse/Green, kappa and independent replication. It is NOT_RUN/PENDING_OWNER at the checked issue state; responsible path is the legitimate canonical Task/native evaluator owner or implementation maintainer, with reproducible original operator receipt and independent review as acceptance.

Formal Gateway 0.6.11 in this run reported research_authority_granted=false and executor_binding_configured=false. Own checkpoint list returned ACCESS_DENIED; original request `research-onhour-20261031-0205-dispatch-r15` returned CONTROL_REQUEST_NOT_FOUND in this client scope. Preserve that request and previously independent staging; do not derive a native session, claim, run, Source checkpoint, Result, admission or reviewer identity from this GitHub evidence. Frozen scientific Source pin, P000, ACTIVE worldview, Research-vs-maintenance identity separation and existing schedule/notification settings remain unchanged.

**Provenance:** prior p13 signed beta/CM Wronskian bridge `f416522fd1d194a55e2bdc2cc393a887526ff979`; original 216 frozen R port alignment `2d7bdfd7821d3afac8eaefb4b88bfedca8ff46be`; Guo–Zudilin 2304 q-microscope arXiv:1803.01830 is an earlier separate published input, not a proof of this tail-even cancellation.
