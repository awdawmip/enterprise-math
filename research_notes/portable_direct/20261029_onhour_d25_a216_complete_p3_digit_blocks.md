# D25 / SECOND-DIGIT-LIFT: complete p^3 digit-block lift for original A216, including all carry tiers

Date: 2026-10-29. Status: AUTHOR-SIDE / HAND PROOF / EXECUTED INTEGER CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. This is an external scalar auxiliary theorem, not the native H0/B0 experiment.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Research lane chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance. This extends (without re-attributing) the earlier supported-digit p^2 theorem in research_notes/portable_direct/20261029_onhour_d25_original216_weighted_p2_dwork_lift.md, retaining the original coefficient, sign, index and p-adic source information.

## Statement

Fix any prime p=6m+1 >= 7, any integer u>=0, and 0<=r<p. In Z_(p), let

a_n = binom(2n,n)^2 binom(3n,n) / 216^n,  w_n = (6n+1)a_n.

There are three distinguished numerator hits in the exact recurrence

a_(n+1)/a_n = [(n+1/2)(n+1/3)(n+2/3)]/[2(n+1)^3]:

j_1=2m for 1/3, j_2=3m for 1/2, j_3=4m for 2/3. Set

eta_r(u) = (3u+1)^[r>2m] (2u+1)^[r>3m] ((3u+2)/2)^[r>4m],
h_r = [r>2m]+[r>3m]+[r>4m].

Construct the multiset N_r of the 3r rational numbers j+1/2, j+1/3, j+2/3 for j=0,...,r-1. Remove each distinguished numerator hit p/3,p/2,2p/3 when its j occurs; call the remaining multiset N_r^*. Every member of N_r^* is a p-adic unit. Define the two unit harmonic ports

D_r = sum_(d in N_r^*) d^(-1) - 3 sum_(j=1)^r j^(-1),
E_r = sum_(d in N_r^*) d^(-2) - 3 sum_(j=1)^r j^(-2).

Let q=(216^(p-1)-1)/p be the actual *integer* Fermat quotient (use q modulo p^2 for p^3 predictions), d_r=D_r-q, and

J_r(u)=1+pu d_r+(p^2/2)[u^2(d_r^2-E_r)+u q^2].

**Exact universal congruences (all u and all base-p digits r, including nonunit hit branches):**

(1) a_(pu+r) = a_u a_r eta_r(u) J_r(u)  (mod p^3).

(2) w_(pu+r) = a_u a_r eta_r(u) {
 (6r+1) + pu[6+(6r+1)d_r]
 + p^2[(6r+1)/2 * (u^2(d_r^2-E_r)+u q^2)+6u^2 d_r]
} (mod p^3).

No division by a_u, a_r, eta_r, or any p-nonunit is made in these congruences. The u=0 case is exact as stated, and q, D, E are to be reduced at the precision forced by p^3.

## Complete proof

**Step 1, all-multiple binomial lemma.** For any p>=5 and integers A>=B>=0,

binom(Ap,Bp) = binom(A,B) (mod p^3).

Proof: H_2=sum_(j=1)^(p-1) 1/j^2=0 (mod p) by the nontrivial power-sum identity over F_p. Pairing j with p-j shows H_1=sum_(j=1)^(p-1) 1/j=0 (mod p^2). Every p-depleted factorial block is therefore

prod_(j=1)^(p-1)(sp+j)
= (p-1)! {1+spH_1+(s^2p^2/2)(H_1^2-H_2)}
= (p-1)! (mod p^3).

Write (np)! = p^n n! prod_(0<=s<n) prod_(1<=j<p)(sp+j), and cancel p-depleted factorial units. This proves the binomial lemma for arbitrary A,B, without assuming binom(A,B) is a unit.

Applied to original binom(2pu,pu)^2 binom(3pu,pu), the lemma gives

a_(pu) = a_u (1+pq)^(-u)
= a_u [1-puq+(p^2/2)u(u+1)q^2] (mod p^3).

