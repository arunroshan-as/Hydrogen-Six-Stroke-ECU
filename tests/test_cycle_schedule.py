from ecu_concept import build_schedule, stroke_at


def test_six_strokes_cover_1080_deg():
    s = build_schedule()
    assert len(s) == 6
    assert s[0].start_deg == 0 and s[-1].end_deg == 1080


def test_power_strokes_are_third_and_fifth():
    names = {s.index: s.name for s in build_schedule()}
    assert "Power" in names[3] and "Power" in names[5]


def test_stroke_lookup_wraps():
    assert stroke_at(1080 + 10).index == 1
    assert stroke_at(400).index == 3
