# D25 — E3 signed quadratic Frobenius on all four inert residue classes

2026-11-11 Asia/Hong_Kong. **AUTHOR_SIDE DERIVATION / ALL-INERT ORIGINAL E3 GEOMETRY / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_H0B0**. Frozen task source `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`.

## The actual original curve and a sign-discriminating theorem

Take the original CM family `E_3(t): y²+xy+(t/27)y=x³` with `t=(2-T)/4, T²=2`. For p>3, p mod24 in {13,17,19,23}, the CM field `K=Q(sqrt(-6))` has `(-6/p)=-1` and the reduction is supersingular and nonsingular. Treat the two algebraic conjugate parameters (T and -T) as distinct inputs whenever 2 is a square modulo p.

**Claim (under standard CM reduction, and the previously derived nonsplit-2 original E3 case):** On each actual E3 branch over F_(p²), the quadratic geometric Frobenius is
\[
\pi_{p^2}=\left(\frac{-3}{p}\right)[p],\qquad
\#E_3(\mathbf F_{p^2})=\bigl(p-\left(\frac{-3}{p}\right)\bigr)^2.
\]
Equivalently: classes 13,19 have +[p] and counts (p−1)²; classes 17,23 have −[p] and counts (p+1)².

**Proof split by original coefficient field.**
1. `p≡13,19 mod24`: (2/p)=−1 and p≡1 mod3. The parameter lies in F_(p²). Consume the previous author-side original E3 exact CM result (note `20261111_onhour_d25_original_E3_geometric_frobenius_signed_trace.md`): q-Frobenius in the CM centralizer is ±p, and original rational 3-torsion point P=(0,0) is fixed by q-F; as [p]P=P but [−p]P=−P, choose +p. This step inherits the prior CM endomorphism-field assumption and is not an independent review.
2. `p≡17,23 mod24`: (2/p)=+1 and p≡2 mod3. There are two separate parameters `t_±=(2∓sqrt2)/4∈F_p`. For each original elliptic curve E_3(t_±)/F_p, good inert CM reduction is supersingular. Therefore `a_p≡0 mod p`; the Hasse bound `|a_p|≤2sqrt(p)<p` (p≥17) forces `a_p=0`. Its p-Frobenius satisfies `π_p²−a_p π_p+[p]=0`, hence the geometric q-Frobenius `π_{p²}=π_p²=−[p]`. This proves the previously untreated two classes without assuming that an external Hesse candidate equals a native coefficient.
3. For both branches `(-3/p)=+1` at p≡1 mod3 and −1 at p≡2 mod3; the formula follows.

The original E3 geometric sign is thus a well-typed four-class **comparison invariant**. It agrees in sign with the independently *finite-tested* original scalar W216 law `W_p≡(-3/p)p mod p³` for 1,227 primes, but **the equality of signs does not supply the missing H0/B0-to-scalar operator map or an all-prime W216 supercongruence**. The native benchmark and κ/η remain unresolved.

## Actual independent finite point-count check on the newly covered branch

For each p in {17,23,41,47,89,113,137,167}, compute every root T of `T²=2` in Fp. Each branch has `a3=(2−T)/(108)∈Fp`. The original Weierstrass discriminant for fixed x is `D(x)=(x+a3)²+4x³`. Exact count:
\[
\#E_3(\mathbf F_p)=p+1+\sum_{x\in\mathbf F_p}\left(\frac{D(x)}p\right).
\]
The two T branches were enumerated for each p by integer squares and exact Euler quadratic character. Both branches give #E(Fp)=p+1, so a_p=0, in all **16 original branch checks**. Their implied q counts are: p17:324; 23:576; 41:1764; 47:2304; 89:8100; 113:12996; 137:19044; 167:28224. Representative T roots: p17 (6,11), p23 (5,18), p41 (17,24), p47 (7,40). No numerical approximations.

Self-contained reproducer:

```python
ps=[17,23,41,47,89,113,137,167]
for p in ps:
    roots=[T for T in range(p) if T*T%p==2]
    assert len(roots)==2
    for T in roots:
        a3=((2-T)*pow(108,-1,p))%p
        s=0
        for x in range(p):
            d=((x+a3)**2+4*x**3)%p
            s+=0 if d==0 else (1 if pow(d,(p-1)//2,p)==1 else -1)
        assert p+1+s==p+1,(p,T,s)
    print(p, "branches", roots, "q-count", (p+1)**2)
```

**BRC/observer:** original conjugate branches retained at p17/23 and checked separately; only then aggregate the separately certified Frobenius sign. The p-adic W216 moment and geometric E3 Frobenius remain distinct observers. `BRC_REUSE_RESOLUTION=COMPOSE_APPLIED`.

**Source/lane/recovery:** author-side Research logical ID `chatgpt-research-onhour-enterprise-math-20260923`; maintenance lane not used. Previous native exact continuation and session-start requests `onhour11-20261111-0959-exact-cont` and `onhour11-20261111-1000-onhour-researcher-start` remain for original-receipt reconciliation; this note is not a Source checkpoint or accepted Result. The original [support issue #1559](https://github.com/awdawmip/enterprise-math/issues/1559) asks the native evaluator to run `[X]U mod139129`, obtain actual rank, semilinear F and basis η, odd signed κ, the original Δ−R port, and independent replication before an authenticated comparison to this geometric invariant. No additional scheduler, duplicate Issue or borrowed execution identity.
