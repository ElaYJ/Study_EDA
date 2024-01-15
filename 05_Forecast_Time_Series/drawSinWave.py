
import numpy as np 
import matplotlib.pyplot as plt 

def plotSinWave(**kwargs):
    # Docstring
    """
    plot sine wave 
    y = a sin(2 pi f t + t_0) + b
    - Param:
        - amplitude: 진폭
        - frequency: 주파수, 진동
        - t_0: start time
    """
    kwargs = {
        "amp": 1,
        "freq": 1,
        "startTime": 0,
        "endTime": 1.01,
        "sampleTime": 0.01,
        "bias": 0,
        "figsize": (12, 6)
    }
    amp = kwargs.get("amp")
    freq = kwargs.get("freq")
    sampleTime = kwargs.get("sampleTime")
    startTime = kwargs.get("startTime")
    endTime = kwargs.get("endTime")
    bias = kwargs.get("bias")
    figsize = kwargs.get("figsize")
    
    time = np.arange(startTime, endTime, sampleTime)
    fsin = amp * np.sin(2 * np.pi * freq * time + startTime) + bias
    
    plt.figure(figsize)
    plt.plot(time, fsin)
    plt.grid(True)
    plt.xlabel("time")
    plt.ylabel("sin")
    plt.title(str(amp) + "*sin(2*pi" + str(freq) + "*t+" + str(startTime) + ")+" + str(bias))
    plt.show()
    
if __name__ == "__main__":
    print("hello world~!!")
    print("this is test graph!!")
    plotSinWave(amp=1, endTime=2)
