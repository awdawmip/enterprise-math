# D25/LIFT — source-selective Hasse-jet derivative sidecar ladder

2026-10-26. **Source-neutral author mathematics only.** Status: AUTHOR-PROVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_SOURCE_CHECKPOINT.

Frozen task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; mathematical source c47e13e4aba0e006366f989d6334d443f6333ae3 **unchanged**. Consume, do not recredit, the six-channel rank-6 and affine no-go theorems and the previously published scalar-shift safe quotient at research_notes/portable_direct/20261026_offphase_d25_six_hasse_scalar_shift_safe_quotient_source_neutral.md. This theorem covers a **new, restricted operator family**: factor-selective jet derivatives, not the authentic J/E WZ operator or native H0/B0.

## Formal labelled input

Let p=6m+1 >=13 be prime, S=Z_(p)/p^r for any r>=1. Represent the six free labelled Hasse source ports by

$$F(x,y)=a+bx+cy+dx^2+exy+fy^2,$$

with $(a,b,c,d,e,f)=(C_{02},C_{12},C_{03},C_{22},C_{13},C_{04})$. The low and residual-high formal-jet variables are separately typed. The earlier three-jet diagonal scalar observer is

$$M_2F=F(t,t)\bmod t^3=(a,b+c,d+e+f).$$

The labelled degree-two carrier is $E_2=S[x,y]/(x,y)^3$. It is not asserted that its arbitrary coefficient vectors all occur as a single genuine Hasse pair.

## Theorem A: sharp two-sidecar first-derivative budget

The degree-lowering formal derivative $D_x:E_2\to E_1=S[x,y]/(x,y)^2$ is well-defined, because the derivative of a cubic lies in $(x,y)^2$. The diagonal low-source derivative observation is

$$Q_x(F)=M_1(D_xF)=(b,2d+e).$$

The map $(M_2,Q_x):E_2\to S^3\oplus S^2$ is split-surjective, with exact kernel

$$\boxed{\ker(M_2,Q_x)=S(x-y)^2.}$$

Proof: the kernel of $M_2$ has the three free generators $x-y$, $x(x-y)$, $y(x-y)$. Their $Q_x$ images are $1$, $t$, $t$ respectively, so $Q_x(\ker M_2)=S\oplus St$ and two independent sidecars are **necessary and sufficient** to preserve both coefficients of $D_x$ in addition to the scalar three-jet. Solving both kernel equations gives $a=b=c=0,e=-2d,f=d$, proving the displayed equality. Reduction modulo p supplies the rank-two minimality lower bound.

The high-source derivative $Q_y=M_1 D_y=(c,e+2f)$ obeys

$$\boxed{Q_x+Q_y=(b+c,2d+2e+2f)=d(M_2F)/dt\bmod t^2.}$$

Thus $Q_y$ adds no further independent information after $M_2,Q_x$, but neither $Q_x$ nor $Q_y$ factors through $M_2$: $F=x-y$ has zero scalar jet yet $Q_xF=1$.

## Theorem B: third sidecar recovers every source label

The second low derivative at the origin gives $Q_{xx}=D_x^2F(0,0)=2d$. The six-output linear map

$$\boxed{O_2F=(a,b+c,d+e+f,b,2d+e,2d)}$$

has integer determinant $-2$, a unit in S. If its outputs are $(A_0,A_1,A_2,B_0,B_1,C)$, the exact inverse is

$$a=A_0,\quad b=B_0,\quad c=A_1-B_0,\quad
d=C/2,\quad e=B_1-C,\quad f=A_2-B_1+C/2.$$

Its complete recovery is universal for every p^r in scope. The one remaining kernel of $(M_2,Q_x)$ is detected by $Q_{xx}((x-y)^2)=2$. Therefore the **minimal free-source observer ladder** for the declared operations has ranks $3\to5\to6$. These ranks count formal provenance ports, **not spatial axes**.

## Theorem C: a cubic input is indispensable for a same-order derivative

Although $d/dt$ maps polynomials of degree at most two into degree at most one, it does **not** define a same-precision derivation on $S[t]/t^3$: $t^3=0$ in this quotient while $d(t^3)/dt=3t^2\ne0$ for p>3.

Indeed $F_0=0$ and $F_1=x^3$ have identical scalar input three-jets modulo $t^3$, yet the exact diagonally differentiated series differ by $3t^2$ modulo $t^3$. Thus obtaining the degree-two coefficient of a full-series derivative requires the cubic input degree (at least one extra scalar jet coefficient), not merely an existing three-jet. This does **not** equate the Ward rank-moment $n z^n$ with deformation-variable differentiation.

## Exact-check evidence and limitations

An actually executed Python-standard-library integer checker exhaustively enumerated all $5^6=15625$ six-port vectors over F5, giving 125 scalar fibres of size 125, 3125 joint scalar+first-derivative fibres of size 5, and 15625 distinct full observations. It checked explicit inverse and first/second derivative witnesses for 2048 deterministic vectors per modulus 25,169,733^3=393832837. All PASS. These tests are author-side finite regressions; the all-prime claims rely on the displayed proofs, not sample extrapolation. Code and JSON were generated in this conversation's local artifact storage; neither is represented as a native original-Hasse experiment.

BRC/进取坐标 use is COMPOSE_APPLIED to exact labelled source factors, prime-power valuations, future operations and observer-defined quotient. Source-sensitive derivation requires provenance sidecars; previous source-blind scalar multiplicative rank shifts still factor through the three-coordinate observer exactly. No native X6/three-dimensional slice transfer is claimed.

**Scientific next action:** derive the **actual** signed J/E $k-1/k-2$ operator from the frozen Hasse source. Check its effects on the three contrast generators $x-y,x(x-y),(x-y)^2$ for nonresonant p=13 and resonant p=733 before selecting minimal sidecars. Genuine Hasse constraints may shrink the realizable source module; original-class H0/B0, [X]U mod p², $\eta,\kappa$, infinity and independent high-high remain unverified. No D25/LIFT all-prime conclusion is inferred.

**Native status:** the direct 0.6.11 continuation read (request chatgpt-r6-20261026T1940-read-d25-continuation) returned CONTROL_QUOTA; Sites static_machine_readonly / write_relay_enabled=false. No new claim, open, session, Source checkpoint, Result, or mathematical admission. The missing UR V2 four-file bundle remains 94687 bytes with expected SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76; no matching original was recovered. CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS requires predecessor completed_units=[]; this author paper is not predecessor-certified progress. Resume by reading the actual subject's recovery_status and exact prior receipts, then canonical continuation and true ownership before any role-bound writer action.
