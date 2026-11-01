# D25 / SECOND-DIGIT-LIFT: Original A216–B2304 signed tier-0/tier-1 three-carry certificate

Date: 2026-10-29, Asia/Hong_Kong.
Status: AUTHOR-SIDE / PROVED CONDITIONAL CARRY DECOMPOSITION / EXECUTED FINITE CERTIFICATE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Research conversation: chatgpt-research-onhour-enterprise-math-20260923. Maintenance conversation is distinct and unused.

## Exact original weighted sources

For every prime p>=5 and 0<=n<p, take the two distinct original p-local rational streams

$$
a_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\qquad
b_n=\frac{\binom{2n}{n}^2\binom{4n}{2n}}{2304^n},\qquad
\chi_p=\left(\frac{-3}{p}\right).
$$

Define A_p^(j) as the sum of (6n+1)a_n over the exact indices v_p(a_n)=j, and B_p^(j) as the sum of (8n+1)b_n over v_p(b_n)=j, preserving the cutoff 0<=n<p and the original weights. The valuations of the coefficients, *before* multiplying by their weights, are exactly

$$v_p(a_n)=\lfloor 2n/p\rfloor+\lfloor 3n/p\rfloor,\qquad
v_p(b_n)=\lfloor 4n/p\rfloor.$$

Work in Z/p^4, and define four distinct ports

$$
C_0=A_p^{(0)}-2B_p^{(0)}+p\chi_p,\qquad
C_j=A_p^{(j)}-2B_p^{(j)}\quad(j=1,2,3).
$$

The current unproved full bridge candidate is
$$
A_p-2B_p+p\chi_p=\sum_{j=0}^3 C_j
\stackrel{?}{\equiv}0\pmod{p^4}.
$$

The previously proved valuation-two first-jet and valuation-three top-reflection formulas already identify Q=C_2/p^2 mod p^2 and D=C_3/p^3 mod p; see the existing 2026-10-29 tier2 and top-tail source notes. Those are inputs, not repeated discoveries.

## Exact three-carry equivalence (proved conditional algebra)

For all primes p>=5, v_p(C_1)>=1, v_p(C_2)>=2 and v_p(C_3)>=3. If p also divides C_0, define

$$
L_0=C_0/p\pmod{p^3},\quad
L_1=C_1/p\pmod{p^3},\quad
Q=C_2/p^2\pmod{p^2},\quad
D=C_3/p^3\pmod p.
$$

Then the original p^4 bridge holds **if and only if** all three successively defined, exact congruences hold:

$$
\begin{aligned}
\mathrm{Carry}_1:&\quad L_0+L_1=0\pmod p,\\
\mathrm{Carry}_2:&\quad (L_0+L_1)/p+Q=0\pmod p,\\
\mathrm{Carry}_3:&\quad ((L_0+L_1)/p+Q)/p+D=0\pmod p.
\end{aligned}
$$

Each division is made only after the preceding divisibility has been established; the expressions are read at their declared quotient-ring precisions. Proof: exact regrouping gives
$$
\sum_j C_j\equiv p(L_0+L_1+pQ+p^2D)\pmod{p^4}.
$$
Successive division by p is equivalent to the three displayed congruences. No prime-sensitive cancellation statement is proved by this elementary equivalence.

For the frozen classes p=13 or 19 (mod 24), the first hypothesis p|C_0 follows from the *preexisting* accepted CM0 source f_0=K_p(1/2)=0 mod p: finite Clausen gives A_p^(0)=K_p(1/2)(K_p+12\Theta K_p)(1/2)=0 mod p. The separately proved Guo–Zudilin B_p=p\chi_p mod p^3 implies B_p^(0)=0 mod p, because its other valuation ports are multiples of p. These are exact prior inputs, not a new proof of CM0 or the B supercongruence. The three carries themselves remain unproved for all target primes.

## New executed source-level certificate

