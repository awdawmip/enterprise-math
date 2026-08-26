# Native filament post-audit hyperbola/Joukowski closure — direct adversarial replication

Status: `DIRECT_NONBLIND_ADVERSARIAL_REPLICATION / NO_INDEPENDENCE_ATTESTATION / PRE-INDEPENDENT-RETURN`

Date: `2026-08-25`

Researcher-ID: `EM-FREE-NEPS-239A6D`

This note does **not** replace blind replication PR #637. The author has already read PR #627. Its purpose is to attack the statement-only #637 packet for hidden hypotheses, sign errors, finite-field exceptions, or counterexamples while the independent return remains reserved.

## Verdict

`DIRECT_ADVERSARIAL_VERDICT = NO_COUNTEREXAMPLE_FOUND / STATEMENTS SURVIVE AT PACKET STRENGTH`.

No new narrowing was found beyond hypotheses already present in the #637 packet.

## H1 — split-hyperbola bridge

For

`Q_i(x)=x^2/(2B)-d_i`,

its tangent at `x=-Bu` is

`T_(i,u): y=-u x-Bu^2/2-d_i`.

Two same-family tangents at `u!=v` intersect at

`x=-B(u+v)/2`,

`y=Buv/2-d_i`.

Substitution into the opposite-family tangent at `w` gives exactly

`B(w-u)(w-v)=2(d_i-d_(1-i))=C_i`.

The negative Legendre dual is

`-Q_i^*(p)=-Bp^2/2-d_i`.

Equality of one value from the two dual images gives

`B(y^2-x^2)=C_i`.

Because char K !=2,

`Phi(x,y)=(y-x,y+x)`

is invertible and carries this equation to

`Bab=C_i`.

Thus H1a--H1c survive exactly.

## H2 — sign quotient

Over F_q, q odd and BC!=0, the map Phi identifies

`R={(x,y):B(y^2-x^2)=C}`

with `ab=C/B`, hence

`|R|=q-1`.

A common dual value determines `x^2`, and the defining equation then determines `y^2`; therefore two representations yield the same common value iff they differ by independent sign changes. Hence the common-value set is exactly `R/K4`.

Burnside gives

`|R/K4|=[q+1+(BC/q)+(-BC/q)]/4`.

The orbit-capacity argument is independent of the character formula: if universal breaking means one quotient orbit, then

`q-1=|R|<=|K4|=4`,

so `q<=5`.

Direct enumeration for the native B=3, C=+-1 cases:

- q=5: |R|=4, quotient=1, orbit sizes `[4]`;
- q=7: |R|=6, quotient=2, orbit sizes `[2,4]`;
- q=13: |R|=12, quotient=4, orbit sizes `[2,2,4,4]`;
- q=53: |R|=52, quotient=13, thirteen regular size-4 orbits.

No H2 exception was found.

## J1 — lane Joukowski map

For

`P_(s,j)(m)=2s m^2+2jm+1`,

with `m=a!=0`, the zero condition is equivalent to

`j=-sa-1/(2a)=Lambda_s(a)`.

The two roots of the quadratic for a fixed image value have product

`1/(2s)`,

so Lambda_s is the quotient of F_q^* by the involution

`a -> 1/(2s a)`.

The involution has

`1+(1/(2s)/q)`

fixed points. Therefore

`|Im Lambda_s|=(q+(1/(2s)/q))/2`.

A direct enumeration for every odd `3<=s<=15` and every prime `q<=101`, `q∤2s`, produced zero mismatches with this formula.

The saturation criterion is tautologically exact: every nonzero `a` hits an allowed lane iff `Lambda_s(a)` lies in the allowed lane set J_s; hence saturation iff `Im Lambda_s subseteq J_s`.

## J2 — extremal uniqueness reconstructed independently

### Upper boundary q=2s+1

Here `s=-1/2 mod q`, so

`Lambda_s(a)=(a-a^(-1))/2`.

For odd s, q=3 mod4, so `-1` is nonsquare; the involution has no fixed points and every image fiber has size 2. Saturation implies `Im Lambda_s=J_s` and therefore

`2 sum_(j in J_s) j^2 = sum_(a!=0) Lambda_s(a)^2 = -(q-1)/2=-s`.

Using

`sum_(j in J_s) j^2=s(s^2-1)/12`

gives

`s^2+5=0 mod q`.

Since `s=-1/2 mod q`, this implies

`q|21`.

With q=2s+1>=7 prime, `q=7`, hence `s=3`.

### Lower boundary q=2s-1

Now `s=1/2 mod q` and

`Lambda_s(a)=-(a+a^(-1))/2`.

The involution has fixed points `a=+-1`, whose singleton image values are `-1,+1`; all other image fibers have size 2. Saturation gives

`2 sum_(j in J_s) j^2 -2 = sum_(a!=0) Lambda_s(a)^2=(q-1)/2=s-1`.

Thus

`sum_(j in J_s) j^2=(s+1)/2`.

Substitution yields

`s^3-7s-6=0 mod q`.

Since `s=1/2 mod q`, this becomes

`q|75`.

With q=2s-1>=5 prime, only `q=5`, hence `s=3`.

### Active counterexample scan

For every odd `3<=s<=101` for which `2s-1` is prime, direct image enumeration found lower-bound saturation only at `(s,q)=(3,5)`.

For every odd `3<=s<=101` for which `2s+1` is prime, direct image enumeration found upper-bound saturation only at `(s,q)=(3,7)`.

No J2 counterexample was found.

## C1 — longitudinal/transverse closure

The two closure equations

`k_*-4=2s-1`,

`k_*-2=2s+1`

are equivalent to

`k_*=2s+3`.

With `k_*=2q_b-1`, one gets

`q_b=s+2`.

For nontrivial odd `s>=3`, this forces `q_b>=5`. The independently established orbit-capacity bound gives odd universal breaker `q_b<=5`; hence uniquely

`(s,q_b,k_*)=(3,5,9)`.

For odd window length k, direct enumeration of all mixed-parity triples confirms

`max |(w-u)(w-v)|=(k-2)(k-4)`

for k=5,7,9,11,13,15. In particular

`M_9=7*5=35`.

Thus

`3*M_9=105`,

`3*M_9+1=106=2*53`.

The statement is strictly a breaker-coprime/divisibility closure; no unrestricted prime-run conclusion was used.

## C2 — C3 bouquet coherence

For tri-sector shell `r=2m`, shell start is

`B_r=1+3r(r-1)/2=6m^2-3m+1`.

At side position `t=m`, the three cyclic slots give

- slot 0: `B_r+m=6m^2-2m+1`;
- slot 1: `B_r+2m+m=6m^2+1`;
- slot 2: `B_r+4m+m=6m^2+2m+1`.

Thus the C3 bouquet is exactly the slot-unfolding of the central filament, and its gate integer `3*5*7=105` equals the longitudinal closure integer `3*M_9`.

## Scope guards retained

1. H1 requires char !=2 and distinct shifts.
2. H2 requires `BC!=0`; the q<=5 breaker bound applies to the nonsingular translated-quadratic carrier.
3. J1 image formula requires odd q with `q∤2s`.
4. J2 is about extremal characteristics `q=2s+-1` that are prime and about the stated saturation notion.
5. `k_*=9` in C1 is breaker-coprime capacity, not by itself the separate native actual-prime island cap.
6. This note is not independence evidence for #637.

## Current disposition

`POSTAUDIT_CLOSURE_DIRECT_ADVERSARIAL_STATUS = SURVIVES`.

Promotion remains blocked on the reserved blind return from #637.