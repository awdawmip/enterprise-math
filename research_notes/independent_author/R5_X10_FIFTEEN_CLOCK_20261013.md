# R5 independent author research: X10 fifteen-clock moving layer (2026-10-13)

Status: **INDEPENDENT_AUTHOR_DRAFT / EXACT_INTEGER_VERIFIED / CT_SYMBOLIC_LEMMA_UNREVIEWED / NO_FORMAL_CLAIM / NOT_ADMITTED**. This source note is not a canonical Task Result, Driver decision, Working Truth, or native six-dimensional Heartbeat World proof.

## Exact model and newly verified theorem candidate

For positive Weighted-BRC integer branch multiplicities set

```
F[x,y](z) = [X^x Y^y] product_(w=0..4) (1 - X*z^w - Y*z^(2*w))^(-1)
H(m;x,y;r) = sum_(n equiv r mod m) [z^n] F[x,y](z).
```

Choose x=10, m=2y+15 odd, y>=4; observer J=A_UW+2*A_VW modulo m. Then the author-level computer-assisted proof gives

```
H(m;10,y;0) - H(m;10,y;m-19) >= 40 > 0
asymptotic = 73*m^13/39721227496980480 + O(m^12).
```

Primality is not assumed. The difference is between observed buckets, **never** negative BRC path mass.

At m=23, y=4: exact total mass = 3063060, H_0=133179, H_(m-19)=133139, difference 40. The carrier is a formal five-clock ordered path model, not a native X6 implementation.

## Exact finite proof certificate and limits

Positive integer recurrence for each w in 0..4:
`new[a,b](z)=old[a,b](z)+z^w new[a-1,b](z)+z^(2w) new[a,b-1](z)`.
Thus every unwrapped polynomial has nonnegative integer coefficients. Mass identity:
`sum_r H_r = binom(y+14,4)*binom(y+10,10)`, and reflection `H_r=H_(-20-r mod m)`.

An independent 1001-multiset expansion of X^10 into 15 one-color Y clocks reproduces **every** histogram bucket at y=4,5,7,16,32. A distinct direct-occupancy coefficient expansion with weights `product_w binom(a_w+b_w,a_w)` reproduces all buckets at y=4,5,7. The unwrapped five-clock method checks all 204 exact histograms for y=0..203, 191 proof-critical integer equalities y=0..190, plus 13 held-out rows.

For each residue r=y mod12, let y0=r if r>=4 else r+12, and k=(y-y0)/12. The exact forward-difference finite certificate contains 14 strictly positive integer coefficients c[r,j] with `Delta(y)=sum_(j=0..13) c[r,j]*binom(k,j)`. All **168** coefficients were evaluated with integers. First coefficients by r=0..11:

```
r:  0     1     2      3      4  5   6     7    8    9     10    11
c0: 501703 339296 674361 2700990 40 165 7050 1973 5591 73769 33487 76747
```

All 12 top coefficients c[r,13] equal `10030594129920`; each row is strictly positive, min=40. The generating series candidate has denominator `(1-t^12)^14`. The author-level CT15 pole/degree lemma bounds the true numerator degree by 190: c=(ell*15-s-S(I))/2, |c|<=22, 15 clocks, finite t poles among 12th roots, order <=14, infinity growth <= t^|c|. The finite-certificate candidate has numerator degree <=171; equality of the first 191 coefficients then gives the all-y formula **conditional on the CT lemma**. Independently computed numerator's last nonzero term is degree 159, and coefficients 160..203 vanish; this does not replace the CT lemma. The lemma's pole analysis is provided in the author proof, but has not been independently audited.

## Reproduction / provenance / next unit

Local exact script: `verify_x10_moving_layer.py`; exact certificate: `x10_moving_exact_certificate.json` SHA256 `08f04ace79c5892c1b609fbec3f8a24b5e0896bc67a999c109f5cdd0860d8d59`. The independently generated local package is available to this conversation, but these files are **not** asserted to be Source-published by this note. Reproduce by applying the recurrence and independent occupancy/multiset algorithms; all integer inputs and the exact range are specified above.

Inherited verified author frontier: X6, X8 formal moving-layer proofs, not independently admitted. Global knowledge source snapshot `awdawmip/chatgpt-global-knowledge@298f0197ea59d0cd217945234a59684a2ad002cc`, Enterprise Math source snapshot `awdawmip/enterprise-math@4a194b8f5324c13a2840a25fd0c0fa1303dda455`; relevant P000, ACTIVE worldview, BRC histogram typing and portable research protocol were read. Native service identity/active-owner verification returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE`; no Researcher ID, native activity, formal Task claim, or independent review has been obtained. This independent author source branch does not make an owner-visible canonical record by itself.

Next research: X12, h=6, m=2y+17 odd >=23, y>=3. The inherited CT bound is numerator degree <=217 with denominator `(1-t^12)^16`; produce 12*16 Newton coefficients and 1820 positive multiset checks, find either a strictly positive certificate or a complete true nonpositive bucket-difference witness. Independently audit the generic CT lemma before mathematical admission.
