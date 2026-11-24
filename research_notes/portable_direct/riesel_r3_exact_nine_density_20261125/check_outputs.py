from fractions import Fraction
import json
def read(p):return json.load(open(p))
x=read('result_forward.json')
assert x['densities']==read('result_alternate.json')['densities']
a=x['densities']['union']['exact9']
b=read('independent_result.json')
assert Fraction(int(a['numerator']),int(a['denominator']))==Fraction(int(b['exact9']['n']),int(b['exact9']['d']))
c=x['densities']['budget8']['at_most9_predicate']
assert 1-Fraction(int(c['numerator']),int(c['denominator']))==Fraction(int(b['no8']['n']),int(b['no8']['d']))
assert x['periodic_set_cover_crosschecks']==246
print('Two decision-diagram orders and independent conditional counting agree exactly.')
