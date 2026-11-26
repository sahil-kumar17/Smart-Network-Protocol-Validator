from dfa import TRANSITIONS
from graphviz import Source

def to_dot():
    lines = ["digraph DFA {", "  rankdir=LR;", '  node [shape=circle];',
             '  q3 [shape=doublecircle];',
             '  start [shape=point]; start -> q0;']
    for src, row in TRANSITIONS.items():
        grouped = {}
        for sym, dst in row.items():
            grouped.setdefault(dst, []).append(sym)
        for dst, syms in grouped.items():
            label = "Σ" if len(syms) == 4 else ", ".join(syms)
            lines.append(f'  {src} -> {dst} [label="{label}"];')
    lines.append("}")
    return "\n".join(lines)

if __name__ == "__main__":
    Source(to_dot()).render("dfa", format="png", cleanup=True)
    print("dfa.png ban gayi")