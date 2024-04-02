import matplotlib.pyplot as plt
import numpy as np

Xvalue = [1 + x for x in range(50)]

# Function to read from a file
def read(file):
    with open(file, 'r', encoding='utf-8') as file:
        probs = file.read()
        print(probs)

if __name__ == "__main__":
    file_read = "Equations.txt"  
    read(file_read)

# Define the functions for each problem
def prob1():
    results = []
    for x in Xvalue:
        h = x
        results.append(h * h + (7 * h) + 2)
    return results

def prob2():
    results = []
    for x in Xvalue:
        h = x
        results.append((3 * h) + 2)
    return results

def prob3():
    results = []
    for x in Xvalue:
        h = x
        results.append(h * h)
    return results

def prob4():
    results = []
    for x in Xvalue:
        h = x
        results.append((h * h) * h)
    return results

def prob5():
    results = []
    for x in Xvalue:
        h = x
        results.append(((((h * h) * h) * h) * h))
    return results

def prob6():
    results = []
    for x in Xvalue:
        h = x
        results.append(((h * h) * h) + (2 * (h * h)) + h + 10)
    return results

def prob7():
    results = []
    for x in Xvalue:
        h = x
        results.append((((h * h) * h) * h) + (2 * (h * h)) - h + 11)
    return results

def prob8():
    results = []
    for x in Xvalue:
        h = x
        results.append(np.sin(h))
    return results

def prob9():
    results = []
    for x in Xvalue:
        h = x
        results.append(np.cos(h))
    return results

def prob10():
    results = []
    for x in Xvalue:
        h = x
        results.append(((((h * h) * h) * h) * h) + (4 * (((h * h) * h) * h)) + ((h * h) * h) - (2 * (h * h)) + 100)
    return results

print("11. Print all equations")
choice = int(input("Enter the problem you want to graph: "))

def write_to_file(results, file_name):
    with open(file_name, 'w') as file:
        for i, result in enumerate(results, start=1):
            file.write(f"Result for Problem {i}:\n")
            for res in result:
                file.write(f"{res}\n")
            file.write("\n")

# Control Structures
if choice == 1:
    results = prob1()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "r", label="x²+7x+2")
elif choice == 2:
    results = prob2()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "b", label="3x+2")
elif choice == 3:
    results = prob3()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "g", label="x²")
elif choice == 4:
    results = prob4()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "c", label="x³")
elif choice == 5:
    results = prob5()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "m", label="x⁵")
elif choice == 6:
    results = prob6()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "y", label="x³+2x²+x+10")
elif choice == 7:
    results = prob7()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "k", label="x⁴-3x³+2x²-x+11")
elif choice == 8:
    results = prob8()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "orange", label="Sin(x)")
elif choice == 9:
    results = prob9()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "purple", label="Cos(x)")
elif choice == 10:
    results = prob10()
    write_to_file([results], "Result.txt")
    plt.plot(Xvalue, results, "brown", label="x⁵+4x⁴+x³-2x²+100")
elif choice == 11:
    all_results = [prob1(), prob2(), prob3(), prob4(), prob5(), prob6(), prob7(), prob8(), prob9(), prob10()]
    write_to_file(all_results, "Result.txt")
    colors = ["brown", "purple", "k", "m", "c", "y", "g", "b", "orange", "r"]
    labels = ["x²+7x+2", "3x+2", "x²", "x³", "x⁵", "x³+2x²+x+10", "x⁴-3x³+2x²-x+11", "Sin(x)", "Cos(x)", "x⁵+4x⁴+x³-2x²+100"]
    for result, color, label in zip(all_results,colors, labels):
        plt.plot(Xvalue, result, color, label=label)

    plt.legend()
    plt.show()
    exit()
else:
    print("Invalid input of choice!")
    exit()

plt.legend()
plt.show()
