"""Cross-language FULL-record checks; Node uses its native Web Crypto digest.

No browser DOM mocks are used by this suite. Python M03 executes unchanged BRC.
All large numeric inputs cross JSON as decimal strings, not rounded Numbers.
"""
from __future__ import annotations
import json
import random
import shutil
import subprocess
import unittest
from pathlib import Path
from nollm_visual_toolkit import certified_hex as py
from nollm_visual_toolkit.angular_dispersion_browser import SCRIPT as ANGULAR
from nollm_visual_toolkit.certified_hex_browser import SCRIPT as CELLS
from nollm_visual_toolkit.multiplication_lab import smallest_factors,prime_phases,phases

BRIDGE=r'''
const fs=require('node:fs');
async function dispatch(a){
 const C=NollmCertifiedHex;
 if(a.op==='locate')return C.locate(...a.args);
 if(a.op==='round')return C.roundAxial(...a.args);
 if(a.op==='root'){const [v,r]=C.rootRatioBound(...a.args);return [v.record(),r];}
 if(a.op==='phase')return C.phaseBounds(...a.args).map(x=>x.record());
 if(a.op==='population')return await C.population(...a.args);
 if(a.op==='scale')return C.parseScale(a.args[0]);
 if(a.op==='verify')return C.verifyCellRecord(a.args[0]);
 if(a.op==='mul'){const [a0,a1,b0,b1,b]=a.args;return new C.Interval(a0,a1,b).mul(new C.Interval(b0,b1,b)).record();}
 if(a.op==='box')return C.certifyBox(...a.args.map(x=>new C.Interval(...x)));
 if(a.op==='division'){const t=NollmAngularExact.evaluateDivision(...a.args);return Object.fromEntries(Object.entries(t).map(([k,v])=>[k,String(v)]));}
 if(a.op==='withoutMath'){
  const old={};for(const k of ['sqrt','sin','cos','atan2','floor','round','pow']){old[k]=Math[k];Math[k]=()=>{throw Error('floating Math forbidden');};}
  try{return C.locate(...a.args);}finally{Object.assign(Math,old);}
 }
 throw Error('unknown bridge op');
}
(async()=>{const requests=JSON.parse(fs.readFileSync(0,'utf8')),out=[];
 for(const a of requests){try{out.push({ok:true,result:await dispatch(a)});}catch(e){out.push({ok:false,error:e.name+': '+e.message});}}
 console.log(JSON.stringify(out));
})().catch(e=>{console.error(e);process.exit(1);});
'''

def invoke(requests):
    if not shutil.which('node'):
        raise RuntimeError('Node is required: no silent skips')
    result=subprocess.run(['node','-e',ANGULAR+CELLS+BRIDGE],input=json.dumps(requests),text=True,capture_output=True,timeout=150)
    if result.returncode:raise AssertionError(result.stderr)
    return json.loads(result.stdout)

def results(requests):
    outputs=invoke(requests)
    for r in outputs:
        if not r['ok']:raise AssertionError(r)
    return [r['result'] for r in outputs]

