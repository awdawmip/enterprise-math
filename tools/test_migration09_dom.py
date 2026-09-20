#!/usr/bin/env python3
"""M09 real rendered legacy-template DOM tests, not file/http navigation acceptance.

Chromium set_content executes the real page. SHA256 is explicitly a hashlib test
adapter; Node tests separately use native crypto. No managed restriction bypass.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit import multiplicative as m
from playwright.sync_api import sync_playwright
SHIM="""() => {Object.defineProperty(globalThis.crypto,'subtle',{configurable:true,value:{
 digest:async(name,bytes)=>{if(name!=='SHA-256')throw Error('unexpected digest');
 return new Uint8Array(await m09TestSHA256(Array.from(new Uint8Array(bytes.buffer,bytes.byteOffset,bytes.byteLength)))).buffer;}
 }});} """

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=ROOT/'evidence/migration09');p.add_argument('--chromium',default='/usr/bin/chromium');a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 html=m.render(a.out/'lab.html',m.config(256)).read_text()
 original=(ROOT/'evidence/migration09/frozen_multiplicative_lab.html').read_text().replace('__LAB_SEED__',json.dumps({'config':m.config(256)}))
 checks=[];errors=[];captures={}
 def check(name,value):
  if not value:raise AssertionError(name)
  checks.append(name);print('PASS',name,flush=True)
 with sync_playwright() as pw:
  b=pw.chromium.launch(executable_path=a.chromium,headless=True,args=['--no-sandbox'])
  def load(text):
   page=b.new_page(viewport={'width':1450,'height':1100});page.on('pageerror',lambda e:errors.append(str(e)))
   page.expose_function('m09TestSHA256',lambda data:list(hashlib.sha256(bytes(data)).digest()));page.evaluate(SHIM);page.set_content(text);return page
  page=load(html);page.wait_for_function("window.MulLab&&MulLab.status().state==='READY'");old=load(original)
  check('legacy_default_preserved',page.evaluate("MulLab.status().cell_status==='LEGACY_FLOAT'"))
  # Actual original/new UI comparison, not a fabricated numeric fixture.
  for scheme in ('valuation','mixed','spiral','radial'):
   for scale in (.5,1,1.5):
    cfg=m.config(256,scheme,scale)
    prev=old.evaluate('(c)=>{MulLab.build(c);return {data:MulLab.data(),stats:MulLab.stats()};}',cfg)
    now=page.evaluate('async(c)=>{await MulLab.build(c);return {data:MulLab.data(),stats:MulLab.stats()};}',cfg)
    check(f'legacy_original_all_fields_{scheme}_{scale}',prev==now)
  # Exercise actual controls: values stay lexical before certified input parsing.
  page.locator('#cellScale').fill('0.50');page.locator('#cellEngine').select_option('certified');page.wait_for_function("MulLab.status().state==='READY'&&MulLab.status().cell_status==='CERTIFIED_ALL'")
  check('actual_control_preserves_decimal_50_100',page.evaluate("MulLab.data().cell_scale_source.numerator==='50'&&MulLab.data().cell_scale_source.denominator==='100'"))
  check('exact_readout_uses_integer_plus_residual', '1000000' in page.locator('#cv').inner_text() and page.locator('#cellReadout').inner_text().startswith('+ '))
  check('exact_report_no_float_cv_or_error',page.evaluate("()=>{const s=MulLab.stats();return s.angular_cv===null&&s.area_sector_cv===null&&s.iid_cv_scale===null&&s.max_display_quantization_error===null;}"))
  cfg=m.config(64,overrides={'2':8192,'3':16384})
  page.evaluate('async(c)=>{await MulLab.build(c,{engine:"certified",scale:"1/2",initialBits:64,maxBits:192});}',cfg)
  py=m.build_field(cfg,cell_scale=(1,2))['cell_membership_exact']['certificates']
  for n in (3,4):check(f'full_tie_certificate_{n}_matches_python',page.evaluate('(n)=>MulLab.certificate(n)',n)==py[n])
  captures['tie4']=page.evaluate('MulLab.certificate(4)')
  # Tie-specific inputs may legitimately retain other unresolved points.
  page.evaluate('async(c)=>await MulLab.build(c)',m.config(64))
  # Mutating public outputs must not modify source/config or a published proof.
  check('public_outputs_detached',page.evaluate("()=>{const orig=JSON.stringify(MulLab.report()),d=MulLab.data(),h=MulLab.hexData(),s=MulLab.session(),c=MulLab.certificate(4);d.config.scale=99;h.metadata.config.scale=99;s.cell_options.scale='3';c.cell[0]='99';return orig===JSON.stringify(MulLab.report())&&MulLab.certificate(4).cell[0]!=='99';}"))
  # Invalid configuration leaves the previously verified state intact.
  check('invalid_scale_does_not_replace_state',page.evaluate("async()=>{const before=JSON.stringify(MulLab.report());let rejected=false;try{await MulLab.configureCells({scale:'1\\n'});}catch(e){rejected=true;}return rejected&&JSON.stringify(MulLab.report())===before;}"))
  # Stop at a cooperative yield and test every read/export boundary.
  race=page.evaluate("""async()=>{const c={...MulLab.data().config,count:512,scheme:'mixed'};
   const first=MulLab.build(c,{engine:'certified',scale:'1',initialBits:64,maxBits:192});
   const pending=MulLab.status(),blocked={};for(const key of ['data','stats','report','hexData','session','snapshot']){try{MulLab[key]();blocked[key]=false;}catch(e){blocked[key]=true;}}
   try{MulLab.certificate(3);blocked.certificate=false;}catch(e){blocked.certificate=true;}
   const heat=document.getElementById('heat'),pixels=heat.getContext('2d').getImageData(0,0,heat.width,heat.height).data;
   const cleared=Array.from(pixels).every(x=>x===0);
   const second=MulLab.build({...c,count:64,scheme:'radial'},{engine:'certified',scale:'2/2',initialBits:64,maxBits:192});
   const results=await Promise.all([first,second]);return {pending,blocked,cleared,results,last:MulLab.status()};}""")
  check('pending_state_no_old_totals',race['pending']['state']=='COMPUTING' and all(race['pending'][k] is None for k in ('occupied_hex_centers','collision_groups','extra_identities_at_shared_centers','largest_fiber')))
  check('pending_all_read_export_methods_reject',all(race['blocked'].values()))
  check('pending_old_heatmap_cleared',race['cleared'])
  check('last_valid_generation_wins',race['results'][0] is None and race['last']['count']==64 and race['last']['phase_scheme']=='radial' and race['last']['cell_options']['scale']=='2/2')
  # Delayed restore must not overwrite a later build/view selection.
  check('stale_restore_cannot_overwrite_later_selection',page.evaluate("""async()=>{const s=MulLab.session();s.config.count=512;s.config.scheme='mixed';s.view_state.selected=12;s.view_state.view='stack';
   const first=MulLab.restore(s);const second=MulLab.build({...s.config,count:64,scheme:'radial'});
   await Promise.all([first,second]);return MulLab.status().count===64&&MulLab.status().view!=='stack'&&MulLab.status().selected!==12;}"""))
  # Exact session & snapshot keep lexical provenance, old session is never inferred.
  page.evaluate("async()=>await MulLab.configureCells({scale:'0.50'})")
  exactSession=page.evaluate('MulLab.session()');saved=page.evaluate('MulLab.snapshot()')
  check('session_v2_preserves_original_text',exactSession['schema']=='NOLLM_MULTIPLICATIVE_SESSION_V2' and exactSession['cell_options']['scale']=='0.50')
  reload=load(saved);reload.wait_for_function("window.MulLab&&MulLab.status().state==='READY'")
  check('saved_html_set_content_replays_exact_session',reload.evaluate('MulLab.session()')==exactSession)
  check('saved_html_certificate_replay',reload.evaluate('MulLab.certificate(17)')==page.evaluate('MulLab.certificate(17)'))
  reload.close()
  oldSession=dict(exactSession);oldSession.pop('cell_options');oldSession['schema']='NOLLM_MULTIPLICATIVE_SESSION_V1';oldSession['config']=dict(oldSession['config'],scale=1.5)
  page.evaluate('async(s)=>await MulLab.restore(s)',oldSession)
  check('v1_restore_is_legacy_no_float_reverse_inference',page.evaluate("MulLab.status().cell_status==='LEGACY_FLOAT'&&MulLab.session().schema==='NOLLM_MULTIPLICATIVE_SESSION_V1'"))
  forged=dict(oldSession,cell_options=exactSession['cell_options'])
  check('v1_cannot_spoof_exact_options',page.evaluate("async(s)=>{try{await MulLab.restore(s);return false;}catch(e){return MulLab.status().cell_status==='LEGACY_FLOAT';}}",forged))
  # Real SHA failure: remove test interface, don't provide fallback.
  failed=page.evaluate("""async()=>{Object.defineProperty(crypto,'subtle',{configurable:true,value:undefined});let rejected=false;try{await MulLab.configureCells({engine:'certified'});}catch(e){rejected=true;}
   const blocked={};for(const key of ['data','report','hexData','snapshot']){try{MulLab[key]();blocked[key]=false;}catch(e){blocked[key]=true;}}
   return {rejected,blocked,state:MulLab.status()};}""")
  check('sha_failure_rejects_without_float_fallback',failed['rejected'] and failed['state']['state']=='FAILED')
  check('sha_failure_no_stale_exports',all(failed['blocked'].values()) and failed['state']['occupied_hex_centers'] is None)
  page.evaluate(SHIM);page.evaluate('async()=>await MulLab.configureCells({engine:"certified"})')
  check('failure_retry_recovers_and_clears_error',page.evaluate("MulLab.status().state==='READY'") and page.locator('#error').inner_text()=='')
  # Deliberately unresolved populations remain readable as honest partial evidence.
  page.evaluate('async(c)=>await MulLab.build(c,{engine:"certified",scale:"1",initialBits:8,maxBits:8})',m.config(512,'mixed'))
  low=page.evaluate('MulLab.report()');captures['unresolved_report']=low
  check('low_budget_state_explicit',low['cell_membership_exact']['status']=='UNRESOLVED_BOUNDARY')
  check('low_budget_four_complete_totals_null',all(low['statistics'][k] is None for k in ('occupied_hex_centers','collision_groups','extra_identities_at_shared_centers','largest_fiber')))
  check('low_budget_collision_ui_is_not_fake_number',page.locator('#collision').inner_text()=='未判定')
  n=int(low['cell_membership_exact']['unresolved_identities'][0]);page.locator('#query').fill(str(n));page.locator('#find').click()
  check('unresolved_point_no_same_cell_selection',json.loads(page.locator('#detail').inner_text())['hex_qrs'] is None and page.locator('#next').is_disabled())
  check('unresolved_hex_export_is_rejected',page.evaluate("()=>{try{MulLab.hexData();return false;}catch(e){return true;}}"))
  for view in ('ideal','hex','stack'):
   page.locator('#view').select_option(view)
   for color in ('phase','n','prime','omega','loss'):
    page.locator('#color').select_option(color);page.wait_for_timeout(20)
   check('unresolved_all_identities_drawn_'+view,page.evaluate('MulLab.status().drawn')==512)
  page.screenshot(path=str(a.out/'unresolved_dom.png'),full_page=True)
  page.locator('details').evaluate('(el)=>el.open=true')
  with page.expect_download(timeout=8000) as info:page.locator('#report').click()
  download=info.value;download.save_as(str(a.out/'downloaded_unresolved_report.json'))
  downloaded=json.loads((a.out/'downloaded_unresolved_report.json').read_text())
  check('real_download_preserves_unresolved_report',downloaded['cell_membership_exact']==low['cell_membership_exact'])
  # Exact complete data download; template/transport fields stay typed and detached.
  page.evaluate('async()=>await MulLab.configureCells({initialBits:64,maxBits:192,scale:"0.50"})')
  with page.expect_download(timeout=8000) as info:page.locator('#json').click()
  info.value.save_as(str(a.out/'downloaded_hex.json'))
  d=json.loads((a.out/'downloaded_hex.json').read_text())
  check('real_hex_download_retains_all_ids_and_source',len(d['records'])==512 and d['metadata']['cell_scale_source']['text']=='0.50' and d['metadata']['cell_scale_source']['denominator']=='100')
  check('no_uncaught_browser_errors',not errors)
  record={'schema':'M09_REAL_TEMPLATE_DOM_VALIDATION_V1','checks':len(checks),'passed':checks,'page_errors':errors,'chromium_version':b.version,
   'actual_template_blob':'6619c5da7ad03f38766bfc383d60b5505cb863e0','legacy_original_comparisons':12,'real_downloads':2,
   'execution':'SET_CONTENT_ORIGINAL_RENDERED_HTML; SAVED_HTML_REEXECUTED_WITH_SET_CONTENT',
   'digest':'EXPLICIT_HASHLIB_TEST_ADAPTER_NOT_NATIVE_BROWSER_CRYPTO','not_validated':['native_file_or_http_navigation','native_browser_WebCrypto','Safari_iOS','whole_repository','independent_review']}
  (a.out/'dom_validation.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');(a.out/'dom_witnesses.json').write_text(json.dumps(captures,ensure_ascii=False,indent=2)+'\n')
  b.close();print(json.dumps(record,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
