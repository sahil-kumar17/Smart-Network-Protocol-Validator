from dfa import run

def to_symbol(flags, from_client):
    if flags == "S" and from_client:
        return "SYN"
    if flags == "SA" and not from_client:
        return "SYN-ACK"
    if flags == "A" and from_client:
        return "ACK"
    return None  # galat direction ya irrelevant packet

if __name__ == "__main__":
    tests = {
        "D-01": (("S", True), "SYN"),
        "D-02": (("SA", False), "SYN-ACK"),
        "D-03": (("A", True), "ACK"),
        "D-04": (("SA", True), None),   # SYN-ACK client se: galat direction
        "D-05": (("S", False), None),   # SYN server se: galat direction
        "D-06": (("A", False), None),   # ACK server se: galat direction
    }
    for name, ((flags, from_client), expected) in tests.items():
        got = to_symbol(flags, from_client)
        print(name, "PASS" if got == expected else f"FAIL (got {got})")