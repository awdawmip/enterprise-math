"""Moving prime windows in the localized Weil form. Requires python-flint 0.9.0."""
import argparse
import hashlib
import json
from math import factorial
from pathlib import Path

import flint
from flint import acb, arb, ctx

PRIME_POWERS = (2, 3, 4)
I = acb(0, 1)


def interval(x, digits=8):
    scale = 10**digits
    return [int((x.lower()*scale).floor().unique_fmpz()),
            int((x.upper()*scale).ceil().unique_fmpz()), scale]


def weight(n):
    return arb(2 if n == 4 else n).log()/arb(n).sqrt()


def frequencies(parity, j):
    # f=(1+cos(pi*x))^j times either 1 or sin(pi*x/2).
    out = {0:acb(1)} if parity == 1 else {-1:I/2, 1:-I/2}
    for _ in range(j):
        nxt = {}
        for k, value in out.items():
            for delta, factor in ((-2, arb(1)/2), (0, 1), (2, arb(1)/2)):
                nxt[k+delta] = nxt.get(k+delta, acb(0))+factor*value
        out = nxt
    return out


def exponential_jet(frequency, shift, L, h, degree):
    exponent = I*frequency*shift
    coeff = [exponent.exp()]
    for j in range(1, degree+1):
        coeff.append(sum(i*exponent*(-1/L)**i*coeff[j-i] for i in range(1,j+1))/j)
    return sum(c*h**j for j,c in enumerate(coeff))


def phase_integral(k,left,right):
    if not k:
        return acb(right-left)
    t = I*arb.pi()*k/2
    return ((t*right).exp()-(t*left).exp())/t


