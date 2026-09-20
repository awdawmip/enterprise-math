from __future__ import annotations
import json
import shutil
import subprocess
import unittest

from nollm_visual_toolkit import certified_hex as base
from nollm_visual_toolkit import multiplicative as mul
from nollm_visual_toolkit.angular_dispersion_browser import SCRIPT as ANGULAR
from nollm_visual_toolkit.certified_hex_browser import SCRIPT as CELLS

BRIDGE=r'''
const fs=require('node:fs');
async function dispatch(a){
 const C=NollmCertifiedHex;
 if(a.op==='adapt')return C.adaptLexicographicCell(C.locate(...a.args));
 if(a.op==='lexPopulation')return await C.populationLexicographic(...a.args);
 if(a.op==='onCell'){
   const seen=[];const args=a.args.slice(),options=args[3]??{};
   args[3]={...options,onCell:(rec,i)=>seen.push([i,rec])};
   const result=await C.populationLexicographic(...args);return {result,seen};
 }
 if(a.op==='withoutMathLex'){
   const old={};for(const k of ['sqrt','sin','cos','atan2','floor','round','pow']){old[k]=Math[k];Math[k]=()=>{throw Error('floating Math forbidden');};}
   try{return C.adaptLexicographicCell(C.locate(...a.args));}finally{Object.assign(Math,old);}
 }
 throw Error('unknown op');
}
(async()=>{const requests=JSON.parse(fs.readFileSync(0,'utf8')),out=[];for(const a of requests){try{out.push({ok:true,result:await dispatch(a)});}catch(e){out.push({ok:false,error:e.name+': '+e.message});}}console.log(JSON.stringify(out));})().catch(e=>{console.error(e);process.exit(1);});
'''


def invoke(requests):
    if not shutil.which('node'):
        raise RuntimeError('Node is required: no silent skips')
    run=subprocess.run(['node','-e',ANGULAR+CELLS+BRIDGE],input=json.dumps(requests),text=True,capture_output=True,timeout=180)
    if run.returncode:
        raise AssertionError(run.stderr)
    return json.loads(run.stdout)


def results(requests):
    out=invoke(requests)
    for row in out:
        if not row['ok']:
            raise AssertionError(row)
    return [row['result'] for row in out]


def wrapped(source):
    cell=mul._lexicographic_tie_cell(source) if source['status']=='CERTIFIED_TIE' else source['cell']
    return {'schema':'NOLLM_MULTIPLICATIVE_CELL_CERTIFICATE_V1','status':source['status'],'cell':cell,
            'tie_rule':mul.LEXICOGRAPHIC_CELL_TIE_RULE,'base_certifier_tie_rule':source.get('tie_rule'),
            'base_certificate':source}


def phi_for(count,scheme):
    cfg=mul.config(count,scheme)
    _,_,phase,_=mul._phase_state(cfg)
    return [None,*phase[1:]]


class LexicographicBrowserAdapterTests(unittest.TestCase):
    def test_known_tie_rule_difference_full_wrapper(self):
        cases=[(4,16384,1,2),(3,16384,1,2),(28,16384,1,2),(811,16384,1,1)]
        got=results([{'op':'adapt','args':case} for case in cases])
        expected=[wrapped(base.PolarSource(*case).locate()) for case in cases]
        self.assertEqual(got,expected)
        self.assertEqual(expected[0]['base_certificate']['cell'],['0','1'])
        self.assertEqual(expected[0]['cell'],['-1','1'])

    def test_full_population_wrapper_matches_python_m06(self):
        requests=[];expected=[]
        for count in (16,64,256):
            for scheme in ('valuation','mixed','spiral','radial'):
                phi=phi_for(count,scheme)
                for sn,sd in ((1,2),(1,1),(3,2)):
                    requests.append({'op':'lexPopulation','args':[phi,sn,sd,{'includeCertificates':True}]})
                    expected.append(mul._certified_lexicographic_population(phi,sn,sd,initial_bits=64,max_bits=192))
        self.assertEqual(results(requests),expected)

    def test_unresolved_population_matches_python(self):
        phi=phi_for(512,'mixed');options={'initialBits':8,'maxBits':8,'includeCertificates':True}
        got=results([{'op':'lexPopulation','args':[phi,1,1,options]}])[0]
        want=mul._certified_lexicographic_population(phi,1,1,initial_bits=8,max_bits=8)
        self.assertEqual(got,want)
        self.assertEqual(got['status'],'UNRESOLVED_BOUNDARY')
        self.assertTrue(got['unresolved_identities'])
        for key in ('occupied_cells','collision_groups','excess_identities_if_collapsed','max_cell_load'):
            self.assertIsNone(got[key])

    def test_finite_tie_audit_reproduces_1080_and_504(self):
        cases=[]
        for sn,sd in ((1,2),(1,1),(3,2)):
            for t in (0,16384,32768,49152):
                cases.append((0,None,sn,sd))
                cases.extend((n,t,sn,sd) for n in range(1,513))
        base_records=[base.PolarSource(*case).locate() for case in cases]
        tie_cases=[case for case,record in zip(cases,base_records) if record['status']=='CERTIFIED_TIE']
        tie_records=[record for record in base_records if record['status']=='CERTIFIED_TIE']
        got=results([{'op':'adapt','args':case} for case in tie_cases])
        want=[wrapped(record) for record in tie_records]
        self.assertEqual(got,want)
        differences=sum(record['cell']!=adapted['cell'] for record,adapted in zip(tie_records,want))
        self.assertEqual(len(tie_records),1080)
        self.assertEqual(differences,504)

    def test_incremental_on_cell_callback_receives_adapted_records(self):
        phi=phi_for(64,'valuation')
        got=results([{'op':'onCell','args':[phi,1,2,{'includeCertificates':False}]}])[0]
        full=mul._certified_lexicographic_population(phi,1,2,initial_bits=64,max_bits=192)
        self.assertIsNone(got['result']['certificates'])
        self.assertEqual([record for _,record in got['seen']],full['certificates'])
        self.assertEqual([i for i,_ in got['seen']],list(range(64)))

    def test_adapter_has_no_floating_math_dependency(self):
        self.assertNotIn('Math.',CELLS)
        case=(10007,12345,3,2)
        got=results([{'op':'withoutMathLex','args':case}])[0]
        self.assertEqual(got,wrapped(base.PolarSource(*case).locate()))

    def test_invalid_include_certificates_rejected_before_population(self):
        phi=phi_for(16,'valuation')
        out=invoke([{'op':'lexPopulation','args':[phi,1,1,{'includeCertificates':1}]}])[0]
        self.assertFalse(out['ok'])


if __name__=='__main__':
    unittest.main(verbosity=2)
