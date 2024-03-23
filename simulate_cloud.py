from scipy.stats import norm
from csv import writer
import numpy as np

def a_generate_points(num_points:int):
    distribution_x = norm(loc=0, scale=a_dlug)
    distribution_y = norm(loc=0, scale=a_szer)
    distribution_z = norm(loc=0.2, scale=0.05)

    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)

    points = zip(x, y, z)
    return points

def b_generate_points(num_points:int):
    distribution_x = norm(loc=0, scale=0.05)
    distribution_y = norm(loc=0, scale=b_szer)
    distribution_z = norm(loc=0.2, scale=b_wys)

    x = distribution_x.rvs(size=num_points)
    y = distribution_y.rvs(size=num_points)
    z = distribution_z.rvs(size=num_points)

    points = zip(x, y, z)
    return points

def cylinderfun(num_points:int, promien:int, wysokosc:int):
    theta = np.random.uniform(0, 2*np.pi, num_points)
    r = np.random.uniform(0, promien, num_points)
    z = np.random.uniform(0, wysokosc, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    points = np.column_stack((x, y, z))
    return points

if __name__ == '__main__':
    a_szer=100                      #szerokosc do zadania a
    a_dlug=100                      #dlugosc do zadania a
    a_ile_pkt = 5000                #ilosc punktow w chmurze a
    zadanie_a = a_generate_points(a_ile_pkt)
    with open('a.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for a in zadanie_a:
            csvwriter.writerow(a)

    b_szer = 300                    #szerokosc do zadania b
    b_wys = 150                     #wysokosc do zadania b
    b_ile_pkt = 5000                #ilosc punktow w chmurze b
    zadanie_b = b_generate_points(b_ile_pkt)
    with open('b.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for b in zadanie_b:
            csvwriter.writerow(b)

    promien = 20                    #promień cylindra
    wys = 500                       #wysokość cylindra
    num_points = 5000               #ilość punktów w chmurze c
    cylinder = cylinderfun(num_points, promien, wys)
    with open('cylinder_points.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
        csvwriter = writer(csvfile)
        for cyl in cylinder:
            csvwriter.writerow(cyl)