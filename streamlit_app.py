
import streamlit as st
from streamlit_javascript import st_javascript

st.title("iPhone Accelerometer and Gyroscope Data")

# JavaScript code to capture accelerometer and gyroscope data
js_code = """
    async function getMotionData() {
        return new Promise((resolve, reject) => {
            if (window.DeviceMotionEvent) {
                window.addEventListener('devicemotion', function(event) {
                    const motionData = {
                        acceleration: event.acceleration,
                        accelerationIncludingGravity: event.accelerationIncludingGravity,
                        rotationRate: event.rotationRate,
                        interval: event.interval
                    };
                    resolve(motionData);
                });
            } else {
                reject("DeviceMotionEvent is not supported.");
            }
        });
    }

    getMotionData().then(data => data).catch(error => error);
"""

# Execute the JavaScript and return the motion data
motion_data = st_javascript(js_code)

# Check if motion data is available and display it
if motion_data:
    st.write("Acceleration (without gravity):", motion_data.get('acceleration', 'Unavailable'))
    st.write("Acceleration (with gravity):", motion_data.get('accelerationIncludingGravity', 'Unavailable'))
    st.write("Rotation rate:", motion_data.get('rotationRate', 'Unavailable'))
    st.write("Sensor data interval:", motion_data.get('interval', 'Unavailable'))
else:
    st.write("Unable to fetch motion data. Make sure motion access is enabled on your device.")
