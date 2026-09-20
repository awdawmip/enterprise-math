#!/usr/bin/env python3
"""M10 real generated-page startup DOM tests, not native file/http navigation.

Runs set_content on about:blank with an explicit hashlib SHA256 test adapter.
Production HTML has no shim; Node regression uses native Web Crypto separately.
"""
from __future__ import annotations
import argparse,hashlib,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit'),str(ROOT/'tools/nollm_visual_toolkit/tests')]
from nollm_visual_toolkit import multiplicative as m
from test_multiplicative_startup import cli,seed_of
from playwright.sync_api import sync_playwright

SHIM="""() => {
 Object.defineProperty(globalThis.crypto,'subtle',{configurable:true,value:{
  digest:async(name,bytes)=>{
   if(name!=='SHA-256')throw Error('unexpected test digest');
   return new Uint8Array(await globalThis.m10TestSHA256(Array.from(new Uint8Array(bytes.buffer,bytes.byteOffset,bytes.byteLength)))).buffer;
  }
 }});
}"""


def replace_seed(html,seed):
    return re.sub(r'(<script id="lab-seed" type="application/json">).*?(</script>)',lambda q:q[1]+json.dumps(seed,ensure_ascii=False).replace('<','\\u003c')+q[2],html,count=1,flags=re.S)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=ROOT/'evidence/migration10');p.add_argument('--chromium',default='/usr/bin/chromium');a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    checks=[];errors=[]
    def check(name,truth):
        if not truth:raise AssertionError(name)
        checks.append(name);print('PASS',name,flush=True)
    htmlfile=a.out/'cli_exact.html';reportfile=a.out/'cli_report.json'
    code,_,err=cli('--count','64','--scale','2','--cell-scale','0.50','--out',htmlfile,'--report',reportfile)
    if code:raise AssertionError(err)
    html=htmlfile.read_text();report=json.loads(reportfile.read_text());seed=seed_of(htmlfile)
    check('production_html_has_no_test_digest_adapter','m10TestSHA256' not in html)
    with sync_playwright() as pw:
        browser=pw.chromium.launch(executable_path=a.chromium,headless=True,args=['--no-sandbox'])
        native=[]
        def load(text,*,adapter=True,wait=True,setup=None):
            page=browser.new_page(viewport={'width':1440,'height':1100},accept_downloads=True)
            page.on('pageerror',lambda e:errors.append(str(e)))
            native.append(page.evaluate('({secure:isSecureContext,subtle:!!crypto?.subtle})'))
            if adapter:
                page.expose_function('m10TestSHA256',lambda b:list(hashlib.sha256(bytes(b)).digest()))
                page.evaluate(SHIM)
            if setup:page.evaluate(setup)
            page.set_content(text)
            if wait:page.wait_for_function("window.MulLab && ['READY','FAILED'].includes(MulLab.status().state)")
            return page
        page=load(html.replace('function round(x,y){',"function round(x,y){throw Error('old float quantizer invoked');"))
        check('first_load_is_exact_without_manual_toggle',page.evaluate("MulLab.status().cell_status")=='CERTIFIED_ALL')
        check('first_load_full_summary_matches_cli',page.evaluate('MulLab.report().cell_membership_exact')==report['cell_membership_exact'])
        check('source_and_display_scale_match_cli',page.evaluate('MulLab.report().cell_scale_source')==report['cell_scale_source'] and page.evaluate('MulLab.report().config.scale')==2)
        check('actual_controls_receive_original_text',page.locator('#cellScale').input_value()=='0.50' and page.locator('#cellEngine').input_value()=='certified')
        check('actual_cv_is_integer_residual',page.locator('#cvLabel').inner_text().endswith('（整数＋残差）') and page.evaluate('MulLab.stats().area_sector_cv') is None)
        page.wait_for_function('MulLab.status().drawn===64')
        check('all_initial_identities_drawn',page.evaluate('MulLab.status().drawn')==64)
        session=page.evaluate('MulLab.session()');saved=page.evaluate('MulLab.snapshot()')
        check('initial_exact_session_is_v2',session['schema']=='NOLLM_MULTIPLICATIVE_SESSION_V2' and session['cell_options']==seed['cell_options'])
        check('saved_page_has_no_runtime_test_adapter','m10TestSHA256' not in saved)
        # Load from the original unpoisoned page for the saved-HTML re-execution test.
        plain=load(html);saved=plain.evaluate('MulLab.snapshot()');reopened=load(saved)
        check('saved_html_reexecution_keeps_source',reopened.evaluate('MulLab.report().cell_scale_source')==report['cell_scale_source'])
        check('saved_html_reexecution_keeps_all_summary_fields',reopened.evaluate('MulLab.report().cell_membership_exact')==report['cell_membership_exact'])
        plain.locator('summary').click()
        with plain.expect_download() as event:plain.locator('#report').click()
        event.value.save_as(a.out/'downloaded_report.json')
        check('actual_download_keeps_exact_source',json.loads((a.out/'downloaded_report.json').read_text())['cell_scale_source']==report['cell_scale_source'])
        with plain.expect_download() as event:plain.locator('#session').click()
        event.value.save_as(a.out/'downloaded_session.json')
        check('actual_session_download_keeps_options',json.loads((a.out/'downloaded_session.json').read_text())['cell_options']==seed['cell_options'])
        # The frozen A2 tie semantics remain unchanged at the actual startup boundary.
        tiehtml=m.render(a.out/'tie_exact.html',m.config(16,overrides={'2':8192,'3':16384}),cell_scale_text='1/2').read_text()
        tiepage=load(tiehtml)
        expected=m.build_field(m.config(16,overrides={'2':8192,'3':16384}),cell_scale=(1,2))
        for n in (3,4):check('startup_full_tie_certificate_'+str(n),tiepage.evaluate('(n)=>MulLab.certificate(n)',n)==expected['cell_membership_exact']['certificates'][n])
        legacyhtml=m.render(a.out/'legacy.html',m.config(64)).read_text();legacy=load(legacyhtml)
        oldsession=legacy.evaluate('MulLab.session()')
        check('ordinary_default_is_unchanged_legacy',legacy.evaluate('MulLab.status().cell_status')=='LEGACY_FLOAT')
        plain.evaluate('(s)=>MulLab.restore(s)',oldsession)
        check('v1_restore_is_not_laundered_to_exact',plain.evaluate('MulLab.status().cell_status')=='LEGACY_FLOAT' and plain.evaluate('MulLab.session().schema')=='NOLLM_MULTIPLICATIVE_SESSION_V1')
        # Invalid startup must publish FAILED, never a completed legacy fallback.
        badseeds=[{},None,{**seed,'schema':'unknown'}, {'config':seed['config'],'schema':seed['schema']},
                  {**seed,'cell_options':{**seed['cell_options'],'engine':'legacy-float'}},
                  {**seed,'cell_options':{**seed['cell_options'],'scale':.5}},
                  {**seed,'cell_options':{**seed['cell_options'],'scale':'1/5'}},
                  {**seed,'session':session}]
        savedbad={'config':{**session['config'],'count':32},'session':session};badseeds.append(savedbad)
        for i,bad in enumerate(badseeds):
            badpage=load(replace_seed(html,bad))
            state=badpage.evaluate('MulLab.status()')
            check('bad_seed_failed_without_old_results_'+str(i),state['state']=='FAILED' and state['drawn']==0 and all(state[k] is None for k in ('occupied_hex_centers','collision_groups','extra_identities_at_shared_centers','largest_fiber')))
            check('bad_seed_ready_rejects_'+str(i),badpage.evaluate('async()=>{try{await MulLab.ready;return false;}catch(e){return true;}}'))
            badpage.close()
        missing=load(html,setup="() => {Object.defineProperty(crypto,'subtle',{configurable:true,value:undefined});}")
        check('digest_failure_cannot_downgrade_startup',missing.evaluate('MulLab.status().state')=='FAILED')
        check('failed_startup_report_is_unavailable',missing.evaluate('()=>{try{MulLab.report();return false;}catch(e){return true;}}'))
        missing.evaluate(SHIM);missing.evaluate("()=>MulLab.configureCells({engine:'certified',scale:'0.50'})")
        check('failed_startup_can_recover_explicitly',missing.evaluate('MulLab.report().cell_membership_exact')==report['cell_membership_exact'])
        # Hold the digest so the startup is genuinely pending, then replace it.
        pending=load(html,wait=False,setup="""() => {const old=crypto.subtle.digest;crypto.subtle.digest=async(...args)=>{await new Promise(r=>globalThis.releaseM10Digest=r);return old(...args);};}""")
        pending.wait_for_function("window.releaseM10Digest && MulLab.status().state==='COMPUTING'")
        check('pending_startup_reports_no_complete_totals',all(pending.evaluate('MulLab.status()')[k] is None for k in ('occupied_hex_centers','collision_groups','extra_identities_at_shared_centers','largest_fiber')))
        check('pending_startup_report_rejected',pending.evaluate('()=>{try{MulLab.report();return false;}catch(e){return true;}}'))
        pending.evaluate("async()=>{const old=MulLab.ready;await MulLab.configureCells({engine:'legacy-float'});releaseM10Digest();await old;}")
        check('stale_startup_cannot_replace_new_configuration',pending.evaluate('MulLab.status().cell_status')=='LEGACY_FLOAT')
        unresolvedhtml=m.render(a.out/'low_budget.html',m.config(512,'mixed'),cell_scale_text='1',cell_bits=8,cell_max_bits=8).read_text()
        low=load(unresolvedhtml);low.wait_for_function('MulLab.status().drawn===512')
        check('low_budget_initial_state_is_honest_partial',low.evaluate('MulLab.status().cell_status')=='UNRESOLVED_BOUNDARY')
        check('partial_keeps_all_identities',low.evaluate('MulLab.status().drawn')==512)
        check('partial_full_hex_export_is_rejected',low.evaluate('()=>{try{MulLab.hexData();return false;}catch(e){return true;}}'))
        low.screenshot(path=str(a.out/'unresolved_startup.png'),full_page=True)
        check('no_uncaught_page_errors',not errors)
        result={'schema':'M10_STARTUP_DOM_VALIDATION_V1','checks':len(checks),'passed':checks,'page_errors':errors,'chromium_version':browser.version,
                'execution':'REAL_GENERATED_HTML_SET_CONTENT_ABOUT_BLANK','crypto':'EXPLICIT_HASHLIB_TEST_ADAPTER','native_context_before_adapter':native[0],
                'downloads':2,'saved_page_reexecution':True,'native_navigation':False,'safari_ios':False}
        (a.out/'dom_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2));browser.close()
if __name__=='__main__':main()
