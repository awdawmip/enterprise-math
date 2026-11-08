// Sample-learned residual sorting, continuing the frozen Nov 7 experiment.
// Baselines and generators are included unchanged. Small derived condition
// recipes retain their preceding seeds; new held-outs have separate seeds.
#ifndef BRC_BASE_SOURCE
#define BRC_BASE_SOURCE "../brc_residual_sort_expanded_20261107_b0e94005/pure_bench.cpp"
#endif
#ifndef BRC_LOCAL_KERNELS
#define BRC_LOCAL_KERNELS "../brc_residual_sort_local_20261107_b0e94005/local_kernels.hpp"
#endif
#define main brc_previous_experiment_main
#include BRC_BASE_SOURCE
#undef main
#include BRC_LOCAL_KERNELS
#include "sampled_kernels.hpp"
#include "flat_frequency.hpp"
#include <map>
#include <set>
#include <string_view>

namespace sampled_experiment {

template<void (*Function)(std::vector<u64>&, Stats*)>
void wrap_baseline(std::vector<u64>& values, SampleStats* stats) {
    Function(values, stats ? &stats->base : nullptr);
}

template<void (*Function)(std::vector<u64>&, SampleStats*)>
void wrap_timing(std::vector<u64>& values, Stats*) {
    Function(values, nullptr);
}

struct Candidate {
    Algorithm timing;
    void (*diagnostic)(std::vector<u64>&, SampleStats*);
    bool new_algorithm = false;
    bool shift_algorithm = false;
    std::size_t sample_limit = 0;
};

const std::array<Candidate, 14> candidates{{
    {{"std_sort", standard_sort}, wrap_baseline<standard_sort>},
    {{"offset_radix", offset_radix}, wrap_baseline<offset_radix>},
    {{"range_count_or_radix", dense_range}, wrap_baseline<dense_range>},
    {{"frequency_sort", frequency_sort}, wrap_baseline<frequency_sort>},
    {{"affine_range_local", affine_sort<false>}, wrap_baseline<affine_sort<false>>},
    {{"affine_square_local", affine_sort<true>}, wrap_baseline<affine_sort<true>>},
    {{"brc_old_onecorrect", brc_sort<1>}, wrap_baseline<brc_sort<1>>},
    {{"brc_residual_div", brc_sort<2>}, wrap_baseline<brc_sort<2>>},
    {{"brc_local_center", local_center_cached}, wrap_baseline<local_center_cached>},
    {{"brc_local_adaptive", local_adaptive_cached}, wrap_baseline<local_adaptive_cached>},
    {{"flat_frequency", flat_frequency_sort}, wrap_baseline<flat_frequency_sort>, true},
    {{"full_shift_local", wrap_timing<full_shift_local>}, full_shift_local, true, true},
    {{"sampled_shift_1024", wrap_timing<sampled_shift_1024>}, sampled_shift_1024, true, true, 1024},
    {{"sampled_shift_4096", wrap_timing<sampled_shift_4096>}, sampled_shift_4096, true, true, 4096}
}};

std::string observed_path(const Candidate& candidate, const SampleStats& stats) {
    if (candidate.shift_algorithm) return sample_path_name(stats.path);
    if (std::string_view(candidate.timing.name).starts_with("brc_local_"))
        return local_residual_path_name(stats.base.path);
    return path_name(stats.base.path);
}

enum class ExtraKind { none, upper_tail, new_jitter_quarter, new_jitter_threequarter,
    skew90, rare_far, outliers, positional_trap, log_bits, power2_clusters };

struct ExperimentCondition {
    Condition base;
    std::string stage = "regression";
    unsigned old_jitter_variant = 0;
    ExtraKind extra = ExtraKind::none;
};

std::vector<ExperimentCondition> selected_conditions() {
    std::vector<ExperimentCondition> out;
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
    // Exactly the 24 condition recipes used by the preceding local experiment.
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
    out.push_back({{"uint64_top_window", 100000, UNIFORM, 0, 0, 0, 0, MAX_VALUE},
                   "regression", 0, ExtraKind::upper_tail});
    for (const auto& [name, variant] : std::array<std::pair<const char*, unsigned>, 4>{{
             {"heldout_jitter_K8", 1}, {"heldout_jitter_K2", 2},
             {"heldout_jitter_3K4", 3}, {"positive_jitter_5K4", 4}}})
        out.push_back({{name, 100000, SQUARE, 1000000, 20, 8, 0, 0}, "regression", variant});

    const std::set<std::pair<std::string, std::size_t>> calibration{
        {"uniform_1e6", 100}, {"uniform_1e6", 100000}, {"uniform_1e12", 100000},
        {"square1e6_s0", 100000}, {"jitter1e6_B20_D8", 100000},
        {"square1e6_B256_D8", 100000}, {"square1e6_B256_D512", 100000},
        {"unique1e6_B256_D512", 100000}, {"uint64_top_window", 100000}};
    for (auto& c : out)
        if (calibration.contains({c.base.name, c.base.n})) c.stage = "calibration";

    const auto heldout = [&](const char* name, ExtraKind extra) {
        out.push_back({{name, 100000, SQUARE, 1000000, 20, 8, 0, 0}, "heldout", 0, extra});
    };
    heldout("new_jitter_quarter_seeds", ExtraKind::new_jitter_quarter);
    heldout("new_jitter_threequarter_seeds", ExtraKind::new_jitter_threequarter);
    heldout("skew90_cluster0", ExtraKind::skew90);
    heldout("rare_far_cluster", ExtraKind::rare_far);
    heldout("two_uint64_outliers", ExtraKind::outliers);
    heldout("sample_position_trap", ExtraKind::positional_trap);
    out.push_back({{"uniform_uint64", 100000, UNIFORM, 0, 0, 0, 0, MAX_VALUE}, "heldout"});
    heldout("log_uniform_bits64", ExtraKind::log_bits);
    out.push_back({{"uniform_4096", 100000, UNIFORM, 0, 0, 0, 0, 4095}, "heldout"});
    heldout("power2_separated_clusters", ExtraKind::power2_clusters);
    return out;
}

bool select_condition(const ExperimentCondition& c, const std::string& subset) {
    if (subset.empty() || subset == "all") return true;
    if (subset == "evaluation") return c.stage != "calibration";
    if (subset == "calibration" || subset == "regression" || subset == "heldout")
        return c.stage == subset;
    return c.base.name.find(subset) != std::string::npos;
}

std::string seed_regime(const ExperimentCondition& c) {
    if (c.extra == ExtraKind::new_jitter_quarter || c.extra == ExtraKind::new_jitter_threequarter)
        return "independent_offsets_and_labels_per_bank";
    if (c.base.kind == JITTERED || c.old_jitter_variant)
        return "fixed_offsets_varying_labels";
    if (c.extra == ExtraKind::positional_trap)
        return "deterministic_sample_positions_varying_hidden_values";
    return "varying_input_seed_per_bank";
}

std::vector<u64> input_bank(const ExperimentCondition& c, unsigned bank) {
    const auto n = c.base.n;
    const u64 fresh_seed = 0x53414D504C454E38ull + u64(n) * 0x9e3779b97f4a7c15ull
        + u64(bank) * 0xD1B54A32D192ED03ull;
    std::mt19937_64 rng(fresh_seed);
    if (c.extra == ExtraKind::power2_clusters) {
        constexpr u64 origin = u64(1) << 48, spacing = u64(1) << 20;
        std::vector<u64> a(n);
        for (auto& x : a) {
            const u64 label = bounded(rng, 160);
            x = origin + (label / 8) * spacing + label % 8;
        }
        if (n) a.front() = origin;
        if (n > 1) a.back() = origin + 19 * spacing + 7;
        return a;
    }
    if (c.extra == ExtraKind::upper_tail) {
        // Preserve the previous top-window input bytes.
        rng.seed(0xB0E9400520261107ull + u64(n) * 0x9e3779b97f4a7c15ull
                 + u64(bank) * 0xD1B54A32D192ED03ull);
        std::vector<u64> a(n);
        for (auto& x : a) x = MAX_VALUE - bounded(rng, 65536);
        if (n) a.front() = MAX_VALUE - 65535;
        if (n > 1) a.back() = MAX_VALUE;
        return a;
    }
    if (c.extra == ExtraKind::skew90 || c.extra == ExtraKind::rare_far) {
        std::vector<u64> a(n);
        for (auto& x : a) {
            const u64 j = c.extra == ExtraKind::skew90
                ? (bounded(rng, 10) ? 0 : 1 + bounded(rng, 19))
                : (bounded(rng, 1000) ? bounded(rng, 20) : 5000);
            const u64 k = c.base.K + j;
            x = k * k + bounded(rng, 8);
        }
        return a;
    }
    if (c.extra == ExtraKind::log_bits) {
        std::vector<u64> a(n);
        for (auto& x : a) {
            const unsigned exponent = unsigned(bounded(rng, 64));
            const u64 scale = u64(1) << exponent;
            x = scale + bounded(rng, scale);
        }
        return a;
    }
    auto a = make_data(c.base, bank);
    if (c.extra == ExtraKind::outliers) {
        if (n) a[bounded(rng, n)] = 0;
        if (n > 1) {
            const auto zero = std::find(a.begin(), a.end(), 0) - a.begin();
            auto position = std::size_t(bounded(rng, n - 1));
            if (position >= std::size_t(zero)) ++position;
            a[position] = MAX_VALUE;
        }
        return a;
    }
    if (c.extra == ExtraKind::positional_trap) {
        // This is an explicit adversarial construction, not random sampling.
        // Both sample sets see zero; nonsampled positions retain distinct data.
        for (auto& x : a) x = 1000000000000ull + bounded(rng, 1000000000ull);
        for (std::size_t limit : {std::size_t(1024), std::size_t(4096)})
            for (auto position : brc_sampled_detail::sample_indices(n, limit)) a[position] = 0;
        return a;
    }
    if (!c.old_jitter_variant && c.extra != ExtraKind::new_jitter_quarter
        && c.extra != ExtraKind::new_jitter_threequarter) return a;

    const u64 K = c.base.K, B = c.base.B;
    const bool new_offsets = !c.old_jitter_variant;
    const bool positive = c.old_jitter_variant == 4;
    const u64 amplitude = new_offsets
        ? (c.extra == ExtraKind::new_jitter_quarter ? K / 4 : 3 * K / 4)
        : (c.old_jitter_variant == 1 ? K / 8
           : c.old_jitter_variant == 2 ? K / 2
           : c.old_jitter_variant == 3 ? 3 * K / 4 : 5 * K / 4);
    const u64 offset_seed = new_offsets
        ? (fresh_seed ^ (c.extra == ExtraKind::new_jitter_quarter
                         ? 0xA0958F37B41C902Dull : 0x630DEA5F12E44897ull))
        : 0x48454C444F5554ull + u64(c.old_jitter_variant) * 0x9e3779b97f4a7c15ull;
    std::mt19937_64 offset_rng(offset_seed);
    std::vector<std::int64_t> offsets(B, 0);
    for (u64 j = 1; j + 1 < B; ++j)
        offsets[j] = positive ? std::int64_t(bounded(offset_rng, amplitude + 1))
            : std::int64_t(bounded(offset_rng, 2 * amplitude + 1)) - std::int64_t(amplitude);
    for (auto& x : a) {
        const u64 j = exact_root(x) - K;
        const __int128 shifted = __int128(x) + offsets[j];
        require(shifted >= 0 && u128(shifted) <= MAX_VALUE, "jitter input overflow");
        x = u64(shifted);
    }
    return a;
}

struct InputShape {
    u64 distinct = 0, minimum = 0, maximum = 0;
    u128 span = 0;
};

InputShape input_shape(const std::vector<u64>& sorted) {
    InputShape out;
    if (sorted.empty()) return out;
    out.minimum = sorted.front(); out.maximum = sorted.back();
    out.span = u128(out.maximum) - out.minimum + 1;
    out.distinct = 1;
    for (std::size_t i = 1; i < sorted.size(); ++i)
        out.distinct += sorted[i] != sorted[i - 1];
    return out;
}

void check_diagnostics(const Candidate& c, const SampleStats& s,
                       const std::vector<u64>& input, const InputShape& shape) {
    const auto n = input.size();
    if (std::string_view(c.timing.name) == "flat_frequency" && n >= 2) {
        require(s.base.counter_cells == shape.distinct, "flat distinct count");
        std::size_t expected_capacity = 512;
        while (shape.distinct > expected_capacity * 7 / 10) expected_capacity *= 2;
        require(s.base.buckets == expected_capacity, "flat capacity grows with support");
    }
    if (!c.shift_algorithm) return;
    const auto p = s.path;
    if (p == SamplePath::trivial || p == SamplePath::small_std_sort) return;
    require(s.shift <= 54, "coarse shift outside uint64 range");
    require(s.covered + s.spills == s.processed, "counting scan conservation");
    require(s.processed <= n, "processed exceeds input");
    if (c.sample_limit)
        require(s.sample_count == std::min(n, c.sample_limit), "actual sample size");
    if (p == SamplePath::sampled_count || p == SamplePath::sampled_spill_merge) {
        require(s.processed == n, "accepted sample path did not process all input");
        require(s.spills <= brc_sampled_detail::spill_budget(n), "accepted spill budget");
        require(s.counter_cells_allocated == s.counter_cells_demanded, "allocated sampled layout");
        require(s.counter_cells_demanded <= brc_sampled_detail::cell_budget(n), "accepted cell budget");
        require((s.spills == 0) == (p == SamplePath::sampled_count), "spill merge path name");
        require(s.full_data_visits == n, "sample counting visit count");
    } else if (p == SamplePath::sample_cell_radix || p == SamplePath::full_cell_radix) {
        require(s.counter_cells_demanded > brc_sampled_detail::cell_budget(n), "cell rejection reason");
        require(s.counter_cells_allocated == 0 && s.processed == 0, "early rejection before count scan");
    } else if (p == SamplePath::sample_spill_radix) {
        require(s.spills == brc_sampled_detail::spill_budget(n) + 1, "spill cutoff boundary");
        require(s.counter_cells_allocated == s.counter_cells_demanded, "late rejection retained layout");
        require(s.full_data_visits == s.processed, "late rejection prefix visits");
    } else if (p == SamplePath::full_count) {
        require(s.processed == n && s.covered == n && s.spills == 0, "full count conservation");
        require(s.counter_cells_allocated == s.counter_cells_demanded, "full count layout");
    }
}

void check_constructive_family(const ExperimentCondition& condition, const Candidate& candidate,
                               const SampleStats& stats, const std::vector<u64>& input) {
    if (condition.extra != ExtraKind::power2_clusters || !candidate.sample_limit) return;
    constexpr u64 origin = u64(1) << 48;
    std::array<bool, 20> seen{};
    for (auto index : brc_sampled_detail::sample_indices(input.size(), candidate.sample_limit)) {
        const u64 offset = input[index] - origin;
        const auto cluster = std::size_t(offset >> 20);
        require(cluster < seen.size(), "constructive cluster input domain");
        seen[cluster] = true;
    }
    if (std::all_of(seen.begin(), seen.end(), [](bool value) { return value; })) {
        require(stats.path == SamplePath::sampled_count && stats.spills == 0,
                "sampled constructive family zero-spill prediction");
        require(stats.counter_cells_demanded <= 800, "constructive family local-width bound");
    }
}

u64 checked_inputs = 0, checked_outputs = 0;
void check_input(const std::vector<u64>& input, bool only_new = false) {
    auto expected = input;
    std::sort(expected.begin(), expected.end());
    const auto shape = input_shape(expected);
    for (const auto& c : candidates) {
        if (only_new && !c.new_algorithm) continue;
        auto actual = input; SampleStats stats;
        c.diagnostic(actual, &stats);
        if (actual != expected)
            throw std::runtime_error(std::string("instrumented mismatch: ") + c.timing.name);
        check_diagnostics(c, stats, input, shape);
        actual = input; c.timing.run(actual, nullptr);
        if (actual != expected)
            throw std::runtime_error(std::string("timed-path mismatch: ") + c.timing.name);
        checked_outputs += 2;
    }
    ++checked_inputs;
}

std::vector<std::size_t> unsampled_positions(std::size_t n, std::size_t limit) {
    std::vector<bool> sampled(n, false);
    for (auto i : brc_sampled_detail::sample_indices(n, limit)) sampled[i] = true;
    std::vector<std::size_t> out;
    for (std::size_t i = 0; i < n; ++i) if (!sampled[i]) out.push_back(i);
    return out;
}

const Candidate& candidate_for_limit(std::size_t limit) {
    for (const auto& c : candidates) if (c.sample_limit == limit) return c;
    throw std::runtime_error("missing sampled candidate");
}

std::vector<u64> cell_budget_witness(std::size_t limit, bool exceed) {
    // 32-wide coarse intervals; singleton sample windows have width 17 in the
    // interior or 9 at a clipped boundary. 8*17+440*9=4096;
    // 7*17+442*9=4097. Min0/max32767 force shift5 with 1024 coarse slots.
    constexpr std::size_t n = 8192;
    const unsigned interiors = exceed ? 7 : 8;
    const unsigned edges = exceed ? 442 : 440;
    std::vector<u64> support;
    const unsigned total = interiors + edges;
    for (unsigned q = 0; q + 1 < total; ++q)
        support.push_back(u64(q) * 32 + (q >= 1 && q <= interiors ? 16 : 0));
    support.push_back(32767);
    std::vector<u64> input(n, 0);
    const auto indices = brc_sampled_detail::sample_indices(n, limit);
    for (std::size_t i = 0; i < indices.size(); ++i) input[indices[i]] = support[i % support.size()];
    return input;
}

void verify_sampled() {
    u64 lifted_arrays = 0, cap_cases = 0, spill_cases = 0, sample_index_sets = 0;
    for (unsigned length = 0; length <= 6; ++length) {
        const u64 possibilities = u64(1) << (2 * length);
        for (u64 code = 0; code < possibilities; ++code) {
            constexpr u64 alphabet[] = {0, 2, 3, 7};
            std::vector<u64> word(length); u64 remaining = code;
            for (auto& x : word) { x = alphabet[remaining % 4]; remaining /= 4; }
            check_input(word, true);
            if (length && length <= 5) {
                std::vector<u64> lifted(257);
                for (std::size_t i = 0; i < lifted.size(); ++i) lifted[i] = word[i % length];
                check_input(lifted, true); ++lifted_arrays;
                for (auto& x : lifted) x = MAX_VALUE - x;
                check_input(lifted, true); ++lifted_arrays;
            }
        }
    }
    for (const auto& input : std::vector<std::vector<u64>>{
            {}, {0}, {MAX_VALUE}, {0, MAX_VALUE}, {1, MAX_VALUE},
            {MAX_VALUE, 0, MAX_VALUE, 1, 0},
            {9223372036854775807ull, 9223372036854775808ull, 9223372036854775809ull},
            std::vector<u64>(256, 0), std::vector<u64>(257, MAX_VALUE),
            std::vector<u64>(5000, 0), std::vector<u64>(5000, MAX_VALUE)})
        check_input(input);

    std::mt19937_64 rng(0xB0E9400520261108ull);
    for (std::size_t length : {255u, 256u, 257u, 511u, 512u, 1023u, 1024u, 1025u,
                              4095u, 4096u, 4097u, 8192u}) {
        for (unsigned mode = 0; mode < 4; ++mode) {
            std::vector<u64> input(length);
            for (auto& x : input)
                x = mode == 0 ? bounded(rng, 1000001)
                    : mode == 1 ? MAX_VALUE - bounded(rng, 4096)
                    : mode == 2 ? rng() : bounded(rng, 8);
            check_input(input);
        }
    }
    for (std::size_t limit : {std::size_t(1024), std::size_t(4096)}) {
        for (std::size_t n : {0u, 1u, 256u, 257u, 1023u, 1024u, 1025u,
                             4095u, 4096u, 4097u, 20000u}) {
            const auto indices = brc_sampled_detail::sample_indices(n, limit);
            const auto count = std::min(n, limit);
            require(indices.size() == count, "sample index count");
            for (std::size_t i = 0; i < count; ++i) {
                require(indices[i] < n, "sample index range");
                require(!i || indices[i - 1] < indices[i], "sample indices unique and ordered");
                const auto low = std::size_t(u128(i) * n / count);
                const auto high = std::size_t(u128(i + 1) * n / count);
                require(indices[i] >= low && indices[i] < high, "stratified sample position");
            }
            ++sample_index_sets;
        }
        const auto& candidate = candidate_for_limit(limit);
        constexpr std::size_t n = 20000;
        const auto free = unsampled_positions(n, limit);
        const auto budget = std::size_t(brc_sampled_detail::spill_budget(n));
        for (std::size_t misses : {std::size_t(1), std::size_t(2), budget, budget + 1}) {
            constexpr u64 center = 1000000;
            std::vector<u64> input(n, center);
            for (std::size_t i = 0; i < misses; ++i) {
                const std::array<u64, 5> residue{0, MAX_VALUE, center - 1, center + 1, 0};
                input[free[i]] = residue[i % residue.size()];
            }
            auto actual = input; SampleStats stats;
            candidate.diagnostic(actual, &stats);
            require(stats.spills == misses, "exact planted spill count");
            require(stats.path == (misses > budget ? SamplePath::sample_spill_radix
                                                  : SamplePath::sampled_spill_merge),
                    "planted spill transition");
            check_input(input, true); ++spill_cases;
        }
        for (bool exceed : {false, true}) {
            auto input = cell_budget_witness(limit, exceed);
            auto actual = input; SampleStats stats;
            candidate.diagnostic(actual, &stats);
            require(stats.shift == 5, "cell boundary witness shift");
            require(stats.counter_cells_demanded == (exceed ? 4097 : 4096),
                    "exact learned-cell threshold witness");
            require(stats.path == (exceed ? SamplePath::sample_cell_radix : SamplePath::sampled_count),
                    "exact learned-cell threshold path");
            check_input(input, true); ++cap_cases;
        }
        // Learned origin and upper clipping, including unobserved values on
        // both sides. The sample itself is not a completeness certificate.
        for (u64 center : {u64(0), u64(1000000000000ull), MAX_VALUE}) {
            std::vector<u64> input(n, center);
            input[free[0]] = center ? 0 : MAX_VALUE;
            input[free[1]] = center == MAX_VALUE ? MAX_VALUE - 1 : center + 1;
            input[free[2]] = MAX_VALUE;
            check_input(input, true);
        }
    }
    // Full-domain shift arithmetic with values straddling coarse boundaries.
    for (unsigned shift : {0u, 1u, 7u, 31u, 54u}) {
        const u64 step = u64(1) << shift;
        const u64 high = shift == 54 ? MAX_VALUE : (u64(1024) << shift) - 1;
        const std::array<u64, 8> support{0, 1, step - 1, step, step + 1,
                                      high - 1, high, high};
        std::vector<u64> input(8193);
        for (std::size_t i = 0; i < input.size(); ++i) input[i] = support[i % support.size()];
        std::shuffle(input.begin(), input.end(), rng);
        check_input(input);
    }
    // Exercise collision chains and repeated rehashing in the strong baseline.
    {
        std::vector<u64> input;
        for (u64 key = 0; input.size() < 40; ++key)
            if ((flat_frequency_detail::mix(key) & 511) == 0) input.push_back(key);
        for (unsigned i = 0; i < 5000; ++i) input.push_back(rng());
        for (unsigned i = 0; i < 1000; ++i) input.push_back(i & 1 ? 0 : MAX_VALUE);
        std::shuffle(input.begin(), input.end(), rng);
        check_input(input);
    }
    for (auto c : selected_conditions()) {
        c.base.n = std::min<std::size_t>(c.base.n, 5000);
        const auto input = input_bank(c, 0);
        check_input(input);
        if (c.extra == ExtraKind::power2_clusters)
            for (const auto& candidate : candidates) if (candidate.sample_limit) {
                auto actual = input; SampleStats stats;
                candidate.diagnostic(actual, &stats);
                check_constructive_family(c, candidate, stats, input);
            }
    }
    // Keep the large learned-position trap large enough that neither sampling
    // variant can observe all entries or hit the small-array cutoff.
    const ExperimentCondition trap{{"sample_position_trap", 20000, SQUARE, 1000000, 20, 8},
                                    "heldout", 0, ExtraKind::positional_trap};
    const auto trapped = input_bank(trap, 7);
    for (const auto& candidate : candidates) if (candidate.sample_limit) {
        auto actual = trapped; SampleStats stats;
        candidate.diagnostic(actual, &stats);
        require(stats.path == SamplePath::sample_spill_radix, "sample-position trap must trigger fallback");
    }
    check_input(trapped);

    std::cout << "{\"result\":\"PASS\",\"domain\":\"full uint64\",\"value_bytes\":" << sizeof(u64)
              << ",\"algorithms\":" << candidates.size()
              << ",\"new_algorithms\":4,\"verified_input_arrays\":" << checked_inputs
              << ",\"verified_algorithm_outputs\":" << checked_outputs
              << ",\"lifted_above_cutoff_arrays\":" << lifted_arrays
              << ",\"sample_index_sets\":" << sample_index_sets
              << ",\"exact_cell_budget_cases\":" << cap_cases
              << ",\"planted_spill_cases\":" << spill_cases
              << ",\"sample_constant_nonconstant_input_checked\":true"
              << ",\"sample_position_trap_checked\":true"
              << ",\"backward_merge_duplicates_checked\":true"
              << ",\"full_uint64_shift_edges_checked\":true"
              << ",\"flat_collision_growth_checked\":true"
              << ",\"constructive_zero_spill_bound_checked\":true"
              << ",\"instrumented_and_timed_paths_checked\":true"
              << ",\"unchanged_root_divider_checks_reused\":true}\n";
}

void benchmark_sampled(const std::string& output_path, std::size_t max_n,
                       double target_seconds, const std::string& subset) {
    constexpr unsigned BANKS = 8, ROUNDS = 7;
    constexpr std::size_t A = candidates.size();
    require(target_seconds > 0 && target_seconds <= 1, "target_seconds must be in (0,1]");
    std::ofstream file(output_path);
    require(bool(file), "cannot open sampled benchmark output");
    file << "stage,family,n,seed_regime,algorithm,value_bytes,banks,rounds,median_us,p10_us,p90_us,min_us,max_us,calls_per_round,"
         << "mean_distinct,mean_min,mean_max,mean_numeric_span,"
         << "roots,predictions,direct_hits,up_corrections,down_corrections,fallback_elements,failed_predictions,"
         << "quotient_calls,counter_cells,auxiliary_vector_bytes,buckets,radix_passes,"
         << "sample_count,learning_visits,processed,covered,spills,full_data_visits,active_buckets,shift,origin,"
         << "counter_cells_demanded,counter_cells_allocated,sample_vector_bytes,bucket_vector_bytes,spill_vector_bytes,"
         << "path,path_mix,round1_us,round2_us,round3_us,round4_us,round5_us,round6_us,round7_us\n";
    file << std::setprecision(21);
    u64 completed = 0, validated_banks = 0;
    for (const auto& condition : selected_conditions()) {
        const auto& c = condition.base;
        if (c.n > max_n || !select_condition(condition, subset)) continue;
        std::vector<std::vector<u64>> banks;
        for (unsigned bank = 0; bank < BANKS; ++bank) banks.push_back(input_bank(condition, bank));
        std::array<std::vector<SampleStats>, A> diagnostics;
        std::vector<InputShape> shapes;
        for (const auto& input : banks) {
            auto expected = input; std::sort(expected.begin(), expected.end());
            const auto shape = input_shape(expected); shapes.push_back(shape);
            for (std::size_t ai = 0; ai < A; ++ai) {
                auto actual = input; SampleStats stats;
                candidates[ai].diagnostic(actual, &stats);
                if (actual != expected)
                    throw std::runtime_error("diagnostic mismatch " + c.name + "/" + candidates[ai].timing.name);
                check_diagnostics(candidates[ai], stats, input, shape);
                check_constructive_family(condition, candidates[ai], stats, input);
                diagnostics[ai].push_back(stats);
                actual = input; candidates[ai].timing.run(actual, nullptr);
                if (actual != expected)
                    throw std::runtime_error("timed path mismatch " + c.name + "/" + candidates[ai].timing.name);
            }
            ++validated_banks;
        }
        std::array<std::size_t, A> cycles{};
        std::array<std::vector<double>, A> timings;
        for (std::size_t ai = 0; ai < A; ++ai) {
            const double one = timed(candidates[ai].timing, banks, 1, 0);
            cycles[ai] = std::clamp<std::size_t>(std::size_t(target_seconds / std::max(one, 1e-9) + .999), 1, 100000);
        }
        std::mt19937_64 order_rng(0x5A6D1EDB0E94005ull + c.n + completed * 31337);
        for (unsigned round = 0; round < ROUNDS; ++round) {
            std::array<std::size_t, A> order;
            std::iota(order.begin(), order.end(), 0);
            std::shuffle(order.begin(), order.end(), order_rng);
            for (auto ai : order)
                timings[ai].push_back(timed(candidates[ai].timing, banks, cycles[ai], round)
                                     * 1e6 / (cycles[ai] * BANKS));
        }
        for (std::size_t ai = 0; ai < A; ++ai) {
            const auto mean_stats = [&](auto getter) {
                long double sum = 0;
                for (const auto& stats : diagnostics[ai]) sum += static_cast<long double>(getter(stats));
                return sum / BANKS;
            };
            const auto mean_shape = [&](auto getter) {
                long double sum = 0;
                for (const auto& shape : shapes) sum += static_cast<long double>(getter(shape));
                return sum / BANKS;
            };
            std::map<std::string, unsigned> paths;
            for (const auto& stats : diagnostics[ai]) ++paths[observed_path(candidates[ai], stats)];
            file << condition.stage << ',' << c.name << ',' << c.n << ',' << seed_regime(condition)
                 << ',' << candidates[ai].timing.name << ',' << sizeof(u64) << ',' << BANKS << ',' << ROUNDS
                 << ',' << quantile(timings[ai], .5) << ',' << quantile(timings[ai], .1)
                 << ',' << quantile(timings[ai], .9) << ',' << quantile(timings[ai], 0)
                 << ',' << quantile(timings[ai], 1) << ',' << cycles[ai] * BANKS;
            for (auto member : {&InputShape::distinct, &InputShape::minimum, &InputShape::maximum})
                file << ',' << mean_shape([&](const InputShape& shape) { return shape.*member; });
            file << ',' << mean_shape([](const InputShape& shape) { return shape.span; });
            for (auto member : {&Stats::roots, &Stats::predictions, &Stats::direct, &Stats::up, &Stats::down,
                                &Stats::fallback_elements, &Stats::failed_predictions, &Stats::quotient_calls,
                                &Stats::counter_cells, &Stats::auxiliary_vector_bytes, &Stats::buckets, &Stats::radix_passes})
                file << ',' << mean_stats([&](const SampleStats& stats) { return stats.base.*member; });
            for (auto member : {&SampleStats::sample_count, &SampleStats::learning_visits,
                                &SampleStats::processed, &SampleStats::covered, &SampleStats::spills,
                                &SampleStats::full_data_visits, &SampleStats::active_buckets,
                                &SampleStats::shift, &SampleStats::origin})
                file << ',' << mean_stats([&](const SampleStats& stats) { return stats.*member; });
            file << ',' << mean_stats([](const SampleStats& stats) { return stats.counter_cells_demanded; });
            for (auto member : {&SampleStats::counter_cells_allocated, &SampleStats::sample_vector_bytes,
                                &SampleStats::bucket_vector_bytes, &SampleStats::spill_vector_bytes})
                file << ',' << mean_stats([&](const SampleStats& stats) { return stats.*member; });
            file << ',' << (paths.size() == 1 ? paths.begin()->first : "mixed") << ',';
            bool first = true;
            for (const auto& [name, count] : paths) {
                if (!first) file << ';';
                file << name << ':' << count; first = false;
            }
            for (double measurement : timings[ai]) file << ',' << measurement;
            file << '\n';
        }
        file.flush(); ++completed;
        std::cerr << "completed sampled " << condition.stage << '/' << c.name << " n=" << c.n << '\n';
    }
    require(completed > 0, "no conditions selected");
    std::cout << "{\"result\":\"PASS\",\"subset\":\"" << subset
              << "\",\"conditions\":" << completed << ",\"benchmark_rows\":" << completed * candidates.size()
              << ",\"validated_input_banks\":" << validated_banks << ",\"algorithms\":" << candidates.size()
              << ",\"banks\":" << BANKS << ",\"rounds\":" << ROUNDS << ",\"value_bytes\":" << sizeof(u64)
              << ",\"target_seconds\":" << target_seconds
              << ",\"instrumented_and_timed_paths_checked\":true,\"observable_sink\":" << observed << "}\n";
}

} // namespace sampled_experiment

int main(int argc, char** argv) {
    try {
        if (argc == 2 && std::string(argv[1]) == "--verify") sampled_experiment::verify_sampled();
        else if (argc >= 3 && std::string(argv[1]) == "--bench")
            sampled_experiment::benchmark_sampled(argv[2], argc > 3 ? std::stoull(argv[3]) : 1000000,
                                                  argc > 4 ? std::stod(argv[4]) : .012,
                                                  argc > 5 ? argv[5] : "all");
        else if (argc == 2 && std::string(argv[1]) == "--list")
            for (const auto& c : sampled_experiment::selected_conditions())
                std::cout << c.stage << ',' << c.base.name << ',' << c.base.n << ','
                          << sampled_experiment::seed_regime(c) << '\n';
        else {
            std::cerr << "usage: sampled_bench --verify | --list | --bench output.csv "
                         "[max_n=1000000] [target_seconds=.012] [subset=all]\n";
            return 2;
        }
    } catch (const std::exception& error) {
        std::cerr << error.what() << '\n';
        return 1;
    }
    return 0;
}
