import re
import time

with open("keys_and_messages.txt", "r", encoding="utf-8") as infile, open("output.txt", "w", encoding="utf-8") as outfile:
    for line in infile:
        # Extract numbers (digits, n, e, c) directly from each line
        nums = re.findall(r"\d+", line)
        if not nums:
            continue

        digits, n, e, c = map(int, nums)
        if digits > 5:
            continue

        start = time.perf_counter()

        # Factorize n
        p = next(i for i in range(2, int(n ** 0.5) + 1) if n % i == 0)
        q = n // p

        # Decrypt message
        d = pow(e, -1, (p - 1) * (q - 1))
        m = pow(c, d, n)
        message = m.to_bytes(max(1, (m.bit_length() + 7) // 8), "big").decode()

        elapsed = time.perf_counter() - start

        # Write to file in required format
        outfile.write(f"p:{p}, q:{q}, message:{message}, time:{elapsed:.6f}s\n")