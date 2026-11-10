# PREFIX-678-R6 — Optimizing the certified slot interval for the frozen BRC diagonal-edge crossing

Date: 2026-11-11 Asia/Shanghai. Status: AUTHOR_DERIVED / EXACT_FRACTION_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Predecessors: PREFIX-676 exact 189-level diagonal-edge threshold (cd2c6681a6ed4857bb7d416e82a8642f6cc0739f); point jets (d344451396a9bace91a9cbcdb14475c6641a9223); PREFIX-677 full proof and exact certificate (b1cda0db8097c4addac67899ecfe32dc7aa1446e).
Observer probabilities p,z are typed scalar outputs of the frozen Heartbeat World X6 BRC path model; no change to P000, science pin or formal task Owner.

## New theorem

Put b=53/1000, rho=1/330000000, and I=[b-rho,b+rho]. For the frozen two independent first-stop clocks, let V_q(p,z)=q² Var[max(Y_p,Y_z)] - q E[max(Y_p,Y_z)] for real 12<=q<=24.
Let A(z)=Var[max(Y_z,Y_z)]-Var[max(Y_0,Y_z)], B(z)=E[max(Y_z,Y_z)]-E[max(Y_0,Y_z)], q0(z)=B(z)/A(z), and R(z)=B'(z)A(z)-B(z)A'(z).

For every z in I:
- A(z)>439/1000 and A(z)<442/1000;
- R(z)>6500, and consequently q0'(z)>33000;
- 1789/100<q0(z)<449/25.

For every **real** q in the explicit rational interval
[1794869/100000, 1794888/100000] = [17.94869,17.94888],
there is **exactly one** z_q in I such that V_q(z_q,z_q)=V_q(0,z_q).
Within I, the diagonal wins for z<z_q, and the edge wins for z>z_q.
The certified q interval's width is 190/11 (>17) times the fixed rational q interval in PREFIX-677.

## Proof and parameter tradeoff

From the exact 189-layer predecessor at b:
11/25<A(b)<441/1000, 789/100<B(b)<79/10,
-1681<A'(b)<-1680, 128<B'(b)<129,
17948788665/10^9 < q0(b) < 17948788666/10^9.
These imply R(b)>332788/25.

The uniform survivor Bernstein bounds from PREFIX-677, based on original finite moment kernels, give |A''|<=A2=281945567232 and |B''|<=B2=133031808 for all z in [0,1/2].
For the present rho define
dA=1681 rho+(A2/2)rho², dB=129 rho+(B2/2)rho²,
Amin=11/25-dA, Amax=441/1000+dA, Bmin=789/100-dB, Bmax=79/10+dB.
Taylor's theorem supplies these bounds throughout I.

Because R'=B''A-BA'', and A,B stay strictly positive on I,
|R'|<=L=B2*Amax+A2*Bmax.
Exact integer/Fraction arithmetic certifies
R(z)>332788/25-L rho
= 533060940984960033988583/81237792968750000000 >6500.
It also verifies Amin>439/1000, Amax<442/1000,
Bmin>(1789/100)Amax and Bmax<(449/25)Amin.
Therefore q0'(z)=R(z)/A(z)² >6500/(442/1000)²>33000.
Strictly increasing q0(I) contains
[q0(b)-33000 rho, q0(b)+33000 rho].
Using the rational bounds on q0(b),
17948788666/10^9 -33000 rho <1794869/10^5
<1794888/10^5 <17948788665/10^9+33000 rho.
Hence all real q in the stated fixed q-band are in the interior of q0(I).
The intermediate-value theorem and injectivity give exactly one z_q.
Finally V_q(z,z)-V_q(0,z)=q A(z)(q-q0(z)), which supplies the sign orientation. QED.

The improvement comes from optimizing the *slot window* rather than the *z radius*: the larger z radius of PREFIX-677 gave R>200, while the narrower current radius preserves R>6500, producing much stronger uniform q sensitivity. This is a quantitative local result for the frozen observer, not an asserted global maximum in the full p,z domain.

## Exact verification and next unit

PREFIX678_R6_SLOT_BAND_OPT_CERTIFICATE.py uses only integers and Fraction, checks all displayed universal-bound implications, interval inclusion, and the exact width ratio 190/11; its JSON companion records exact rational budgets. The center jets are reused from immutable predecessor evidence; the 189-level recurrence was not repeated. Independent review and project theorem admission remain open.

Next: replace coarse global A2,B2 budgets by signed local Bernstein or exact second-order jets, build larger connected z and q coverage, establish uniqueness or additional roots on the full (13/250,27/500) diagonal-edge crossing bracket, and connect the sign-correct split to full 2D variance pruning against PREFIX-675's complete boundary maximum.
