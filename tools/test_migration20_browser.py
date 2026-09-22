#!/usr/bin/env python3
"""Execute the real shared arithmetic script in Chromium, without navigation.

No digest adapter is installed. This covers synchronous arithmetic/certificates,
not native WebCrypto population hashing, the Phase32 UI, or saved-file loading.
"""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import certified_hex as c
from nollm_visual_toolkit.angular_dispersion_browser import SCRIPT as ANGULAR
from nollm_visual_toolkit.certified_hex_browser import SCRIPT
from playwright.sync_api import sync_playwright

def main():
    checks=[];errors=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    mod=1<<32
    phases=[(t,64,m) for m in (4,256,65536,mod) for t in (0,1,m//4,m//2,m-1)]
    args=[(n,t,sn,sd) for n in (1,3,4,65535) for t in (1,mod//4,mod//2+1,mod-1) for sn,sd in ((1,2),(1,1),(3,2))]
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
        page=browser.new_page();page.on('pageerror',lambda e:errors.append(str(e)))
        page.set_content('<!doctype html><meta charset="utf-8"><title>M20 arithmetic check</title>')
        page.add_script_tag(content=ANGULAR);page.add_script_tag(content=SCRIPT)
        observed=page.evaluate('(v)=>v.map(x=>NollmCertifiedHex.phaseBounds(...x).map(a=>a.record()))',phases)
        check('four_carrier_bounds_equal_python',observed==[[x.as_record() for x in c.phase_bounds(*v)] for v in phases])
        observed=page.evaluate('(v)=>v.map(x=>NollmCertifiedHex.locate(...x,{phaseModulus:"4294967296"}))',args)
        expected=[c.PolarSource(*v,mod).locate() for v in args]
        check('48_full_certificates_equal_python',observed==expected)
        check('uint32_max_tick_retained',observed[-1]['source']['phase_tick']==str(mod-1))
        check('all_records_replay',page.evaluate('(v)=>v.every(x=>NollmCertifiedHex.verifyCellRecord(x))',observed))
        altered=json.loads(json.dumps(observed[0]));altered['source']['phase_modulus']='65536'
        check('wrong_carrier_rejected',not page.evaluate('(v)=>NollmCertifiedHex.verifyCellRecord(v)',altered))
        pitch=page.evaluate('NollmCertifiedHex.parsePitch("0.50")')
        check('literal_pitch_preserved',pitch==dict(text='0.50',numerator='50',denominator='100',syntax='DECIMAL',unreduced=True))
        tie=page.evaluate('NollmCertifiedHex.adaptPhase32Cell(NollmCertifiedHex.locate(4,1073741824,1,2,{phaseModulus:"4294967296"}))')
        check('caller_tie_and_base_both_preserved',tie['cell']==['-1','1'] and tie['base_certificate']['cell']==['0','1'])
        record=page.evaluate('''()=>{const old=Math.sqrt;Math.sqrt=()=>{throw Error('floating sqrt');};try{return NollmCertifiedHex.locate(17,4294967295,1,1,{phaseModulus:"4294967296"});}finally{Math.sqrt=old;}}''')
        check('no_floating_sqrt',record==c.PolarSource(17,mod-1,1,1,mod).locate())
        check('no_uncaught_errors',not errors)
        result=dict(schema='M20_CHROMIUM_ARITHMETIC_V1',checks=len(checks),passed=checks,page_errors=errors,
                    chromium_version=browser.version,execution='SET_CONTENT_WITH_M20_SHARED_ARITHMETIC_SCRIPT',
                    record_comparisons=len(args),phase_comparisons=len(phases),
                    no_digest_adapter=True,native_navigation=False,phase32_ui_tested=False,
                    native_browser_webcrypto_population=False)
        browser.close()
    out=ROOT/'evidence/migration20/browser.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));return 0
if __name__=='__main__':raise SystemExit(main())
