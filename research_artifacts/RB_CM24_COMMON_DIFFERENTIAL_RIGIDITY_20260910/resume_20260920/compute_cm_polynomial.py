"""Optional local FLINT cross-check of the published H_{-24} table entry."""
import json
import flint
from flint import fmpz_poly
h=fmpz_poly.hilbert_class_poly(-24)
assert [int(x) for x in h]==[14670139392,-4834944,1]
print(json.dumps({'python_flint_version':flint.__version__,'FLINT_version':flint.__FLINT_VERSION__,
                  'input_discriminant':-24,'coefficients_constant_first':[int(x) for x in h],
                  'polynomial':str(h),'periods_of_phi_evaluated':False}))
