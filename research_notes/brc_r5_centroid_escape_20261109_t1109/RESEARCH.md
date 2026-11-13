# R5: exact centroid of the four-dimensional Blackwell coupling polytope and mean atlas escape

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR_DERIVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.
Source: PR #1866, immutable 7a2c8c48873499a3c998d5587ff9dbf4b32a14c3; PR #1859, immutable f63a0250714f2445e8b406754b85f26d983ec3a6.
Frozen scientific pins retained: GK a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Current behavioral rules are separate.

## Problem and theorem

For positive real a,b,d, use the abstract 7-facet polytope Q(a,b,d) from PR #1866:

    s,t,u,v >= 0,
    13s+18t <= 23a,
    18u-13v <= 23b+13s,
    10v-5u <= 23d+5t.

For the fixed physically lawful marginals from PR #1859, Q is precisely the complete coupling polytope; for arbitrary positive a,b,d this is an abstract polyhedral extension.

Let V = Vol_4 Q in the declared (s,t,u,v) coordinates. Define its normalized Lebesgue centroid c_bar=(S,T,U,W)=V^{-1} integral_Q(s,t,u,v) ds dt du dv. Set

    P = 2125a^2 + 7200ab + 17640ad + 5400b^2
        +38880bd +25272d^2.

The complete exact centroid for EVERY positive real a,b,d is:

    S = 23a (965a^2 + 2700ab + 7650ad + 1800b^2
             +12960bd +8424d^2)/(13P).

    T = 23a (245a^2 + 900ab + 1860ad + 600b^2
             +4320bd +2808d^2)/(6P).

    U = (101425a^3 + 486000a^2b + 869850a^2d + 855000ab^2
         +3175200abd +2063880ad^2 + 531000b^3
         +3499200b^2d +4548960bd^2 +1971216d^3)/(90P).

    W = (116375a^3 + 486000a^2b +1511550a^2d +648000ab^2
         +4665600abd +6684120ad^2 +324000b^3
         +3499200b^2d +12597120bd^2 +8946288d^3)/(180P).

The volume is the verified predecessor formula V=12167 a^2 P / 90979200. All denominators are positive for a,b,d>0, and the centroid lies strictly inside Q. Its coordinates are rational functions of a,b,d, homogeneous of degree one.

## Direct proof (entire continuous parameter domain)

The base triangle has vertices (0,0), (23a/13,0), (0,23a/18). Above (s,t) set B=23b+13s and D=23d+5t. The fiber quadrilateral has vertices:

    (0,0),
    (B/18,0),
    ((10B+13D)/115,(5B+18D)/115),
    (0,D/10).

Triangulating this quadrilateral along its diagonal from the origin gives the fiber area and its *unnormalized* first moments:

    A(B,D) = (25B^2 + 180BD + 117D^2)/20700;
    Mu(B,D) = integral_fiber u du dv
            = (7375B^3 + 48600B^2D + 63180BD^2 + 27378D^3)/128547000;
    Mv(B,D) = integral_fiber v du dv
            = (250B^3 + 2700B^2D + 9720BD^2 + 6903D^3)/14283000.

Parametrize the base by s=(23a/13)x, t=(23a/18)y for x,y>=0, x+y<=1. Then B=23b+23ax and D=23d+(115a/18)y. Let J=(23a/13)(23a/18). The four first moments are exactly

    J*(23a/13) integral_triangle x A(B,D) dxdy;
    J*(23a/18) integral_triangle y A(B,D) dxdy;
    J*integral_triangle Mu(B,D) dxdy;
    J*integral_triangle Mv(B,D) dxdy.

Apply the polynomial simplex rule integral_triangle x^m y^n dxdy=m!n!/(m+n+2)! and divide by J integral_triangle A(B,D) dxdy. Expanding yields exactly S,T,U,W above. Since all integral identities are polynomial identities with rational coefficients, this proves the four formulas for every positive REAL parameter triple (not only sampled rationals). Strict centroid interior follows from Q having a nonempty interior and positivity of uniform Lebesgue density.

## The fixed physical Blackwell pair: exact mean escape cost

Use the exact frozen parameter values:

    a=3997/690000,
    b=170189123/37621284000,
    d=8294919533/677183112000.

The exact normalized centroid becomes

    S=2355585076519534536727043/652766585956905903520171875
    T=35502889966272874093017097/14461290519660684631831500000
    U=1464603788539721806976442485094641/90675386274443700028094716941000000
    W=181049273329192438370158704401311/7254030901955496002247577355280000.

The cost identity from PR #1859 is, on the ENTIRE fixed coupling polytope,

    epsilon_S(E)=225713944957/3385915560000
                 +(28/23)t +(5/23)u +(13/23)v.

Thus the *exact average escaped mass with respect to normalized four-dimensional Lebesgue measure on this Q* is

    688104890147354659193365423065427
    /7884816197777713045921279734000000
    = approximately 0.08726961705731236.

The exact minimum 225713944957/3385915560000 and maximum
8555233477/73606860000 from PR #1861 straddle this average strictly.

This average uses only uniform volume in the declared q-parameter coordinates; a different parameter measure can yield a different average. On the interior, all 17 permitted coupling edges are strictly positive; faces with fewer positive edges have zero four-dimensional Lebesgue measure. This gives a mathematically precise distinction between sparse extrema and typical coordinate-volume couplings for this fixed pair.

## Computational verification

VERIFY.py uses only Python standard-library Fraction. It reconstructs fiber area and first moments via an independent two-triangle calculation at exact test inputs, implements polynomial simplex integration with exact factorial weights, checks the 4D volume and four frozen centroid coordinates, and checks the exact averaged cost and its bounds. Its mathematical proof for all positive parameters is the coefficient-by-coefficient polynomial integration shown above, not the finite sample checks. EXACT_OUTPUT.txt is the actual execution text.

Next: turn the known support saturation Phi=0 into a variable-marginal perturbation family, derive new edge prices/support chambers, and test an open observer region for 13/14-edge certificates or a certified 15-edge lower-bound witness. Maintain the distinction between the frozen statistical observer model and native X6 spatial semantics. Formal owner/claim/review/admission require their own control receipts.
