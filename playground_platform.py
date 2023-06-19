from platform import platform, machine, processor, system, version, \
    python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr, end='.')


print(system())
print(version())
print(processor())

print(machine())

print(platform())
print(platform(1))
print(platform(0, 1))
