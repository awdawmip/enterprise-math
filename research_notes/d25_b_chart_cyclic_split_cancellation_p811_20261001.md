# D25 portable research: cyclic split cancellation at p=811 and the four-wall residue criterion

Status: AUTHOR_PORTABLE_PROOF / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT

This unit continues the portable upper-B-chart lane only. It does not claim a native session, CLAIM, run, Result, review, or theorem admission.

## Source boundary

- GLOBAL_KNOWLEDGE_V1 canonical main for this execution phase: 60c40d00c0666c5bcf0a375ab8c095362bd42023.
- Enterprise Math canonical main for this execution phase: ff1e5a5862eba2eb7cd0c6d9159a7191aa2f8fec.
- P000 remains ACTIVE_LOCKED; current research position remains RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.
- Canonical D25 local-progress blob remains 51dd15a8142f3dda0506a306f9c0693a036f5891.
- Durable portable branch head before this attempted write: 60a4dddfb92f3a856cafd1d18b0fa7f5a8a382d4.
- Current recovery request for EM-DIRECT-C4D02C could not be created because the host blocked the GitHub mutation before Issue creation. The last independently read successful recovery remains Issue #2578: session_state=ABSENT, no pending/run/claim/upload/staging, execution_authorized=false.

## 1. Cyclic gauge recalled and rederived

Let

q(x)=32(3x+1)(6x+5)/(9(4x+1)(4x+3))
    =4 (x+1/3)(x+5/6)/((x+1/4)(x+3/4)),

K(x)=8(3x+1)(5616x^3+14208x^2+11449x+2927)
     /(135(x+1)(2x+1)(4x+1)(4x+3)).

For p>3, set
Q_0(x)=1,
Q_j(x)=prod_{i=0}^{j-1} q(x+i).

Because in F_p(x),
prod_{i=0}^{p-1}(x+i+a)=x^p-x
for every a in F_p, one has

Q_p(x)=4.

Therefore

S_p(x)=sum_{j=0}^{p-1} K(x+j)Q_j(x)

satisfies
q(x)S_p(x+1)-S_p(x)=3K(x),

and the unique cyclic rational splitting gauge is

R_p(x)=S_p(x)/3.

Uniqueness follows because a homogeneous solution H would satisfy
H(x)=Q_p(x)H(x+p)=4H(x), hence 3H=0.

## 2. Arithmetic observer and singular schedule

Now let p=6m+1 with p == 13 or 19 (mod 24), and inspect the arithmetic observer x=m.

The first q-pole encountered by j=0,1,... is at

a=floor(m/2),

and its exact characteristic-zero denominator equals p/4 at x=m.

The first q-zero is j=m, so Q_j carries that simple pole exactly for
j=a+1,...,m. The term j=a itself has a simple pole from K. Hence the whole first singular block is j=a,...,m and is centered at p/4.

The second q-pole is at

b=ceil(7m/2),

with exact denominator 3p/4. It is cancelled by the q-zero at j=4m. Hence the second singular block is j=b,...,4m and is centered at 3p/4.

The remaining K poles occur at
j=2m, with exact denominator p/2,
and
j=5m, with exact denominator p.

No other j gives a pole at x=m. Each term has at most a simple pole.

## 3. Four-wall residue identity

Write
tau_n=t_{2n},
Omega_n=sum_{r=1}^{2n} t_r (26/5+7/(3r)),

so that the already-derived exact transport law is

Omega_{n+1}-Omega_n=K(n)tau_n,

and Q_j(m)=tau_{m+j}/tau_m as an exact rational identity.

If a rational term F(m+eps) has its sole p-divisible denominator as
eps+c p, then

Res_{eps=0}(F mod p) == c * p * F(m)  (mod p).

Applying this termwise to the four singular walls gives

