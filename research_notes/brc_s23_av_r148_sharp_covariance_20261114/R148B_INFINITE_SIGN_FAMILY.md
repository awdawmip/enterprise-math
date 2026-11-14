# R148B — An infinite Sturmian family with alternating signed CRT covariance

**Date:** 2026-11-14 (Asia/Shanghai). **Frozen scientific input:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. **Scope:** external scalar S23 tied-phase integer-fiber observer. **Status:** author-side exact proof with finite rational checker; `NOT_REVIEWED`.

**Dependency:** R148 sharp covariance and equality theorem, same research directory `PROOF.md`. This result upgrades R148's length-14 positive witness to an explicit infinite family.

## Theorem R148B.1 (all integers r>=1)

Set `w_r = 0^r 1 0^r 1 0^r`, a word of length `m=3r+2`. Let `Gamma_{w_r}` be R147's full-period covariance between the two integer-phase residue components for this finite Sturmian word. Then

```
alpha_{w_r} = 1/(r+2),     beta_{w_r} = 3/(3r+2),
U_{w_r} = 2,              V_{w_r} = 0,
g_r = gcd(r+2,3r+2) = gcd(r+2,4),
```

and the **exact all-r sign law** is

```
                                  { 0,                         r odd,
Gamma_{w_r} =                     { 1/[4(r+2)(3r+2)],         r = 0 (mod 4),
                                  { -3/[4(r+2)(3r+2)],        r = 2 (mod 4).
```

Hence `w_{4k}`, `k>=1`, is an infinite family of valid finite Sturmian words with **positive covariance attaining R148's sharp positive upper bound**, at lengths `m=12k+2`. The family `w_{4k+2}`, `k>=0`, has negative covariance, and odd `r` produces coprime endpoints and zero covariance.

### Proof: exact slope-support and intercept endpoints

For any word `w` with prefix sums `s_j`, the strict free-intercept support endpoints are

```
alpha=max(0,max_{i<j}(s_j-s_i-1)/(j-i)),
beta=min(1,min_{i<j}(s_j-s_i+1)/(j-i)).
```

The word `w_r` has exactly two ones, at zero-indexed positions `r` and `2r+1`.

To maximize the lower slope constraint, a substring must contain both ones: substrings with 0 or 1 one have nonpositive lower bound. The shortest substring containing both ones has length `r+2`, giving `alpha=1/(r+2)`.

For the upper slope constraint, group substrings by the number `k` of ones. Among substrings containing `k=0,1,2` ones, the maximum possible respective lengths are `r, 2r+1, 3r+2`. Consequently their smallest upper ratios are `1/r`, `2/(2r+1)`, `3/(3r+2)`. The last is strictly the smallest for every `r>=1`, so `beta=3/(3r+2)`. These reduced fractions satisfy `alpha<beta`, proving `w_r` is Sturmian for every `r>=1`.

At `alpha`, the upper-intercept envelope `u(alpha)=min_j(s_j+1-j alpha)` may be minimized separately over the three prefix-index blocks `0..r`, `r+1..2r+1`, and `2r+2..3r+2`. Their minima are `2/(r+2), 3/(r+2), 4/(r+2)`, so `U=(r+2)u(alpha)=2`.

At `beta`, the lower-intercept envelope `ell(beta)=max_j(s_j-j beta)` has block maxima `0, -1/(3r+2), -2/(3r+2)`, so `V=(3r+2)ell(beta)=0`.

### Proof: exact joint-residue covariance

R148.1 yields

```
Gamma_{w_r} = 1/(g*b*d) sum_{t=0}^{g-1}
    ( (t-2 mod g) - (g-1)/2 )
    ( (-3t mod g) - (g-1)/2 ),
b=r+2, d=3r+2.
```

The gcd reduces to `g=gcd(r+2,4)`. If `r` is odd, `g=1` and both centered residues vanish, hence `Gamma=0`.

If `r=0 (mod 4)`, then `g=2`, and `(t-2) mod 2 = t`, `(-3t) mod 2=t`; the two centered permutations align. The centered sum is `1/2`, so `Gamma=(1/2)/(2bd)=1/(4bd)`. Equivalently, the sharp positive congruences `a+c=4=0 (mod 2)`, `U+V=2=0 (mod 2)` hold.

If `r=2 (mod 4)`, then `g=4`. The centered residues are `x_t=(t-2) mod 4`, `z_t=t` for `t=0,1,2,3`. Their centered dot product is `-3`, hence `Gamma=-3/(4bd)`. This proves the claimed trichotomy for every positive integer `r`. QED.

## Exact verification

The companion `check_r148b.py` independently reconstructs every word `w_r`, its complete rational prefix-pair support and `U,V`, then computes the exact `g`-residue covariance. All **50 values `r=1,...,50`** match the theorem: 12 positive, 13 negative, 25 zero. Output marker: `R148B_INFINITE_SIGN_FAMILY_FINITE_RECHECK_PASS`. This is a finite implementation crosscheck of the general derivation.

## Next

This family establishes both covariance signs in an infinite set of real finite Sturmian words. Analyze the sign and extremal classes for general words by their Euclidean/Farey structure, and test whether this can improve the one-fiber-loss near the permanent-saturation threshold `E(m)`. The sharp covariance law remains a statement about multiplicity; word presence is still governed by R146's integer count.
