"""Count repeated identity prefixes, retain full actual signed suffix matrices."""
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import hashlib

from paid_aggregator import PaidAggregator, CarryExecutor, Arithmetic, LazyModularColumns
from paid_aggregator import verify_lazy_permutation, normalized, require


def pair_count(H, M, rho, arithmetic):
    """Actual typed count of (u,v) in [0,H)^2 with v-u=rho modulo M."""
    require(type(H) is int and H >= 1 and type(M) is int and M >= 1,
            'positive integer interval and modulus required')
    require(type(rho) is int and 0 <= rho < M, 'canonical count residue required')
    v, u, split = arithmetic.divide(H, M)
    vv, vv_op = arithmetic.multiply(v, v)
    base, base_op = arithmetic.multiply(M, vv)
    vu, vu_op = arithmetic.multiply(v, u)
    twice, twice_op = arithmetic.add(vu, vu)
    count, add_op = arithmetic.add(base, twice)
    rel1, diff1, cmp1 = arithmetic.compare(u, rho)
    tail1 = diff1 if rel1 >= 0 else 0
    _, back, back_op = arithmetic.compare(M, rho)
    rel2, diff2, cmp2 = arithmetic.compare(u, back)
    tail2 = diff2 if rel2 >= 0 else 0
    count, plus1 = arithmetic.add(count, tail1)
    count, plus2 = arithmetic.add(count, tail2)
    return count, {'H': H, 'M': M, 'rho': rho, 'v': v, 'u': u, 'count': count,
        'tail1': tail1, 'tail2': tail2, 'operations': [split, vv_op, base_op,
        vu_op, twice_op, add_op, cmp1, back_op, cmp2, plus1, plus2]}


class LeadingZeroAggregator(PaidAggregator):
    def __init__(self, program, history):
        super().__init__(program, history)
        self._leading_source = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    def gamma_leading_zero(self, depth, target, address_certificate):
        """A conditional fast path; all order discovery/address replay is charged.

        With ell nontrivial suffix bits, this enumerates 2^(ell+1)-1 signed
        displacements. It is only useful when ell is small. No cutoff quietly
        drops terms. Full residual rows and both sides of every action survive.
        """
        require(hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == self._leading_source,
                'leading-zero source changed')
        verification = self._verify_address(depth, target, address_certificate)
        replay = verification['replay']
        record = {'depth': depth, 'target': target, 'address_verification': verification,
                  'contraction_method': 'leading_zero_counted_full_suffix'}
        if replay['status'] == 'NONMEMBER':
            self.aggregation_stats['nonmember_zero_queries'] += 1
            record['nonmember_zero'] = True
            self.aggregation_queries.append(record)
            return self._zero()
        r, R, s = replay['r'], replay['R'], replay['s']
        K = 0
        while K < depth and self.history[K] == 0:
            K += 1
        ell = depth-K
        P, H, g = 1 << ell, 1 << K, 1 << min(ell, s)
        arithmetic = Arithmetic()
        M, remainder, modulus_division = arithmetic.divide(R, g)
        require(remainder == 0, 'certified two-part must divide R')
        A = 1 << max(ell-s, 0)
        inverse_table, inverse_replay, inverse = None, None, None
        if M > 1:
            _, A_mod, A_reduction = arithmetic.divide(A, M)
            inverse_table = LazyModularColumns(M, A_mod)
            inverse_replay = verify_lazy_permutation(inverse_table)
            inverse = inverse_table.inverse_multiplier
        else:
            A_reduction = None
        suffix = CarryExecutor(self.program, self.history[K:depth])
        routes, terms = [], []
        for d in range(1-P, P):
            _, dmod, d_reduction = arithmetic.divide(abs(d), R)
            negate = None
            if d < 0:
                dmod, negate = arithmetic.modsubtract(0, dmod, R)
            delta, difference_ops = arithmetic.modsubtract(r, dmod, R)
            delta_q, delta_r, congruence_division = arithmetic.divide(delta, g)
            route = {'d': d, 'd_mod_R': dmod, 'd_reduction': d_reduction,
                'negation': negate, 'delta': delta, 'difference': difference_ops,
                'delta_quotient': delta_q, 'delta_remainder': delta_r,
                'congruence_division': congruence_division}
            if delta_r:
                route.update(count=0, reason='incompatible two-adic residue')
            else:
                if M == 1:
                    rho, residue_ops = 0, None
                else:
                    rho, residue_ops = arithmetic.modmul(inverse, delta_q, M)
                count, count_evidence = pair_count(H, M, rho, arithmetic)
                route.update(rho=rho, residue_operations=residue_ops, count=count,
                             count_evidence=count_evidence)
                if count:
                    coefficient = suffix.coefficient(ell, d)
                    terms.append((count, coefficient))
                    self.aggregation_stats['suffix_coefficient_queries'] += 1
            routes.append(route)
        den = max((matrix.den for _, matrix in terms), default=1)
        rows = []
        for i in range(self.dim):
            row = []
            for j in range(self.dim):
                products = []
                for count, matrix in terms:
                    shift = den.bit_length()-matrix.den.bit_length()
                    value = matrix.rows[i][j] << shift
                    if value:
                        products.append((Fraction(count), Fraction(value)))
                if products:
                    self.observation_count += 1
                    value = self.observer.evaluate(f'{self.observation_count}:weighted_suffix', tuple(products))
                    require(value.denominator == 1, 'aligned weighted sum must be integral')
                    row.append(value.numerator)
                else:
                    row.append(0)
            rows.append(tuple(row))
        answer = normalized(tuple(rows), den << (2*K))
        self._observe_size((answer,))
        self.aggregation_stats['leading_zero_queries'] += 1
        record.update(K=K, ell=ell, P=P, H=H, r=r, R=R, s=s, g=g, M=M, A=A,
            modulus_division=modulus_division, A_reduction=A_reduction,
            inverse_table=None if inverse_table is None else inverse_table.export_certificate(),
            inverse_permutation_replay=inverse_replay, routes=routes,
            suffix_evidence=suffix.evidence(), index_arithmetic_operations=deepcopy(arithmetic.operations),
            index_arithmetic_stats=dict(arithmetic.stats),
            weighted_matrix_terms=len(terms), leading_zero_source_sha256=self._leading_source,
            denominator_scaling='C_suffix includes 4^-ell; weighted sum divided by 4^K exactly once')
        self.aggregation_queries.append(record)
        return answer

    def evidence(self):
        require(hashlib.sha256(Path(__file__).read_bytes()).hexdigest() == self._leading_source,
                'leading-zero source changed')
        evidence = super().evidence()
        evidence['leading_zero_source_sha256'] = self._leading_source
        return evidence
