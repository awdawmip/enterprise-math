# Exact 45-term logarithm refinement: sharp uniform alpha floor certificates to index 47,981,775,566,332,592

Date: 2026-11-09 (Asia/Shanghai). Status: **AUTHOR_SIDE EXACT ANALYTIC/NUMBER-THEORETIC PROOF** with locally executed `Fraction` verification; independent review pending. Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This is an arithmetic preflight for the S23/AV *auxiliary* observer, not new N(h) capacity or native X6 theorem.

## Setup

Put `r=ln7/ln(10/7)` and `alpha=(2074774-380295*r)/(79*r-431)`. The determinant identity `79*2074774-380295*431=1` gives `d(alpha)/dr=-1/(79*r-431)^2<0`.

For `0<z<1`, the series `ln((1+z)/(1-z))=2*sum_{m>=0} z^(2m+1)/(2m+1)` has strict rational truncation bounds after 45 terms: let `S_z=2*sum_{m=0}^{44}z^(2m+1)/(2m+1)` and `E_z=2*z^91/(91*(1-z^2))`; then `S_z<ln((1+z)/(1-z))<S_z+E_z`.

Set `(a,b)=(S_(1/3),S_(1/3)+E_(1/3))`, `(c,d)=(S_(1/9),S_(1/9)+E_(1/9))`, and `(e,f)=(S_(1/15),S_(1/15)+E_(1/15))`. The identities `ln7=3ln2-ln(8/7)` and `ln(10/7)=ln(5/4)+ln(8/7)` give strict rational bounds

```
r_-=(3a-f)/(d+f) < r < r_+=(3b-e)/(c+e).
alpha_-=(2074774-380295*r_+)/(79*r_+-431)
alpha_+=(2074774-380295*r_-)/(79*r_--431).
```

The `Fraction` verifier proves `0<alpha_-<alpha<alpha_+<1` by positive denominators and exact inequalities.

## Exact theorem

The **first denominator at which this precise 45-term interval can straddle an integer floor** is

```
q=47,981,775,566,332,593;
p=28,098,009,034,709,137.
```

For all integers `1<=i<=47,981,775,566,332,592`, one has

```
floor(i*alpha_-)=floor(i*alpha_+)=floor(i*alpha).
```

At the sharp first uncertified index q,

```
floor(q*alpha_-)=28,098,009,034,709,136,
floor(q*alpha_+)=28,098,009,034,709,137.
```

This is an **uncertainty of the stated finite rational enclosure** at q, not proof that the exact `floor(q*alpha)` is wrong or unknowable.

In particular the earlier coarse 26-decimal-digit interval's first ambiguity at `i=36,493,923` is **resolved** by this refined interval:

```
floor(36493923*alpha)=21370751.
```

## Short exact Farey proof of optimality

Choose reduced Farey neighbors

```
L=23,798,916,978,108,300 / 40,640,398,818,107,773
R=4,299,092,056,600,837 / 7,341,376,748,224,820 .
```

Their determinant `bc-ad` is exactly 1. Exact integer cross multiplication against the rational logarithm enclosures verifies

```
L < alpha_- < (a+c)/(b+d)=p/q < alpha_+ < R.
```

For Farey neighbors `a/b<c/d` with determinant 1, any rational `m/n` strictly between them satisfies `n=d*(bm-an)+b*(cn-dm)>=b+d`; both parenthesized integers are positive. Here `b+d=q`.

If for an `i<q` the two floors differed, an integer `m` with `i*alpha_-<m<=i*alpha_+` would define a rational `m/i` strictly in `(L,R)` with denominator `i<q`, a contradiction. This proves equality of all floors for every index below q **without enumerating indices**. At q the mediant `p/q` lies strictly between the alpha bounds; the direct exact checks `floor(q*alpha_-)=p-1` and `floor(q*alpha_+)=p` establish sharpness for the given enclosure.

## Scientific meaning and limits

This is a large exact uniform numerical-meaning certificate for the slope's integer observer, which avoids a per-index rational-floor bracketing check in any future certified checker using the refined bounds. It does not prove all critical cells are covered, establish the global S23/AV capacity formula, or solve the six-source/ten-label observation bridge. Binary bit-complexity of the rational fractions and further proof obligations remain explicit. The original published checker continues to use its own coarse bounds and is **not silently modified** by this research note.

The BRC residual is the narrow undecided integer-floor branch at the first q of a chosen interval: refinement resolves the old residual at `36,493,923` while exposing a later one. No source branch, provenance, X6 coordinate, or joint observation is projected away. Independent review/admission pending.

Sources: frozen scientific pin above; exact 45-term arithmetic from the existing `research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py` Git blob `261d7e22da0e62d667009cb50acfe77ac4e35c3f`; preceding coarse Farey proof in `research_notes/brc_s23_av_alpha_floor_farey_cert_20261109_research1/PROOF.md` at `dfb7286f50e454df339e848d4b550961a59bf79e`.
