import numpy as np
import matplotlib.pyplot as plt


def plot_math_function():
    x = np.arange(0, 6.01, 0.01)
    y = np.cos(5 * x) * np.exp(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, 'b-')
    plt.title('y(x) = cos(5x) · e^x')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.grid(True)
    plt.show()


def create_smartphone_data():
    brands = ['Samsung', 'Xiaomi', 'Apple', 'Realme', 'OPPO']
    popularity = [32, 25, 18, 12, 8]
    return brands, popularity


def create_bar_chart(brands, popularity):
    plt.figure(figsize=(8, 5))
    plt.bar(brands, popularity)
    plt.title('Популярность смартфонов')
    plt.ylabel('Доля рынка (%)')
    plt.show()


def create_pie_chart(brands, popularity):
    plt.figure(figsize=(8, 5))
    plt.pie(popularity, labels=brands, autopct='%1.1f%%')
    plt.title('Доли рынка смартфонов')
    plt.show()


def create_scatter_plot():
    x = np.random.normal(0, 1, 700)
    y = np.random.normal(0, 1, 700)

    plt.figure(figsize=(8, 8))
    plt.scatter(x, y, alpha=0.5)
    plt.title('Нормальное распределение 700 точек')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()


def main():
    #Математический график
    plot_math_function()

    #Данные для смартфонов
    brands, popularity = create_smartphone_data()

    #Столбчатая диаграмма
    create_bar_chart(brands, popularity)

    #Круговая диаграмма
    create_pie_chart(brands, popularity)

    #точечный график
    create_scatter_plot()


if __name__ == "__main__":
    main()
