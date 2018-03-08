words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
newwords = words.replace("day", "month")
print newwords

x = [2,54,-2,7,12,98]
print min(x)
print max(x)


z = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print z[0], z[len(z)-1]
newz = [z[0], z[len(z)-1]]
print newz


y = [19,2,54,-2,7,12,98,32,10,-3,6]
y = sorted(y)
print y
firsthalf = y[0:(len(y)/2)]
print firsthalf
secondhalf = y[5:]
print secondhalf
secondhalf.insert(0, firsthalf)
print secondhalf