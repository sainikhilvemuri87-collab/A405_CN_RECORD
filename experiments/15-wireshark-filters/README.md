# Experiment 15 — Wireshark filter expressions

Capture filters: `host 192.168.1.10`, `net 192.168.1.0/24`, `src host 192.168.1.10`, `dst port 53`, `tcp port 443`, `udp`.
Display filters: `ip.addr == 192.168.1.10`, `tcp.port == 80`, `dns`, `icmp`, `http.request.method == "GET"`, `tcp.flags.syn == 1 && tcp.flags.ack == 0`.
Save screenshots of applied filters and matching packets.
