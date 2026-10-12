def xor_division(bits, divisor):
    bits = list(bits)
    divisor = list(divisor)
    for i in range(len(bits) - len(divisor) + 1):
        if bits[i] == "1":
            for j in range(len(divisor)):
                bits[i + j] = str(int(bits[i + j] != divisor[j]))
    return "".join(bits[-(len(divisor) - 1):]) if len(divisor) > 1 else ""

data = input("Enter data bits: ").strip()
generator = input("Enter generator bits: ").strip()
if not data or not generator or set(data + generator) - {"0", "1"} or generator[0] != "1":
    print("Enter valid binary data and a generator that starts with 1.")
else:
    remainder = xor_division(data + "0" * (len(generator) - 1), generator)
    codeword = data + remainder
    print("CRC remainder:", remainder)
    print("Transmitted codeword:", codeword)
    received = input("Enter received codeword (Enter to check generated codeword): ").strip() or codeword
    check = xor_division(received, generator)
    print("Syndrome:", check)
    print("Result:", "No error detected" if set(check) <= {"0"} else "Error detected")
