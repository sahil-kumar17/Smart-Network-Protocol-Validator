from scapy.all import sniff, IP, TCP, conf
from analyzer import to_symbol

PORT = 8080

def handle(pkt):
    if IP in pkt and TCP in pkt:
        flags = str(pkt[TCP].flags)
        from_client = pkt[TCP].dport == PORT
        sym = to_symbol(flags, from_client)
        print(f"{pkt[IP].src}:{pkt[TCP].sport} -> {pkt[IP].dst}:{pkt[TCP].dport}"
              f"  flags={flags}  symbol={sym}")

print("Capture shuru... (band karne ke liye Ctrl + C)")
sniff(iface=conf.loopback_name, filter=f"tcp port {PORT}", prn=handle, store=False)