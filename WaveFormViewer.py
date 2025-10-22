import streamlit as st
import librosa
import matplotlib.pyplot as plt
import numpy as np

st.title("Heartbeat Waveform Visualizer")

uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"], key="heartbeatupload")

if uploaded_file is not None:
    if st.button("Show Waveform"):
        y, sr = librosa.load(uploaded_file, sr=None)

        # Limit duration to 1 second
        duration_limit = 1
        max_samples = int(duration_limit * sr)
        y_trimmed = y[:max_samples]

        # Scale amplitude for visibility
        amplitude_factor = 500
        y_trimmed *= amplitude_factor

        # Time axis
        time = np.linspace(0, len(y_trimmed) / sr, num=len(y_trimmed))

        # Plot waveform
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.plot(time, y_trimmed, color='blue')
        ax.set_title("Heartbeat Waveform")
        ax.set_xlabel("Time [s]")
        ax.set_ylabel("Amplitude")
        ax.grid(True)

        # Display plot
        st.pyplot(fig)

        # Show success message
        st.success(f"Waveform plotted! Sample rate: {sr} Hz | Duration: {len(y)/sr:.2f} seconds")


else:
    st.write("Please upload the WAV file")
