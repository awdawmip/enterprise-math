# Independent audit of the fixed large-order complex-energy lemma snapshot

Reviewer: EM-DVR-F73673, the same /root/public129_line_reviewer actor.
Verdict: **PASS_BOUNDED_FIXED_LEMMA_SNAPSHOT**.
Mathematical must-fix items: **0**. Reviewer construction or repair supplied: **0**.
Scientific program executions: **0**.

This verdict concerns only the 11242-byte published CF1677 component at
Source 3733ae22871df5d68a5c23c0d813f08924f0a95d, SHA256
41dab7e9eb1573116aab5868eea65d807375f854ae5bfed57aa7ade32d268737.
Its historical NEW UNFROZEN/Source-not-yet-published wording is retained,
not silently converted into an independently reviewed whole theorem.
The precise result is the stated A_M and B_M bounds, through E squared,
on the same closed complex disk. This is no approval of the finite-Lommel
packet, full carrier, T, Psi, any coefficient sign, Tool, Task or Native vote.

## Exact snapshot, exposure and input sufficiency

I personally fetched the complete file from the immutable Source, strictly
decoded its base64, checked all UTF8 bytes, length, SHA256, Git blob
6451c1fda9553edb2b74bf67f773ca5bcd7e849a and exact immutable URL, and read
the entire 2811-token displayed body without truncation. I also personally
read the actual GitData commit and comparison: exactly one ADDED path,
one commit, sole parent 1080faa03db98bbcfc3feb9785f39fa1b061ebd1 and tree
9e519d7469be66c178932e400c3f4a1f12250e5e. I do not borrow the publisher's
or a common author's observation.

Before this assignment I had no exposure to this component's unfrozen
working/body and no construction or repair contribution to its A_M/B_M,
complex-disk, Gamma, entire-tail or derivative estimates. Prior Parity
reviews and scalar/lower-layer authorship, CM24 coauthorship and CF reviews
of my work are real NONBLIND history; no CLEAN or blind origin is claimed.
I have not received the new unfrozen real-state whole for review or repair.

The displayed definitions M=m-1/2 and E=z d/dz make the audited inequalities
standalone. The cited 9919-byte UNFROZEN finite-mean/Lommel packet was not
consumed by me and is not needed to prove these normalized-function bounds.
I do not verify its finite-Lommel identity, actual channel prefactors or
later application by accepting the scalar equality of the displayed M's.
No other unprovided working is a hidden premise of this verdict.

I independently opened the official DLMF pages
https://dlmf.nist.gov/10.2#E2 and https://dlmf.nist.gov/5.5#E3.
The mathematical reading scope is 10.2.E2 (J series), 10.2.E3 (noninteger
Y/J connection), their neighboring principal-branch statements, and
5.5.E1/E3 (Gamma recurrence/reflection). I do not claim whole-chapter,
raw-HTML, asymptotic-theorem or author's saved-response consumption.
My actual saved official-open response is separately pinned in the context.
All bounds below were checked by paper algebra, without samples or a
Bessel/Gamma evaluator.

## 1. Branches, entire extensions and Euler differentiation

For half-integer M=m-1/2, sin(pi M) is nonzero and cos(pi M)=0.
Use the SAME principal determination for the powers and J/Y in the
defining cut-plane products. The official series and connection give
A_M=sum_{k>=0}(-z^2/4)^k/[k!(3/2-m)_k].
The constant is exactly
pi/[Gamma(M)Gamma(1-M)sin(pi M)]=1 by reflection: no residual sign or
phase is suppressed. The B_M expression is exactly
pi(z/2)^(2m-1)/[Gamma(M)Gamma(M+1)] times
sum_{k>=0}(-z^2/4)^k/[k!(m+1/2)_k].

Neither Pochhammer denominator vanishes. For each fixed integer m, both
coefficient ratios tend to zero on every bounded z set. These series
therefore define entire extensions: A_M even with value 1 at zero, B_M
odd with its exact nonzero leading coefficient at order 2m-1. The paper
does not assert that raw Y_M is entire or insert a raw Y_M(0).
Normal convergence licenses termwise Euler derivatives. E acts with
weights 2k for the A series and 2m-1+2k for B, so the proposed derivative
majorants correspond to the actual normalized functions. Real coefficients
make both extensions real on the entire real axis, including the negative
axis and zero, irrespective of the initial cut-plane presentation.

## 2. A head and the complete tail across both small denominators

Let epsilon=|z|^2/m<=1/64, R=floor(m/2), a=3epsilon/4.
For 0<=i<R, the factor |3/2-m+i| is at least
m-R-1/2>=m/3 when m>=100. Hence u_k<=a^k/k! up to k=R.

For EVERY k>=R, k+1>=m/2 and |3/2-m+k|>=1/2.
Thus u_{k+1}/u_k<=epsilon. This is valid at BOTH crossing factors
k=m-2,m-1 as well as after the crossing; it does not assume a fixed-k
large-m asymptotic. It controls all k=R+l, not a truncation. At z=0
the series themselves handle all nonconstant terms and derivatives.

