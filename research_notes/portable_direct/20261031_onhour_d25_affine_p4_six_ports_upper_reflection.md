# D25: six exact p-adic ports and a reflected fourth-order upper-tail theorem

**2026-10-31; AUTHOR-SIDE / PROVED ELEMENTARY PORT THEOREM / FINITELY EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**

Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **unchanged scientific source pin** c47e13e4aba0e006366f989d6334d443f6333ae3. These are classical arithmetic coefficient/valuation observers, not native X6/H0/B0/Frobenius computations. Research lane: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance).

## Exact statement

Let p>3 be prime, and define in Z_(p)

a_k=(2k)!(3k)!/(k!)^5 /216^k,   b_k=(4k)!/(k!)^4 /2304^k,  0<=k<p.

The **original** weighted full-cutoff sums are A_p=Σ(6k+1)a_k, B_p=Σ(8k+1)b_k. Their proposed fourth-order affine relation

A_p-2B_p+p χ_{-3}(p) = 0 (mod p^4)

**remains unproved**; the existing published Guo–Zudilin theorem concerns B_p mod p^3, not A_p.

**Theorem 1 (exact six source strata).** For all 0<=k<p,

v_p(a_k)=floor(2k/p)+floor(3k/p),    v_p(b_k)=floor(4k/p).

Consequently, over the six half-open integer bands
I_0=[0,p/4), I_1=[p/4,p/3), I_2=[p/3,p/2),
I_3=[p/2,2p/3), I_4=[2p/3,3p/4), I_5=[3p/4,p),

the pair (v_p(a_k),v_p(b_k)) is respectively

(0,0), (0,1), (1,1), (2,2), (3,2), (3,3).

The endpoints are rational thresholds interpreted by inequalities on *integer* k. The weights 6k+1 and 8k+1 may increase a particular term valuation, so these are valuations of the unweighted coefficients.

Define D_{r,p}=Σ_{k∈I_r} [(6k+1)a_k-2(8k+1)b_k]. Then

A_p-2B_p+pχ = pχ + Σ_{r=0}^5 D_{r,p}

exactly in Z_(p), preserving all distinct original source ports.

**Theorem 2 (universal explicit highest port).** Put m=floor(p/4) and define sequences in F_p:

P_0=Q_0=1,

P_{j+1}=P_j 36(j+1)^3 /((2j+3)(3j+4)(3j+5)),

Q_{j+1}=Q_j 288(j+1)^3 /((2j+3)(4j+5)(4j+7)),

for 0<=j<m-1. All denominators are p-units within this index range. Then

D_{5,p} ≡ p^3 U_p (mod p^4),

U_p = Σ_{j=0}^{m-1} [ (5+6j)P_j - 2(7+8j)Q_j ] (mod p).

In particular, for every p>3,

a_{p-1}/p^3 ≡ b_{p-1}/p^3 ≡ -1 (mod p),

and the **single k=p−1 original weighted affine term**, divided by p^3, equals -9 modulo p. Thus a termwise high-tail deletion cannot be justified from p^4 precision alone.

An equivalent rational-hypergeometric normalization is

P_j=2^j (j!)^3 /[(3/2)_j(4/3)_j(5/3)_j],

Q_j=9^j (j!)^3 /[(3/2)_j(5/4)_j(7/4)_j],

where Pochhammer denominators are interpreted in F_p and are units on j<m.

## Proof

The first theorem follows by Legendre's factorial valuation, since k<p, 2k<2p, 3k<3p and 4k<4p: v_p((tk)!)=floor(tk/p) for t=2,3,4. Collect threshold crossings at 1/4,1/3,1/2,2/3,3/4.

For the terminal coefficient, Wilson's (p-1)!≡-1 (mod p) and Fermat 216^(p-1)≡2304^(p-1)≡1 give

(2p-2)!/p ≡ (p-1)!(p-2)! ≡ -1,

(3p-3)!/p^2 ≡ 2((p-1)!)^2 (p-3)! ≡ -1,

