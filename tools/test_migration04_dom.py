#!/usr/bin/env python3
"""Real Chromium DOM/script/layout harness, NOT a navigation acceptance test.

Managed Chromium in this host blocks file: and localhost navigation. set_content
runs the original generated page in about:blank. SHA-256 is explicitly injected
as a TEST adapter backed by Python hashlib; native Web Crypto is separately
covered by the Node differential suite. No production arithmetic is replaced.
"""
from __future__ import annotations
import argparse, ast, hashlib, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit.multiplication_lab import build_lab,smallest_factors,prime_phases,phases
from nollm_visual_toolkit.certified_hex import certified_population,PolarSource
from playwright.sync_api import sync_playwright

SHIM="""() => {
 Object.defineProperty(globalThis.crypto,'subtle',{configurable:true,value:{
 digest:async(name,bytes)=>{
  if(name!=='SHA-256')throw Error('unexpected test digest');
  return new Uint8Array(await globalThis.m04TestSHA256(Array.from(new Uint8Array(bytes.buffer,bytes.byteOffset,bytes.byteLength)))).buffer;
 }}});
}"""

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--out',type=Path,default=ROOT/'evidence/migration04')
 parser.add_argument('--chromium',default='/usr/bin/chromium')
 args=parser.parse_args();args.out.mkdir(parents=True,exist_ok=True)
 html=build_lab(args.out/'lab256.html',count=256).read_text(); checks=[]; errors=[]
 def check(name,truth):
  if not truth:raise AssertionError(name)
  checks.append(name);print('PASS',name,flush=True)
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path=args.chromium,headless=True,args=['--no-sandbox'])
  def load(text,adapter=True):
   page=browser.new_page(viewport={'width':1400,'height':1100})
   page.on('pageerror',lambda e:errors.append(str(e)))
   if adapter:
    page.expose_function('m04TestSHA256',lambda a:list(hashlib.sha256(bytes(a)).digest()))
    page.evaluate(SHIM)
   page.set_content(text)
   page.wait_for_function("window.NumberFieldLab && NumberFieldLab.status().status !== 'COMPUTING'")
   return page
  def literal(path,name):
   tree=ast.parse(path.read_text())
   return ast.literal_eval(next(n.value for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets)))
  original=literal(ROOT/'evidence/migration04/frozen_m03_multiplication_ui.py','TEMPLATE')
  old_angular=literal(ROOT/'evidence/migration04/frozen_m02_angular_dispersion_browser.py','SCRIPT')
  payload=re.search(r'<script id="payload" type="application/json">(.*?)</script>',html,re.S).group(1)
  old_html=original.replace('__LAB_PAYLOAD__',payload).replace('__ANGULAR_EXACT_SCRIPT__',old_angular)
  old_page=load(old_html)
  page=load(html); L='NumberFieldLab'
  check('original_page_and_legacy_default',page.evaluate(L+".status().state.cellEngine")=='legacy-float')
  baseline=page.evaluate(L+'.report()')
  def old_subset(old,new):
   if isinstance(old,dict):return all(k in new and old_subset(v,new[k]) for k,v in old.items() if k!='drawn')
   if isinstance(old,list):return isinstance(new,list) and len(old)==len(new) and all(old_subset(a,b) for a,b in zip(old,new))
   return old==new
  for count in [16,64,256]:
   for mode in ['golden','rank','zero']:
    for scale in [0.5,1,1.5]:
     change={'limit':count-1,'selected':3,'mode':mode,'scale':scale}
     old_page.evaluate('(s)=>NumberFieldLab.configure(s)',change)
     page.evaluate('(s)=>NumberFieldLab.configure(s)',change)
     check('old_ui_fields_'+str(count)+'_'+mode+'_'+str(scale),old_subset(old_page.evaluate(L+'.report()'),page.evaluate(L+'.report()')))
  page.evaluate('(s)=>NumberFieldLab.restore(s)',{'schema':'NOLLM_MULTIPLICATION_SESSION_V2','lab_version':baseline['lab_version'],'data_sha256':baseline['data_sha256'],'state':baseline['state']})

  def conf(ch):page.evaluate('(v)=>NumberFieldLab.configure(v)',ch)
  def match():
   status=page.evaluate(L+'.report()');phi=page.evaluate('Array.from({length:NumberFieldLab.status().population},(_,i)=>NumberFieldLab.phase(i))')
   c=status['cell_scale_source'];s=status['state']
   expected=certified_population(phi,int(c['numerator']),int(c['denominator']),initial_bits=s['cellBits'],max_bits=s['cellMaxBits'])
   return status,status['cell_membership_exact']==expected
  conf({'cellEngine':'certified','cellScale':'1/2','overrides':{'3':16384},'selected':3,'quantized':True})
  check('browser_boundary_cell',page.evaluate(L+'.inspect(3).cell')==[-1,1])
  check('browser_boundary_full_certificate',page.evaluate(L+'.certificate(3)')==PolarSource(3,16384,1,2).locate())
  check('all_population_fields_match_python',match()[1])
  check('exact_does_not_publish_float_metrics',page.evaluate(L+'.report().angular_cv') is None and page.evaluate(L+'.report().quantized_relative_error_mean') is None)
  check('report_marks_pixels_approximate_not_cells',page.evaluate(L+'.report().pixel_rendering_is_approximate') and not page.evaluate(L+'.report().quantization_is_floating'))
  # Exercise the real DOM inputs/listeners rather than only the public API.
  page.locator('#cellScale').fill('0.50');page.locator('#applyCellScale').click()
  page.wait_for_function("NumberFieldLab.status().status==='CERTIFIED_ALL'")
  check('text_input_preserves_unreduced_source',page.evaluate(L+'.report().cell_scale_source')=={'text':'0.50','numerator':'50','denominator':'100'})
  for mode in ['rank','zero','golden']:
   for scale in ['1/2','1','3/2']:
    conf({'mode':mode,'cellScale':scale,'overrides':{},'cellBits':64,'cellMaxBits':192})
    check('ui_python_'+mode+'_'+scale,match()[1])
  for color in ['mod3','prime','n','q16','load']:
   page.locator('#color').select_option(color)
   page.wait_for_function("NumberFieldLab.status().status==='CERTIFIED_ALL'")
   check('color_'+color,page.evaluate(L+'.status().state.color')==color)
  conf({'quantized':True,'stack':True,'pitch':0.75});page.wait_for_timeout(50)
  check('stack_and_quantized_draw_all',page.evaluate(L+'.status().drawn')==256)
  conf({'cellBits':8,'cellMaxBits':8,'stack':False,'pitch':0,'overrides':{},'cellScale':'1','color':'load'})
  st,eq=match();check('unresolved_matches_python',eq and st['status']=='UNRESOLVED_BOUNDARY')
  check('unresolved_totals_null',all(st[k] is None for k in ['occupied_cells','collision_groups','excess_identities_if_collapsed','max_cell_load']))
  n=int(st['cell_membership_exact']['unresolved_identities'][0]);conf({'selected':n})
  check('unresolved_inspection_null_and_next_disabled',page.evaluate(L+f'.inspect({n}).cell') is None and page.locator('#next').is_disabled())
  check('unresolved_ui_explicit','未判定' in page.locator('#occupied').inner_text() and '上下界' in page.locator('#overlap').inner_text())
  check('unresolved_json_safe',json.loads(page.evaluate('JSON.stringify(NumberFieldLab.report())'))['occupied_cells'] is None)
  page.wait_for_timeout(60);page.screenshot(path=str(args.out/'unresolved_dom_harness.png'),full_page=True)
  before=page.evaluate(L+'.snapshot()');caught=page.evaluate("() => {try{NumberFieldLab.configure({cellScale:'0.1e1'});return false;}catch(e){return true;}}")
  check('invalid_input_keeps_state',caught and page.evaluate(L+'.snapshot()')==before)
  conf({'cellScale':'9007199254740993/9007199254740992','cellBits':64,'cellMaxBits':192})
  check('beyond_safe_number_scale_literal',page.evaluate(L+'.report().cell_scale_source.numerator')=='9007199254740993' and match()[1])
  conf({'cellScale':'1','selected':3})
  # Every read during an unfinished generation must say unfinished, never stale.
  raced=page.evaluate("""async()=>{
   const first=NumberFieldLab.configure({mode:'golden',cellScale:'1/2'});
   const mid=NumberFieldLab.status();const inspected=NumberFieldLab.inspect(3);
   let rejected=false;try{NumberFieldLab.report();}catch(e){rejected=true;}
   const second=NumberFieldLab.configure({mode:'zero',cellScale:'3/2'});
   await Promise.all([first,second]);
   return {mid,inspected,rejected,final:NumberFieldLab.report()};
  }""")
  check('pending_cannot_export_old_report',raced['mid']['status']=='COMPUTING' and raced['rejected'])
  check('pending_cannot_inspect_old_cell',raced['inspected']['cell'] is None and raced['inspected']['cell_status']=='COMPUTING')
  check('last_configuration_wins',raced['final']['state']['mode']=='zero' and raced['final']['cell_scale_source']['text']=='3/2' and match()[1])
  snap=page.evaluate(L+'.snapshot()');conf({'mode':'rank'});page.evaluate('(s)=>NumberFieldLab.restore(s)',snap)
  check('v2_snapshot_roundtrip',page.evaluate(L+'.snapshot()')==snap and match()[1])
  old=json.loads(json.dumps(snap));old['schema']='NOLLM_MULTIPLICATION_SESSION_V1'
  for k in ['cellEngine','cellScale','cellBits','cellMaxBits']:old['state'].pop(k)
  old['state']['scale']=1.1
  page.evaluate('(s)=>NumberFieldLab.restore(s)',old)
  check('v1_not_laundered_to_exact',page.evaluate(L+'.status().state.cellEngine')=='legacy-float')
  bad=json.loads(json.dumps(old));bad['state']['cellEngine']='certified'
  check('v1_exact_spoof_rejected',page.evaluate('(s)=>{try{NumberFieldLab.restore(s);return false;}catch(e){return true;}}',bad))
  page.evaluate('(s)=>NumberFieldLab.restore(s)',snap)
  saved=page.evaluate(L+'.exportHTML()');page2=load(saved)
  check('saved_html_dom_restore_not_navigation',page2.evaluate(L+'.snapshot()')==snap and page2.evaluate(L+'.report().cell_membership_exact')==page.evaluate(L+'.report().cell_membership_exact'))
  # Missing digest is a real error, not permission to report a fake certificate.
  failure=page.evaluate("""async()=>{delete crypto.subtle;try{await NumberFieldLab.configure({mode:'rank'});}catch(e){}let reportRejected=false,certRejected=false;try{NumberFieldLab.report();}catch(e){reportRejected=true;}try{NumberFieldLab.certificate(3);}catch(e){certRejected=true;}return {s:NumberFieldLab.status(),reportRejected,certRejected,inspect:NumberFieldLab.inspect(3)};}""")
  check('digest_failure_no_float_fallback',failure['s']['status']=='COMPUTATION_FAILED' and all(failure['s'][k] is None for k in ['occupied_cells','collision_groups','excess_identities_if_collapsed','max_cell_load']))
  check('failed_certificate_and_report_rejected',failure['reportRejected'] and failure['certRejected'] and failure['inspect']['cell'] is None)
  page.evaluate(SHIM);conf({'mode':'golden'});check('retry_after_failure',match()[1])
  # Point decisions must not call the old float quantizer or floating root/trig.
  no_float=page.evaluate("""async()=>{const old={};for(const k of ['sqrt','sin','cos','atan2','floor','round']){old[k]=Math[k];Math[k]=()=>{throw Error('float called');};}try{const r=NumberFieldLab.certificate(3);return r.cell!==null;}finally{Object.assign(Math,old);}}""")
  check('real_inspection_certificate_no_float',no_float)
  page.evaluate('(s)=>NumberFieldLab.restore(s)',{'schema':'NOLLM_MULTIPLICATION_SESSION_V2','lab_version':baseline['lab_version'],'data_sha256':baseline['data_sha256'],'state':baseline['state']})
  restored=page.evaluate(L+'.report()');check('legacy_old_fields_unchanged',all(restored[k]==v for k,v in baseline.items() if k not in ['drawn']))
  page.wait_for_timeout(30);check('no_uncaught_page_error',not errors)
  result={'schema':'M04_CHROMIUM_DOM_HARNESS_V1','checks':len(checks),'passed':checks,'page_errors':errors,'chromium_version':browser.version,'navigation':'BLOCKED_BY_ADMINISTRATOR_FOR_FILE_AND_LOCALHOST_IN_SEPARATE_ATTEMPTS','execution':'ORIGINAL_GENERATED_HTML_VIA_SET_CONTENT_ON_ABOUT_BLANK','digest':'EXPLICIT_TEST_ADAPTER_PYTHON_HASHLIB; NODE_NATIVE_WEB_CRYPTO_SEPARATE','not_covered':['successful_file_or_http_navigation','native_browser_secure_context_WebCrypto','real_saved_file_navigation','Safari_iOS','independent_review']}
  (args.out/'dom_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
  browser.close();print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
