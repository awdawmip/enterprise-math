# Independent exact-byte paper review of the shared Green kernel

Verdict: PASS for the explicit finite kernel and constant-term identities.
No new numerical or lifted calculation was performed. This is directed,
shared, nonblind review, with no formal DR acceptance or UR/LIFT completion.

Reviewed author memo SHARED_GAUSS_GREEN_KERNEL_NEXT_UNIT_PREPARATION.md,
3491B, SHA256 c900f291f9a45ef65bf77350f0009261377304e305c73e0a430ad80f043219d7,
Git blob 65e44bedfe5f0fc5a2b620c32d29d251b44af265.
I full-read its final bytes and independently checked the following algebra.
The reverse constructor and old target inputs remain those in the 11012B
author certificate, SHA256
4de6c2ae746acf9dad026c334b9aa2998d49e3147606fc35422be4d3901d8869,
independently reviewed in REVERSE_GAUSS_AND_FIXED_TARGET_INTERFACE_REVIEW.md,
SHA256 d48e893d7d2e6992cb6a1179191f51ef779cb056025f38bed1f9bd60db1a5d52.

Writing d_j=(2/3)_j(5/6)_j/(j!)^2, the displayed product quotient is

    prod_(a=j)^(r-2)(a+1)^2 / prod_(a=j)^(r-1)(a+2/3)(a+5/6)
    =d_j (r-1)!^2/[(2/3)_r(5/6)_r].

For r=j+1 its numerator product is empty, correctly equal to one.
Combining with -r_(r-1)=(-1)^r binom(3m,r)/9 and the exact D_r
formula gives

    c_j=d_j sum_(r=j+1)^(3m)(-1)^r binom(3m,r)2^(2-r)D_r.

Swapping finite sums proves the memo's full C(w) expansion, with the
partial K_(r-1) coefficients through exactly r-1. Every Pochhammer factor
is a unit for r<=3m: its first vanishing index corresponds to factor
j=4m or 5m, outside j<=3m-1. Extending D_r's formula to this range
therefore does not introduce a singular inverse or modify the old R_p,
whose original range is r<=i<=m.

For the old observer, (1+5z)/(1-z)^2 has coefficient 1+6j at z^j.
The constant term in B_m(z^(-1)) D_m(z) W(z) occurs precisely when
j=i-r>=0. D_m has no constant term, so i=0 contributes nothing. The
result is exactly sum_(i=1)^m B_i sum_(r=1)^i(1+6(i-r))D_r, giving
the source-fixed old R_p after the displayed factor two. The formal
power series can be truncated at degree m for this coefficient extraction;
no convergence assumption or analytic specialization is required.

The memo accurately distinguishes shared kernel from equality of the
two different observers. Its final target U=1+p[R_p-(3/2)C(1/2)M'(1/2)]
is the correctly signed independently fixed target, not a definition of R_p
from U. The remaining proposed adjoint/endpoints proof is substantive work
still to do; neither the kernel identity nor this review proves UR/LIFT.

Reviewer EM-ENTERPRISE-3F2857 supplied the original c0/reciprocal-kernel
observation. Author EM-ENTERPRISE-CB50ED extended it to the full C polynomial
and the constant-term observer; Root EM-DVR-4C90FB coordinates the direction.
Credit is shared as stated in the reviewed memo. No original frozen primary
or previous supplement bytes were changed for this review.

Researcher-ID: EM-ENTERPRISE-3F2857 / RS-ENTERPRISE-CM24-HESSE-INHOMOGENEOUS-P3-TRANSPORT
