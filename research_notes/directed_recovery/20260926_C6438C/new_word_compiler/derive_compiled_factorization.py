"""Derive a separate recursive driver with honest compiler interruptions."""
from pathlib import Path
import hashlib, json

root=Path(__file__).resolve().parent
source=root.parent/'integration'/'complete_factorization.py'
text=source.read_text(encoding='utf-8')
old='        bank, dim, error = phase_provider(t)\n'
new='''        try:
            bank, dim, error = phase_provider(t)
        except CompilationPending as exc:
            guaranteed_budget = False
            events.append({'input': value, 'multiplicity': multiplicity,
                'action': 'COMPILATION_PARTIAL',
                'non_perfect_power_certificate_id': pp_id,
                'composite_certificate_id': prime_id, 't': t,
                'compilation': exc.report})
            unresolved.append({'cofactor': value, 'multiplicity': multiplicity,
                'status': 'COMPILATION_PARTIAL', 'event_index': len(events)-1})
            continue
'''
assert text.count(old)==1
text=text.replace(old,new)
prefix='''# Derived from the existing verified recursive factorization driver.
# The only algorithmic loop change preserves unfinished compilation as a leaf.
from pathlib import Path as _Path
import sys as _sys
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / 'integration'))

class CompilationPending(Exception):
    def __init__(self, report):
        super().__init__('Complete phase bank is not yet certified')
        self.report = report

'''
# Preserve the source docstring/future-import positions by removing only the
# future directive and putting it in the generated module's legal first slot.
future='from __future__ import annotations\n'
assert text.count(future)==1
text=future+prefix+text.replace(future,'')
out=root/'compiled_factorization_core.py'
out.write_text(text,encoding='utf-8')
manifest={'source':str(source),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'output':out.name,'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'algorithmic_change':'Catch typed CompilationPending; retain entire cofactor and multiplicity, certificates, resume report and product ledger; disable uninterrupted-run stochastic budget claim',
 'old_fragment':old,'new_fragment':new,
 'unchanged':'Prechecks, sparse original-CF factor_attempts, factor validation, recursion, retry budgets, product invariant and deterministic verifier'}
(root/'COMPILED_FACTORIZATION_DERIVATION.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in manifest.items() if k not in ('old_fragment','new_fragment')}))
