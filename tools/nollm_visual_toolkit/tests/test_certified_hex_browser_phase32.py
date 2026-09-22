"""M20 full-record cross-language checks for the shared browser uint32 carrier.

Node uses native Web Crypto, not a mocked digest. Python executes unchanged BRC.
The frozen M19 browser module is an explicit compatibility oracle, not proof of
independent mathematical correctness.
"""
from __future__ import annotations
import copy
import importlib.util
import json
import random
import shutil
import subprocess
import unittest
from pathlib import Path

from nollm_visual_toolkit import certified_hex as py, phase32_lab as phase32
from nollm_visual_toolkit.multiplicative import parse_cell_scale_text
from nollm_visual_toolkit.angular_dispersion_browser import SCRIPT as ANGULAR
from nollm_visual_toolkit.certified_hex_browser import SCRIPT

ROOT = Path(__file__).resolve().parents[3]
M32 = 1 << 32
spec = importlib.util.spec_from_file_location('m20_frozen_browser', ROOT / 'evidence/migration20/frozen_certified_hex_browser.py')
frozen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frozen)

BRIDGE = r'''
const fs=require('node:fs');
async function dispatch(a){
 const C=NollmCertifiedHex;
 if(a.op==='phase')return C.phaseBounds(...a.args).map(x=>x.record());
 if(a.op==='locate')return C.locate(...a.args);
 if(a.op==='lexCell')return C.adaptPhase32Cell(C.locate(...a.args));
 if(a.op==='population')return await C.population(...a.args);
 if(a.op==='lexPopulation')return await C.populationLexicographic(...a.args);
 if(a.op==='phase32')return await C.populationPhase32(...a.args);
 if(a.op==='pitch')return C.parsePitch(...a.args);
 if(a.op==='scale')return C.parseScale(...a.args);
 if(a.op==='verify')return C.verifyCellRecord(...a.args);
 if(a.op==='withoutMath'){
   const saved={};for(const k of ['sqrt','sin','cos','atan2','floor','round','pow','log','log2','hypot']){saved[k]=Math[k];Math[k]=()=>{throw Error('floating Math forbidden');};}
   const N=globalThis.Number;globalThis.Number=new Proxy(N,{apply(){throw Error('Number conversion forbidden');}});
   try{return {record:C.locate(...a.args),pitch:C.parsePitch('0.50')};}
   finally{Object.assign(Math,saved);globalThis.Number=N;}
 }
 if(a.op==='snapshot'){
   const [phi,pn,pd,options]=a.args;let yielded=0;
   options.yieldControl=async()=>{yielded++;phi.fill('0');options.phaseModulus=4;options.initialBits=8;options.maxBits=8;};
   const record=await C.population(phi,pn,pd,options);return {yielded,record};
 }
 if(a.op==='cancel'){
   let calls=0,flag=a.when==='before';
   const options={phaseModulus:'4294967296',includeCertificates:true,
     cancelled:()=>flag,onCell:()=>calls++,yieldControl:async()=>{flag=true;}};
   try{await C.populationPhase32(...a.args,options);return {threw:false,calls};}
   catch(e){return {threw:true,calls,error:e.message};}
 }
 if(a.op==='preflight'){
   let calls=0;const [phi,n,d,opts]=a.args;
   try{await C.population(phi,n,d,{...opts,onCell:()=>calls++});return {rejected:false,calls};}
   catch(e){return {rejected:true,calls};}
 }
 if(a.op==='hashPhase32'){
   const record=await C.populationPhase32(...a.args), certs=record.certificates;
   const canonical=x=>x===null||typeof x!=='object'?JSON.stringify(x):Array.isArray(x)?'['+x.map(canonical).join(',')+']':'{'+Object.keys(x).sort().map(k=>JSON.stringify(k)+':'+canonical(x[k])).join(',')+'}';
   const sha=x=>require('node:crypto').createHash('sha256').update(canonical(x)).digest('hex');
   return {summary:Object.fromEntries(Object.entries(record).filter(([k])=>k!=='certificates')),
     certificates_sha256:sha(certs),cells_sha256:sha(certs.map(r=>r.cell)),full_record_sha256:sha(record)};
 }
 throw Error('unknown op');
}
(async()=>{const requests=JSON.parse(fs.readFileSync(0,'utf8')),out=[];
 for(const a of requests){try{out.push({ok:true,result:await dispatch(a)});}catch(e){out.push({ok:false,error:e.name+': '+e.message});}}
 process.stdout.write(JSON.stringify(out));
})().catch(e=>{console.error(e);process.exit(1);});
'''

def invoke(requests, *, old=False, timeout=180):
    node = shutil.which('node')
    if node is None:
        raise RuntimeError('Node is required; no silent numerical skip')
    run = subprocess.run([node, '-e', ANGULAR + (frozen.SCRIPT if old else SCRIPT) + BRIDGE],
                         input=json.dumps(requests), text=True, capture_output=True, timeout=timeout)
    if run.returncode:
        raise AssertionError(run.stderr)
    return json.loads(run.stdout)


