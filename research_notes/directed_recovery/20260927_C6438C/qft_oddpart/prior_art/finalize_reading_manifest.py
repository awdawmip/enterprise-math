"""Record source-reading bytes and the publication allowlist; no science/network."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    (ROOT/path).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


sources = [
    {'id':'Dang-Hill-Hollenberg-1712.07311v4',
     'url':'https://arxiv.org/pdf/1712.07311v4',
     'publication_url':'https://quantum-journal.org/papers/q-2019-01-25-116/',
     'local_reading_copy':'dang_hill_hollenberg_1712.07311v4.pdf',
     'source_type':'author preprint, v4; published article identified separately',
     'actual_read_scope':'Abstract/setup; Sections 4–5, PDF pages 4–7; dynamic layout, Schmidt plateau and odd-part dependence.',
     'whole_paper_fully_read':False,
     'discovery':'Existing KQB2489 Scholar PARTIAL cache; no repeat provider query.'},
    {'id':'Pohlig-Hellman-1978',
     'url':'https://ee.stanford.edu/~hellman/publications/28.pdf',
     'publication_url':'https://doi.org/10.1109/TIT.1978.1055817',
     'local_reading_copy':'pohlig_hellman_1978.pdf',
     'source_type':'original published article hosted by author',
     'actual_read_scope':'Sections III–IV, printed pages 108–110 (PDF pages 3–5), exponent digits, prime-power components, CRT and operation counts.',
     'whole_paper_fully_read':False,
     'discovery':'Official-source web lookup, no professional provider task.'},
    {'id':'Kiefer-2009.01217v1',
     'url':'https://arxiv.org/pdf/2009.01217v1',
     'local_reading_copy':'kiefer_2009.01217v1.pdf',
     'source_type':'author manuscript explaining classical weighted-automata results',
     'actual_read_scope':'Section 1 definitions and Sections 3–4, PDF pages 5–9; Theorems 3.6 and 4.3 and forward/backward conjugacy.',
     'whole_paper_fully_read':False,
     'discovery':'Official-source web lookup, no professional provider task.'},
    {'id':'Kimura-Fujita-Wille-2512.01186v1',
     'url':'https://arxiv.org/pdf/2512.01186v1',
     'local_reading_copy':'kimura_fujita_wille_2512.01186v1.pdf',
     'source_type':'preprint v1, not asserted peer reviewed',
     'actual_read_scope':'Sections II–IV and V.C–VI, PDF pages 2–3 and 5–6; weighted DD definition, heuristic ordering, Shor scope and float caveat.',
     'whole_paper_fully_read':False,
     'discovery':'New KQB2497 Scholar metadata; followed to actual official PDF.'}
]
for source in sources:
    path = ROOT/source['local_reading_copy']
    source.update(bytes=path.stat().st_size,sha256=sha(path),
                  redistribute_full_document_in_research_package=False)
write('READING_EVIDENCE.json', {'schema':'BOUNDED_PRIMARY_READING_EVIDENCE_V1',
    'authority_scope':'Direct partial full-text reading at stated sections; not merely abstract retrieval; not a claim to have read every page.',
    'sources':sources,
    'metadata_only_hits':'Seven other KQB2497 records were not followed to full text.',
    'scientific_executions_in_this_unit':0,
    'query_cache_commit':'ed11167f4102d004e010643d74c00f0c658556a0',
    'professional_queries_submitted':1,'queries_retried':0,
    'copyright_scope':'Publication includes bibliographic metadata, reading scopes, document hashes and original research note only; full local PDF/text reading copies excluded.'})

excluded = {'KQB_FIRST_READBACK.json','KQB_FINAL_READBACK.json','KQB_RESULT.json'}
files, local_only = [], []
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or '__pycache__' in path.parts or path.name == 'PUBLICATION_MANIFEST.json':
        continue
    relative = path.relative_to(ROOT).as_posix()
    item = {'path':relative,'bytes':path.stat().st_size,'sha256':sha(path)}
    if path.suffix in ('.pdf','.txt') or path.name in excluded:
        item['reason'] = 'Full reading text or unabridged provider snippet transport, retained locally; official URL/Issue and exact metadata extraction remain in published evidence.'
        local_only.append(item)
    else:
        files.append(item)
write('PUBLICATION_MANIFEST.json', {'schema':'BOUNDED_PRIOR_ART_PUBLICATION_ALLOWLIST_V1',
    'status':'FROZEN_SHARED_CONTEXT_READING_AND_SYMBOLIC_REVIEW',
    'publication_files':files,'local_only_files':local_only,
    'instruction':'Publish only publication_files plus this manifest; do not recursively include the local PDF/text/raw-snippet files.',
    'query_archive_status':'ARCHIVED_VERIFIED',
    'query_archive_commit':'ed11167f4102d004e010643d74c00f0c658556a0',
    'no_new_scientific_execution':True})
print(json.dumps({'publication_files':len(files),'local_only_files':len(local_only),
    'note_sha256':sha(ROOT/'PRIOR_ART_AND_USABLE_LEMMAS.md'),
    'manifest_sha256':sha(ROOT/'PUBLICATION_MANIFEST.json'),
    'reading_sha256':sha(ROOT/'READING_EVIDENCE.json')},indent=2))
