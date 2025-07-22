import matplotlib.pyplot as plt

def graph(func, true_func, step: int = 2, true_x_domain: tuple[int,int] = (-10,10), true_y_domain: tuple[int,int] = (-5,5), exclude: set = set(), grid: bool = True):
    abscissa = []
    y1 = []
    y2 = []

    domain = [int(true_x_domain[0]/step), int(true_x_domain[1]/step)]

    if callable(true_func):
        for i in range(domain[0], domain[1]):
            total_step = i*step
            abscissa.append(total_step)
            if total_step not in exclude:
                y1.append(func(total_step))
                y2.append(true_func(total_step))
            else:
                y1.append(float("inf"))
                y2.append(float("inf"))
    else:
        for i in range(domain[0], domain[1]):
            total_step = i*step
            abscissa.append(total_step)
            y1.append(func())
            y2.append(true_func())

    if grid:
        plt.grid()
        plt.axhline(linewidth=1, color='black')
        plt.axvline(linewidth=1, color='black')

    plt.plot(abscissa, y2, label="True Function", color="red", linestyle='-')
    plt.plot(abscissa, y1, label=func.__name__, color="blue", linestyle='-')
    plt.title(f"Accuracy Chart for '{func.__name__}'")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(true_y_domain[0], true_y_domain[1])
    plt.legend()
    plt.show()