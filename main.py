import random
import uuid
import time
import os
import sys

class Molecule:
    def __init__(self, energy, speed, interaction_radius):
        self.id = uuid.uuid4()
        self.energy = energy
        self.speed = speed
        self.interaction_radius = interaction_radius
        self.x = random.uniform(0, 100)
        self.y = random.uniform(0, 100)

    def move(self):
        self.x += random.uniform(-self.speed, self.speed)
        self.y += random.uniform(-self.speed, self.speed)
        self.x = max(0, min(99, self.x))
        self.y = max(0, min(99, self.y))

    def interact(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        if distance <= self.interaction_radius:
            if self.energy > other.energy:
                self.energy += other.energy // 2
                other.energy //= 2
            else:
                other.energy += self.energy // 2
                self.energy //= 2

    def mutate(self):
        if random.random() < 0.01:
            self.energy += random.randint(-10, 10)
            self.speed *= random.uniform(0.9, 1.1)
            self.interaction_radius += random.randint(-1, 1)

class Environment:
    def __init__(self, width, height, initial_molecule_count):
        self.width = width
        self.height = height
        self.molecules = [self.spawn_molecule() for _ in range(initial_molecule_count)]

    def spawn_molecule(self):
        return Molecule(
            energy=random.randint(50, 100),
            speed=random.uniform(0.5, 2.0),
            interaction_radius=random.randint(1, 5)
        )

    def remove_molecule(self, molecule):
        self.molecules.remove(molecule)

    def step(self):
        for molecule in self.molecules:
            molecule.move()
            for other in self.molecules:
                if molecule != other:
                    molecule.interact(other)
            if molecule.energy <= 0:
                self.remove_molecule(molecule)
            molecule.mutate()
        if random.random() < 0.05:
            self.molecules.append(self.spawn_molecule())
        return  self.visualize()

    def visualize(self):

        field = ""

        grid = [['.' for _ in range(self.width)] for _ in range(self.height)]
        for molecule in self.molecules:
            x, y = int(molecule.x), int(molecule.y)
            if 0 <= x < self.width and 0 <= y < self.height:
                grid[y][x] = str(molecule.energy)#'O'

        for row in grid:
            field += ''.join(row) + "\n"

        field += "\n" + "-" * self.width + "\n"

        return field


def run_simulation(steps, initial_molecule_count):
    os.environ['TERM'] = 'xterm-256color'
    env = Environment(100, 30, initial_molecule_count)
    for _ in range(steps):
        f = env.step()
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()
        print(f)
        time.sleep(0.33)

if __name__ == "__main__":
    run_simulation(steps=1000, initial_molecule_count=50)