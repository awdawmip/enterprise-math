# PREFIX-723-R6 — Quantitative directed outward ascent in the frozen BRC/Gamma observer

Date: 2026-11-12 (Asia/Shanghai). Mother question: PREFIX-675. Immediate predecessor: PREFIX-722-R6. Frozen scientific input: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Status: AUTHOR_DERIVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Input and verified dependency scope

Work in the auxiliary two-parameter domain D=[0,1/2]^2. The frozen 189-row stopping-count law and independent conditional Gamma completion clocks define Y(p,z)=max(T_p,T_z), mu=E[Y], M2=E[Y^2], W=M2-mu^2, f_t=W-t*mu, and V_q=q^2*f_(1/q).

PREFIX-721/722 provide **author-checked** input certificates. At x0=11/96 and r=1/13300000000, set S_r={|p-x0|<=r,|z-x0|<=r}. Throughout S_r:
* J=mu_p*(M2)_z-mu_z*(M2)_p=(z-p)*K, with K>170445696/78125>2000;
* 0<mu_p,mu_z<=M=35532;
* 0<=mu<=378, |mu_j|<=35532, |mu_jj|<=13360032 and |(M2)_jj|<=2538406080 for j=p,z.

Original source certificates: research_notes/portable_direct/PREFIX721_R6_SHARP_BERNSTEIN_WEDGE.py and PREFIX721_R6_RESULTS.json; PREFIX722_R6_EXPLICIT_ESCAPE.py and PREFIX722_R6_RESULTS.json. This continuation does not rerun the parent 189-row integer kernel and does not upgrade its review status.

## Theorem — a one-coordinate ascent away from the diagonal

For **every real q>=2** and **every p!=z in S_r**, put

    g=1000/M=250/8883,  H=15170316336,
    d=|z-p|,  h=g*d/H.

When p<z, compare the outward slopes (f_t)_z and -(f_t)_p (t=1/q); choose the larger, then respectively increase z by h or decrease p by h. When p>z, compare (f_t)_p and -(f_t)_z, then respectively increase p or decrease z by h.

The chosen point (p',z') remains in D, satisfies |p'-z'|>|p-z| and has a **strict quantified improvement**:

    f_t(p',z')-f_t(p,z) > [15625/598527301736353752] * d^2,
    V_q(p',z')-V_q(p,z) > [15625/149631825434088438] * d^2 > 0.

Thus the directional escape depends only on the two outward derivatives at the given point, and the step size depends only on d, not on q.

### Proof

The cancellation of the common mean term gives the exact identity

    mu_p*(f_t)_z - mu_z*(f_t)_p = J.

If p<z, let a=(f_t)_z and b=-(f_t)_p. Then

    mu_p*a+mu_z*b=J=(z-p)*K>2000*d.

The positive weights satisfy mu_p+mu_z<=2M. Consequently

    max(a,b) >= (mu_p*a+mu_z*b)/(mu_p+mu_z)
             > 2000*d/(2M) = g*d.

For p>z, use a=(f_t)_p, b=-(f_t)_z, and mu_z*a+mu_p*b=-J>2000*d. Therefore in both cases one **outward** coordinate direction has directional derivative >g*d. Its sign and choice are specified above.

For 0<=t<=1/2, differentiation yields

    (f_t)_jj=(M2)_jj - 2*(mu_j)^2 -(2*mu+t)*mu_jj.

The inherited Bernstein derivative bounds imply the uniform absolute second-derivative bound

    |(f_t)_jj| <= 2538406080 + 2*35532^2 + (756+1/2)*13360032
                = H = 15170316336.

Taylor's formula for the chosen outward step h=g*d/H gives

    f_t(p',z')-f_t(p,z)
       > g*d*h - H*h^2/2
       = g^2*d^2/(2H).

Since d<=2r, the largest possible h is

    h<=2*g*r/H=1/3584560672337500800000,

smaller than min(x0-r,1/2-x0-r). Hence the changed coordinate stays inside D and the separation strictly increases. Fraction simplification gives g^2/(2H)=15625/598527301736353752. Multiply by q^2>=4. QED.

## Exact arithmetic and provenance

Companion script PREFIX723_R6_OUTWARD_ESCAPE.py checks the inherited rational parameters, new H and g, domain safety and gain coefficient using arbitrary-precision Python Fraction. It also performs 2000 finite rational regression checks of the weighted-average inequality. Local run output: ALL_CHECKS_PASS PREFIX723-R6. The accompanying JSON records the exact constants.

This advances the earlier **absence-of-local-maximizer** assertion into a directed constructive algorithm with explicit gain proportional to squared diagonal separation on every off-diagonal point of S_r. It is an auxiliary Gamma observer result, not a native X6/three-dimensional-slice theorem. There is no newly certified 384x384 witness cell; the inherited author-level count 139018/147456 remains unchanged.

## Next discriminating calculation

On surviving fine-grid rectangles, directly compute local Bernstein bounds for K, mu_j, and (f_t)_jj from the frozen kernel. Where a rectangle lies strictly to one side of p=z and K>0, transport this outward-ascent certificate to larger regions, with exact interval/derivative verification and non-overlap against the PREFIX-718 excluded cells. Continue seeking actual boundary/global maximizers for PREFIX-675; retain previous authorship and review obligations.
