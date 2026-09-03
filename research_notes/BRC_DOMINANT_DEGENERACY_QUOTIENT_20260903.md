# BRC Dominant-Degeneracy Quotient of the Universal Histogram

Status: `RESEARCH CANDIDATE / EXACT FINITE POSITIVE HISTOGRAM / NOT YET FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-BRCFB-93C7D1`
Parent: `BRC_PRIME_VALUATION_UNIVERSAL_TRANSFER_20260903.md`

## 1. Motivation

The universal positive-rational histogram carrier

\[
H=\sum_qc_q[q]\in\mathbb N[\mathbb Q_{>0}^{\times}]
\]

contains strictly more information than CWM. One particularly small extra coordinate survives tropical/max collapse: the multiplicity of the largest-weight branch.

Leading-term semirings, tropical multiplicities and layered tropical structures are classical/general mathematics. No generic novelty claim is made. The BRC value is the exact interpretation of equal-branch `ln k` as the leading multiplicity term of the general histogram moment asymptotic.

## 2. Leading pair

For a nonzero histogram define

\[
M(H)=\max\{q:c_q>0\},
\]

and

\[
\boxed{d(H)=c_{M(H)}}.
\]

Thus `d` is the number of alternatives tied for exact dominant weight.

For the zero histogram set

\[
(M,d)=(0,0).
\]

Define

\[
\boxed{\operatorname{Lead}(H)=(M(H),d(H)).}
\]

## 3. Leading-pair semiring

On pairs `(M,d)` with `M>0,d>=1` plus zero `(0,0)`, define recoalescence

\[
(M_1,d_1)\boxplus(M_2,d_2)
=
\begin{cases}
(M_1,d_1),&M_1>M_2,\\
(M_2,d_2),&M_2>M_1,\\
(M_1,d_1+d_2),&M_1=M_2,
\end{cases}
\]

and serial multiplication

\[
\boxed{
(M_1,d_1)\boxtimes(M_2,d_2)
=(M_1M_2,d_1d_2).
}
\]

Zero is absorbing for multiplication and neutral for `boxplus`; one is `(1,1)`.

### Candidate BRC-DG1

\[
\boxed{
\operatorname{Lead}(H\oplus K)
=\operatorname{Lead}(H)\boxplus\operatorname{Lead}(K)
}
\]

and

\[
\boxed{
\operatorname{Lead}(H\otimes K)
=\operatorname{Lead}(H)\boxtimes\operatorname{Lead}(K).
}
\]

Thus dominant weight plus dominant multiplicity is an exact semiring quotient of the universal histogram carrier.

Pure max-times is the further forgetful quotient `(M,d)->M`.

## 4. CWM does not determine dominant degeneracy

Consider the positive branch families

\[
A=\{1,1,1/4,1/4\},
\]

\[
B=\{1,1/2,1/2,1/2\}.
\]

Both have

\[
C=4,
\qquad
W=5/2,
\qquad
M=1,
\]

but

\[
d(A)=2,
\qquad
d(B)=1.
\]

Therefore

\[
\boxed{(C,W,M)\text{ is not complete for the leading pair }(M,d).}
\]

The universal histogram strictly refines CWM even if only first tropical correction data is desired.

## 5. Exact large-m moment asymptotic

For nonzero `H`, write

\[
\Phi_m(H)=\sum_qc_qq^m.
\]

Factor out the dominant weight:

\[
\frac{\Phi_m(H)}{M^m}
=d+
\sum_{q<M}c_q(q/M)^m.
\]

Every lower ratio satisfies `0<q/M<1`, hence

\[
\boxed{
\lim_{m\to\infty}\frac{\Phi_m(H)}{M^m}=d.
}
\]

Equivalently,

\[
\boxed{
\ln\Phi_m(H)
=m\ln M+\ln d+o(1).
}
\]

The logarithm is a derived readout; the exact core statement is the rational limit above.

## 6. Explicit finite error bound

If `H` has any subdominant support, let

\[
r=\max\{q/M:q<M,c_q>0\}<1
\]

and

\[
C_{<}=\sum_{q<M}c_q=C-d.
\]

Then for every integer `m>=0`,

\[
\boxed{
0\le
\frac{\Phi_m(H)}{M^m}-d
\le C_{<}r^m.
}
\]

So the dominant multiplicity is approached exponentially fast in moment order, with an exact rational rate `r`.

If all branches are dominant, `C_< =0` and the identity is exact at every m:

\[
\Phi_m=dM^m.
\]

## 7. `ln k` generalized

For `k` equal-weight branches, every branch is dominant:

\[
M=q,
\qquad d=k.
\]

Therefore

\[
\Phi_m=kq^m
\]

and

\[
\ln\Phi_m=m\ln q+\ln k.
\]

Thus the previously discovered equal-branch `ln k` has the general interpretation

\[
\boxed{\ln d=\text{dominant-degeneracy log surplus}.}
\]

When not all branches are dominant, the same `ln d` remains the exact subleading large-m term.

## 8. Path semantics

Because `Lead` is a semiring homomorphism, applying it entrywise to the universal histogram matrix commutes with path powers.

For every fixed length `n`, the leading pair of

\[
(\mathcal W^n)_{ij}
\]

is exactly:

- the largest positive rational weight among length-n paths `i->j`;
- the exact number of length-n paths attaining that largest weight.

Therefore one may compute dominant mass **and the number of strongest paths** without carrying the full histogram.

This is a strict refinement of the existing max-times/tropical path envelope.

## 9. Recurrent boundary

At fixed length, `(M_n,d_n)` is finite. Across all lengths, supported recurrence may produce unbounded path families, so no finite all-depth dominant-degeneracy scalar is asserted without a separately typed length/growth normalization.

The natural next recurrent questions include:

- exponential growth rate of `M_n`;
- exponential/polynomial growth of `d_n` among maximal paths;
- interaction between max-cycle degeneracy and total-mass instability.

Those are not promoted by this note.

## 10. Prior-art and boundary

Leading coefficients, tropical multiplicities/layers and large-power asymptotics are classical/general ideas.

Enterprise Math does not claim generic novelty.

The project-specific synthesis proposed here is the exact quotient chain

\[
\boxed{
\text{weight histogram}
\to(M,d)
\to M
}
\]

and the identification of the existing BRC `ln k` multiplicity surplus with the general dominant-degeneracy term `ln d`.

This quotient does not recover total mass, total count, lower-weight histogram support, signed provenance or semantic path labels.

## 11. Validation plan

1. Exhaust small positive histograms and verify the leading-pair addition/multiplication laws.
2. Verify CWM-collision witness A/B has equal `(C,W,M)` but different `d`.
3. Exhaust tested histograms for moments `m=0..12`; verify exact error bound and convergence toward `d` after division by `M^m`.
4. On an explicit weighted multigraph, compare leading-pair matrix powers with direct enumeration of maximum path weight and number of maximizers through lengths `0..6`.
5. Verify equal-weight branch families give exact `Phi_m=dM^m` for every tested m.
