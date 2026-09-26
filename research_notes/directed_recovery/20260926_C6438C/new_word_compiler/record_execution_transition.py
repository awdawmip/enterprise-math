from pathlib import Path
import hashlib,json

root=Path(__file__).resolve().parent
files=['certified_word_compiler.py','CERTIFIED_WORD_COMPILER_CHECKS.json.gz',
       'COMPILED_STREAMING_RESULTS.json.gz','COMPILED_FACTORIZATION_RESULTS.json.gz']
record={'reason':'Standalone Python decimal-int serialization cap could reject sufficiently large exact certificates. Remove the I/O cap explicitly; unchanged primitive arithmetic and bounded numerical outputs. Source hash change requires fresh evidence binding.',
 'before':{name:{'bytes':(root/name).stat().st_size,'sha256':hashlib.sha256((root/name).read_bytes()).hexdigest()} for name in files},
 'before_factorization_payload_sha256':'7195bf44dec3994bfc68839e9a66e72e8be92a7f2989bb36b846db11576d8a60',
 'before_factorization_cases':'225 compilation PARTIAL retains15^2; cursor resume complete3^2*5^2;21 complete3*7;21 zero-phase PARTIAL',
 'before_factorization_actual_core_calls':16991,
 'state':'REVALIDATION_REQUIRED_AFTER_PATCH',
 'scope':'I/O/source-binding change log, not a mathematical counterexample or a changed native phase'}
(root/'EXECUTION_CHANGE_LOG.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record))
