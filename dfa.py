TRANSITIONS = {
    "q0": {"SYN": "q1", "SYN-ACK": "qE", "ACK": "qE", "TIMEOUT": "q0"},
    "q1": {"SYN": "q1", "SYN-ACK": "q2", "ACK": "qE", "TIMEOUT": "qI"},
    "q2": {"SYN": "q2", "SYN-ACK": "q2", "ACK": "q3", "TIMEOUT": "qI"},
    "q3": {"SYN": "q3", "SYN-ACK": "q3", "ACK": "q3", "TIMEOUT": "q3"},
    "qE": {s: "qE" for s in ("SYN", "SYN-ACK", "ACK", "TIMEOUT")},
    "qI": {s: "qI" for s in ("SYN", "SYN-ACK", "ACK", "TIMEOUT")},
}
START, ACCEPT = "q0", {"q3"}

def run(events):
    state = START
    for e in events:
        state = TRANSITIONS[state][e]
    return state

if __name__ == "__main__":
    tests = {
        "TC-01": (["SYN", "SYN-ACK", "ACK"], "q3"),
        "TC-02": (["ACK"], "qE"),
        "TC-03": (["SYN", "ACK"], "qE"),
        "TC-04": (["SYN", "TIMEOUT"], "qI"),
        "TC-05": (["SYN", "SYN-ACK", "TIMEOUT"], "qI"),
        "TC-07": (["SYN", "SYN"], "q1"),
    }
    for name, (events, expected) in tests.items():
        got = run(events)
        print(name, "PASS" if got == expected else f"FAIL (got {got})")