def results(requests, *, old=False):
    reply = invoke(requests, old=old)
    if not all(x['ok'] for x in reply):
        raise AssertionError(reply)
    return [x['result'] for x in reply]


def actual_phase(count=64, mode='golden', **kwargs):
    model = phase32.build(dict(count=count, mode=mode, **kwargs))
    return [None, *model['phase'][1:]]


class BrowserPhase32Tests(unittest.TestCase):
    def test_default_sources_and_bounds_match_frozen_m19(self):
        rng = random.Random(20260922)
        reqs = [{'op':'locate','args':[rng.randrange(1,4096),rng.randrange(65536),3,2]} for _ in range(60)]
        reqs += [{'op':'phase','args':[tick,64]} for tick in (0,1,16383,16384,16385,32768,49152,65535)]
        self.assertEqual(results(reqs), results(reqs, old=True))

    def test_default_base_and_lex_population_records_unchanged(self):
        reqs=[]
        for mode in ('golden','hash','spiral'):
            phi=[None, *[v % 65536 for v in actual_phase(64,mode)[1:]]]
            for op in ('population','lexPopulation'):
                reqs.append({'op':op,'args':[phi,2,2,{'includeCertificates':True}]})
        self.assertEqual(results(reqs), results(reqs,old=True))

    def test_every_supported_carrier_matches_python_bounds(self):
        cases=[]
        for k in range(2,33):
            m=1<<k
            for tick in sorted(set((0,1,m//4-1,m//4,m//2+1,m-1))):
                for bits in (8,96):cases.append((tick,bits,m))
        got=results([{'op':'phase','args':v} for v in cases])
        self.assertEqual(got,[[x.as_record() for x in py.phase_bounds(*v)] for v in cases])

    def test_cache_keys_include_modulus_and_half_angle_depth(self):
        cases=[(1,64,m) for m in (65536,M32,4,256,M32,65536,4)]
        got=results([{'op':'phase','args':v} for v in cases])
        self.assertEqual(got,[[x.as_record() for x in py.phase_bounds(*v)] for v in cases])
        self.assertNotEqual(got[0],got[1]);self.assertEqual(got[0],got[5])

    def test_uint32_sign_boundary_and_maximum_tick_not_truncated(self):
        ticks=(1,(1<<31)-1,1<<31,(1<<31)+1,M32-2,M32-1)
        reqs=[{'op':'locate','args':[65535,str(t),1,1,{'phaseModulus':str(M32)}]} for t in ticks]
        self.assertEqual(results(reqs),[py.PolarSource(65535,t,1,1,M32).locate() for t in ticks])
        self.assertTrue(all(not r['ok'] for r in invoke([{'op':'phase','args':[t,64,M32]} for t in (-1,M32)])))

    def test_modulus_validation_before_cache_or_callbacks(self):
        invalid=(None,True,0,1,2,3,6,12,(1<<32)+1,1<<33,'04','1e3','4294967296.0')
        reqs=[{'op':'preflight','args':[[None,0],1,1,{'phaseModulus':v}]} for v in invalid]
        for got in results(reqs):self.assertEqual(got,{'rejected':True,'calls':0})

    def test_mixed_precision_full_records_and_zero(self):
        rng=random.Random(89);reqs=[];expected=[]
        for m in (4,256,65536,M32):
            for bits,maximum in ((8,8),(8,64),(64,192)):
                for n in (0,3,4,37,1023):
                    t=None if n==0 else rng.randrange(m)
                    reqs.append({'op':'locate','args':[n,t,3,2,{'phaseModulus':m,'initialBits':bits,'maxBits':maximum}]})
                    expected.append(py.PolarSource(n,t,3,2,m).locate(initial_bits=bits,max_bits=maximum))
        self.assertEqual(results(reqs),expected)

    def test_complete_record_verification_uses_saved_carrier(self):
        original=py.PolarSource(3,M32//4,1,2,M32).locate()
        variants=[original]
        for key,value in (('phase_modulus','65536'),('phase_modulus',M32),('phase_tick','1'),('observer','NATIVE_X6')):
            r=copy.deepcopy(original);r['source'][key]=value;variants.append(r)
        r=copy.deepcopy(original);r['root_certificates'][0]['polynomial_residual']='7';variants.append(r)
        self.assertEqual(results([{'op':'verify','args':[r]} for r in variants]),[True]+[False]*5)

    def test_generic_uint32_population_full_record_matches_python(self):
        phi=actual_phase(96,'hash',seed=123)
        for bits in (8,64):
            opts={'phaseModulus':str(M32),'initialBits':bits,'maxBits':bits,'includeCertificates':True}
            got=results([{'op':'population','args':[phi,3,2,opts]}])[0]
            self.assertEqual(got,py.certified_population(phi,3,2,phase_modulus=M32,initial_bits=bits,max_bits=bits,include_certificates=True))

    def test_phase32_adapter_preserves_full_python_population(self):
        for mode in ('golden','hash','spiral'):
            phi=actual_phase(128,mode)
            for pn,pd in ((50,100),(2,2),(3,2)):
                got=results([{'op':'phase32','args':[phi,pn,pd,{'includeCertificates':True}]}])[0]
                expected=phase32._lexicographic_cells([0,*phi[1:]],pn,pd,initial_bits=64,max_bits=192)
                self.assertEqual(got,expected)

    def test_lexicographic_tie_retains_different_base_selection(self):
        phi=actual_phase(16,overrides={'2':M32//8})
        got=results([{'op':'phase32','args':[phi,2,1,{'includeCertificates':True}]}])[0]
        c=got['certificates'][4]
        self.assertEqual(c['cell'],['-1','1']);self.assertEqual(c['base_certificate']['cell'],['0','1'])
        self.assertEqual(c['status'],'CERTIFIED_TIE')
        self.assertEqual(got,phase32._lexicographic_cells([0,*phi[1:]],2,1,initial_bits=64,max_bits=192))

    def test_positive_counts_exclude_zero_but_identity_is_retained(self):
        got=results([{'op':'phase32','args':[[None,0],10,1,{'includeCertificates':True}]}])[0]
        self.assertEqual(got['population'],'2');self.assertEqual(got['positive_population'],'1')
        self.assertEqual(len(got['certificates']),2);self.assertEqual(got['collision_excess'],'0')
        self.assertEqual(got['max_cell_multiplicity'],'1')
        self.assertEqual(got['certificates'][0]['base_certificate']['source']['phase_tick'],None)

    def test_pitch_lexical_source_matches_existing_python_parser(self):
        texts=['0.50','2/2','3','0.25','8','1/'+'9'*80,'0.'+'0'*60+'1']
        self.assertEqual(results([{'op':'pitch','args':[t]} for t in texts]),[parse_cell_scale_text(t)[1] for t in texts])
        scales=['0.50','1','1.20','2/2','3']
        reqs=[{'op':'scale','args':[t]} for t in scales]
        self.assertEqual(results(reqs),results(reqs,old=True))

    def test_pitch_rejects_float_and_noncanonical_text(self):
        texts=[0.5,1,None,True,'','.5','1.','1e-3','0','0.00','01/2','1/02','1/0','+1',' 1','1 ','nan','1'*257]
        self.assertTrue(all(not x['ok'] for x in invoke([{'op':'pitch','args':[t]} for t in texts])))

    def test_low_budget_keeps_unresolved_and_null_totals(self):
        phi=actual_phase(256,'hash')
        opts={'includeCertificates':True,'initialBits':8,'maxBits':8}
        got=results([{'op':'phase32','args':[phi,1,1,opts]}])[0]
        self.assertEqual(got,phase32._lexicographic_cells([0,*phi[1:]],1,1,initial_bits=8,max_bits=8))
        self.assertEqual(got['status'],'UNRESOLVED_BOUNDARY')
        for key in ('occupied_cells','collision_excess','max_cell_multiplicity'):self.assertIsNone(got[key])
        self.assertTrue(got['unresolved_identities'])

    def test_snapshot_survives_mutation_during_async_yield(self):
        phi=actual_phase(300,'hash')
        opts={'phaseModulus':M32,'includeCertificates':True}
        got=results([{'op':'snapshot','args':[phi,3,2,opts]}])[0]
        self.assertEqual(got['yielded'],2)
        self.assertEqual(got['record'],py.certified_population(phi,3,2,phase_modulus=M32,include_certificates=True))

    def test_cancellation_is_not_a_partial_success(self):
        phi=actual_phase(300,'golden')
        for when,calls in (('before',0),('yield',128)):
            got=results([{'op':'cancel','when':when,'args':[phi,1,1]}])[0]
            self.assertTrue(got['threw']);self.assertEqual(got['calls'],calls)
            self.assertEqual(got['error'],'CERTIFICATION_CANCELLED')

    def test_phase32_rejects_conflicting_modulus_or_invalid_inputs(self):
        opts=({'phaseModulus':65536},{'phaseModulus':None},{'includeCertificates':1},{'initialBits':128,'maxBits':64})
        reqs=[{'op':'phase32','args':[[None,0],1,1,o]} for o in opts]
        reqs += [{'op':'phase32','args':[[None,0],n,d]} for n,d in ((0,1),(1,0),(True,1),(1,1.5))]
        self.assertTrue(all(not r['ok'] for r in invoke(reqs)))

    def test_no_float_math_or_number_conversion_in_source_computation(self):
        args=['65535',str(M32-1),'3','2',{'phaseModulus':str(M32)}]
        got=results([{'op':'withoutMath','args':args}])[0]
        self.assertEqual(got['record'],py.PolarSource(65535,M32-1,3,2,M32).locate())
        self.assertEqual(got['pitch'],parse_cell_scale_text('0.50')[1])

    def test_summary_and_full_certificates_have_identical_counts(self):
        phi=actual_phase(32,'hash')
        small,full=results([{'op':'phase32','args':[phi,2,2,{'includeCertificates':v}]} for v in (False,True)])
        self.assertIsNone(small['certificates']);full['certificates']=None;self.assertEqual(small,full)


if __name__=='__main__':unittest.main(verbosity=2)
