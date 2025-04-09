import random

# Use a prime p where p-1 is divisible by small subgroup order
p = 337  # 337 - 1 = 336, which is divisible by 7
g = 2

small_subgroup_order = 7

# Legitimate user's private key
private_key = random.randint(1, p - 2)
print(f"[Victim] Private Key: {private_key}")

# Find elements of the small subgroup of order 7
def find_small_subgroup_elements(p, order):
    elements = []
    for x in range(2, p):
        if pow(x, order, p) == 1 and pow(x, order // 7, p) != 1:
            elements.append(x)
    return elements

small_group_elements = find_small_subgroup_elements(p, small_subgroup_order)

if not small_group_elements:
    print("[!] No elements found in small subgroup. Try different p/order.")
    exit()

print(f"[Attacker] Small Subgroup Elements: {small_group_elements}")

malicious_pubkey = random.choice(small_group_elements)
print(f"[Attacker] Sends malicious pubkey: {malicious_pubkey}")

shared_secret = pow(malicious_pubkey, private_key, p)
print(f"[Victim] Computed Shared Secret (leaked): {shared_secret}")

# Attacker brute-forces the secret
possible_secrets = [pow(malicious_pubkey, k, p) for k in range(small_subgroup_order)]
print(f"[Attacker] Guessed possible shared secrets: {possible_secrets}")

if shared_secret in possible_secrets:
    print("[Attack Success] Attacker narrowed down secret!")
else:
    print("[Attack Failed] Something went wrong.")
