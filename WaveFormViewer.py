import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import librosa

st.title("WaveForm Visualiser.")
uploaded_file= st.file_uploader("Please upload your WAV file.", type="wav" , key="waveformuploader.")
if uploaded_file is not None:
        y,sr= librosa.load(uploaded_file,sr=None)
        duration=st.slider("Select Time duration Scale", 0.25, 5.0, 0.5)
        maxSamples=int(duration*sr)
        y=y[:maxSamples]

        amp = st.slider("Select Amplitude Scale", 100, 5000, 500, step=100)
        y*=amp

        time=np.linspace(0,len(y)/sr,num=len(y))

        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(time, y, color='blue')
        ax.set_title("WaveForm Visualiser")
        ax.set_xlabel("Time [s]")
        ax.set_ylabel(f"Amplitude (Scaled ×{amp})")
        ax.grid(True)

        st.pyplot(fig)
        plt.show()


    