(4p-4)!/p^3 ≡ 6((p-1)!)^3 (p-4)! ≡ -1 (mod p).

The inverses (p-2)!≡1, (p-3)!≡-1/2 and (p-4)!≡1/6 yield a_{p-1}/p^3≡-1 and b_{p-1}/p^3≡-1. These congruences are legitimate because both original terminal coefficients have *exact* valuation 3.

For j=0,...,m-2, invert the **exact** hypergeometric term ratios

a_{k+1}/a_k = (2k+1)(3k+1)(3k+2)/[36(k+1)^3],

b_{k+1}/b_k = (4k+1)(2k+1)(4k+3)/[288(k+1)^3],

at k=p-2-j, reducing only p-units. This gives

(a_{p-2-j}/p^3)/(a_{p-1-j}/p^3)
 ≡ 36(j+1)^3/[(2j+3)(3j+5)(3j+4)],

(b_{p-2-j}/p^3)/(b_{p-1-j}/p^3)
 ≡ 288(j+1)^3/[(4j+7)(2j+3)(4j+5)] (mod p).

The denominators are nonzero: for 0<=j<m-1 their positive factors are <p. Hence a_{p-1-j}/p^3≡-P_j and b_{p-1-j}/p^3≡-Q_j. Also I_5 consists precisely of k=p-1-j for 0<=j<m. Since 6k+1≡-5-6j and 8k+1≡-7-8j, substitution and summation gives U_p as stated. The rising-factorial formulas follow by collecting 36/(2·3·3)=2 and 288/(2·4·4)=9 in the recurrences. QED.

## Exact witnesses and non-droppable ports

At p=13, the six values D_{r,13} modulo 13^4=28561 are, in order,

8085, 3771, 4017, 1521, 2366, 8788.

**Every one is nonzero modulo p^4**. Their sum is -13 modulo p^4, hence this one *finite input* obeys the affine p^4 relation, but omitting any one band without an explicit compensating transformation destroys that identity. The upper port alone is 8788=4·13^3. At p=19 and p=373 the upper port ratios D_5/p^3 (mod p) are 15 and 225, respectively (both nonzero). The topmost individual term always contributes -9·p^3 modulo p^4.

A fully independent standard-library integer verifier, d25_affine_upper_tail_port_20261031.py, was executed on **all 194 primes 5<=p<=1200**. For every k<p it checked the two *exact* unweighted valuations using modular recurrences, the terminal seed congruences, and the reflected closed formula against six separate full-cutoff source ports. For p=5,7,11,13,19,37,67,373 it additionally compared the upper port against direct integer-binomial definitions; all assertions passed. This is a finite code regression of the universal *proved* port theorem, not a verification of the unproved all-prime affine bridge. Independent native H0/B0 benchmark NOT_EXECUTED.

## Reduction and live obligation

The affine p^4 conjecture is **equivalent**, for every prime p>3, to the exactly typed lower-port condition

pχ_{-3}(p)+Σ_{r=0}^4 D_{r,p} ≡ -p^3 U_p (mod p^4).

A future finite WZ/CM/q-microscopic proof can target five lower ports with this *explicit* nonzero upper boundary; it cannot quietly set the entire highest band to zero modulo p^4. This is a boundary-corrected reduction, **not** a proof of the parent supercongruence. The weaker p^3 bridge A_p-B_p≡0 and the exact native p=373 H0/B0 run remain open and distinct.

Control source: existing own-lane recovery awdawmip/kimi-query-bridge#6632 confirms no Source claim; original dispatch request #6633 (research-onhour-20261031-0205-dispatch-r15) FAILED UPSTREAM_CODE_REVIEW_REQUIRED. Do not replay; this author-side note is not a canonical checkpoint/Result/independent review. Native support awdawmip/enterprise-math#1559 remains PENDING_OWNER. Preserve original schedule, notification behavior, Source pin, P000/ACTIVE worldview and separation from chatgpt-hourly-enterprise-math-20260921.