class CertifiedHexBrowserTests(unittest.TestCase):
    def test_signed_rational_cells_full_record(self):
        cases=[(q,r,d) for d in range(1,13) for q in range(-8,9) for r in range(-8,9)]
        self.assertEqual(results([{'op':'round','args':v} for v in cases]),[py.round_axial(*v) for v in cases])

    def test_root_ratio_certificates_full_record(self):
        cases=[(n,d,b) for n in range(25) for d in (1,2,3,7,19) for b in (8,32,64)]
        expected=[]
        for v in cases:
            i,r=py.root_ratio_bound(*v);expected.append([i.as_record(),r])
        self.assertEqual(results([{'op':'root','args':v} for v in cases]),expected)

    def test_outward_interval_products_full_record(self):
        cases=[(a,a+w,b,b+z,8) for a in range(-4,5) for b in range(-4,5) for w in (0,1,3) for z in (0,1,3)]
        self.assertEqual(results([{'op':'mul','args':v} for v in cases]),[(py.DyadicInterval(a,h,t)*py.DyadicInterval(b,k,t)).as_record() for a,h,b,k,t in cases])

    def test_phase_bounds_full_record(self):
        rng=random.Random(20260920)
        ticks=sorted(set([0,1,8192,16383,16384,16385,32768,49152,65535]+rng.sample(range(65536),512)))
        cases=[(t,b) for t in ticks for b in (8,64,128)]
        self.assertEqual(results([{'op':'phase','args':v} for v in cases]),[[i.as_record() for i in py.phase_bounds(*v)] for v in cases])

    def test_cardinal_shared_radicals_full_record(self):
        cases=[(n,t,sn,sd) for n in range(1,65) for t in (0,16384,32768,49152) for sn,sd in ((1,2),(1,1),(3,2))]
        self.assertEqual(results([{'op':'locate','args':v} for v in cases]),[py.PolarSource(*v).locate() for v in cases])

    def test_mixed_precision_polar_full_record(self):
        rng=random.Random(41)
        cases=[(rng.randrange(1,65536),rng.randrange(65536),sn,sd,b,m) for sn,sd in ((1,2),(1,1),(3,2)) for b,m in ((8,8),(8,64),(64,192)) for _ in range(32)]
        self.assertEqual(results([{'op':'locate','args':[n,t,sn,sd,{'initialBits':b,'maxBits':m}]} for n,t,sn,sd,b,m in cases]),[py.PolarSource(n,t,sn,sd).locate(initial_bits=b,max_bits=m) for n,t,sn,sd,b,m in cases])

    def test_large_integer_source_and_literal_denominator(self):
        cases=[((1<<200)+1,12345,(1<<80)+1,(1<<80)+3),(3,16384,10,20),(0,None,2,2)]
        requests=[{'op':'locate','args':[str(n),t,str(sn),str(sd),{'initialBits':256,'maxBits':512}]} for n,t,sn,sd in cases]
        self.assertEqual(results(requests),[py.PolarSource(*v).locate(initial_bits=256,max_bits=512) for v in cases])

    def test_exact_tie_discrepancy_and_irrational_symmetry(self):
        cases=[(3,16384,1,2),(2927,16384,1,2),(811,16384,1,1),(811,16384,3,2)]
        actual=results([{'op':'locate','args':v} for v in cases])
        self.assertEqual(actual,[py.PolarSource(*v).locate() for v in cases])
        self.assertEqual(actual[0]['cell'],['-1','1'])
        self.assertTrue(all(v['cell'] is not None for v in actual))

    def test_complete_population_records(self):
        requests=[];expected=[]
        for count in (16,64,256):
            spf=smallest_factors(count)
            for mode in ('golden','rank','zero'):
                phi=phases(spf,prime_phases(spf,mode))
                for sn,sd in ((1,2),(1,1),(3,2)):
                    requests.append({'op':'population','args':[phi,sn,sd]})
                    expected.append(py.certified_population(phi,sn,sd))
        self.assertEqual(results(requests),expected)

    def test_population_all_certificates_and_unresolved(self):
        spf=smallest_factors(128);phi=phases(spf,prime_phases(spf))
        options={'initialBits':8,'maxBits':8,'includeCertificates':True}
        got=results([{'op':'population','args':[phi,1,2,options]}])[0]
        want=py.certified_population(phi,1,2,initial_bits=8,max_bits=8,include_certificates=True)
        self.assertEqual(got,want);self.assertEqual(got['status'],'UNRESOLVED_BOUNDARY')
        for k in ('occupied_cells','collision_groups','excess_identities_if_collapsed','max_cell_load'):self.assertIsNone(got[k])
        self.assertTrue(got['unresolved_identities'])

    def test_canonical_text_scale_preserves_literal_source(self):
        text=['1','0.50','1.20','3/2','2/2','1.'+'0'*100]
        expected=[('1','1'),('50','100'),('120','100'),('3','2'),('2','2'),('1'+'0'*100,'1'+'0'*100)]
        actual=results([{'op':'scale','args':[v]} for v in text])
        self.assertEqual(actual,[{'text':s,'numerator':n,'denominator':d} for s,(n,d) in zip(text,expected)])

    def test_reject_float_or_noncanonical_scale(self):
        invalid=[0.5,1,True,None,' 1','1 ','01','1e0','+1','1/0','1//2','0','0.49','3.01','NaN','Infinity','1.','1/'+'9'*257]
        self.assertTrue(all(not v['ok'] for v in invoke([{'op':'scale','args':[v]} for v in invalid])))

    def test_strict_record_replay_rejects_tampering(self):
        original=py.PolarSource(3,16384,1,2).locate();bad=[]
        for change in ('cell','root','source','extra','type','schedule'):
            r=json.loads(json.dumps(original))
            if change=='cell':r['cell'][0]='0'
            elif change=='root':r['root_certificates'][0]['polynomial_residual']='0'
            elif change=='source':r['source']['observer']='FAKE'
            elif change=='extra':r['extra']=True
            elif change=='type':r['source']['n']=3
            else:r['refinement_bits']=['08','64']
            bad.append(r)
        self.assertEqual(results([{'op':'verify','args':[r]} for r in [original]+bad]),[True]+[False]*len(bad))

    def test_invalid_source_and_precision_rejected(self):
        cases=[[0,0],[True,0],[1,1.1],[1,-1],[1,65536],[1,None],[1,0,1,0],[1,0,-1,1],[1,0,1,1,{'initialBits':8,'maxBits':7}],[1,0,1,1,{'initialBits':64,'maxBits':32}],[9007199254740992,0]]
        self.assertTrue(all(not v['ok'] for v in invoke([{'op':'locate','args':v} for v in cases])))

    def test_population_validation_precedes_output(self):
        cases=[[[None,0,False],1,1],[[0,0],1,1],[[None],1,1],[[None,0],1,1,{'includeCertificates':1}],[[None,0],1,1,{'initialBits':128,'maxBits':64}]]
        self.assertTrue(all(not v['ok'] for v in invoke([{'op':'population','args':v} for v in cases])))

    def test_no_floating_math_in_kernel(self):
        self.assertNotIn('Math.',CELLS);self.assertNotIn('parseFloat',CELLS);self.assertNotIn('Number(',CELLS)
        got=results([{'op':'withoutMath','args':[10007,12345,3,2]}])[0]
        self.assertEqual(got,py.PolarSource(10007,12345,3,2).locate())

    def test_box_exact_and_nonintersecting(self):
        cases=[[[0,0,8],[0,0,8],[0,0,8]],[[-128,-128,8],[256,256,8],[-128,-128,8]],[[-3,3,8],[-3,3,8],[-3,3,8]]]
        self.assertEqual(results([{'op':'box','args':v} for v in cases]),[py.certify_box(*(py.DyadicInterval(*x) for x in v)) for v in cases])
        self.assertFalse(invoke([{'op':'box','args':[[1,2,8]]*3}])[0]['ok'])

    def test_shared_brc_division_port_reconstruction(self):
        cases=[(n,d) for n in (0,1,5,100,2**100+1) for d in (1,2,3,97)]
        actual=results([{'op':'division','args':[str(n),str(d)]} for n,d in cases])
        self.assertEqual(actual,[{'quotient':str(n//d),'remainder':str(n%d),'collapsed':str(n//d*d)} for n,d in cases])

if __name__=='__main__':unittest.main(verbosity=2)
