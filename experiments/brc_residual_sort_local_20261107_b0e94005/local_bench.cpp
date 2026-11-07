// Focused local-residual experiment, retaining the prior numerical-sort baselines.
// Scientific base: enterprise-math 5b8f9f76cd187d9d5aaa62028af6a9e5e2710b28.
// The relative include is correct in the published experiments/ directory.
// A different local checkout can supply -DBRC_BASE_SOURCE='"/absolute/path.cpp"'.
#ifndef BRC_BASE_SOURCE
#define BRC_BASE_SOURCE "../brc_residual_sort_expanded_20261107_b0e94005/pure_bench.cpp"
#endif
#define main brc_previous_experiment_main
#include BRC_BASE_SOURCE
#undef main
#include "local_kernels.hpp"
#include <string_view>

namespace local_experiment {

const std::array<Algorithm, 12> candidates{{
    {"std_sort", standard_sort},
    {"offset_radix", offset_radix},
    {"range_count_or_radix", dense_range},
    {"frequency_sort", frequency_sort},
    {"affine_range_local", affine_sort<false>},
    {"affine_square_local", affine_sort<true>},
    {"brc_old_onecorrect", brc_sort<1>},
    {"brc_residual_div", brc_sort<2>},
    {"brc_local_floor", local_floor_cached},
    {"brc_local_center", local_center_cached},
    {"brc_local_center_recompute", local_center_recompute},
    {"brc_local_adaptive", local_adaptive_cached}
}};

bool is_local(const Algorithm& a) {
    return std::string_view(a.name).starts_with("brc_local_");
}

std::string observed_path(const Algorithm& a, const Stats& s) {
    if (is_local(a)) return local_residual_path_name(s.path);
    return path_name(s.path);
}

struct LocalCondition {
    Condition original;
    unsigned jitter_variant = 0;
    bool upper_tail = false;
};

std::vector<LocalCondition> selected_conditions() {
    std::vector<LocalCondition> out;
    const auto uniform = [&](const char* name, u64 high,
                             std::initializer_list<std::size_t> sizes) {
        for (auto n : sizes)
            out.push_back({{name, n, UNIFORM, 0, 0, 0, 0, high}});
    };
    const auto square = [&](const char* name, u64 K, u64 B, u64 D, u64 shift,
                            FamilyKind kind, std::initializer_list<std::size_t> sizes) {
        for (auto n : sizes)
            out.push_back({{name, n, kind, K, B, D, shift, 0}});
    };
    uniform("uniform_1e6", 1000000, {100, 100000, 1000000});
    uniform("uniform_1e12", 1000000000000ull, {100000});
    square("square1e6_s0", 1000000, 20, 8, 0, SQUARE, {10000, 100000, 1000000});
    square("jitter1e6_B20_D8", 1000000, 20, 8, 0, JITTERED, {10000, 100000, 1000000});
    square("square900_s0", 900, 20, 8, 0, SQUARE, {100000});
    square("jitter900_B20_D8", 900, 20, 8, 0, JITTERED, {100000});
    square("square900_s1790", 900, 20, 8, 1790, SQUARE, {100000});
    square("square1e6_s1999990", 1000000, 20, 8, 1999990, SQUARE, {100000});
    square("square1e6_B256_D8", 1000000, 256, 8, 0, SQUARE, {100000});
    square("square1e6_B256_D512", 1000000, 256, 512, 0, SQUARE, {100000});
    square("unique1e6_B256_D512", 1000000, 256, 512, 0, UNIQUE_SQUARE, {100000});
    square("square3e9_B20_D8", 3000000000ull, 20, 8, 0, SQUARE, {100000});
    square("square900_anchor7", 900, 20, 8, 0, RESIDUE_ANCHOR7, {100000});
    out.push_back({{"uint64_top_window", 100000, UNIFORM, 0, 0, 0, 0, MAX_VALUE}, 0, true});
    for (const auto& [name, variant] : std::array<std::pair<const char*, unsigned>, 4>{{
             {"heldout_jitter_K8", 1}, {"heldout_jitter_K2", 2},
             {"heldout_jitter_3K4", 3}, {"positive_jitter_5K4", 4}}})
        out.push_back({{name, 100000, SQUARE, 1000000, 20, 8, 0, 0}, variant});
    return out;
}

std::vector<u64> input_bank(const LocalCondition& c, unsigned bank) {
    if (c.upper_tail) {
        const auto n = c.original.n;
        std::mt19937_64 rng(0xB0E9400520261107ull + u64(n) * 0x9e3779b97f4a7c15ull
                            + u64(bank) * 0xD1B54A32D192ED03ull);
        std::vector<u64> a(n);
        for (auto& x : a) x = MAX_VALUE - bounded(rng, 65536);
        if (n) a.front() = MAX_VALUE - 65535;
        if (n > 1) a.back() = MAX_VALUE;
        return a;
    }
    auto a = make_data(c.original, bank);
    if (!c.jitter_variant) return a;
    // Held-out offsets are generated outside timing. Labels, repeats and actual
    // endpoint clusters are exactly those of the inherited unjittered generator.
    const u64 K = c.original.K, B = c.original.B;
    const u64 amplitude = c.jitter_variant == 1 ? K / 8
        : c.jitter_variant == 2 ? K / 2
        : c.jitter_variant == 3 ? 3 * K / 4 : 5 * K / 4;
    std::mt19937_64 rng(0x48454C444F5554ull + u64(c.jitter_variant) * 0x9e3779b97f4a7c15ull);
    std::vector<std::int64_t> offsets(B, 0);
    for (u64 j = 1; j + 1 < B; ++j)
        offsets[j] = c.jitter_variant == 4
            ? std::int64_t(bounded(rng, amplitude + 1))
            : std::int64_t(bounded(rng, 2 * amplitude + 1)) - std::int64_t(amplitude);
    for (auto& x : a) {
        const u64 j = exact_root(x) - K;
        const __int128 shifted = __int128(x) + offsets[j];
        require(shifted >= 0 && u128(shifted) <= MAX_VALUE, "held-out input overflow");
        x = u64(shifted);
    }
    return a;
}

// Input-shape diagnostics are computed from sorted values outside timing.
// The independent bisection oracle is used in --verify. The already-validated
// restoring integer root is reused for actual benchmark diagnostics.
struct Shape {
    u64 distinct = 0, minimum = 0, maximum = 0;
    u64 floor_span = 0, center_span = 0, floor_rspan = 0, center_rspan = 0;
    u128 numeric_span = 0, floor_global_cells = 0, center_global_cells = 0;
    u128 floor_local_cells = 0, center_local_cells = 0;
};

Shape input_shape(const std::vector<u64>& sorted, bool independent_oracle) {
    Shape out;
    if (sorted.empty()) return out;
    out.minimum = sorted.front(); out.maximum = sorted.back();
    out.numeric_span = u128(out.maximum) - out.minimum + 1;
    u64 previous_value = 0, previous_floor = 0, previous_center = 0;
    u64 floor_first = 0, center_first = 0, floor_low = 0, center_low = 0;
    u64 floor_rmin = MAX_VALUE, floor_rmax = 0;
    __int128 center_rmin = 0, center_rmax = 0;
    bool first = true;
    for (u64 x : sorted) {
        if (!first && x == previous_value) continue;
        const u64 k = independent_oracle ? root_oracle(x) : exact_root(x);
        const u64 r = x - k * k, c = k + (r > k);
        const __int128 centered = __int128(x) - __int128(c) * c;
        if (first) {
            floor_low = k; center_low = c;
            floor_first = x; center_first = x;
            center_rmin = center_rmax = centered;
        } else {
            if (k != previous_floor) {
                out.floor_local_cells += u128(previous_value) - floor_first + 1;
                floor_first = x;
            }
            if (c != previous_center) {
                out.center_local_cells += u128(previous_value) - center_first + 1;
                center_first = x;
            }
        }
        floor_rmin = std::min(floor_rmin, r); floor_rmax = std::max(floor_rmax, r);
        center_rmin = std::min(center_rmin, centered); center_rmax = std::max(center_rmax, centered);
        previous_floor = k; previous_center = c; previous_value = x;
        first = false; ++out.distinct;
    }
    out.floor_local_cells += u128(previous_value) - floor_first + 1;
    out.center_local_cells += u128(previous_value) - center_first + 1;
    out.floor_span = previous_floor - floor_low + 1;
    out.center_span = previous_center - center_low + 1;
    out.floor_rspan = floor_rmax - floor_rmin + 1;
    out.center_rspan = u64(center_rmax - center_rmin + 1);
    out.floor_global_cells = u128(out.floor_span) * out.floor_rspan;
    out.center_global_cells = u128(out.center_span) * out.center_rspan;
    return out;
}

void check_local_counter_shape(const Algorithm& a, const Stats& stats, const Shape& shape) {
    if (!is_local(a)) return;
    const bool adaptive = std::string_view(a.name) == "brc_local_adaptive";
    const bool accepted = stats.path == BRC_GRID || (adaptive
        && (stats.path == LOCAL_ADAPTIVE_FLOOR_PATH || stats.path == LOCAL_ADAPTIVE_CENTER_PATH));
    if (!accepted) return;
    const bool centered = adaptive ? stats.path == LOCAL_ADAPTIVE_CENTER_PATH
        : std::string_view(a.name).find("center") != std::string_view::npos;
    const u128 cells = centered ? shape.center_local_cells : shape.floor_local_cells;
    const u64 span = centered ? shape.center_span : shape.floor_span;
    require(u128(stats.counter_cells) == cells, "local counter size differs from independent shape");
    require(stats.kspan == span, "local bucket span differs from independent shape");
    require(stats.rspan == (centered ? shape.center_rspan : shape.floor_rspan),
            "local residual span differs from independent shape");
    if (adaptive) {
        const bool expect_center = shape.center_span <= BUCKET_CAP
            && (shape.floor_span > BUCKET_CAP || shape.center_local_cells < shape.floor_local_cells);
        require(centered == expect_center, "adaptive selection differs from independent local widths");
    }
}

u64 checked_inputs = 0, checked_outputs = 0;
void check_input(const std::vector<u64>& input, bool only_new = false) {
    auto expected = input;
    std::sort(expected.begin(), expected.end());
    const auto shape = input_shape(expected, true);
    for (const auto& a : candidates) {
        if (only_new && !is_local(a)) continue;
        auto actual = input; Stats stats;
        a.run(actual, &stats);
        if (actual != expected) throw std::runtime_error(std::string("instrumented mismatch: ") + a.name);
        check_local_counter_shape(a, stats, shape);
        actual = input; a.run(actual, nullptr);
        if (actual != expected) throw std::runtime_error(std::string("timed path mismatch: ") + a.name);
        checked_outputs += 2;
    }
    ++checked_inputs;
}

void paired_control_check(const std::vector<u64>& a, const std::vector<u64>& b) {
    require(a.size() == b.size(), "paired input size");
    auto av = a, bv = b;
    std::sort(av.begin(), av.end()); std::sort(bv.begin(), bv.end());
    require(av.front() == bv.front() && av.back() == bv.back(), "paired actual endpoints");
    for (std::size_t i = 1; i < av.size(); ++i)
        require((av[i] == av[i - 1]) == (bv[i] == bv[i - 1]), "paired multiplicities");
    for (std::size_t i = 0; i < a.size(); ++i) {
        const auto arank = std::lower_bound(av.begin(), av.end(), a[i]) - av.begin();
        const auto brank = std::lower_bound(bv.begin(), bv.end(), b[i]) - bv.begin();
        require(arank == brank, "paired per-element ranks");
    }
}

void verify_local() {
    // Exhaust short arrays around floor-square and nearest-square boundaries.
    // Existing unchanged root/divider proofs and validations are reused.
    for (unsigned len = 0; len <= 6; ++len) {
        const u64 possibilities = u64(1) << (2 * len);
        for (u64 code = 0; code < possibilities; ++code) {
            constexpr u64 alphabet[] = {0, 2, 3, 7};
            std::vector<u64> a(len); u64 q = code;
            for (auto& x : a) { x = alphabet[q % 4]; q /= 4; }
            check_input(a, true);
        }
    }
    const u64 large_floor = (u64(1) << 32) - 2;
    for (const auto& input : std::vector<std::vector<u64>>{
            {}, {0}, {MAX_VALUE}, {0, MAX_VALUE}, {1, MAX_VALUE}, {3, 4},
            {810007, 811801}, {0, 1, 2, 3, 4, 6, 7, 8, 9, 12, 13, 16},
            {large_floor * large_floor, MAX_VALUE},
            {large_floor * large_floor, MAX_VALUE - 3, MAX_VALUE},
            {MAX_VALUE, MAX_VALUE - 1, 18446744065119617025ull, 0, 1},
            {9223372036854775807ull, 9223372036854775808ull, 9223372036854775809ull},
            std::vector<u64>(100, 0), std::vector<u64>(100, MAX_VALUE)})
        check_input(input);

    // The nonendpoint predicts p=2^32, so its candidate square is 2^64.
    // It must actually execute the wide downward-correction branch; an
    // endpoint-only pair would bypass prediction and miss this boundary.
    for (const auto& a : candidates) if (is_local(a)) {
        std::vector<u64> values{large_floor * large_floor, MAX_VALUE - 3, MAX_VALUE};
        Stats stats;
        a.run(values, &stats);
        require(stats.predictions > 0 && stats.down > 0, "wide candidate correction was not exercised");
    }

    // Exact boundary controls for the per-input counter budget and bucket cap.
    // The asymmetric pairs allow only one of the two partitions at BUCKET_CAP.
    const u64 cap_root = 1000000, cap_square = cap_root * cap_root;
    const u64 cap_high = cap_root + BUCKET_CAP - 1;
    for (const auto& values : std::vector<std::vector<u64>>{
            {cap_square, cap_square + 4095}, {cap_square, cap_square + 4096},
            {cap_square, cap_high * cap_high},
            {cap_square, (cap_high + 1) * (cap_high + 1)},
            {cap_square + cap_root + 1, (cap_high + 1) * (cap_high + 1)},
            {cap_square, cap_high * cap_high + cap_high + 1}})
        check_input(values, true);

    u64 midpoint_values = 0;
    for (u64 c : std::array<u64, 9>{0, 1, 2, 900, 1000000, 2147483647,
                                   3037000499, 4294967295, 4294967296}) {
        std::vector<u64> values;
        const __int128 square = __int128(c) * c;
        for (__int128 x : {square - c - 1, square - c, square - c + 1,
                           square - 1, square, square + 1,
                           square + c - 1, square + c, square + c + 1}) {
            if (x >= 0 && u128(x) <= MAX_VALUE) { values.push_back(u64(x)); ++midpoint_values; }
        }
        std::reverse(values.begin(), values.end());
        if (!values.empty()) values.push_back(values.front());
        check_input(values);
    }
    std::mt19937_64 rng(0x10CA120261107ull);
    for (unsigned trial = 0; trial < 160; ++trial) {
        std::vector<u64> a(bounded(rng, 257));
        for (auto& x : a) {
            if (trial % 4 == 0) x = bounded(rng, 1000001);
            else if (trial % 4 == 1) x = MAX_VALUE - bounded(rng, 100001);
            else if (trial % 4 == 2) x = rng();
            else x = bounded(rng, 257);
        }
        if (trial % 8 == 0 && !a.empty()) a.front() = 0;
        check_input(a);
    }
    for (auto c : selected_conditions()) {
        c.original.n = std::min<std::size_t>(c.original.n, 4000);
        check_input(input_bank(c, 0));
    }

    u64 paired_banks = 0;
    for (unsigned bank = 0; bank < 8; ++bank) {
        const LocalCondition base{{"pair", 4000, SQUARE, 1000000, 20, 8, 0, 0}};
        const auto a = input_bank(base, bank);
        for (unsigned variation = 0; variation <= 4; ++variation) {
            auto changed = base;
            if (!variation) changed.original.kind = JITTERED;
            else changed.jitter_variant = variation;
            const auto b = input_bank(changed, bank);
            paired_control_check(a, b);
            if (variation != 4) {
                for (std::size_t i = 0; i < a.size(); ++i) {
                    const u64 ka = root_oracle(a[i]), kb = root_oracle(b[i]);
                    const u64 ca = ka + (a[i] - ka * ka > ka);
                    const u64 cb = kb + (b[i] - kb * kb > kb);
                    require(ca == cb, "center invariance within stated jitter amplitude");
                }
            } else {
                for (std::size_t i = 0; i < a.size(); ++i)
                    require(root_oracle(a[i]) == root_oracle(b[i]), "positive jitter floor invariance");
            }
            check_input(b, true);
            ++paired_banks;
        }
    }
    {
        const LocalCondition c{{"unique", 100000, UNIQUE_SQUARE, 1000000, 256, 512, 0, 0}};
        auto a = input_bank(c, 0), sorted = a;
        std::sort(sorted.begin(), sorted.end());
        require(std::adjacent_find(sorted.begin(), sorted.end()) == sorted.end(), "unique sample duplicated");
        check_input(a);
    }
    std::cout << "{\"result\":\"PASS\",\"value_bytes\":" << sizeof(u64)
              << ",\"domain\":\"full uint64\",\"new_algorithms\":4,\"total_algorithms\":" << candidates.size()
              << ",\"verified_input_arrays\":" << checked_inputs
              << ",\"verified_algorithm_outputs\":" << checked_outputs
              << ",\"midpoint_boundary_values\":" << midpoint_values
              << ",\"paired_control_banks\":" << paired_banks
              << ",\"independent_local_counter_shape_checked\":true"
              << ",\"wide_nonendpoint_down_correction_checked\":true"
              << ",\"bucket_and_counter_cap_boundaries_checked\":true"
              << ",\"instrumented_and_timed_paths_checked\":true"
              << ",\"unique_100000_checked\":true"
              << ",\"unchanged_root_and_divider_validation_reused\":true}\n";
}

void benchmark_local(const std::string& path, std::size_t max_n, double target_seconds,
                     const std::string& filter) {
    constexpr unsigned BANKS = 8, ROUNDS = 7;
    constexpr std::size_t A = candidates.size();
    require(target_seconds > 0 && target_seconds <= 1, "target_seconds must be in (0,1]");
    std::ofstream file(path);
    require(bool(file), "cannot open local benchmark output");
    file << "family,n,algorithm,value_bytes,banks,rounds,median_us,p10_us,p90_us,min_us,max_us,calls_per_round,"
         << "mean_distinct,mean_min,mean_max,mean_numeric_span,floor_bucket_span,center_bucket_span,"
         << "floor_global_cells,center_global_cells,floor_local_cells,center_local_cells,"
         << "roots,predictions,direct_hits,up_corrections,down_corrections,fallback_elements,failed_predictions,"
         << "quotient_calls,kspan,rspan,counter_cells,auxiliary_vector_bytes,buckets,radix_passes,"
         << "pilot_disabled_fraction,same_basin_fraction,path,"
         << "round1_us,round2_us,round3_us,round4_us,round5_us,round6_us,round7_us\n";
    file << std::setprecision(21);
    u64 completed = 0, validated_banks = 0;
    for (const auto& c : selected_conditions()) {
        const auto& condition = c.original;
        if (condition.n > max_n || (!filter.empty() && condition.name.find(filter) == std::string::npos)) continue;
        std::vector<std::vector<u64>> banks;
        for (unsigned b = 0; b < BANKS; ++b) banks.push_back(input_bank(c, b));
        std::array<std::vector<Stats>, A> diagnostics;
        std::vector<Shape> shapes;
        for (const auto& input : banks) {
            auto expected = input; std::sort(expected.begin(), expected.end());
            const auto shape = input_shape(expected, false);
            shapes.push_back(shape);
            for (std::size_t ai = 0; ai < A; ++ai) {
                auto actual = input; Stats stats;
                candidates[ai].run(actual, &stats);
                if (actual != expected)
                    throw std::runtime_error("diagnostic mismatch " + condition.name + "/" + candidates[ai].name);
                check_local_counter_shape(candidates[ai], stats, shape);
                diagnostics[ai].push_back(stats);
                actual = input; candidates[ai].run(actual, nullptr);
                if (actual != expected)
                    throw std::runtime_error("timed path mismatch " + condition.name + "/" + candidates[ai].name);
            }
            ++validated_banks;
        }
        std::array<std::size_t, A> cycles{};
        std::array<std::vector<double>, A> samples;
        for (std::size_t ai = 0; ai < A; ++ai) {
            const double one = timed(candidates[ai], banks, 1, 0);
            cycles[ai] = std::clamp<std::size_t>(std::size_t(target_seconds / std::max(one, 1e-9) + 0.999), 1, 100000);
        }
        std::mt19937_64 order_rng(0x10CA1B0E94005ull + condition.n + completed * 31337);
        for (unsigned round = 0; round < ROUNDS; ++round) {
            std::array<std::size_t, A> order;
            std::iota(order.begin(), order.end(), 0);
            std::shuffle(order.begin(), order.end(), order_rng);
            for (auto ai : order)
                samples[ai].push_back(timed(candidates[ai], banks, cycles[ai], round) * 1e6 / (cycles[ai] * BANKS));
        }
        for (std::size_t ai = 0; ai < A; ++ai) {
            const auto mean_stats = [&](auto getter) {
                long double sum = 0;
                for (const auto& s : diagnostics[ai]) sum += static_cast<long double>(getter(s));
                return sum / BANKS;
            };
            const auto mean_shape = [&](auto getter) {
                long double sum = 0;
                for (const auto& s : shapes) sum += static_cast<long double>(getter(s));
                return sum / BANKS;
            };
            const auto selected_path = observed_path(candidates[ai], diagnostics[ai].front());
            bool same_path = true;
            for (const auto& s : diagnostics[ai]) same_path &= observed_path(candidates[ai], s) == selected_path;
            file << condition.name << ',' << condition.n << ',' << candidates[ai].name
                 << ',' << sizeof(u64) << ',' << BANKS << ',' << ROUNDS
                 << ',' << quantile(samples[ai], .5) << ',' << quantile(samples[ai], .1)
                 << ',' << quantile(samples[ai], .9) << ',' << quantile(samples[ai], 0)
                 << ',' << quantile(samples[ai], 1) << ',' << cycles[ai] * BANKS;
            for (auto member : {&Shape::distinct, &Shape::minimum, &Shape::maximum})
                file << ',' << mean_shape([&](const Shape& s) { return s.*member; });
            file << ',' << mean_shape([](const Shape& s) { return s.numeric_span; })
                 << ',' << mean_shape([](const Shape& s) { return s.floor_span; })
                 << ',' << mean_shape([](const Shape& s) { return s.center_span; });
            for (auto member : {&Shape::floor_global_cells, &Shape::center_global_cells,
                                &Shape::floor_local_cells, &Shape::center_local_cells})
                file << ',' << mean_shape([&](const Shape& s) { return s.*member; });
            for (auto member : {&Stats::roots, &Stats::predictions, &Stats::direct, &Stats::up, &Stats::down,
                                &Stats::fallback_elements, &Stats::failed_predictions, &Stats::quotient_calls,
                                &Stats::kspan, &Stats::rspan, &Stats::counter_cells, &Stats::auxiliary_vector_bytes,
                                &Stats::buckets, &Stats::radix_passes})
                file << ',' << mean_stats([&](const Stats& s) { return s.*member; });
            file << ',' << mean_stats([](const Stats& s) { return s.pilot_disabled; })
                 << ',' << mean_stats([](const Stats& s) { return s.same_basin; })
                 << ',' << (same_path ? selected_path : "mixed");
            for (double sample : samples[ai]) file << ',' << sample;
            file << '\n';
        }
        file.flush(); ++completed;
        std::cerr << "completed local " << condition.name << " n=" << condition.n << '\n';
    }
    std::cout << "{\"result\":\"PASS\",\"conditions\":" << completed
              << ",\"benchmark_rows\":" << completed * candidates.size()
              << ",\"validated_input_banks\":" << validated_banks
              << ",\"algorithms\":" << candidates.size()
              << ",\"banks\":" << BANKS << ",\"rounds\":" << ROUNDS
              << ",\"value_bytes\":" << sizeof(u64) << ",\"target_seconds\":" << target_seconds
              << ",\"instrumented_and_timed_paths_checked\":true"
              << ",\"observable_sink\":" << observed << "}\n";
}

} // namespace local_experiment

int main(int argc, char** argv) {
    try {
        if (argc == 2 && std::string(argv[1]) == "--verify") local_experiment::verify_local();
        else if (argc >= 3 && std::string(argv[1]) == "--bench")
            local_experiment::benchmark_local(argv[2], argc > 3 ? std::stoull(argv[3]) : 1000000,
                                              argc > 4 ? std::stod(argv[4]) : 0.012,
                                              argc > 5 ? argv[5] : "");
        else if (argc == 2 && std::string(argv[1]) == "--list")
            for (const auto& c : local_experiment::selected_conditions())
                std::cout << c.original.name << ',' << c.original.n << '\n';
        else {
            std::cerr << "usage: local_bench --verify | --list | --bench output.csv "
                         "[max_n=1000000] [target_seconds=.012] [family_substring]\n";
            return 2;
        }
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
}