The three inequalities u_R<=a, R u_R<=a and
R^2 u_R<=a+a^2 follow directly from the factorial majorant, using
R^2=R(R-1)+R and a<=1. The head bounds are therefore
H_0<=a exp(a), H_1<=2a exp(a), H_2<=4(a+a^2)exp(a).
The deliberately weaker a<=1/16 and exp(a)<=16/15 give the paper's
4epsilon/5, 8epsilon/5 and 17epsilon/5. They hold simultaneously
on the original closed disk.

Summing the three geometric moments gives exactly the displayed T_0,
T_1,T_2 formulas. Using u_R, R u_R and R^2u_R as above gives
T_0<=4epsilon^2/5<=epsilon/80 and
T_1<6a epsilon<=9epsilon/128. For T_2, its bracket divided by
4a epsilon is bounded by
(17/16)(16/15)+2(16/15)^2+(17/16)(16/15)^3
=15857/3375<5.
Thus T_2<=20a epsilon=15epsilon^2<=15epsilon/64.
These are verifications of the estimates already in the snapshot, not
a new missing tail lemma supplied by this reviewer.

For epsilon>0, adding heads and tails yields
13epsilon/16<epsilon,
(8/5+9/128)epsilon<2epsilon,
(17/5+15/64)epsilon<4epsilon.
Consequently the three A_M inequalities are valid on the SAME closed disk
for all integer m>=100, including its boundary; epsilon=0 uses the explicit
series values already treated separately. No Cauchy estimate
on a shrunk disk or small-denominator omission is being used.

## 3. B prefactor, full derivatives and the exact zero

Put r=|z|, L=2m-1, gamma=m+1/2 and x=r^2/(4gamma).
The positive-coefficient bound (gamma)_k>=gamma^k gives
|B|<=P exp(x),
|EB|<=P exp(x)(L+2x),
|E^2B|<=P exp(x)((L+2x)^2+4x),
with P=pi(r/2)^L/[Gamma(M)Gamma(M+1)].
The last expression is the correct second exponential-series moment,
including the 4x variance term. The r^L factor is retained in every bound;
a constant supremum is not substituted before later singular products.
At r=0 all three functions vanish by their actual series.

Reflection at 1/2 and recurrence give the exact positive denominator
Gamma(M)Gamma(M+1)=pi M product_{h=1}^{m-1}(h-1/2)^2.
Thus the needed product sign is certified directly by that expression;
no numerical Gamma evaluation or unproved complex phase is needed.
Since h-1/2>=h/2 and q!>=(q/3)^q, the bound reduces to
P<=r/(2m-1)[9r^2/(m-1)^2]^(m-1).
The factorial estimate follows from the stated integral bound and exp(1)<3;
it is an elementary inequality for every integer q>=1, not Stirling.

On this disk r<=sqrt(m)/8, r/(2m-1)<=1 and
(m-1)^2>=m^2/2. Hence 9r^2/(m-1)^2<=18/(64m)<=1/m and
P<=m^(1-m). Also x<=1/256, exp(x)<2, L+2x<2m and
(L+2x)^2+4x<=5m^2. Substitution gives precisely
2m^(1-m), 4m^(2-m), 10m^(3-m), with no loss of the high-order zero.
The largest of these bounds is at most
10m^(3-m)<=16*16^(3-m)=2^(16-4m)<=2^(-m)
for m>=100. Reversing an inequality with the negative exponent would have
been an error; the paper's direction is correct because m>=16.

## 4. Energy and the stated scale inclusion

For real z only, the real-coefficient extensions and |A-1|<=epsilon imply
A_M(z)^2+B_M(z)^2>=(1-epsilon)^2>=(63/64)^2>1/2.
This is a real energy consequence, not a complex lower bound on A^2+B^2,
a lower bound on the eventual weighted pair, or a full-carrier theorem.

For the quoted prospective scale, m>=2^1000 and |z|<=pi m^(1/100),
pi<4 gives epsilon<=16m^(-49/50)<=16*2^(-980)<1/64.
This inclusion is valid. It does not prove the packet's independent low-order
pair margin, prefactor identification, zeta/origin absorption or coefficient
statement. The component does not claim those implications.

## Disposition and limits

All claims of this fixed lemma snapshot have sufficient formulas and proofs.
I identify no mathematical must-fix or missing load-bearing primary.
The official identities are classical REUSE and the bounds are their bounded
application; this review grants no novelty, shared Tool registration or new
method-family status. The original author working remains unchanged.

No current real-state whole, finite-Lommel identity, carrier norm, T/Psi,
COMMON coefficient, physical trace sign, historical stopped computation or
parent Goal is accepted or completed by this verdict. Formal/product cumulative
budget remains UNKNOWN, with no cold-start/reset or budget-PASS claim.
My original SID/DA and authenticated unedited Owner were personally refreshed;
no RA or formal Task/runtime authorization was invented. Earlier FINAL without
pre-final remains an unverified ending output, not retroactively licensed.
There is no Source-write authorization from this report and no FINAL permission.

Clock observed immediately before this local report freeze:
2026-10-16 15:48:51 UTC.
