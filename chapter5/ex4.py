import matplotlib.pyplot as plt
cities = ['LA', 'SD', 'SJ', 'SF', 'Fresno', 'Sac', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim']
areas = [1300, 964, 469, 600, 300, 259, 133, 202, 391, 130]
# sắp xếp giảm dần
data = sorted(zip(areas, cities), reverse=True)
areas, cities = zip(*data)
plt.barh(cities, areas)
plt.title('Top 10 thành phố theo diện tích (California)')
plt.xlabel('Diện tích (km2)')
plt.gca().invert_yaxis()  # lớn nhất lên trên
plt.show()