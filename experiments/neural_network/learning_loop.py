def tokenize(data):
    return float(data)


def neural(data, weight, bias):
    return data * weight + bias


def compare_result(learning_rate, output, target, weight):
    error = output - target
    return weight - learning_rate * error


data = 2
weight = 0.5
bias = 0
target = 2
learning_rate = 0.1

for _ in range(1000):
    integer = tokenize(int(input("Nhập số: ")))
    output = neural(integer, weight, bias)
    weight = compare_result(learning_rate, output, target, weight)

    if abs(output - target) < 0.001:
        break

print(f"output = {output:.4f}, target = {target}")
