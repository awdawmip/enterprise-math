#pragma once

// A compact open-address frequency baseline. The table grows with distinct
// support rather than input length; zero and UINT64_MAX are ordinary keys.
// Include after the frozen pure_bench.cpp definitions.
namespace flat_frequency_detail {

struct Entry {
    u64 key = 0;
    std::size_t count = 0;
};

inline u64 mix(u64 x) {
    x += 0x9e3779b97f4a7c15ull;
    x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ull;
    x = (x ^ (x >> 27)) * 0x94d049bb133111ebull;
    return x ^ (x >> 31);
}

inline std::size_t locate(const std::vector<Entry>& table, u64 key) {
    const std::size_t mask = table.size() - 1;
    std::size_t slot = std::size_t(mix(key)) & mask;
    while (table[slot].count && table[slot].key != key)
        slot = (slot + 1) & mask;
    return slot;
}

inline void grow(std::vector<Entry>& table) {
    if (table.size() > table.max_size() / 2)
        throw std::length_error("flat frequency table capacity");
    std::vector<Entry> larger(table.size() * 2);
    for (const auto& entry : table) if (entry.count)
        larger[locate(larger, entry.key)] = entry;
    table.swap(larger);
}

} // namespace flat_frequency_detail

inline void flat_frequency_sort(std::vector<u64>& values, Stats* stats) {
    if (values.size() < 2) return;
    using namespace flat_frequency_detail;
    std::vector<Entry> table(512);
    std::size_t distinct = 0;
    for (u64 x : values) {
        auto slot = locate(table, x);
        if (table[slot].count) {
            ++table[slot].count;
        } else {
            // At most 70% occupancy; max_size already bounds this arithmetic.
            if (distinct + 1 > table.size() * 7 / 10) {
                grow(table);
                slot = locate(table, x);
            }
            table[slot] = Entry{x, 1};
            ++distinct;
        }
    }
    std::vector<std::pair<u64, std::size_t>> keys;
    keys.reserve(distinct);
    for (const auto& entry : table) if (entry.count)
        keys.emplace_back(entry.key, entry.count);
    std::sort(keys.begin(), keys.end());
    auto output = values.begin();
    for (const auto& [key, count] : keys)
        output = std::fill_n(output, count, key);
    if (stats) {
        stats->path = FREQUENCY;
        stats->counter_cells = distinct;
        stats->buckets = table.size();
        stats->auxiliary_vector_bytes = table.capacity() * sizeof(Entry)
            + keys.capacity() * sizeof(keys[0]);
    }
}