def residual_weights(parity, degree, L, h):
    terms = []
    endpoints = [arb(-1), arb(1)]
    poly = frequencies(parity, degree//2)
    for n in PRIME_POWERS:
        for sign in (-1,1):
            shift = sign*arb(n).log()/L
            shifted = sign*arb(n).log()/(L+h)
            old_cut = sign-shift
            new_cut = sign-shifted
            endpoints += [old_cut,new_cut]
            for k, c in poly.items():
                freq = arb.pi()*k/2
                new = -weight(n)*c*(I*freq*shifted).exp()
                old_taylor = -weight(n)*c*exponential_jet(freq,shift,L,h,degree)
                terms.append((sign, old_cut, new_cut, k, new, old_taylor))
    endpoints.sort(key=lambda z:float(z.mid()))
    assert all(a<b for a,b in zip(endpoints,endpoints[1:]))
    pieces = []
    for left,right in zip(endpoints,endpoints[1:]):
        mid = (left+right)/2
        coeff = dict.fromkeys(poly,acb(0))
        for sign,old_cut,new_cut,k,new,old_taylor in terms:
            if sign*(mid-new_cut)<0:
                coeff[k] += new
            if sign*(mid-old_cut)<0:
                coeff[k] -= old_taylor
        pieces.append((left,right,coeff))
    return pieces


def fourier_piece(piece, k):
    left,right,coeff = piece
    return sum(c*phase_integral(j+k,left,right) for j,c in coeff.items())


def basis_inner(pieces, parity, q):
    if parity == 1 and q == 0:
        return sum(fourier_piece(piece,0) for piece in pieces)/arb(2).sqrt()
    k = 2*q+(parity == -1)
    positive = sum(fourier_piece(piece,k) for piece in pieces)
    negative = sum(fourier_piece(piece,-k) for piece in pieces)
    return (positive+negative)/2 if parity == 1 else (positive-negative)/(2*I)


def leading(parity, a, L):
    # Absolute value at either endpoint of the first nonzero derivative.
    j = a//2
    trace = factorial(a)*(arb.pi()**2/2)**j
    return 2*trace**2*sum(weight(n)**2*(arb(n).log()/L**2)**(2*a+1)
                          for n in PRIME_POWERS)/(factorial(a)**2*(2*a+1))


def interval_test(parity,a,L,h):
    pieces = residual_weights(parity,a,L,h)
    energy = arb(0)
    for left,right,coeff in pieces:
        total = sum(c*d.conjugate()*phase_integral(i-j,left,right)
                    for i,c in coeff.items() for j,d in coeff.items())
        assert total.imag.contains(0)
        energy += total.real
    for q in range(8):
        energy -= abs(basis_inner(pieces,parity,q))**2
    relative = energy/(abs(h)**(2*a+1)*leading(parity,a,L))
    assert relative > 0
    return interval(relative)


def diagonal_cost(hbits,L):
    # Constant even input f=1. Its prime increment consists solely of the six strips.
    h = arb(1)/(2**hbits)
    eps = abs(h)
    cutoffs = []
    exact = arb(0)
    for n in PRIME_POWERS:
        x = 1-arb(n).log()/L
        y = 1-arb(n).log()/(L+h)
        cutoffs.append((x,y,weight(n)))
        exact += 2*weight(n)**2*(y-x)
    def fourier(q):
        if q == 0:
            return -arb(2).sqrt()*sum(w*(y-x) for x,y,w in cutoffs)
        t = arb.pi()*q
        return -2*sum(w*((t*y).sin()-(t*x).sin())/t for x,y,w in cutoffs)
    energy = exact-sum(fourier(q)**2 for q in range(8))
    partial = arb(0)
    included = arb(0)
    stop = 4096
    for q in range(8,stop):
        square = fourier(q)**2
        included += square
        partial += square/arb(2+q).log()
    omitted = energy-included
    assert 0 < omitted < energy
    norm = leading(1,0,L)*eps
    low = -eps.log()*partial/norm
    high = -eps.log()*(partial+omitted/arb(2+stop).log())/norm
    assert low > 0 and high>low
    return {'cutoff':stop,'scaled_H_inverse_lower_upper':
            [interval(low,5)[0],interval(high,5)[1],100000],
            'discarded_unweighted_mass_fraction':interval(omitted/energy,6)}


def main():
    ctx.prec = 384
    left = arb(4)/5
    right = arb(5).log()/2
    Lrange = left.union(right)
    c = [s*(1-arb(n).log()/Lrange) for n in PRIME_POWERS for s in (-1,1)]
    c.extend([arb(-1),arb(1)])
    assert all(abs(a-b)>arb(1)/5 for k,a in enumerate(c) for b in c[k+1:])
    arch_and_pole = 48/left**4+4*right.exp()*(right+4)/24
    assert arch_and_pole < 120
    rows = []
    for name,L,direction in [('left',left,1),('right',right,-1)]:
        for parity in (1,-1):
            for a in (0,2,4):
                for hbits in (11,16):
                    h = direction*arb(1)/2**hbits
                    scaled = interval_test(parity,a,L,h)
                    numerator = 3 if hbits==16 else 100
                    assert scaled[0]*100 > scaled[2]*(100-numerator)
                    assert scaled[1]*100 < scaled[2]*(100+numerator)
                    rows.append({'endpoint':name,'parity':parity,'a':a,'step':str(direction)+'/2^'+str(hbits),
                                 'prime_Q_residual_over_predicted_interval':scaled})
    return {'python_flint':flint.__version__,'precision_bits':ctx.prec,'head_modes':8,
            'source':{'revision':'Hongmin Li v2 (2.1)-(2.5), (3.1)-(3.4)',
                      'local_source_sha256':'ff635e2e070d442ba5b48b20a29a1a908942254887d46bacca77d9cd551f3e8d'},
            'regular_cubic_arch_and_pole_coeff_upper':interval(arch_and_pole),
            'active':list(PRIME_POWERS),'minimum_uniform_separation_from_each_other_and_endpoints_gt':'1/5',
            'even_f1_leading_left':interval(leading(1,0,left)),
            'even_f1_leading_right':interval(leading(1,0,right)),
            'prime_port_rows':rows,
            'diagonal_model_log_2_plus_mode':{str(n):diagonal_cost(n,left) for n in (9,11,13)}}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    parser.add_argument('--li-source',type=Path)
    args = parser.parse_args()
    result = main()
    if args.li_source:
        assert hashlib.sha256(args.li_source.read_bytes()).hexdigest()==result['source']['local_source_sha256']
    serialized = json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(serialized,encoding='utf-8')
    else:
        print(serialized,end='')
