"""Reproduce source-page screenshots. No mathematical computation or OCR evidence."""
from pathlib import Path
import hashlib
import json
import fitz

ROOT = Path(__file__).resolve().parent
PDF = ROOT / "Katz-Crystalline-Cohomology-Dieudonne-Jacobi.pdf"
EXPECTED = "547d6d6059d66b3809bed2d3f9c0301a62e07355bd994259ccc0533815b99da0"
PAGES = [17,18,19,22,23,24,25,26,27,28,29,30,33,34,35,38,39,40,41,43,44,45,46,47,48,49,50]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

assert sha(PDF) == EXPECTED
doc = fitz.open(PDF)
assert len(doc) == 84
screens = []
for page in PAGES:
    out = ROOT / f"evidence-pdf-{page}.png"
    doc[page-1].get_pixmap(matrix=fitz.Matrix(2.7,2.7)).save(out)
    screens.append({"pdf_page_1_based":page,"printed_page":page+164,
                    "local_path":str(out),"sha256":sha(out),"bytes":out.stat().st_size})
note = ROOT / "source_extraction.json"
manifest = {
    "schema":"KATZ_SOURCE_EVIDENCE_MANIFEST_V1",
    "source_pdf_sha256":EXPECTED,"source_pdf_bytes":PDF.stat().st_size,
    "source_url":"https://web.math.princeton.edu/~nmk/old/CrCohDModJacSum.pdf",
    "source_extraction_sha256":sha(note),"source_extraction_bytes":note.stat().st_size,
    "render_script_sha256":sha(Path(__file__)),
    "renderer":"PyMuPDF "+fitz.VersionBind,
    "render_matrix":[2.7,2.7],"rendering":"Full PDF page; no crops, annotations, or OCR overlays.",
    "reproduction":"Place exact source PDF beside render_evidence.py and source_extraction.json; run python render_evidence.py. PNG byte hashes depend on the recorded renderer version.",
    "screenshots":screens,
    "evidence_boundary":"Only passages listed in source_extraction.json were visually verified. Rendering is not reading; not all proof lines on cited pages were checked. OCR is retrieval-only."
}
(ROOT / "evidence_manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n")
print(json.dumps({"source_extraction_sha256":sha(note),"manifest_sha256":sha(ROOT/'evidence_manifest.json'),"screenshots":len(screens)},ensure_ascii=False))