3 Res_{x=m} R_p(x)
==
(p/tau_m) * [
  (1/4)(Omega_{2m+1}-Omega_{floor(3m/2)})
 +(1/2)(Omega_{3m+1}-Omega_{3m})
 +(3/4)(Omega_{5m+1}-Omega_{ceil(9m/2)})
 +(Omega_{6m+1}-Omega_{6m})
]  (mod p).                                      (1)

The bracket is generally p-adically of valuation -1; the displayed product by p is integral. Since tau_m=t_{2m} == 1 (mod p), tau_m may be omitted after the valuation-safe multiplication by p.

Define the four-wall holonomy residue

H_p :=
p * [
  (1/4)(Omega_{2m+1}-Omega_{floor(3m/2)})
 +(1/2)(Omega_{3m+1}-Omega_{3m})
 +(3/4)(Omega_{5m+1}-Omega_{ceil(9m/2)})
 +(Omega_{6m+1}-Omega_{6m})
] mod p.

Then

Res_{x=m} R_p = H_p/3  (mod p).                 (2)

Consequently the unique cyclic gauge is observer-regular exactly when

H_p == 0 (mod p).                               (3)

This is the precise cancellation condition. It is a valuation-weighted four-wall holonomy of the same Omega/tau difference module, not a new unrelated scalar.

## 4. Exact cancellation prime p=811

Take

p=811, m=135, p == 19 (mod 24).

A direct finite-field Laurent recurrence gives the six nontrivial grouped residue contributions before the final factor 1/3:

- first q/K wall boundary: 20,
- first pole-band interior: 248,
- K wall at p/2: 543,
- second q/K wall boundary: 138,
- second pole-band interior: 398,
- K wall at p: 275.

Thus the four aggregated wall contributions are

W_(1/4)=268,
W_(1/2)=543,
W_(3/4)=536,
W_1=275,

and

268+543+536+275=1622=2*811 == 0 (mod 811).

Hence

boxed: Res_{x=135} R_811(x)=0.

Because every term in the cyclic sum has at most a simple pole at this observer, the vanishing residue removes the pole completely. Therefore R_811 is regular at the arithmetic observer.

This is an exact counterexample to the conjecture that observer-singularity persists for every target prime p == 13 or 19 (mod 24).

## 5. Finite scan / falsification evidence

A dependency-free modular scan evaluated the local Laurent residue by tracking only the valuation and leading coefficient of Q_j and K(x+j).

- target primes p<10000 with p == 13 or 19 (mod 24): 312;
- cancellation primes: exactly {811};
- target primes p<20000: 575;
- cancellation primes: again exactly {811}.

The scan is not the proof of (1)-(3). The proof is the singular-schedule and valuation-weighted telescoping argument above. The scan only establishes the stated finite search range and identifies the first cancellation witness.

## 6. BRC consequence

Previous p=13 and p=19 witnesses prove that finite-field cyclic algebraic splitting can be observer-singular.

The present p=811 witness proves that observer singularity is not uniform over the target prime family.

Therefore the correct BRC state is not the Boolean claim "finite-field split is always illegal". The retained datum is the wall-holonomy coordinate H_p with observer lease:

- H_p != 0: the unique cyclic gauge is singular at x=m, so Omega_m cannot be removed by an observer-regular state-linear cyclic quotient;
- H_p = 0: the mod-p cyclic gauge is regular at this observer, so that particular obstruction disappears and the next p-adic/operation-sensitive layer must be checked separately.

This does not prove a p^2 lift at p=811.

Reuse disposition: COMPOSE_APPLIED using the existing Omega/tau non-split difference module, BRC valuation retention, and operation-safe quotient discipline.

## 7. Next exact unit

Do not continue trying to prove uniform nonzero residue.

The next smallest unit is the exceptional-prime lift problem:
for p=811, compute the first p-adic lift of the regular cyclic gauge and decide whether a p-integral observer-regular splitting exists modulo p^2. In parallel, seek a closed arithmetic expression for H_p that may classify further cancellation primes without a full p-term cyclic scan.

Do not reopen Research1 normal-Dixon / double-pole work.
