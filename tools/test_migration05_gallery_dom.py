#!/usr/bin/env python3
"""Chromium srcdoc gallery caller test for the asynchronous NumberFieldLab API.

This is still not file/http navigation acceptance. The child defaults to the
legacy observer, so no Web Crypto test adapter is required here.
"""
from __future__ import annotations
import argparse,json,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'tools/nollm_visual_toolkit')]
from nollm_visual_toolkit.multiplication_lab import build_lab_site
from playwright.sync_api import sync_playwright

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,default=ROOT/'evidence/migration05');p.add_argument('--chromium',default='/usr/bin/chromium');a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
 with tempfile.TemporaryDirectory() as td:
  html=build_lab_site(Path(td),count=64).read_text()
 checks=[];errors=[]
 def check(name,truth):
  if not truth:raise AssertionError(name)
  checks.append(name);print('PASS',name,flush=True)
 with sync_playwright() as pw:
  browser=pw.chromium.launch(executable_path=a.chromium,headless=True,args=['--no-sandbox']);page=browser.new_page(viewport={'width':1400,'height':1000});page.on('pageerror',lambda e:errors.append(str(e)));page.set_content(html)
  page.wait_for_function("window.NumberFieldGallery && NumberFieldGallery.status().state==='READY'")
  st=page.evaluate('NumberFieldGallery.status()');check('initial_ready',st['selected']=='golden' and st['lab']['state']['mode']=='golden')
  check('status_dom_ready',page.locator('#galleryStatus').get_attribute('data-state')=='READY')
  page.locator('a[href="multiplication.html#zero"]').click();page.wait_for_function("NumberFieldGallery.status().state==='READY' && NumberFieldGallery.status().selected==='zero'")
  check('click_awaits_zero',page.evaluate("NumberFieldGallery.status().lab.state.mode")=='zero')
  race=page.evaluate('''async()=>{const api=document.querySelector('iframe').contentWindow.NumberFieldLab,original=api.preset.bind(api);api.preset=async name=>{const p=original(name);if(name==='golden')await new Promise(r=>setTimeout(r,60));return await p;};const first=NumberFieldGallery.selectPreset('golden');const mid=NumberFieldGallery.status();const second=NumberFieldGallery.selectPreset('zero');await Promise.all([first,second]);api.preset=original;return {mid,final:NumberFieldGallery.status()};}''')
  check('gallery_reports_computing',race['mid']['state']=='COMPUTING')
  check('gallery_last_selection_wins',race['final']['state']=='READY' and race['final']['selected']=='zero' and race['final']['lab']['state']['mode']=='zero')
  failed=page.evaluate('''async()=>{const api=document.querySelector('iframe').contentWindow.NumberFieldLab,original=api.preset.bind(api);api.preset=async name=>{if(name==='legacy')throw Error('gallery-test-failure');return original(name);};let rejected=false;try{await NumberFieldGallery.selectPreset('legacy');}catch(e){rejected=e.message==='gallery-test-failure';}const bad=NumberFieldGallery.status();api.preset=original;await NumberFieldGallery.selectPreset('golden');return {rejected,bad,recovered:NumberFieldGallery.status()};}''')
  check('gallery_failure_visible',failed['rejected'] and failed['bad']['state']=='FAILED')
  check('gallery_recovers',failed['recovered']['state']=='READY' and failed['recovered']['selected']=='golden')
  check('no_uncaught_page_error',not errors)
  result={'schema':'M05_GALLERY_ASYNC_DOM_V1','checks':len(checks),'passed':checks,'page_errors':errors,'chromium_version':browser.version,
   'execution':'GENERATED_GALLERY_VIA_SET_CONTENT_WITH_REAL_SRCDOC_CHILD','navigation':'NOT_NATIVE_FILE_OR_HTTP_NAVIGATION','not_covered':['native file/http browser navigation','saved-file navigation','Safari_iOS','independent review']}
  (a.out/'gallery_dom_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');browser.close();print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
