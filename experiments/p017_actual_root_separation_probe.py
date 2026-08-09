from enterprise_math.p017_actual_root_separation import actual_lower_band_overlaps


def main() -> None:
    events = []
    for k in range(2, 5000):
        overlaps = actual_lower_band_overlaps(k)
        if overlaps:
            events.append((k, overlaps))

    print("actual lower-band cross-shell root collisions below k=5000")
    for event in events:
        print(event)
    print("last collision:", events[-1] if events else None)


if __name__ == "__main__":
    main()
