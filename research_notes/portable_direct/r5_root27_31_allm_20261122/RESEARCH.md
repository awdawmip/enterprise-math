# R5: full-threshold nonzero first jets at primitive 27th and 31st roots

**2026-11-22; AUTHOR_PROOF / EXACT_INTEGER_CROSSCHECKED / NOT_REVIEWED.** Independent portable R5 mathematics. Frozen scalar model; not a native Heartbeat X6 result. Scientific parent: `f003690c912ffc1cd923c33176155a6fe82d69ba:research_notes/portable_direct/r5_root27_31_padic_firstjet_20261122/RESEARCH.md`; original true-event correction: `75d986aa23b68a7ecf9b29dc1006f0e322b35a15`. Preserve frozen inputs.

## Theorem

Let nonnegative multiplicities of prices 214,...,314 total N. Let f_m(N) count assignments satisfying at least one original event `E_i: sum_{p in S_i} a_p < m` for a **fixed positive integer m**, with
`S0=214..218`, `S1={214,216,217,218,219,220,221}`, `S2={215,216,217,218,219,220,221}`, `S3=223..290`, `S4=296..312`.
With `F_m(q)=R_m(q)/D(q)`, `D(q)=prod_{p=214}^{314}(1-q^p)`, **for every m>=1** the numerator has an exactly *simple zero* at every primitive 27th or 31st root. The denominator has four zeros, so F_m has a third-order pole at these roots. Consequently for the least period of the quasipolynomial coefficients modulo an `O_m(N)` remainder,

```
for all m>=1: 27 | M_m(O_m(N)), 31 | M_m(O_m(N)), hence 837 | M_m(O_m(N)).
```

This resolves the predecessor's remaining classes, and is a necessary period factor, not a complete minimal-period formula.

## Exact true-event derivative

For each nonempty mask I of the five events, U_I is the union of selected supports and P_{I,m}(q) is the **finite** enumeration satisfying every selected load separately. Exact inclusion-exclusion:
`R_m(q) = sum_{I != empty} (-1)^{|I|+1} P_{I,m}(q) prod_{p in U_I}(1-q^p)`.
At primitive d=27 (resp. 31), the only multiples of d among prices are `216,243,270,297` (resp. `217,248,279,310`). Every support has at least one. Supports S3 and all its supersets, plus mixed S4 masks, have at least two. So the derivative `D_q=q*d/dq` at a primitive root ζ only receives the seven nonempty masks on S0,S1,S2 plus singleton S4. Define p0=216/217, p4=297/310 by d, Q_I=prod_{p in U_I\{p0}}(1-ζ^p), Q4=prod_{p in S4\{p4}}(1-ζ^p). Every first-three mask has exactly one d-multiple.

Let X=ζ^214, Y=ζ^215, W=XY. Let
`J(t)=prod_{p=219}^{221}(1-t ζ^p)^(-1)`,
`U(t)=prod_{p=216}^{218}(1-t ζ^p)^(-1)`,
`H4(t)=prod_{p=296}^{312}(1-t ζ^p)^(-1)`.
The three actual threshold loads in the common coordinates x,y,j,u are
`L0=x+y+u`, `L1=x+j+u`, `L2=y+j+u`, where j sums 219..221 and u sums 216..218. For any selected first-three mask, let h be maximum of selected load expressions with u removed. The correct threshold sum over m>=h+u+1 supplies `t^(h+u)/(1-t)` (not a single union-load bound).

