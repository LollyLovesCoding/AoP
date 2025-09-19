from matplotlib import pyplot as plt

plt.style.use("ggplot")

years_x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 
           2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]

tor_avg_y = [
    385375, 394375, 418950, 463600, 477793,
    537500, 640347, 657125, 682375, 774613,
    859375, 1030875, 856667, 925000, 913750
]

plt.plot(years_x, tor_avg_y, color="b", marker="o", label="Toronto")

van_avg_y = [
    580000, 625000, 640000, 670000, 725000,
    760000, 895000, 1000000, 980000, 975000,
    1050000, 1190000, 1140000, 1160000, 1180000
]

plt.plot(years_x, van_avg_y, color="k", marker="o", label="Vancouver")

plt.legend(loc="upper left")

plt.xlabel("Years")
plt.ylabel("Average House Price (CAD)")
plt.title("Average House Price (CAD) by Year")

plt.grid(True)

plt.show()
