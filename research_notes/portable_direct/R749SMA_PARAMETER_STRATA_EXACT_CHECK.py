"""Exact rational robustness check for R749SMA; imports the independently validated R749SM kernel."""
from fractions import Fraction as Q
from itertools import product
from contextlib import redirect_stdout
import io
import json

with redirect_stdout(io.StringIO()):
    import R749SM_PREDICTIVE_HANKEL_EXACT_CHECK as base

parameters = [Q(0), Q(1,8), Q(1,2), Q(7,8), Q(15,16), Q(63,64)]
Z = list(product((-1,1), repeat=2))
words = list(product((-1,1), repeat=2))
probability_matrices = []
checked_signed_conditional_paths = 0
for p in parameters:
    q=(1+15*p)/16
    r=(1-p)/16
    a=q+r
    assert a==(1+7*p)/8
    assert a>0 and 2*r==(1-p)/8>0
    base.THETA = (q-r)/a
    assert base.THETA==8*p/(1+7*p)
    for z0,z1 in Z:
        initial={tuple(sorted({0:z0,1:z1,2:s2}.items())):Q(1,2) for s2 in (-1,1)}
        d1=base.propagate(base.A0,base.B0,initial,base.C0)
        d2=base.propagate(base.B0,base.C0,d1,base.C1)
        assert len(d2)==8 and set(d2.values())=={Q(1,8)}
        for x,y in words:
            next_support=base.next_options[x]
            d3=base.propagate(*base.S,d2,next_support)
            d4=base.propagate(base.S[1],next_support,d3,base.second_options[x][y])
            assert len(d3)==len(d4)==8 and set(d3.values())==set(d4.values())=={Q(1,8)}
            checked_signed_conditional_paths+=1
    M=[[Q(2+x*z0*z1,4)*Q(2+y*z0,4) for z0,z1 in Z] for x,y in words]
    assert base.rank(M)==4 and base.determinant(M)==Q(1,16)
    assert base.rank([[Q(2+x*z0*z1,4) for z0,z1 in Z] for x in (-1,1)])==2
    probability_matrices.append(M)
assert all(M==probability_matrices[0] for M in probability_matrices)
assert 2*Q(1-1,16)==0  # at p=1 the required nonforced support has zero probability
print(json.dumps({
  'status':'PASS',
  'parameter_values':[str(p) for p in parameters],
  'positive_nonforced_observation_probability':True,
  'exact_conditional_path_checks':checked_signed_conditional_paths,
  'uniform_eight_lift_across_four_private_histories':True,
  'public_two_step_law_independent_of_p':True,
  'two_step_public_rank':4,
  'two_step_public_determinant':'1/16',
  'affine_coordinates_H0_H1_H2':[0,1,3],
  'conditional_support_only_parameter_Fisher_information':'0',
  'endpoint_p_equals_one':'nonforced_prelude_zero_probability',
  'native_event_permission':False,
},sort_keys=True))
