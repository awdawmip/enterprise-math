# Gauge-compatible chart transitions and the active/passive separation

Status: PROVED_CONDITIONAL_FINITE_CLASSIFICATION / NOT_NATIVE_ENDPOINT_GLUE.
Date: 2026-09-05.

Terminology correction to RESEARCH.md: xD_v is a LEFT coset, namely the orbit under right multiplication by local D_v. H w in H\G_dev is a RIGHT coset. The formulas are unchanged.

## 1. Complete transition classification

For a chart change u->v, require gamma_uv in the accepted S4 label action, gamma_uv(u)=v and the shared edge {u,v} fixed. Then gamma_uv(v)=u. If w,z are the remaining vertices, there are exactly two possibilities: (uv) and (uv)(wz). Reverse change is the inverse, so the six edges have 2^6 assignments.

S4-conjugation covariance forces a uniform choice of conjugacy type because S4 is edge-transitive. Thus there are exactly two equivariant assignments: all single swaps or all double swaps.

If the ADDITIONAL selector is flat passive transport, gamma_vw gamma_uv=gamma_uw, only the double swaps remain. This is unique even without covariance: a triangle with an odd number of single swaps has odd product, not identity; a triangle with two single swaps would equate their three-cycle product with the remaining double swap, impossible. Thus every triangle has zero single swaps. Every edge belongs to a triangle. Existence follows since the identity and three double swaps form the Klein group V4. All single swaps around u->v->w->u give (vw), not identity.

Flatness here is explicitly a coordinate-transport choice. It is not derived as a physical law from PF.

## 2. A real passive atlas for the developed packet state

Write a framed description as (u,xi), xi in X_dev. Define reframe to v by (v,rho_gamma_uv(xi)). Fix a reference chart o and decode by rho_gamma_uo(xi). The flat identity proves path independence, roundtrip, gauge invariance and a common FCC readout after expressing coordinates in the reference frame.

A shared positive event t_uv becomes t_vu under this FULL frame change, both of local gauge 1. This is different from imposing the fixed-frame identity t_uv=t_vu^-1, whose gauges are 1 and sqrt(2). Its FCC vector rotates by R_gamma_uv rather than being forcibly compared in two incompatible fixed coordinate systems. No two previously distinct X_dev packets are identified by this coordinate construction.

## 3. Exact V4 loss when passive and active operations are confused

Consider simultaneous relabeling (u,xi)->(gu,rho_g xi). After passive-coordinate quotient and reference decode its action is rho_pi(g), with pi(g)=gamma_(go,o) g in Stab(o). Put b_v=gamma_ov. V4 is regular on the four chart labels and S4=V4 semidirect Stab(o), so g=b_(go) s uniquely. The displayed pi takes exactly the s component; hence its kernel is V4 and its image is S3. It is NOT the original faithful active S4 action.

The API therefore has three different methods:
- reframe: passive coordinate change;
- relabel_chart_and_coordinates: simultaneous atlas relabeling (quotient kernel V4);
- active_rotate: decode the actual candidate packet, apply its original rho_g, encode back.

In chart u with reference o, active_rotate has coordinate action rho_(gamma_ou g gamma_uo). It obeys the complete S4 group law and commutes with passive reframe. Its kernel on X_dev is trivial. This separation prevents treating lost rotation information as a new physical conclusion.

## 4. Nonuniqueness survives local gauge constraints

As a control, G_com=product_v D_v is the abelianization of G_dev. It retains each local factor injectively, the S4 action and the point-valued FCC homomorphism. L_com=sum_v ell_v is a positive subadditive directed gauge with exactly the prescribed local restrictions. Different-chart events commute in G_com but not in G_dev. Therefore the ideal local-action class plus local gauges, label rotations and carrier readout still does not select the actual cross-chart return law H. This is not a proposal to infer spatial dimension from the product's rank.

## 5. Executed checks and scope

Run python check_chart_transport.py after the primary and reference scripts.
The exact checker exhausts all64 edge assignments (2 covariant, 1 flat), all4096 six-vertex chart walks,1600 frame roundtrips,1600 observer compatibilities,1600 gauge compatibilities,100 active/reframe squares,576 active group products, and the exact4-element joint-relabel kernel versus the trivial active kernel.

These are finite self-checks supporting the general arguments above. No external review, Lean or repository-CI certificate is claimed. The native shared-axis orbit law and channel-coverage theorem remain separate requirements.
