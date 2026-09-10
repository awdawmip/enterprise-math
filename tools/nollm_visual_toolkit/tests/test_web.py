from __future__ import annotations
import json
import tempfile
import unittest
import urllib.error
import urllib.request
from pathlib import Path
from nollm_visual_toolkit import core as c
from nollm_visual_toolkit import web as w


class WebTests(unittest.TestCase):
    def test_html_uses_current_package_version(self):
        with tempfile.TemporaryDirectory() as d:
            p = c.html(c.demo_hex(4), Path(d) / 'a.html')
            text = p.read_text(encoding='utf-8')
            self.assertIn(c.VERSION, text)
            self.assertNotIn('0.2.0', text)

    def test_demo_site_is_complete_and_deterministic(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            first = w.demo_site(out, hex_count=16)
            bytes1 = (out / 'manifest.json').read_bytes(), (out / 'index.html').read_bytes()
            second = w.demo_site(out, hex_count=16)
            bytes2 = (out / 'manifest.json').read_bytes(), (out / 'index.html').read_bytes()
            self.assertEqual(first, second)
            self.assertEqual(bytes1, bytes2)
            self.assertEqual(first['schema'], w.SITE_SCHEMA)
            self.assertEqual([p['records'] for p in first['pages']], [16, 729])
            self.assertTrue((out / 'hex-16.html').exists())
            self.assertTrue((out / 'x6-729.html').exists())

    def test_custom_site_preserves_fingerprints(self):
        with tempfile.TemporaryDirectory() as d:
            a, b = c.demo_hex(8), c.demo_x6()
            manifest = w.build_site([('A field', a), ('B field', b)], d, title='研究预览')
            self.assertEqual(manifest['pages'][0]['sha256'], c.fingerprint(a))
            self.assertEqual(manifest['pages'][1]['sha256'], c.fingerprint(b))
            self.assertIn('研究预览', (Path(d) / 'index.html').read_text(encoding='utf-8'))

    def test_site_escapes_labels_and_dedupes_slugs(self):
        with tempfile.TemporaryDirectory() as d:
            data = c.demo_hex(4)
            manifest = w.build_site([('<script>x</script>', data), ('same', data), ('same', data)], d)
            text = (Path(d) / 'index.html').read_text(encoding='utf-8')
            self.assertNotIn('<script>x</script>', text)
            self.assertIn('&lt;script&gt;x&lt;/script&gt;', text)
            hrefs = [p['href'] for p in manifest['pages']]
            self.assertEqual(len(hrefs), len(set(hrefs)))

    def test_empty_site_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                w.build_site([], d)

    def test_preview_directory_serves_index_and_workbench(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / 'site'
            w.demo_site(out, hex_count=4, include_x6=False)
            with w.preview_server(out) as handle:
                index = urllib.request.urlopen(handle.url, timeout=3)
                self.assertEqual(index.status, 200)
                self.assertEqual(index.headers['Cache-Control'], 'no-store')
                page = urllib.request.urlopen(handle.url + 'hex-4.html', timeout=3)
                self.assertEqual(page.status, 200)

    def test_preview_single_file_is_scoped(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            target = c.html(c.demo_hex(4), root / 'study.html')
            (root / 'secret.txt').write_text('not served', encoding='utf-8')
            with w.preview_server(target) as handle:
                self.assertEqual(urllib.request.urlopen(handle.url, timeout=3).status, 200)
                with self.assertRaises(urllib.error.HTTPError) as cm:
                    urllib.request.urlopen(handle.url.rsplit('/', 1)[0] + '/secret.txt', timeout=3)
                self.assertEqual(cm.exception.code, 404)

    def test_preview_rejects_non_html_file(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'data.json'; p.write_text('{}')
            with self.assertRaises(ValueError):
                with w.preview_server(p):
                    pass

    def test_preview_remote_bind_needs_explicit_opt_in(self):
        with tempfile.TemporaryDirectory() as d:
            p = c.html(c.demo_hex(4), Path(d) / 'study.html')
            with self.assertRaises(ValueError):
                with w.preview_server(p, host='0.0.0.0'):
                    pass

    def test_manifest_matches_file_payload(self):
        with tempfile.TemporaryDirectory() as d:
            manifest = w.demo_site(d, hex_count=8, include_x6=False)
            stored = json.loads((Path(d) / 'manifest.json').read_text(encoding='utf-8'))
            self.assertEqual(stored, manifest)
            self.assertEqual(stored['toolkit_version'], c.VERSION)

    def test_add_multiplicative_page(self):
        with tempfile.TemporaryDirectory() as d:
            out=Path(d)
            manifest=w.demo_site(out,hex_count=8,include_x6=False)
            w.add_multiplicative_page(manifest,out,count=256,seed=123)
            self.assertEqual(manifest['pages'][-1]['kind'],'multiplicative-field-observer')
            self.assertEqual(manifest['pages'][-1]['records'],256)
            self.assertTrue((out/manifest['pages'][-1]['href']).exists())
            stored=json.loads((out/'manifest.json').read_text())
            self.assertEqual(stored,manifest)

    def test_demo_site_can_include_multiplicative(self):
        with tempfile.TemporaryDirectory() as d:
            manifest=w.demo_site(d,hex_count=128,include_x6=True,include_multiplicative=True,multiplicative_seed=7)
            self.assertEqual([p['kind'] for p in manifest['pages']],['hex','x6','multiplicative-field-observer'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
