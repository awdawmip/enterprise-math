"""Complete or resumable factorization with requested-accuracy native words."""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import sys

from compiled_factorization_core import factor_integer, verify_factorization, CompilationPending


class CompiledPhaseProvider:
    """One declared budget per request; immutable source seeds, no outcome fitting.

    Resume using phase_cursors from the previous wrapper result. A seed policy
    is chosen before any sample. With pair_budget=None the compiler's fair tail
    is continued until its separately proved finite termination point.
    """
    def __init__(self, *, pair_budget=256, observer_start_bits=48, phase_cursors=None,
                 activity='RA-CAAAC604CB513AEA8BBC1DFC'):
        if pair_budget is not None and (not isinstance(pair_budget,int) or isinstance(pair_budget,bool) or pair_budget<0):
            raise ValueError('nonnegative compiler pair budget or None required')
        self.pair_budget=pair_budget
        self.observer_start_bits=observer_start_bits
        self.cursors=dict(phase_cursors or {})
        self.activity=activity
        self.reports={}
        self.cache={}

    def __call__(self,t):
        if t in self.cache:
            return self.cache[t]
        from compiled_streaming import compile_bank
        sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'phases'))
        from closed_phase_bank import load_certified_bank
        # Seeds reuse existing fixed letters. They do not alter the target,
        # infer an order, or substitute for the compiler's complete fair tail.
        bank,_,_,_=load_certified_bank(t,cutoff=33,
            expected_payload_sha256='feecbc02808991f6d7b1e2c3179c8da2018b76901ef34c26ef0d28b65729dd5c')
        seeds={2:[(('swap',0,1),('neg',1))]}
        seeds.update({m:[tuple(bank[m].inverse_phase_word)] for m in range(3,t+1)})
        epsilon=F(1,8*t)  # t=2n gives exactly 1/(16n).
        cursor=self.cursors.get(str(t))
        while True:
            adapted=compile_bank(t,epsilon,seed_words=seeds,cursor=cursor,
                pair_budget=256 if self.pair_budget is None else self.pair_budget,
                observer_start_bits=self.observer_start_bits,activity=self.activity)
            report=adapted['compilation']
            self.reports[str(t)]=report
            cursor=report.get('cursor')
            self.cursors[str(t)]=cursor
            if adapted['status']=='CERTIFIED':
                error=adapted['error_certificate']
                if not F(0)<=F(error['terminal_TV_bound'])<=epsilon:
                    raise ValueError('Compiler returned an invalid requested accuracy')
                self.cache[t]=(adapted['bank'],adapted['dim'],error)
                return self.cache[t]
            if adapted['status']!='PARTIAL':
                raise ValueError('Unknown compiler result')
            if self.pair_budget is not None:
                raise CompilationPending(report)


def factor_integer_compiled(N,rng,*,failure_bits=16,max_attempts=None,
                            base_provider=None,compiler_pair_budget=256,
                            observer_start_bits=48,phase_cursors=None):
    provider=CompiledPhaseProvider(pair_budget=compiler_pair_budget,
        observer_start_bits=observer_start_bits,phase_cursors=phase_cursors)
    result=factor_integer(N,rng,provider,failure_bits=failure_bits,
        max_attempts=max_attempts,base_provider=base_provider)
    result['native_word_compiler']={
        'profile':'FIXED_ALPHABET_VARIABLE_WORD_COMPILER_V1',
        'phase_compilations':provider.reports,
        'phase_cursors':provider.cursors,
        'compiler_pair_budget_per_request':compiler_pair_budget,
        'observer_start_bits':observer_start_bits,
        'requested_single_program_error':'epsilon(t)=1/(8t)=1/(16n)',
        'resume':'Repeat this input with saved phase_cursors and the same compiler profile/seed source; completed prime ledger remains certified. Random histories are not replayed by a compiler cursor.',
        'no_order_or_factor_input':True}
    return result
