"""E001.10 deterministic sampled-tunneling phase-count probe."""

from enterprise_math.scale_tunneling_1d import Wall1D
from enterprise_math.tunneling_phase_diagram import tunneling_phase_diagram


def print_table(wall, radius, max_factor, displacement_start, displacement_stop):
    diameter = 2 * radius + 1
    effective = wall.thickness_cells + diameter
    print(
        f"wall_thickness={wall.thickness_cells} body_diameter={diameter} "
        f"effective_thickness={effective}"
    )
    header = "s\\d " + " ".join(f"{factor:>9}" for factor in range(1, max_factor + 1))
    print(header)
    for displacement in range(displacement_start, displacement_stop + 1):
        cells = []
        for factor in range(1, max_factor + 1):
            report = tunneling_phase_diagram(
                wall, radius, displacement, factor
            )
            cells.append(
                f"{report.transmitting_phases}/{report.positive_clearance_crossing_phases}"
            )
        print(f"{displacement:>3} " + " ".join(f"{cell:>9}" for cell in cells))
    print()


def main() -> None:
    print_table(Wall1D(0, 0), radius=0, max_factor=5, displacement_start=1, displacement_stop=12)
    print_table(Wall1D(0, 2), radius=1, max_factor=5, displacement_start=4, displacement_stop=18)


if __name__ == "__main__":
    main()
