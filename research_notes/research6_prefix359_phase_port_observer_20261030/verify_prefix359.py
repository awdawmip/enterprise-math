"""PREFIX359: exact observer inequality certificate, conditional on PREFIX358 cubes."""
from fractions import Fraction as F

lo=F('0.0598990506977195435624')
hi=F('0.0598990506977195435625')
rad=F(1,10000)
eps=F(1,500000)
a=F('-0.717408911887365257')
b=F('-0.998209376262943823')
assert hi-lo==F(1,10**22) and lo-eps>0 and hi+eps<F(1,4)
# Source branches certified for all t in [lo-eps,hi+eps] by PREFIX358.
# Gauge-invariant coherent readout C=|y1+y3|^2;
# Theta=q3-3q1/4; C-Theta=2q1*(Re(v)+7/8).
delta_1=a-rad+F(7,8)
delta_2=-b-rad-F(7,8)
assert delta_1>F(3,20) and delta_2>F(3,25)
min_q1=F(34000,59536)  # strict lower bound because t>0
margin_1=2*min_q1*F(3,20)
margin_2=2*min_q1*F(3,25)
gap=2*min_q1*(a-b-2*rad)
assert margin_1==F(1275,7442) and margin_2==F(510,3721)
assert margin_1>F(1,8) and margin_2>F(1,8) and gap>F(3,10)
print('PASS_PREFIX359_EXACT_ROBUST_PHASE_PORT_OBSERVER')
print('margin_1_lower',margin_1)
print('margin_2_lower',margin_2)
print('gap_lower',gap)
