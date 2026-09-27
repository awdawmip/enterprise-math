"""Only the newly identified K=0 boundary; do not repeat the main fixture set."""
from copy import deepcopy
from pathlib import Path
from time import perf_counter
import gzip
import hashlib
import json
from check_paid_aggregation import packed, sources, LeadingZeroAggregator, CarryExecutor
from check_paid_aggregation import load_bank, ExactCarrierCodec, LazyStreamingProgram, discover_aliases, CALLS, verify_vendor

ROOT = Path(__file__).resolve().parent


def main():
    first, start = len(CALLS), perf_counter()
    guard = json.loads((ROOT.parent/'STARTUP_GUARD.json').read_bytes())
    assert guard['activity_allowed'] and guard['persistence_allowed'] and not guard['sync_debt_events']
    before = sources()
    before['check_zero_prefix_boundary.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    main_sources = json.loads((ROOT/'PAID_AGGREGATION_SUMMARY.json').read_bytes())['source_sha256']
    assert all(before[k] == v for k,v in main_sources.items())
    vendor = verify_vendor()
    bank, bank_source = load_bank()
    program = LazyStreamingProgram(21, 2, 4, bank, 61, codec=ExactCarrierCodec(61, tuple(range(6))))
    history, depth = (1,0,1), 3
    agg, base = LeadingZeroAggregator(program, history), CarryExecutor(program, history)
    targets = (1,program.modular_powers[depth-1])
    aliases = discover_aliases(program, depth, targets, 3)
    cases, certificates = [], []
    for target in targets:
        certificate = agg.discover_address(depth, target, 3)
        certificates.append(certificate)
        a = agg.gamma_with_address(depth, target, certificate)
        b = agg.gamma_leading_zero(depth, target, certificate)
        c = base.sum_coefficients(depth, aliases['aliases'][target])
        query = agg.aggregation_queries[-1]
        assert query['K'] == 0 and query['ell'] == depth and query['H'] == 1
        assert a == b == c
        cases.append({'N':21,'a':2,'history':history,'depth':depth,'target':target,
            'r':certificate['r'],'R':certificate['R'],'K':query['K'],'ell':query['ell'],
            'all_matrix_entries_equal':True,'matrix':{'rows':a.rows,'den':a.den},
            'any_residual_row_or_column_entry':any(v for j,row in enumerate(a.rows)
                for k,v in enumerate(row) if j>=2 or k>=2),
            'aliases':aliases['aliases'][target], 'weights':[{k:r[k] for k in ('d','count')} for r in query['routes']]})
    after = sources()
    after['check_zero_prefix_boundary.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    assert before == after
    payload = {'schema':'COUNTED_SUFFIX_K_ZERO_BOUNDARY_V1',
        'status':'AUTHOR_ACTUAL_NATIVE_BOUNDED_SHARED_CONTEXT_NOT_ADMITTED',
        'source_sha256':before,'source_unchanged_during_run':True,'startup_guard':guard,
        'vendor':vendor,'bank_source':bank_source,'cases':cases,'address_certificates':certificates,
        'alias_evidence':aliases,'aggregation_evidence':agg.evidence(),'baseline_evidence':base.evidence(),
        'program':{'N':program.N,'a':program.a,'t':program.t,'dim':program.dim,'full_dim':program.full_dim,
            'phase_bindings':program.phase_bindings,'codec_binding':program.codec_binding,'h4_binding':program.h4_binding,
            'modular_powers':program.modular_powers,'program_table_instances':program.lazy_factory.export_certificate(),
            'program_permutation_verifications':program.lazy_permutation_verifications},
        'native_core_call_receipts':CALLS[first:],'actual_native_core_calls':len(CALLS)-first,
        'elapsed_seconds':perf_counter()-start,
        'scope':'K=0 is exact no-acceleration fallback; complete nonzero residual matrices retained; no general complexity claim'}
    raw = packed(payload)
    output = ROOT/'K_ZERO_BOUNDARY_RESULTS.json.gz'
    output.write_bytes(gzip.compress(raw,compresslevel=9,mtime=0))
    assert gzip.decompress(output.read_bytes()) == raw
    summary = {k:v for k,v in payload.items() if k in ('schema','status','source_sha256','actual_native_core_calls','elapsed_seconds','scope')}
    summary.update(case_count=len(cases),payload_bytes=len(raw),payload_sha256=hashlib.sha256(raw).hexdigest(),
        gzip_bytes=output.stat().st_size,gzip_sha256=hashlib.sha256(output.read_bytes()).hexdigest(),
        cases=[{k:v for k,v in c.items() if k != 'matrix'} for c in cases])
    (ROOT/'K_ZERO_BOUNDARY_SUMMARY.json').write_bytes(packed(summary))
    print(json.dumps(summary),flush=True)


if __name__ == '__main__':
    main()
