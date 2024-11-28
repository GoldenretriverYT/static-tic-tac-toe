import itertools


first_char_options = ['o', 'x']


second_char = '-'


last_char_options = ['x', 'o', '_']


output_file = "combinations.txt"


with open(output_file, "w") as f:
    pass

batch_size = 1000
batch = []

count = 0
for first in first_char_options:
    for comb in itertools.product(last_char_options, repeat=9):
        os = comb.count("o")
        xs = comb.count("x")

        if abs(os - xs) > 1:
            print(f"skip: {comb}")
            continue

        combination = first + second_char + ''.join(comb)
        batch.append(combination)
        count += 1

        if len(batch) >= batch_size:
            with open(output_file, "a") as f:
                f.write('\n'.join(batch) + '\n')
            batch.clear()


if batch:
    with open(output_file, "a") as f:
        f.write('\n'.join(batch) + '\n')

print(f"Total combinations written: {count}")
print(f"Combinations saved to {output_file}")
