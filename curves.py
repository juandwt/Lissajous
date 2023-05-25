import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


plt.style.use('science')
fig, ax = plt.subplots(figsize=(7,5))

x = np.arange(0, 2*np.pi, 0.0001)
#x = np.linspace(0, 2*np.pi, 500)
line, = ax.plot(x, np.sin(x), c = '#000000', lw =0.9)
#l,    = plt.plot(0, 0, 'o',c='#ff0000')
#l2,   = plt.plot(0, 0, 'o',c='#7d2181')
w   =  2

l, =  plt.plot(0, 0, 'o', markersize=10, markerfacecolor='#51d1f6', 
         markeredgecolor='#606060', markeredgewidth=1.0, alpha=0.5)
l2, =  plt.plot(0, 0, 'o', markersize=10, markerfacecolor='#ff0000', 
         markeredgecolor='#606060', markeredgewidth=1.0, alpha=0.5)
plt.plot(3, 0.002, 'o', markersize=15, markerfacecolor='#000000', 
         markeredgecolor='#606060', markeredgewidth=1.0, alpha=0.9)
#plt.plot(2.9, 0.0025, 'o', markersize=15, markerfacecolor='#ff0000', 
#         markeredgecolor='#606060', markeredgewidth=1.0, alpha=0.9)

plt.title(r'Atom (Hidrogen) A$sin(\omega t + \psi)$', size= 16)

def animate(i): # i = 1
    x1 = 3 + np.sin(w*x[i] + i/20)
    y1 = np.sin(x[i] + i/20)
    x2 = 3 +  np.sin(w*x[i] + i/20)
    y2 = -np.sin(x[i] + i/20)
    l.set_data(x1, y1)
    l2.set_data(x2, y2)
    line.set_xdata(3+np.sin(w*x+ i/50))#  lisayus
    #line.set_xdata(3+np.sin(w*x+ i/20)) 
    return line, l, l2,

ani = animation.FuncAnimation(fig, animate, repeat=True, interval=20, blit=True, save_count=50)

'''
    fig
    animate: se invoca a la funcion en cada cuadro
    interval = 20 : timepo en milisegundos de retraso en daca frame
    blit = True :valor booleano que mejora el renderizado:
    save_count = 50 : parametro auxiliar ?
'''

    #ax.tick_params(direction="in")
    #ax.tick_params(direction="in")
    #ax.set_axis_off()
    #plt.xticks([])
    #plt.yticks([])
    #plt.yticks(np.linspace(-5,5,7))

    #ani.save('L2.mp4', 
    #         writer = 'ffmpeg', fps = 60)
plt.show()
