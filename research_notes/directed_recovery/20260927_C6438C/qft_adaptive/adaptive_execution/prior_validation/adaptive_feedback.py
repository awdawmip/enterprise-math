"""History-consistent gate omission with exact actual-native Gram certificates.

This is a bounded reference implementation, not an efficient Gram oracle.
The caller supplies an admitted fixed bank. Past selected words never change.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parents[1]
sys.path.insert(0, str(BASE/'sep27-qft-carry-execution'))
from carry_executor import phase_snapshot, GRAM_SHA, OLD
from gram_sampler import GramSampler, Correlation, normalized
from certified_word_compiler import packed


def digest(value):
    return hashlib.sha256(packed(value)).hexdigest()


def strict_bytes(value):
    """Cursor schema encoding; unlike Python equality it distinguishes bool/int."""
    return json.dumps(value, sort_keys=True, separators=(',', ':'),
                      ensure_ascii=False, allow_nan=False).encode('utf-8')


@dataclass(frozen=True)
class CommittedStep:
    history: tuple
    reference_ids: tuple
    selected_ids: tuple
    charge: F
    bit: int
    certificate_sha256: str


class AdaptiveFeedbackGram(GramSampler):
    policy = 'DROP_OLDEST_WORD_IF_REMAINING_BUDGET_CERTIFIES_V1'

    def __init__(self, program, epsilon, *, query_budget=1000):
        if hashlib.sha256((OLD/'gram_sampler.py').read_bytes()).hexdigest() != GRAM_SHA:
            raise ValueError('frozen inherited Gram source changed')
        if isinstance(epsilon, bool) or not isinstance(epsilon, (str, int, F)):
            raise ValueError('explicit exact rational budget required')
        epsilon = F(epsilon)
        if not 0 <= epsilon <= 1:
            raise ValueError('total TV charge budget must lie in [0,1]')
        super().__init__(program, query_budget=query_budget)
        self.epsilon = epsilon
        self.steps = ()
        self.pending = None
        self.certificates = []
        self._bound = phase_snapshot(program)
        self._own_source = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        self._program_digest = digest({'N':program.N, 'a':program.a, 't':program.t,
            'dim':program.dim, 'full_dim':program.full_dim,
            'powers':program.modular_powers, 'phases':program.phase_bindings,
            'codec':program.codec_binding, 'two_h4':program.h4_binding})
        self.policy_stats = {'candidate_tests':0, 'accepted_omissions':0,
            'reference_fallbacks':0, 'identity_steps':0, 'prepared_cache_hits':0,
            'defect_matrix_entries_observed':0}

    def _check(self):
        if phase_snapshot(self.program) != self._bound:
            raise ValueError('admitted program changed')
        if tuple(s.bit for s in self.steps) != self.history:
            raise ValueError('history changed outside the committed ledger')
        if self.pending is not None and tuple(self.pending['history']) != self.history:
            raise ValueError('pending decision no longer belongs to this prefix')

    def _gates(self, depth):
        self._check()
        if depth < len(self.steps):
            ids = self.steps[depth].selected_ids
        elif depth == len(self.steps) and self.pending is not None:
            ids = self.pending['selected_ids']
        else:
            raise ValueError('feedback requires a prepared or committed step')
        return tuple(self.program.bank[m] for m in ids)

    def gamma(self, depth, residue):
        self._check()
        return super().gamma(depth, residue)

    def _observe(self, label, terms):
        self.observation_count += 1
        return self.observer.evaluate(f'{self.observation_count}:{label}', tuple(terms))

    def defect(self, covariance, reference_ids, selected_ids):
        """Full signed (T-S) C (T-S)^T; no residual projection or scalar shortcut."""
        ref = tuple(self.program.bank[m] for m in reference_ids)
        low = tuple(self.program.bank[m] for m in selected_ids)
        tc = self._left(covariance, ref)
        sc = self._left(covariance, low)
        terms = ((1,self._right_transpose(tc,ref)),
                 (-1,self._right_transpose(tc,low)),
                 (-1,self._right_transpose(sc,ref)),
                 (1,self._right_transpose(sc,low)))
        quarter = self._combine(terms)
        # _combine includes one native branch-pair factor 1/4. Here there is no
        # new branch; restore that exact structural dyadic factor.
        matrix = normalized(tuple(tuple(v << 2 for v in row) for row in quarter.rows),
                            quarter.den)
        self.policy_stats['defect_matrix_entries_observed'] += self.dim*self.dim
        return matrix, self._trace(matrix, 'full_gate_action_defect')

    def prepare_next(self):
        self._check()
        if len(self.history) >= self.program.t:
            raise ValueError('terminal prefix has no next decision')
        if self.pending is not None:
            self.policy_stats['prepared_cache_hits'] += 1
            return json.loads(packed(self.pending))
        depth = len(self.history)
        reference = tuple(depth-c+1 for c in range(depth) if self.history[c])
        covariance = self.gamma(depth,1)
        mass = self._trace(covariance, 'policy_prefix_mass')
        if mass < 0:
            raise AssertionError('negative prefix mass')
        spent = self._sum('committed_charge', (s.charge for s in self.steps))
        remaining = self._observe('remaining_charge', ((self.epsilon,),(-F(1),spent)))
        if not 0 <= remaining <= self.epsilon:
            raise AssertionError('budget ledger inconsistent')
        selected, charge, defect, A, margin = reference, F(0), None, F(0), None
        decision = 'REFERENCE_ZERO_MASS' if mass == 0 else 'REFERENCE_ZERO_BUDGET'
        candidate = reference[1:] if reference else reference
        if not reference:
            decision = 'IDENTITY'
            self.policy_stats['identity_steps'] += 1
        elif mass and remaining:
            self.policy_stats['candidate_tests'] += 1
            defect,A = self.defect(covariance,reference,candidate)
            if not 0 <= A <= 4*mass:
                raise AssertionError('orthogonal action defect outside [0,4M]')
            margin = self._observe('rational_local_trace_distance_test',
                ((F(8),A,mass),(-F(1),A,A),
                 (-F(16),remaining,remaining,mass,mass)))
            if margin <= 0:
                selected,charge,decision = candidate,remaining,'OMIT_OLDEST_CERTIFIED'
                self.policy_stats['accepted_omissions'] += 1
            else:
                decision = 'REFERENCE_FAILED_CERTIFICATE'
                self.policy_stats['reference_fallbacks'] += 1
        elif reference:
            self.policy_stats['reference_fallbacks'] += 1
        self.pending = {'history':self.history,'reference_ids':reference,
            'candidate_ids':candidate,'selected_ids':selected,
            'remaining_before':remaining,'charge':charge,'decision':decision,
            'mass':mass,'candidate_A':A,'rational_test_margin':margin,
            'covariance':{'rows':covariance.rows,'den':covariance.den},
            'candidate_defect':None if defect is None else {'rows':defect.rows,'den':defect.den},
            'zero_mass_is_not_normalized_certificate':mass==0}
        return json.loads(packed(self.pending))

    def probabilities(self):
        self.prepare_next()
        return super().probabilities()

    def advance(self, bit):
        if type(bit) is not int or bit not in (0,1):
            raise ValueError('one exact classical bit required')
        plan = self.probabilities()
        if plan['child_masses'][bit] <= 0:
            raise ValueError('cannot select a zero-mass child')
        p = self.pending
        cert = json.loads(packed(p))
        step = CommittedStep(self.history,tuple(p['reference_ids']),tuple(p['selected_ids']),
                             p['charge'],bit,digest(p))
        self.steps += (step,)
        self.history += (bit,)
        self.certificates.append(cert)
        self.pending = None
        if self.mass() != plan['child_masses'][bit]:
            raise AssertionError('committed feedback recurrence disagrees with child mass')
        return plan

    def cursor(self):
        self._check()
        return {'schema':'BRC_ADAPTIVE_FEEDBACK_CURSOR_V1','policy':self.policy,
            'epsilon':str(self.epsilon),'program_sha256':self._program_digest,
            'source_sha256':self._own_source,'history':list(self.history),
            'steps':[{'history':list(s.history),'reference_ids':list(s.reference_ids),
                'selected_ids':list(s.selected_ids),'charge':str(s.charge),'bit':s.bit,
                'certificate_sha256':s.certificate_sha256} for s in self.steps],
            'pending_certificate_sha256':None if self.pending is None else digest(self.pending),
            'restore_mode':'REEXECUTE_COMMITTED_PREFIX_AND_PENDING_DECISION',
            'query_cache_or_random_tape_restored':False}

    @classmethod
    def restore(cls, program, cursor, *, query_budget=1000):
        if type(cursor) is not dict or type(cursor.get('history')) is not list:
            raise ValueError('strict cursor object and history required')
        if any(type(b) is not int or b not in (0,1) for b in cursor['history']):
            raise ValueError('cursor bits must be integers, not booleans')
        new = cls(program,cursor.get('epsilon'),query_budget=query_budget)
        for bit in cursor['history']:
            new.advance(bit)
        if cursor.get('pending_certificate_sha256') is not None:
            new.prepare_next()
        if strict_bytes(new.cursor()) != strict_bytes(cursor):
            raise ValueError('cursor differs from exact deterministic replay')
        return new

    def evidence(self):
        self._check()
        return {'cursor':self.cursor(),'policy_stats':dict(self.policy_stats),
            'certificates':self.certificates,
            'pending':None if self.pending is None else json.loads(packed(self.pending)),
            'inherited':super().evidence(),
            'source_sha256':self._own_source,
            'status':'AUTHOR_EXECUTED_IF_CALLED; NOT_A_POLYNOMIAL_GRAM_ORACLE'}