Put `B_Z(t)=J(Zt)/(1-Zt)+(J(t)-J(Zt))/(1-Z)`, Z∈{X,Y}, with well-defined 1-Z. The seven exact kernel functions:
```
A1 = 1/((1-Xt)(1-Yt))
A2 = J(t)/(1-Xt); A4 = J(t)/(1-Yt)
A3 = B_Y(t)/(1-Xt); A5 = B_X(t)/(1-Yt)
A6 = J(t)*[1/((1-Wt)(1-Xt)) + Yt/((1-Wt)(1-Yt))]
A7 = J(Wt²)/((1-Xt)(1-Yt))
   + [J(t)-J(Wt²)]/((1-Wt)(1-Yt))
   + Xt*[J(t)-J(Wt²)]/((1-Wt)(1-Xt)).
```
The triple formula partitions j<=x,y; x<j with x<=y; y<j with y<x (one-sided ties); maxima are respectively x+y, j+y, j+x. It respects every original selected inequality. Hence the exact rational identity
```
G_d(t) := sum_{m>=1} D_q R_m(ζ) t^(m-1)
 = [-p0 U(t)*sum_{I=1}^7 (-1)^(|I|+1) Q_I A_I(t) - p4 Q4 H4(t)]/(1-t).
```

## Pole order and universal recurrence

At d∈{27,31}, the prices 219,220,221 are distinct mod d, as are 216,217,218 and 296,...,312; hence each J,U,H4 pole in t is simple. X,Y,W are pairwise distinct and not any 219..221 root factor. In A7 a J(Wt²) pole cannot coincide with an Xt,Yt,Wt pole because it would require a J price congruent to -1,+1,or 429 modulo d, respectively; none occurs. Inspecting the formulas shows **each A_I has at most simple poles**. All poles are 2d-th roots of unity. G_d is proper at infinity, and every term has pole order at most three (A_I,U,1/(1-t)); S4 term at most two. Thus, exactly as rational functions:
```
G_d(t)=P_d(t)/(1-t^(2d))^3, degree(P_d)<6d.
a_{m+6d}-3a_{m+4d}+3a_{m+2d}-a_m=0  (all m>=1),
where a_m = D_q R_m(ζ).
```
In each phase r=1..T where T=2d, a_{r+kT} is a vector-valued polynomial in k of degree <=2.

## Exact finite proof certificate

The accompanying standard-library `VERIFY_ALLM.py` uses integer cyclic group ring Z[q]/(q^d-1), then the complete cyclotomic normal forms:
`Φ27=1+q^9+q^18` (18 coordinates), `Φ31=1+q+...+q^30` (30 coordinates). It expands the exact A_I series, producing a_m for 1..162 at d27 and 1..186 at d31, plus five extra terms each. For **every r=1..T** it checks the entire cyclotomic-vector identity `a_(r+2T)-2a_(r+T)+a_r=0`. Combined with the proved rational recurrence, this yields for every k>=0:
```
a_(r+kT) = a_r + k*(a_(r+T)-a_r).
```
For r=1..49 at d27 and r=1..57 at d31 the checker constructs an explicit nonzero integer 2x2 coordinate minor of (a_r,a_(r+T)), proving rational linear independence. For the remaining five phases (50..54 and 58..62), it verifies exactly `a_(r+T)=2*a_r` and a nonzero coordinate of a_r. Hence none of the above sequences can be zero for any integer k>=0. These are exhaustive **54/54 and 62/62 phase certificates**.

The first five full cyclotomic vector SHA256s at both roots match the previous saved `f003690c.../CERTIFICATE.json` (ten regression witnesses). A separate direct enumerator of the *original* simultaneous inequalities (without A_I rational kernels) matched full vectors at d27 m=1,2,3,5,8,9,27 and d31 m=1,2,3,5,27,30,31; for m=1 it also checked the complete original 31 masks. Integer arithmetic only; no floating-point or finite-window extrapolation for universality. Review remains `NOT_REVIEWED`.

**Interpretation:** vanishing zero-order cyclotomic readout can leave an exact nonzero first derivative jet; this is a typed residual observer, not an assumed positive-mass BRC/complex-sign identification or native X6 theorem.

**Next science:** complete other primitive-root orders and higher jets for O_m(N), check previous author-side minimal-period chain independently, then classify exact periods. **Control:** original native owner inventory request `r5-20261122-0640-owner-bounded-observe-v1` returned `FAILED / SOURCE_TREE_TRUNCATED`; no live owner or this session's authenticated Researcher binding was established. This independent GitHub return is not a formal CLAIM/RUN, Activity CAS, Result or Review.