**Step 2, exact hit factors.** Multiply the original coefficient recurrence from n=pu to n=pu+r-1. For every numerator p-unit d=j+c the ratio of the pu+j factor to the j factor is (1+pu/d); the denominator provides (1+pu/(j+1))^-3. At j=2m,3m,4m the exact ratios are 3u+1,2u+1,(3u+2)/2, respectively. Thus the following is an exact rational factorization, before modular reduction:

a_(pu+r)/a_(pu)
 = a_r eta_r(u) prod_(d in N_r^*)(1+pu/d)
   prod_(j=1)^r(1+pu/j)^(-3).

The two unit products expand, by elementary symmetric sums or the truncated formal logarithm, to

1+puD_r+(p^2u^2/2)(D_r^2-E_r) (mod p^3).

Multiply by Step 1's base factor, collect terms and complete the square to obtain exactly (1). Finally multiply by the *original* signed weight 6(pu+r)+1 = (6r+1)+6pu. The cross term 6p^2 u^2 d_r gives (2); it cannot be deleted.

## Proven filtration and use boundary

For a digit 0<=r<p, v_p(a_r)=h_r, with exact four-tier breakdown:

- 0<=r<=2m: h=0; keep the constant, p and p^2 terms of J.
- 2m<r<=3m: h=1; only the constant and p terms survive mod p^3.
- 3m<r<=4m: h=2; only the constant survives mod p^3.
- 4m<r<p: h=3; the whole digit block vanishes mod p^3.

This is an exact branch-sensitive compression relative to the declared mod-p^3 observer. It preserves the original multiplicity of numerator hits. The theorem does not replace the original A216 cutoff n=p-1 with a p^2-length sum; any multi-digit/Frobenius application must preserve that separately.

## Executed independent integer certificates

The companion guard research_notes/portable_direct/d25_a216_p3_all_digit_lift_guard_20261029.py computes the LEFT side from the original integer-binomial expression, not from the right-hand harmonic formula. For all 18 primes p=1 (mod 6), 7<=p<180, u=0,1,2,3 and every 0<=r<p, it verified BOTH a and the original weighted w: **5904 exact congruence pairs**, distributed as tier counts (2016,972,972,1944). All passed.

At p=373 (modulus 373^3=51,895,117), 22 independently computed cross-tier cases for u=1,2 and r in {0,1,62,124,125,186,187,248,249,300,372} also passed. Selected independent observations with u=1:

| r | h | a_(373+r) mod p^3 | w_(373+r) mod p^3 |
|---:|---:|---:|---:|
| 124 | 0 | 15567268 | 42925846 |
| 125 | 1 | 50004753 | 6269757 |
| 187 | 2 | 9599901 | 38399604 |
| 249 | 3 | 0 | 0 |

These exact finite checks are implementation witnesses, not the universal proof's substitute.

## Next canonical scientific obligation and immutable frontier

Consume rather than re-prove: accepted D24 unit reciprocity; original A216 six-port identity; previously attributed frozen Theta_p reflection; prior p^2 supported-digit block; existing p^3 cutoff/source conservation. The new proved all-digit formula (1)-(2) may be reused in future multi-digit recurrences.

The frozen hard target is still, for every p=13 or 19 (mod 24),

T00+T01+T02+T10+T11 = p-p^2 Theta_p (mod p^3),

with the original p-1 cutoff, signs, exact observer, and frozen reflection scalar. Next mathematical proof should target first-five-port finite WZ/CM character-sum cancellation, not conflate it with any substituted multi-digit sum. No universal supercongruence acceptance claimed.

The native benchmark remains a separate highest-priority execution obligation: same-original-class p=373 H0/B0 divided-power [X]U mod139129, real module rank, semilinear Frobenius direction/basis eta, odd signed Green/Hesse, kappa and Delta_p-R_p with independent reproduction. Intake issue awdawmip/enterprise-math#1559 is an unassigned support path, not an executable native certificate.

As checked 2026-10-29, the connected Site was static_machine_readonly (Researcher authority false; write relay false), and its adapter job quota was 5/5. This author-side file is NOT an authenticated Source checkpoint, service Research-Activity, CLAIM, open run, Result, independent review or admitted theorem. The live Source owner/session/claim/run/request frontier remains unverified in this client; do not borrow maintenance's identity. P000 and frozen science source pin unchanged.
