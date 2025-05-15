def perket(s, b, n):
  global m
  if n < 0:
    return

  s *= inputs[n][0]
  b += inputs[n][1]

  if abs(s - b) < m:
    m = abs(s - b)

  perket(s, b, n - 1)
  perket(s // inputs[n][0], b - inputs[n][1], n - 1)


if __name__ == "__main__":
  inputs = [[int(i) for i in i.split()]
            for i in input("Enter Input : ").split(',')]
  m = int(10e9)
  perket(1, 0, len(inputs) - 1)
  print(m)