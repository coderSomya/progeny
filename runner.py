from bcc import BPF
from pathlib import Path

bpf_source = Path('probe.c').read_text()
bpf = BPF(text=pbf_source).trace_print()


