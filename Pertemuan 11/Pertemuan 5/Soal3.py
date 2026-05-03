celcius_to_fahrenheit = lambda C: (9/5) * C + 32
celcius_to_reamur = lambda C: 0.8 * C

print(f"Input C = 100. Output F = {celcius_to_fahrenheit(100)}")
print(f"Input C = 80. Output R = {celcius_to_reamur(80)}")
print(f"Input C = 0. Output F = {celcius_to_fahrenheit(0)}")