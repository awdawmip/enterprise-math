#!/usr/bin/env python3
"""Three lossless complete native physical-index decision tree witnesses for EC49FSW.
zlib compressed JSON uses original 228 named physical observation indices and 141 leaves.
Requires no external input to recover the exact tree bytes. To validate semantics, run
the companion complete-source checker with the frozen physical-response matrix."""
import base64, zlib, hashlib, json
TREES = {
"D_7_16": ("f6854068c15fc02323cf7584f2e39a81b720f7ca02cfc20a434f6a6d38652899", "eNqVV0tuWzEMvIvXXZDUP5cp0sZFC6QpkALdBLl7bMrBG5GS0qwMEHrUcDgcyi+n7z9/PT48n59Ody8nLvH6gyEhvv48nu9/nO5aef1yEs5HhJk0VI9QjNeICB5iDUU4lF4voaf73+eHr3++/T0//zs/X/JfYlySx1COL0O+5qIGkaoQ6IjkDgqQR9EIgKpJIwHy9OoAJVNPnSARWQpKsgwwKUZGjE0ZQETB0tSSZYmpf4b3dyqH28qMS+WJCxxsVSOAKl0r5sqO8LEastgTW+whOFiBp7AURBV/ZcFvxXJamiOHHTkcaHan6JXBXjmQU/shSJajRgBWVX22CV04EZKdHkSVJYShaiks2VeYLKtND4UhU5vVTApVtlCLNg2Jj1MpxTztZDwYG2itMFMiB2XvcmINBSwhaAjIV3q4ZYcf+UliBXDBNB+FNf7s8aPSOw7km11JBci+KYWOGkf6G5ZNzinnBZClhy/zti6p+JLgjlyOcbiRHazSc9IIgG0dw6DOesAaixwsLLhxCHYaZF00yjVuaq7bNko5XOfW2J0m2pZAHXCuceuasbkVwGubrlBmcr6Ts6UidurRMkU/a3Dh3Bh6iV3R6xLZumF1I1r4wDCOKApV+qoYngxh3W4cj5A2+HlhO2tf9rZcnQ7906VYU74NLeZp1pMlLSus6F+29S0sFgwCaG7ttamyensQJ+eD4zE9mnH0r5DofHbamU27xLcLS3K7N1hqSt1k96sd7Tm7hZOrFTP9z7ohR4N8Yt3IYaAjVLwiWWBZNsk+sF62ik/NKr7LGx/B9IEXj9hxwGjuB8MaqW6f5pVLrcv2VyBjNVtvbM4aeZPdbxKEW4vd/k3coJFsxLofv+rHz71y/BswlJUDCCH4HvH+ElCDup4DyjwtN5eQm708vGeuisugkukYs+4zocm/T3Smbk2zUwNd+mim4e9E/qTGhNxoZbxD/wXm4UFWTaHzR/N7pXlbQ5Hj0HtVsgFbtg1lSraj3PdaQIPtkbpPlexni/fqJFhlTgi9vgGgOs3f"),
"S_7_16": ("8bbc01610444decb81275e7a50170b79110c032dfb9e8a450fb28fe5e1e5f396", "eNqVV0tuWzEMvIvXXZDUP5cp0sZFC6Qp4ALdBL57/SQbGpGSgqweQDxRwyE5pN5P33/+en25nN9OT+8nTv74oEmIj8/r+fnH6amk65eTcOwWZqqm3E3eHxYR/ImrycNP4XozvT3/Pr98/fPt7/ny73y5+b/ZOAWLIfWTLh6+qIAlVwjULbGBAuReqgVA5VAtDvy06AAlU3MdwBFpClLQDDBVjIwYS2UAETlNUwmaJaZ2DO9vVA63pRmXlSdO8GPJ1QKowhExZ9aEc07on+pfcI7dgYKLmEwhDYENC26BdGb19Vax2OCKVDq0EQfWqKvJdw4rsszurIEWxqO0weYMNqQ7S/0JchfbMeA2l37jGr9EU2FSa1UITVkXVIqmoDjo8in1Jzd42pAjW6ipFjVDhH5anH6X8mBTDqkTMUmiVo2YX3HVBORXerhEgx/5CaL77YbpsyUbLX5AGxoO5JtNSAnIvlcK9RhH+rEvhYz2zgMgTQ8vehNKdgwJ7oipt8OdbKcrPQYtIqVhGKozd1hjkIMoOtMOTneDrIPGcvWbmPM2jZK6PN0Tu6uJsiWwNjhnv5VTX4yc8lr4M4QZjO7EqKnwjXrUfanHClw4F4YWYqvodYis1TCbFk3cMYwtioUqbQIOS4hbp3sYW2GDnxeys9ZlK8vZ1KFdhpIW5XvTop+iNVnCMsKM+qVTX9xiwCCAYraMMq2slh7EybFzPLpHMfZ2r/FGZ6eZ2aRrshhgSGb2Ok1NyhvvdrRPZB0VO5oZFOf+RfcizdVmnEtk+JLPzqXiFzHd4RpgYdctH2g069YIRbdG6wPcv+kD0R6xW0lFPWPSepY3+cBxHHciZwchCliO+tJiNJQ3KOzIQWA56TWhiOlIkg36fZ9m26dmHbLLoksrqRBC8M1ihchhmdc57rDMw3LECZkmjcPic1RchJKY5p/r4BOaPHwnpuEJ4fvBB11hmdzhDcubPhWavH+NKeK19U2Kkc7X60eow9Mob4DELQFJOtpH/LLxlrapZwo699xGpUPNbpa8dxX0scUKPDFmmTNH1/9X0AT3"),
"S_57_128": ("5d4c455547d7a56751ab0e9939be0aa90ea593636bb11fc209024b9f43dfdd15", "eNqVV9tuXCEM/Jd97gM2N5OfqdJmq1ZKU2kr9SXKv2cP7IrBBtI8Hck6wHg8HsPr6fvPX89Pl/PL6eH1RDkcHwyxo+PzfH78cXoo+e3LiSn1CJGrIemhEI4IM/5ENRTgp/h2Db08/j4/ff3z7e/58u98ue5/jVGOFkPuK3069nIFIlIhuB5JDRQgD1wjAEpijXjYp2UHKMm1rSNs5DQFOWoGyFWMhBhLZQAReU1TiZolcm0Znt+oHE7LMy4rT5ThxyI1AqjikTEJacJJMu7v6l+wjvyBggqbSiENkQwLfoF0Fg31VLbY4IhcOrQRB2rU1+J7j4osszNrooVwqdtg8wYb0i1cf4LapbYMuJXST1zj52QUxlWr7DAkWlA5GUFR1PIp9Sc/7LQhh7dQcxU1QYZhKs6wK3m0JYfSMZsiuaZGrC/7GgLyKz1UksGP/ETW/XbF9FnJJosf0MaGA/kmk1IGsm9KcT3HkX7sS3bGe+cJOE0PLXoTJDumBGek3NvhRrbXSk9Rm0hpGAZ1Soc1JjmYojft4HU38DpplGvY5CzbMnLu9nQr7E4TZUtgbXCSsLXTUIyd0tr4BdKMxndS0lSERj36PtdlBQ6cG0NLsSl6nSJpNxTTopk6hrFFUajcJuBwCfHrcg9jK27w08J21r5sbVmMDu1lKGtTvjUt7lO0J3NcZijoX7r0xS8GDAIo5pZRpspq5UGclDrH4/ZoxsHea4Lx2WllNuWaXAwwJTN7vaYmy2Z3O9rRnpMZOEm0mN3/jBtnaOBPjBvuBjoSAVkm1r0fd03wgfWSVnwsWvFN3nitdh948YjdOiXaFDltUyIbbvBNsPMuO9+wlJL0ocVYI21Q2EmCwCTr6V/YNJrjDfp9+4ltP3PLsXdAn1cOwA7Bt4j1F48yr+PZo8zjcnKxM72XhvvMobgEkpjWn+o8Yzd5z05Cw8sg9IV3uuKyuMPTlDbXQnaTZ60JJTy2PjUx0/mt+Z7q8OKRDZC0JSBzR3vPnze75W3pyUVde2oT0KMVt4jst4p62eJmOwkKz5lzb+9ly/c1")
}
VECTORS={"D_7_16":(319,18,75,141),"S_7_16":(327,9,97,141),"S_57_128":(325,12,92,141)}
def decode(name):
    expected,encoded=TREES[name]
    raw=zlib.decompress(base64.b64decode(encoded))
    assert hashlib.sha256(raw).hexdigest()==expected,(name,"SHA256 mismatch")
    return json.loads(raw)
if __name__=="__main__":
    from collections import Counter
    for name in TREES:
        tree=decode(name);used=Counter()
        def walk(node):
            if "leaf" in node: return 1
            q=node["named_observer"];assert 0<=q<228
            count=0
            for child in node["children"].values():count+=walk(child)
            used[q]+=count
            return count
        assert walk(tree)==141
        assert (sum(used.values()),used[32],used[34],used[140])==VECTORS[name]
        print(name,"sha256-verified, 141 named leaves, vector",VECTORS[name])
