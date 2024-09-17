import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

# Parameters for audio stream
SAMPLE_RATE = 44100  # Sampling rate (Hz)
CHUNK_SIZE = 1024    # Number of audio frames per buffer

# Initialize the plot
plt.ion()  # Interactive mode for real-time updating
fig, ax = plt.subplots()
x = np.arange(0, CHUNK_SIZE)
line, = ax.plot(x, np.random.rand(CHUNK_SIZE))
ax.set_ylim([-1, 1])
ax.set_xlim([0, CHUNK_SIZE])
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.title('Real-Time Voice Waveform')

# Real-time audio callback function
def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    # Update the plot with new data from the microphone
    line.set_ydata(indata[:, 0])  # Update with mono channel data
    plt.draw()
    plt.pause(0.001)  # Pause for plot update

# Start the audio stream with sounddevice
with sd.InputStream(callback=audio_callback, channels=1, samplerate=SAMPLE_RATE, blocksize=CHUNK_SIZE):
    print("Speak into the microphone, press Ctrl+C to stop.")
    plt.show(block=True)  # Keep the plot window open

# added a line
