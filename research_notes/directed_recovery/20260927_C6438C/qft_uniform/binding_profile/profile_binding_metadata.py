"""Host metadata-only microprofile; no scientific arithmetic or sampler run."""
from copy import deepcopy
from pathlib import Path
from time import perf_counter
import gzip
import hashlib
import json

ROOT = Path(__file__).resolve().parent
source = ROOT.parent/'uniform_execution/UNIFORM_FEEDBACK_RESULTS.json.gz'
compressed = source.read_bytes()
assert hashlib.sha256(compressed).hexdigest() == '14456595a5ff8e7c3e67d78fe091b1aefec68be835a9674cefbd4dfba3b0b015'
payload = json.loads(gzip.decompress(compressed))
metadata = (payload['programs'][0]['phase_bindings'],payload['programs'][0]['codec_binding'])
frozen_copies = deepcopy(metadata)
def encode(value):
    return json.dumps(value,sort_keys=True,separators=(',', ':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
expected = tuple(encode(v) for v in metadata)
repetitions = 200
trials = []
for repetition in range(3):
    start = perf_counter()
    for _ in range(repetitions):
        assert tuple(encode(v) for v in metadata) == expected
    encoded_time = perf_counter()-start
    start = perf_counter()
    for _ in range(repetitions):
        assert metadata == frozen_copies
    equality_time = perf_counter()-start
    trials.append({'trial':repetition,'serialization_seconds':encoded_time,
                   'plain_python_equality_seconds':equality_time})
# Plain Python equality does not preserve JSON type distinctions. Demonstrate
# why the faster operation is a diagnostic, not a replacement admission check.
strict_type_counterexample = {'python_bool_int_equal':({'x':True}=={'x':1}),
                             'canonical_JSON_equal':encode({'x':True})==encode({'x':1})}
assert strict_type_counterexample == {'python_bool_int_equal':True,'canonical_JSON_equal':False}
record = {'schema':'HOST_BINDING_METADATA_MICROPROFILE_V1',
    'source_gzip_sha256':hashlib.sha256(compressed).hexdigest(),
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'metadata_bytes':[len(v) for v in expected], 'repetitions_per_trial':repetitions,
    'trials':trials, 'strict_type_counterexample':strict_type_counterexample,
    'scientific_execution_performed':False,
    'scope':'Serialization of previously recorded metadata only. Not full _program_view, complete sampler, isolated end-to-end benchmark or attribution of the previous elapsed-time difference. Plain equality is not an accepted replacement certificate.'}
target = ROOT/'BINDING_METADATA_PROFILE.json'
if target.exists():raise ValueError('refusing to replace a recorded timing run')
target.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record))
