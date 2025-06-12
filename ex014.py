tc = float (input ('Temperatura em Celsius:'))
k = tc + 273.15
f = (tc * 9/5) + 32
print ('Com {} C° temos {} K {} °F '.format(tc, k, f))

tf = float (input ('Temperatura em Fahrenheit:'))
k = ( tf - 32)
kf = k * 5/9 + 273.15
c = (tf - 32)
cf = c * 5/9
print ('Com {} F° temos {} K {} °F '.format(tf, kf, cf))
tk = float (input ('Temperatura em Kelvin:'))
c = tk - 273.15
fk = (tk - 273.15)
ff = fk * 9/5 + 32
print ('Com {} K temos {:.2f} C° {:.2f} °F '.format(tk, c, ff))