The companion executed, reusable standard-library Python script
research_notes/portable_direct/d25_onhour_tier01_signed_bridge_20261029.py
uses the *different original* A and B coefficient recurrences modulo p^4, keeps each n, v_p, signed weight, and stratum separate, and recomputes every original A/B stratum by a second direct integer binomial route at p=5,7,11,13,19,31,373.

Actual stdout: PASS_EXACT_ORIGINAL_TIER01_FIRST_CARRY, all 237 primes 5<=p<1500. Of these, 60 are frozen target classes (31 of 13 mod 24, 29 of 19 mod 24). In all 237 finite cases both C_0,C_1 are divisible by p, Carry 1, Carry 2 and Carry 3 pass. **In all 60 frozen-class samples both L_0 and L_1 are individually nonzero modulo p**: the first p-adic digit cancels only when the separate valuation-zero and valuation-one sources are composed. This refutes the tempting stronger proposal that either low port vanishes individually modulo p^2 (already p=13 is an exact counterexample). The 237-prime finite check does not prove a universal fourth-digit bridge.

| p | C0 mod p4 | C1 mod p4 | L0 mod p | L1 mod p | (C0+C1)/p2 mod p2 | Q mod p2 | D mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 15522 | 364 | 11 | 2 | 94 | 166 | 6 |
| 19 | 61503 | 24415 | 7 | 12 | 238 | 294 | 10 |
| 373 | 17219030260 | 14763248615 | 21 | 352 | 90746 | 33463 | 40 |

At p=373, p^2=139129 and p^3=51895117, and the *distinct* source values are

$$L_0=46163620=21\pmod{373},\qquad L_1=39579755=352=-21\pmod{373}.$$

Their composite is J=L_0+L_1=33848258=373*90746 modulo 373^3; then 90746+33463=124209=373*333, and finally 333+40=373. The three successive carries all close at their exact declared precision while the individual sources remain nonzero.

At p=13 the chain is (L0+L1)/13=94; 94+166=13*20; 20+6=2*13. At p=19 it is 238; 238+294=19*28; 28+10=2*19. All are executed finite integer certificates, not all-prime proofs.

Script Git blob sha1: 38df31730c39c62590a0b49863abf994053680a8 (matches the executed local file). All denominators inverted are explicit p-units; no floating-point or alternate native definition is involved.

## BRC and research obligations

BRC: COMPOSE_APPLIED. The carrier is (A/B original source, exact index, unweighted coefficient valuation, original signed weight, precision, future observer, operation order). The aggregate C^(01) is sufficient for the final scalar observer but loses the **nonzero first-carry source labels**. This new witness distinguishes a genuine cross-tier transfer from erroneous per-tier zero claims, narrowing finite WZ/CM proof construction directly at the unfinished tier-0/tier-1 level. It makes no native X6 or physical Frobenius assertion.

Next exact mathematical obligation: prove Carry 1 for the **original** tier-0 and tier-1 signed streams using a finite hypergeometric transformation, WZ or CM character certificate; then prove Carry 2 and Carry 3 using already proved Q,D first jets. The weaker frozen target A_p-B_p=0 mod p^3 on p=13,19 mod 24 remains open and follows if the stronger p^4 bridge is proved together with the external B theorem.

Independent native benchmark #1559: same-original-class p373 divided-power H0/B0 [X]U mod139129, module rank, actual semilinear Frobenius/eta, odd signed Green/Hesse, kappa, Delta-R and independent acceptance remain PENDING_OWNER/NOT_EXECUTED in the current evidence. This portable scalar source ledger does not fulfill that benchmark. Site status on 2026-10-29 reports research_authority_granted=false and write_relay_enabled=false, and em_checkpoint_list returned ACCESS_DENIED; native session/CLAIM/open/Source checkpoint/Result and review are unverified. No previously rejected operation was reissued and no maintenance identity was borrowed. Preserve P000, ACTIVE worldview, frozen scientific pin and the existing task schedule/notification configuration.
