#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>

// Exact dyadic filter for all normalized odd-RHS Boolean pair cuts.
// The Python driver verifies every threshold candidate with exact rationals.
int main(int argc, char** argv) {
    if (argc != 2) return 2;
    std::ifstream in(argv[1]);
    unsigned dimension, count;
    std::int64_t scale;
    in >> dimension >> count >> scale;
    if (dimension != 27 || scale != (std::int64_t(1) << 40)) return 3;
    const std::size_t size = std::size_t(1) << dimension;
    std::vector<std::int64_t> a(size, 0);
    std::int64_t absolute_sum = 0;
    for (unsigned j = 0; j < count; ++j) {
        std::size_t column;
        std::int64_t weight;
        in >> column >> weight;
        if (column >= size) return 4;
        a[column] += weight;
        absolute_sum += weight < 0 ? -weight : weight;
    }
    // Every butterfly entry is a signed sum of distinct input contributions.
    if (absolute_sum > 10 * scale) return 5;
    const auto start = std::chrono::steady_clock::now();
    for (std::size_t step = 1; step < size; step *= 2)
        for (std::size_t block = 0; block < size; block += 2 * step) {
            std::int64_t* first = a.data() + block;
            std::int64_t* second = first + step;
            for (std::size_t j = 0; j < step; ++j) {
                const std::int64_t u = first[j], v = second[j];
                first[j] = u + v;
                second[j] = u - v;
            }
        }
    const std::int64_t threshold = 8 * scale - count;
    std::uint64_t retained = 0;
    for (std::size_t j = 0; j < size; ++j)
        if (a[j] >= threshold) { ++retained; std::cout << j << " " << a[j] << "\n"; }
    std::cerr << "indexed " << size << " retained " << retained
              << " input_absolute_sum " << absolute_sum
              << " threshold " << threshold
              << " seconds " << std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()
              << "\n";
}
