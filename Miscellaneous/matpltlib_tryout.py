import matplotlib.pyplot as plt
import numpy as np
plt.interactive(False)
myX = np.arange(0,6)
myx2 = myX**2
myx3 = myX**3
plt.plot(myX, myx2, color="black", linewidth=0.5, linestyle="-.", label="f(x)=x^22")
plt.plot(myX, myx3, color="blue", linewidth=0.5, linestyle="--", label="f(x)=x^3" )
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(loc="upper left")
plt.show()
