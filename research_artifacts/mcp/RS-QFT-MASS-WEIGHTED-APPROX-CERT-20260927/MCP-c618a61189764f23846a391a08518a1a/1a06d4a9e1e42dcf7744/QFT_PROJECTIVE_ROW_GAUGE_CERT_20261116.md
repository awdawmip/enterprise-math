# Projective row-gauge invariance and a charged certificate baseline for native QFT single-walker sampling
Date: 2026-11-16. Task: RS-QFT-MASS-WEIGHTED-APPROX-CERT-20260927 (TP2-96E6EEEAE62D04B03180).
Status: scoped author-side exact derivation; no independent review, no completion of the task's low-cost approximate oracle target.
Frozen sources: enterprise-math@86022c1ee4de09a9c9055f4c6806a5d35459edfc, qft_row_queries/point_queries/MASS_WEIGHTED_APPROXIMATION_BOUND.md and qft_row_queries/README.md.

## Theorem: positive public row gauge
Let the full raw native row v_h(w) and an independently fixed, trajectory-consistent approximate row u_h(w) share the work/residual carrier and the source's single-walker proposal (a fair choice between W and P_i W). Let each positive scalar c_h be determined publicly by the prefix h, not by the sampled latent W, and fixed across repeated (h,w) queries. Define u'_h(w)=c_h u_h(w). The entire approximate joint output law, including all future history bits and latent labels, is IDENTICAL whether the single-walker uses u or u'.

Proof. At each h,z the source's two arms (x,y) from u are replaced by (c_h x,c_h y); linearity of T_h gives the second identity. Therefore S'=c_h² S and
||c_h x+c_h y||²/(2S')=||x+y||²/(2S)
when S>0. If S=0, both versions invoke the same fair fallback. The latent successor is z in both and their proposal coins and P_i are unchanged. Thus the conditional transition kernels coincide at every state; induction over all remaining steps proves equality of complete terminal joint distributions. No noncommuting feedback is reordered. QED.

## Gauge-adapted error certificate
For an arbitrary publicly specified positive gauge c_h, write E_h^(c)=sum_w ||v_h(w)-c_h u_h(w)||² on the COMPLETE work/residual carrier, and for a publicly specified bad set B_i let beta_i bound the true exact mass sum_{h in B_i} M_h. If epsilon_i^(c) is a verified upper bound on sum_{h outside B_i} E_h^(c), the frozen mass-weighted theorem applied to u'=c u yields

TV(final(v),final(u)) <= min(1, sum_i [beta_i+sqrt(epsilon_i^(c))]).

The equality of approximate sampler laws is exact. The bound retains the source's hypotheses, including full raw rows, fixed public/independent seed and all precision/failure accounting. The scalar optimization is optional; certifying its aggregate error remains an independent obligation.

## Exact nonzero-feedback control family
For EVERY native instance (including the source's N=21, a=2, t=4 ordered nonzero-residual/feedback example), take the fixed deterministic wrapper u_h(w)=v_h(w)/2 at all prefixes and labels. The public certificate c_h=2 yields E_h^(c)=0 for all h,w, hence beta_i=0, epsilon_i^(c)=0 and terminal TV=0 exactly, with zero work-label/history enumeration FOR CERTIFICATE ALGEBRA. By the source's instrument normalization sum_h M_h=1 at every depth, the original un-gauged aggregate row error is exactly sum_h E_h=1/4 and its sqrt bound gives t/2, capped by 1. This distinguishes a genuine sampler-equivalent gauge perturbation from amplitude discrepancy. The feedback remains that of the original native program; no classical replacement for exact row values is asserted.

## Full cost and limits
The wrapper c_h=2 costs constant-size exact rational data, one multiply/divide per queried raw amplitude/component, and O(t) explicit depth/certificate entries; exact structural verification checks the deterministic wrapper identity and the existing source normalization/linearity argument. Its underlying v_h(w) evaluation, residual association, initial program representation, integer bit lengths, precision, and queried-label schedule are UNCHANGED from the frozen exact oracle and must all be charged. No general cheaper approximate oracle or factor/order computation is obtained. For any proposed non-wrapper u, even finding/verifying good public c_h and the full epsilon_i^(c) may require exhaustive work: this theorem supplies no free certification shortcut.

## Discriminating continuation
Search for an independently computable orbit/character/recurrence certificate of projective row agreement or bounded gauge-corrected error on a native nonzero-feedback infinite subfamily, with source-verified exact inputs, including generation, verification, big-int, failure/precision and query costs; otherwise record a matching oracle/query lower bound with explicit model. Preserve this gauge lemma as a scoped local result, without upgrading the full QFT task to solved.
