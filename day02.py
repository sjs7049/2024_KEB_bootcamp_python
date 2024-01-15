# y = x + 5 (error: x 초기화 하지 않음)
# print(y)

x = 7
y = x + 5
print(y)


print(type(3.14))
print(type(3.14) == float)
print(isinstance(3.14, float))
print(isinstance("Inha", float))
print(isinstance(55, float))


artists = ['BTS', 'newjeans', '핑클', 'SES', 'HOT', 'blackpink']
groups = artists
print(artists, groups)
artists[2] = 'seventeen'
print(artists, groups)


