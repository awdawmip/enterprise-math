"""R149C: exact finite parity tests, using the R149 helper. All integer arithmetic."""
from check_r149 import slope_support, count

def main():
    cases = 0
    for m in range(1, 13):
        words = [slope_support(format(n, f'0{m}b')) for n in range(1 << m)]
        words = [p for p in words if p is not None]
        for K in range(2, 36):
            fibers = [count(p, K) for p in words]
            assert sum(x > 0 for x in fibers) % 2 == 0
            assert sum(fibers) % 2 == 0
            cases += 1
    assert cases == 408
    print('R149C_COMPLEMENT_PARITY_PASS',
          {'lengths': '1..12', 'K': '2..35', 'cases': cases})

if __name__ == '__main__':
    main()
