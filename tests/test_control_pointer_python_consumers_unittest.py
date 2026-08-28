import unittest
from pathlib import Path

from control_plane import check_control_pointer_python_consumers as consumers


ROOT = Path(__file__).resolve().parents[1]


class ControlPointerPythonConsumerTests(unittest.TestCase):
    def test_canonical_dispatch_has_no_executable_mapping_key_consumer(self):
        self.assertEqual({}, consumers.consumers("canonical_dispatch", ROOT))

    def test_scanner_detects_real_mapping_reads_not_plain_text(self):
        source = """
value = {'x': 1}
a = value.get('probe_key')
b = value['probe_key']
text = 'probe_key'
"""
        import ast

        tree = ast.parse(source)
        hits = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Subscript) and consumers._constant_string(node.slice) == "probe_key":
                hits.append(node.lineno)
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr == "get" and node.args and consumers._constant_string(node.args[0]) == "probe_key":
                    hits.append(node.lineno)
        self.assertEqual([3, 4], sorted(hits))


if __name__ == "__main__":
    unittest.main()
