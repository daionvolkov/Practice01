import math

d1 = int(input(
    "Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды) =>"))
d2 = int(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы) =>"))
h = int(input("Введите боковое смещение между спасателем и утопающим, h (ярды) =>"))
v_sand = int(
    input("Введите скорость движения спасателя по песку, v_sand (мили в час) =>"))
n = int(input("Введите коэффициент замедления спасателя при движении в воде, n =>"))
theta1 = float(
    input("Введите направление движения спасателя по песку, theta1 (градусы)"))


def send_distance_convert_miles(d1):
    d1_miles = d1*0.000568182
    return d1_miles


def water_distance_convert_miles(d2):
    d2_miles = d2*0.000189394
    return d2_miles


def shore_length_miles(h):
    h_miles = h*0.000568182
    return h_miles


def get_degrees_radians(theta1):
    theta_radians = theta1 * math.pi / 180
    return theta_radians


def get_send_distance():
    l1 = send_distance_convert_miles(d1)/math.cos(get_degrees_radians(theta1))
    return l1


def get_water_distance():
    x = math.sqrt(get_send_distance()**2 - send_distance_convert_miles(d1)**2)
    l2 = math.sqrt((shore_length_miles(h)-x)**2 +
                   water_distance_convert_miles(d2)**2)
    return l2


def get_time_resque(theta1):
    t = round((1/v_sand)*(get_send_distance()+n*get_water_distance())*3600, 1)
    return f"Если спасатель начнёт движение под углом theta1, равным {theta1} градусам, он достигнет утопащего через {t} секунды"


print(get_time_resque(theta1))
