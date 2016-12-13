''' Tribonacci sequence'''

def tribonacci(signature, n):
	while len(signature) < n:
		signature.append(sum(signature[-3:]))
	return signature[:n]

# Other
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res