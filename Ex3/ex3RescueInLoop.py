import math


def MenResque(d1, d2, h, v_sand, n):
    d1_miles = d1*0.000568182
    d2_miles = d2*0.000189394
    h_miles = h*0.000568182

    min_t = 1000
    best_angle = 0
    i = 20
    while i < 50:
        l1 = d1_miles/math.cos(i*0.01745)
        x = math.sqrt(l1**2 - d1_miles**2)
        l2 = math.sqrt((h_miles-x)**2+d2_miles**2)
        t = round((1/v_sand)*(l1+n*l2)*3600, 1)
        if t < min_t:
            min_t = t
            best_angle = i
        i += 1
    return f"Если спасатель начнёт движение под углом theta1, равным {best_angle} градусам, он достигнет утопащего через {min_t} секунды"


d1 = int(input(
    "Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) =>"))
d2 = int(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) =>"))
h = int(input("Введите боковое смещение между спасателем и утопающим, h (ярды) =>"))
v_sand = int(
    input("Введите скорость движения спасателя по песку, v_sand (мили в час) =>"))
n = int(input("Введите коэффициент замедления спасателя при движении в воде, n =>"))
theta1 = float(
    input("Введите направление движения спасателя по песку, theta1 (градусы)"))


print(MenResque(d1, d2, h, v_sand, n))
