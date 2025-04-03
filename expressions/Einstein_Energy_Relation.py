C: int = 299792458  # The speed of light in m/s


def energy():
    mass_in_kg: float = float(input("Enter kilo of mass: "))

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("E = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")

    print(str(energy_in_joules) + " joules of energy!")


if __name__ == '__main__':
    energy()
