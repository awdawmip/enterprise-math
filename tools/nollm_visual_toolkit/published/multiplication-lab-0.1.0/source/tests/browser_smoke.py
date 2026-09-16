"""Optional Chromium UI acceptance. No remote navigation or server is required.
Run from package root: python tests/browser_smoke.py --out /tmp/nollm-ui
Requires Playwright and Chromium; these are test-only, not app dependencies.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
import random
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from nollm_visual_toolkit import core as c

def main():
    from playwright.sync_api import sync_playwright
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);args=p.parse_args();out=args.out;out.mkdir(parents=True,exist_ok=True)
    hexdata=c.demo_hex();xdata=c.demo_x6();hexhtml=c.html(hexdata,out/'nollm_workbench.html');xhtml=c.html(xdata,out/'nollm_x6.html')
    checks=[];errors=[];requests=[]
    def ck(name,condition):
        assert condition,name
        checks.append(name); print("PASS",name,flush=True)
    with sync_playwright() as pw:
        kw={'headless':True}
        exe=os.environ.get('CHROMIUM_PATH','/usr/bin/chromium')
        if Path(exe).exists():kw['executable_path']=exe
        browser=pw.chromium.launch(**kw)
        page=browser.new_page(viewport={'width':1600,'height':1000},accept_downloads=True)
        page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda r:requests.append(r.url))
        page.set_content(hexhtml.read_text());page.wait_for_function('NollmWorkbench.status().drawn===65536')
        status=lambda:page.evaluate('NollmWorkbench.status()')
        ck('full_65536_render_no_sampling',status()['drawn']==65536)
        ck('hex_data_fingerprint_matches_python',status()['data_sha256']==c.fingerprint(hexdata))
        ck('zero_browser_errors_initial',not errors)
        for text in ['', 'abc', 'a'*55,'a'*56,'a'*64,'a'*1000,'六轴🙂'*13]:
            ck('sha256_'+str(len(text)),page.evaluate('x=>NollmWorkbench.sha256Text(x)',text)==hashlib.sha256(text.encode()).hexdigest())
        ck('csv_python_roundtrip_browser',json.loads(page.evaluate('JSON.stringify(NollmWorkbench.parseCSV(NollmWorkbench.csv()))'))==hexdata)
        # Data object property order differs between parsers; compare semantic equality too.
        csvtext=page.evaluate('NollmWorkbench.csv()');(out/'browser_export.csv').write_text(csvtext)
        ck('csv_import_in_python_lossless',c.read_data(out/'browser_export.csv')==hexdata)
        page.locator('#query').fill('3');page.locator('#find').click()
        ck('lookup_by_n_or_id',status()['selected']=='3')
        page.locator('#factor').fill('4');page.locator('#trace').click()
        ck('multiplication_trajectory',status()['state']['path']==c.trajectory(hexdata,3,4,64))
        page.locator('#neighbors').click()
        ck('native_hex_neighborhood',set(status()['state']['highlight'])==set(c.neighborhood(hexdata,'3',1)))
        page.locator('#field').select_option('q16r');page.locator('#weight').fill('2731');page.locator('#weight').dispatch_event('change')
        ck('q16_selected_remainder',json.loads(page.locator('#detail').inner_text())['Q16']['remainder']==8193)
        page.locator('#coordQuery').fill('[0,1]');page.locator('#findCoord').click();ck('coordinate_inverse_lookup',status()['selected']=='2')
        page.locator('#slice').check();page.locator('#sliceNumber').fill('0');page.locator('#sliceNumber').dispatch_event('change')
        expected=sum(r['coord'][0]==0 for r in hexdata['records'])
        ck('exact_slice_population',status()['visible']==expected)
        page.locator('#sliceNumber').fill('999999');page.locator('#sliceNumber').dispatch_event('change');ck('empty_slice_safe',status()['visible']==0)
        page.locator('#slice').uncheck();page.locator('#view').select_option('cube');page.wait_for_function('NollmWorkbench.status().drawn===65536')
        ck('cube_is_explicit_plane_mode',status()['state']['view']=='cube')
        before=page.evaluate('NollmWorkbench.sha256Text(JSON.stringify(NollmWorkbench.data()))');page.locator('#turn').click();ck('camera_does_not_modify_coordinates',page.evaluate('NollmWorkbench.sha256Text(JSON.stringify(NollmWorkbench.data()))')==before)
        page.locator('#view').select_option('stack');ck('explicit_layer_mode',status()['state']['view']=='stack')
        page.locator('#view').select_option('hex');page.locator('#field').select_option('mod3');page.locator('#clear').click()
        saved=page.evaluate('NollmWorkbench.session()');page.locator('#turn').click();page.evaluate('x=>NollmWorkbench.restore(x)',saved)
        ck('session_restore_exact_state',status()['state']==saved['state'])
        bad=copy.deepcopy(saved);bad['data_sha256']='bad'
        rejected=page.evaluate('async x=>{try{await NollmWorkbench.restore(x);return false;}catch(e){return true;}}',bad)
        ck('wrong_dataset_session_rejected',rejected)
        bad=copy.deepcopy(saved);bad['state']['sliceAxis']='999'
        ck('invalid_session_axis_rejected',page.evaluate('async x=>{try{await NollmWorkbench.restore(x);return false;}catch(e){return true;}}',bad))
        svg=page.evaluate('NollmWorkbench.svg()');ck('vector_export_full_population',svg.count('<polygon ')==65536)
        (out/'full_cells.svg').write_text(svg)
        page.locator('summary').click()
        with page.expect_download() as dl:page.locator('#json').click()
        dl.value.save_as(out/'browser_export.json');ck('json_download_lossless',c.read_data(out/'browser_export.json')==hexdata)
        with page.expect_download() as dl:page.locator('#png').click()
        dl.value.save_as(out/'canvas_export.png');ck('png_download_signature',(out/'canvas_export.png').read_bytes().startswith(b'\x89PNG'))
        page.locator('summary').click();page.locator('#fit').click();page.screenshot(path=str(out/'hex_workbench.png'))
        page.close()
        # Second actual browser document, explicit 6-component data.
        page=browser.new_page(viewport={'width':1600,'height':1000});page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda r:requests.append(r.url))
        page.set_content(xhtml.read_text());page.wait_for_function('NollmWorkbench.status().drawn===729')
        ck('x6_full_population',status()['total']==729 and status()['drawn']==729)
        ck('exact_fcc_collision_audit',status()['overlapGroups']==135)
        ck('x6_data_fingerprint_matches_python',status()['data_sha256']==c.fingerprint(xdata))
        page.locator('#query').fill('x364');page.locator('#find').click()
        detail=json.loads(page.locator('#detail').inner_text());ck('all_six_coordinates_retained',detail['coord']==[0]*6)
        fiber=detail['same_projection_ids'];ck('coincident_records_not_merged',len(fiber)>1)
        page.locator('#next').click();ck('cycle_hidden_identity',status()['selected']!='x364')
        page.locator('#query').fill('x364');page.locator('#find').click();page.locator('#neighbors').click();ck('native_12_neighbors_plus_self',len(status()['state']['highlight'])==13)
        page.locator('#view').select_option('selected');ck('three_axis_observation_keeps_full_population',status()['visible']==729)
        page.locator('#trueSlice').check();ck('true_native_slice_only_27',status()['visible']==27)
        page.locator('#trueSlice').uncheck();page.locator('#view').select_option('fcc')
        # Actual pointer hit-test, not only direct API calls.
        page.locator('#clear').click();xy=page.evaluate('NollmWorkbench.projectId("x364")');box=page.locator('#fieldCanvas').bounding_box();page.mouse.click(box['x']+xy[0],box['y']+xy[1]);ck('canvas_pointer_selects_record',status()['selected'] is not None)
        page.locator('#clear').click();page.screenshot(path=str(out/'six_axis_workbench.png'))
        ck('no_page_errors',not errors);ck('no_network_requests',not requests)
        # Responsive controls tested in an actual narrow Chromium viewport; not Safari certification.
        page.set_viewport_size({'width':390,'height':844});page.wait_for_timeout(120)
        ck('mobile_no_horizontal_overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth+1'))
        ck('mobile_canvas_has_height',page.locator('#fieldCanvas').bounding_box()['height']>=380)
        page.screenshot(path=str(out/'mobile_workbench.png'),full_page=True)
        # Data import rejection leaves the prior population untouched.
        bad=c.demo_hex(4);bad['kind']='x6'
        rejected=page.evaluate('x=>{try{NollmWorkbench.load(x);return false;}catch(e){return true;}}',bad)
        ck('bad_import_no_silent_padding',rejected and status()['kind']=='x6')
        browser.close()
    result={'schema':'NOLLM_VISUAL_UI_ACCEPTANCE_V1','checks_passed':len(checks),'checks':checks,'page_errors':errors,'network_requests':requests,'browser':'Chromium via Playwright; supplied HTML document','limits':['Native file/http navigation blocked by the test host; supplied HTML content executed instead.','Not tested on native iOS Safari; mobile viewport only.'],'full_hex_records':65536,'full_x6_records':729}
    (out/'browser_acceptance.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
