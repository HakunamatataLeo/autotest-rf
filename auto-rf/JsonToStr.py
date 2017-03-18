#coding=utf-8

s = {
    "HOST":"xxxx.com",
    "SENDMSG":"/url/index"
}
c = ""
k = s.keys()
v = s.values()

for i in range(len(k)):
    c = c + k[i] + "=" + v[i] + ";"
print c[:-1]

	

