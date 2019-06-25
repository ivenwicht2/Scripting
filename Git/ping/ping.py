import subprocess 

from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange


figure = pyplot.figure()


x,y  = [],[]

line, = pyplot.plot(y,x,'-' )

i = 0
def update(frame) :
        global i
        try:
            op = str(subprocess.check_output(["fping","8.8.8.8","-C","1"]))
            print(op[int(op.find('bytes'))+7:int(op.find('('))-4])
            x.append( float(op[int(op.find('bytes'))+7:int(op.find('('))-4]))
        except Exception  as e:
            x.append(9999)
            print(e)
        y.append(i)
        i+=1

        line.set_data(y, x)
        figure.gca().relim()
        figure.gca().autoscale_view()
        return line


animation = FuncAnimation(figure, update, interval=200)
pyplot.show()



