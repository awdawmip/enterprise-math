# OAI7-090-C — explicit Fourier-tail error for finite centered disks
Date: 2026-11-16. Author-side supplementary exact lemma; depends on the staged OAI7_090C_FINITE_RADIUS_GAUSSIAN_MIXTURE_TRANSFER_20261116.md and the same Fourier convention.

Let phi in C_c^infinity(R^2), 0<=phi<=1, phi=1 on B_1, supported in B_(1+d). Define H_phi=||Delta^2 phi||_(L^1), finite. For every a>0, the Fourier transform obeys
 |hat(phi)(u)| <= H_phi/(16*pi^4*|u|^4) for u!=0,
because hat(Delta^2 phi)(u)=16*pi^4*|u|^4*hat(phi)(u), and |hat(Delta^2 phi)(u)|<=H_phi. Polar coordinates give the exact integral
 int_(|u|>a) |u|^(-4) du = 2*pi*int_a^infty r^(-3)dr = pi/a^2.
Therefore the smooth disk-cutoff tail used by the centered-density comparison has the explicit bound
 Delta_R(epsilon,phi) <= H_phi/(16*pi^3*(R*epsilon)^2).             (A)
Let D_R = min(1, H_phi/(16*pi^3*(R*epsilon)^2)), and let m_f(epsilon)=min_(|xi|<=epsilon)hat(f)(xi)>=0. For ANY finite configuration C_R subset B_R with N>=1 and ANY real even Schwartz f with hat(f)>=0, the ordered off-diagonal energy satisfies
  (1/N)sum_(x!=y) f(x-y)
  >= [N/(pi*R^2*(1+d)^2)]*(1-D_R)^2*m_f(epsilon)-f(0).            (B)
The Gaussian k_alpha(z)=exp(-pi*alpha*|z|^2) can replace f in the left side whenever f<=k_alpha away from zero; nonnegative finite combinations can be summed as in the parent lemma.

Proof of (B): the parent note proves its exact inequality with q_R=(max(0,1-Delta_R))^2; (A), monotonicity of x->(max(0,1-x))^2 and D_R<=1 supply the claimed explicit lower bound. No data about translated disks or minimum separation is used.

This makes the Fourier-cutoff error O_phi((R*epsilon)^-2) at any fixed cutoff. The separate density discrepancy N/(pi*R^2)-1, frequency modulus hat(f)(0)-m_f(epsilon), and d-dependent window norm remain explicit and should be certified separately for any numerical application. This calculation is a quantitative extraction of the Fourier cutoff argument already present in the September 26 external manuscript; it is not a new proof of the sharp all-alpha auxiliary construction.
