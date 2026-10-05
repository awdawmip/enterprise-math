# D25 root-free common-shift observer reduction

Status: INDEPENDENT_VERIFICATION_ONLY / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING

Authority read: enterprise-math main@09d35689b0460e3639837bb00b52d93f34a37098.
Canonical D25 owner/frontier is unchanged; this note does not claim a session, CLAIM, run, Result, review, admission, or ownership transfer.

## New strict reduction

Let

F_p(Z) = _2F_1(1/3,2/3;1;Z)_{p-1}

and define the common top-parameter tangent

S_p(Z) = (partial_a+partial_b) _2F_1(a,b;1;Z)_{p-1}|_{(1/3,2/3)} mod p.

Euler transformation at a+b=1 gives coefficientwise below degree p

S_p(Z) = trunc_{<p}((-log(1-Z)) F_p(Z)) mod p.

Equivalently, if c_k and h_k are the coefficients of F_p and S_p,

c_0=1, h_0=0,

c_{k+1}=c_k (k+1/3)(k+2/3)/(k+1)^2,

h_{k+1}=(h_k(k+1/3)(k+2/3)+c_k(2k+1))/(k+1)^2.

The second recurrence remains valid through the numerator zero and does not divide by a vanishing top Pochhammer factor.

For D25 put

Q(Z)=Z^2-Z+1/8,

whose roots are A_+=(2+s)/4 and A_-=(2-s)/4, s^2=2.

Reduce

S_p(Z) = sigma_0 + sigma_1 Z mod (p,Q).

Define the base-field observer

tau_p = sigma_0 + (5/8) sigma_1.

Then for

W_p=(1+2s)S_p(A_+)-(1-2s)S_p(A_-)

one has exactly

W_p/s = 4 tau_p.

The quotient observer also has a one-dimensional recurrence.  If r_0=1,
r_1=5/8 and r_{k+2}=r_{k+1}-r_k/8, then

tau_p = sum_{k=0}^{p-1} h_k r_k mod p.

Now let n=(p-1)/3 and

U_n(Z)=_2F_1(-n,1/3-n;1;Z).

Since -n=1/3-p/3 and 1/3-n=2/3-p/3,

U_n(Z)=F_p(Z)-(p/3)S_p(Z) mod p^2

coefficientwise.

On the already typed D25 supersingular lane p=13 or 19 mod24,

F_p(A_+)=F_p(A_-)=p beta_p mod p^2.

For the previously defined projective observer

Theta_p=((1+2s)U_n(A_+)-(1-2s)U_n(A_-))/p mod p,

the preceding identities give

Theta_p/s = 4 beta_p - (4/3) tau_p.

Therefore

Theta_p=0  iff  tau_p=3 beta_p.

Combining with the preceding exact coordinates also gives

q_n = 4 d_p + 4 tau_p mod p

and

q_n-12 beta_p-4d_p = 4(tau_p-3 beta_p).

Thus q_n, d_p, m_p and the explicit quadratic sheet are no longer needed by the minimal open direction observer.

## Evidence boundary

A standalone checker verified the new Taylor/quotient identities and the scalar recurrence.  On the unchanged 166 D25 target primes p<5000 it observes

tau_p = 3 beta_p.

This is finite regression only and is not promoted.

## Next exact action

Prove tau_p=3 beta_p through a finite-Euler / finite-log first-lift identity, equivalently a telescoping certificate for

p tau_p - 3 F_p(A_±) mod p^2.

Do not reopen q_n, d_p, m_p, low-jet isogeny work, or the canonical owner's normalized companion/Lcomp_p unless a proof step genuinely requires them.
