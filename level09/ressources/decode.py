data = open("token", "rb").read()
decoded = bytes([(b - i) % 256 for i, b in enumerate(data)])
print(decoded.decode('utf-8', errors='ignore'))
