"""Standalone decimal I/O smoke; this is not scientific BRC arithmetic."""
import json
import sys
from pathlib import Path

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(4300)
limit_before = sys.get_int_max_str_digits() if hasattr(sys, 'get_int_max_str_digits') else None
import certified_word_compiler as compiler
from stage45.brc_loop_recheck import CALLS

calls_before = len(CALLS)
decimal = '1' + '0'*5000
integer = int(decimal)
encoded = compiler.packed({'large_certificate_integer': integer})
decoded = json.loads(encoded)
assert str(decoded['large_certificate_integer']) == decimal
assert len(CALLS) == calls_before == 0
report = {'status': 'PASSED', 'scope': 'ordinary certificate decimal I/O only',
          'decimal_digits': len(decimal), 'limit_before_import': limit_before,
          'limit_after_import': sys.get_int_max_str_digits() if hasattr(sys, 'get_int_max_str_digits') else None,
          'actual_BRC_core_calls': 0, 'scientific_execution': False,
          'roundtrip_exact': True}
(Path(__file__).resolve().parent / 'LARGE_CERTIFICATE_IO_SUMMARY.json').write_text(
    json.dumps(report, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report))
