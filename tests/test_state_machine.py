from ecu_concept import ECUStateMachine, ECUState, SensorSnapshot


def run_to_crank_sync(m):
    m.step(SensorSnapshot())   # INIT -> SAFETY_CHECK
    m.step(SensorSnapshot())   # -> CRANK_SYNC


def test_nominal_start_and_stop():
    m = ECUStateMachine()
    run_to_crank_sync(m)
    assert m.state == ECUState.CRANK_SYNC
    m.step(SensorSnapshot(crank_synced=True, tdc_detected=True))
    assert m.state == ECUState.RUN
    m.step(SensorSnapshot(stop_requested=True))
    assert m.state == ECUState.STOP


def test_stays_in_crank_sync_without_tdc():
    m = ECUStateMachine()
    run_to_crank_sync(m)
    m.step(SensorSnapshot(crank_synced=True, tdc_detected=False))
    assert m.state == ECUState.CRANK_SYNC


def test_leak_latches_fault():
    m = ECUStateMachine()
    run_to_crank_sync(m)
    m.step(SensorSnapshot(h2_leak_detected=True))
    assert m.state == ECUState.FAULT
    m.step(SensorSnapshot())
    assert m.state == ECUState.FAULT
    m.reset()
    assert m.state == ECUState.INIT


def test_peak_pressure_limit():
    m = ECUStateMachine()
    run_to_crank_sync(m)
    m.step(SensorSnapshot(peak_pressure_bar=120))
    assert m.state == ECUState.FAULT and "peak" in m.fault_reason
