#!/usr/bin/env python3
"""Full lossless EC49FSX new native tree witnesses.
The existing D tree is at EC49FSW PR 2735, and upper-bound NS_up at EC49FSV PR 2728;
all five are packaged with source and replay logs in the full evidence archive.
These three NEW witnesses are embedded here without any private or identifying data.
"""
import json,zlib,base64,hashlib
TREES={
    "T": ("7a9e008c522ab3e3688ab65f402984d13691921a819f9a565b409c832fe03e0e", [325,9,94,141], "eNqVV0tuWzEMvIvXXZDUP5cp0sZFC6Qp4ALdBL57/SQbGpGSgqwMEE/ScDgc0u+n7z9/vb5czm+np/cTJ3/8YEiIj5/X8/OP01NJ1y8n4dgjzFRDuYe8PyIi+BHXkIePwvUWenv+fX75+ufb3/Pl3/lyu/8W4xQshtRPunjcRQUiuUKgHokNFCD3UiMAKocacXBPyw5QMrWrA1xEmoIUNANMFSMjxlIZQERO01SCZompHcP3G5XDa2nGZeWJE3xYco0AqnBkzJk14ZwT3k/1KzjH7kDBRUylkIbAhgW3QDqL+vqqWGzwRCod2ogDNepq8Z1DRZbZmzXRwniUNticwYZ0Z6kfQe1iOwbc5tJfXOOXaBQmVatCGMpaUCkaQXHQ8in1IzfctCFHtlBTFTVDhn4qTr8rebAlh9KJmCJRUyPWV1wNAfmVHi7R4Ed+guh+u2H6rGSjxQ9oQ8OBfLNJKQHZd6VQz3GkH/tSyHjvPAHS9PCiN0GyY0rwRky9He5kO630GLSJlIZhUGfusMYkB1N0ph2c7gZZJ41y9Zuc87aMkro93Qu700TZElgbnLPf2qkvxk55bfwZ0gzGd2LUVPhGPfq+1GMFHpwbQ0uxKXqdIms3zKZFE3cMY4uiUKVNwGEJcetyD2MrbPDzwnbWvmxtORsd2mUoaVO+Ny3eU7QnS1hmmNG/dOmLWwwYBFDMllGmymrlQZwcO8fj9WjG3u413vjstDKbck0WA0zJzF6nqUl5c7sd7RNbR8eOZgbF+f2ie5HmbjPOJTJ8yWfnUvGLnO5wDbCw65YPPJp1a4SiW6P1Ae7f9IFpj9itpaKfMWk/y5t64DiOO5OzgxANLEf9aDEeyhsUduQgsJz0mlDEdCTJBv2+T7PtU7MO2WXRpZVVCCH4FrFG5FDmdY47lHlYjjgh06RxWHwOxUWQxLT+XAef0OSP7yQ0/IXw/eCDrrAs7vAfljd9KmRaK+Ib9Q9oHDa3rBKdb9ePTOM2rSQdwyMr2YBN24IyBV1RbgPQoRO3SN5fFfSxxWI7CWaZE0LX/zh99xI="),
    "C": ("6f782b161be4e1585b942215fd0b7577ed5d25fc929328c75c478fe53af000e3", [323,12,89,141], "eNqVV0tuWzEMvIvXXYjUj8plirRx0QJpCrhAN0HuHj/JhkakpDSrBxD6DIfDod7r6fvPX89Pl/PL6eH1RDkcHwyxo+PzfH78cXoo+e3LiSn1CJGrIemhEI4IMy6iGgqwKL5dQy+Pv89PX/98+3u+/DtfrudfY5SjxZD7Tp+Os1yBiFQIrkdSAwXIA9cIgJJYIx7OadkBSnLt6AgHOU1BjpoBchUjIcZSGUBEXtNUomaJXNuG9zcqh9vyjMvKE2VYWKRGAFU8MiYhTThJxvNdXQX7yB8oqLCpFNIQybDgF0hn0VBvZYsNrsilQxtxoEZ9Lb73qMgyu7MmWgi3ug02b7Ah3cJ1EdQutW3ArZR+4xo/J6MwrlplhyHRgsrJCIqilk+pi/xw0oYc3kLNVdQEGYapOMOu5NGWHErHbIrkmhqxvuxrCMiv9FBJBj/yE1n32xXTZyWbLH5AGxsO5JtMShnIvinF9RxH+rEv2RnvnSfgND206E2Q7JgS3JFyb4cb2V4rPUVtIqVhGNQpHdaY5GCK3rSD193A66RRrmGTs2zLyLnb062wO02ULYG1wUnC1k5DMXZKa+MXSDMa30lJUxEa9ej7XLcVuHBuDC3Fpuh1iqTdUEyLZuoYxhZFoXKbgMMjxK/LPYytuMFPC9tZ+7K1ZTE6tI+hrE351rR4TtGezHGZoaB/6dIXvxgwCKCYV0aZKquVB3FS6hyPx6MZB/uuCcZnp5XZlGvyMMCUzOz1mposm9PtaEd7TmbgJNFidv8zbpyhgT8xbrgb6EgEZJlY937cNcEH1kta8bFoxTd547PafeDFI3brlGhT5LRNiWy4wX+CnXfZ+YallKQvLcYaaYPCThIEJllP/8Km0Rxv0O/bT2z7mVeOfQP6vHIAdgi+Ray/eJR5Hc8eZR6Xk4ud6b00vGcOxSWQxLT+VOcZu8n/7CQ0/BmEvvFOV1wWd/g1pc2zkJ1prYR31P/KNDzIRCU6fzTfM03btDJ3DPeseAM2bwtKLuqKUptrHg22RWR/VNTbFu/VSVB4Toh7eweF9Olf"),
    "N_below": ("1cf0e74e8ab1747d783cf9c242e7658dd6553312be39362870da136f7a249958", [319,12,81,141], "eNqVV8tuGzEM/BefeyCpF5WfKdLGRQukKZACvQT599qSjR2RktKeFiB2pZkhOeS+nb5+//H89Hp+OT28nbjE6wNDQnx9PJ8fv50eann/dBLOR4SZWkiPUIzXiAi+xC0U4aX0fgm9PP48P33+9eX3+fXP+fVy/iXGJXkM5fgy5OtZVCGiDQIdkdxBAfIoLQKgNLVIgHM6O0DJ1I9OcBBZCUqyCjA1jIwYa1MAEQUrU01WJab+Gd7fpRxuKzMtm05c4MWqLQKo0pUxKzvBRzZksSe22ENwsAJPYTUQKv7Kgt+K1bRUJw47cTjQ7E5pVwZ75SCO9pfgsBxbBGBpq886kQs7QrKrB2mVJYQhtRKW7Bkmq2ptL4XhpDrjTA2qbKGWljQUPk5LKeZpJuOh2CCrQk+JHJLdy4lbKCCF0EIgfpOHa3b4UZ8ktgAumOatsMafPX6s9I4D9WZHqYDYt0qhg+Mof0Xa5JxyToCsPHzptzWl4inBHbkc7XATO9hKz6lFAGztGIbq1APWSHKwsODaIdhukDVpLNe44azbNEo5XOeW2F1N1K2ArcFZ49Y1Y3UjgNc2rUAzOd/J2UoRu/RomdI+q3Dh3Bg6xV7Ra4ps3VBdixY+MIwtioUqfVQMK0NYpxvbI6QNfl7YztqXvS2rq0O/uhRryremxXOq9WRJS4aK/mVTX8NiwCCA6sZenVZWTw/i5HxoPB6PZhz9FhKdz04zs0mX+HQhJTd7g5Wm6OZ0P9rRnrMbOFltMdO/jBtyMsh/jBs5DHQUAlhmsb2fdk3wgfWyrfhUbcX38sYlmD7w4hG7d0q0KSZrU6obbXCD33mXn2+YSs320uqskTco/CRBYFrs9K/iGo1kg37ffurbz205fgcMZeUAQgi+R7y/BCzzNp4DlnlaTi4h13t52GeuFZehJKb55zbPhCZ/n5MQmlV3KxrkSsvkDj+SvFkLhVxrZbyj/QXmYSFTQ3S+NN+Z5i2tIgeGOyvZgC3bhDIlm1Hucy2gwfaI7o9K9rPFvjoJqswFofe/IYrN4w=="),
}
def decode(name):
    expected,vector,encoded=TREES[name]
    raw=zlib.decompress(base64.b64decode(encoded))
    assert hashlib.sha256(raw).hexdigest()==expected
    return json.loads(raw)
def verify_native(V):
    from collections import Counter
    assert len(V)==228 and all(len(x)==141 for x in V)
    for name in TREES:
        tree=decode(name);count=Counter()
        for i in range(141):
            node=tree;seen=set()
            while "named_observer" in node:
                q=node["named_observer"]
                assert 0<=q<228 and q not in seen
                seen.add(q);count[q]+=1
                node=node["children"][str(V[q][i])]
            assert node=={"leaf":i}
        assert [sum(count.values()),count[32],count[34],count[140]]==TREES[name][1]
    print("PASS 3 native new trees, 141 named paths")
if __name__=="__main__":
    for k in TREES:decode(k)
    try:
        from EC49FQI_NATIVE_DATA import V
    except ImportError:
        print("SHA256_TREE_BYTES_PASSED; supply pinned EC49FQI_NATIVE_DATA.py for semantic replay")
    else:
        verify_native(V)
