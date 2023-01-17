# imports
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


# def reverse(sig: np.ndarray) -> np.ndarray:
#     print(type(sig))
#     a = sig
#     print("after reverse")
#     print(-sig)
#     # add the negative of the signal to the signal of every index

#     # printing sum of the signal and the negative of the signal

#     return -sig


def getNoise():
    # reads the noise file
    raw = wave.open("Ensoniq-ZR-76-01-Dope-77.wav")
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype="int16")
    print("noise")
    print(signal)
    return -signal


# shows the sound waves
def visualize(path: str):

    # reading the audio file
    raw = wave.open(path)

    # reads all the frames
    # -1 indicates all or max frames
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype="int16")
    getNoise()

    # gets the frame rate
    f_rate = raw.getframerate()

    # to Plot the x-axis in seconds
    # you need get the frame rate
    # and divide by size of your signal
    # to create a Time Vector
    # spaced linearly with the size
    # of the audio file
    time = np.linspace(
        0,  # start
        len(signal) / f_rate,
        num=len(signal)
    )
    # create an array

    # using matplotlib to plot
    # creates a new figure
    plt.figure(1)

    # title of the plot
    plt.title("Sound Wave")

    # label of x-axis
    plt.xlabel("Time")

    # actual plotting
    new_arr = []
    i = 0
    rev_noise = getNoise()
    while i < len(signal):
        if(i < len(rev_noise)):
            new_arr.append(signal[i] + -rev_noise[i])
        i = i + 1
    plt.plot(time, signal, color='red')
    new_arr = np.array(new_arr)
    plt.plot(time, new_arr, color='green')
    print(type(signal))
    print(new_arr)
    # print(new_arr)
    # shows the plot
    # in new window
    plt.show()

    # you can also save
    # the plot using
    # plt.savefig('filename')
    



if __name__ == "__main__":

    # gets the command line Value
    path = "mixed.wav"

    visualize(path)
