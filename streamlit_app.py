import streamlit as st
from streamlit_javascript import st_javascript

st.title("iPhone Accelerometer Data Capture")

# Include the JavaScript code for motion data collection
js_code = """
let motionData = [];
let isSending = false;
const correctPasswordHash = 'Skijump2023'; // Hashing is simulated

function startSending() {
    const enteredPassword = prompt('Enter the password:');

    // Check if motion data permission is required
    if (typeof DeviceMotionEvent.requestPermission === 'function') {
        // Request permission from the user
        DeviceMotionEvent.requestPermission()
            .then(permissionState => {
                if (permissionState === 'granted') {
                    // Permission granted, start listening to motion events
                    handleMotionPermissionGranted();
                } else {
                    alert('Motion data permission denied.');
                }
            })
            .catch(error => {
                console.error('Error requesting motion data permission:', error);
                alert('Error requesting motion data permission.');
            });
    } else {
        // Browser or device doesn't support the Permissions API
        handleMotionPermissionGranted();
    }

    function handleMotionPermissionGranted() {
        // Validate the password
        if (enteredPassword === correctPasswordHash) {
            if (window.DeviceMotionEvent) {
                window.addEventListener('devicemotion', handleMotion);
                isSending = true;
                motionData = []; // Clear existing data when starting
                setTimeout(stopSending, 5000); // Set capture duration
            } else {
                alert("Device Motion not supported.");
            }
        } else {
            alert("Incorrect password.");
        }
    }
}

function stopSending() {
    window.removeEventListener('devicemotion', handleMotion);
    isSending = false;
    sendDataToStreamlit(motionData); // Send data to Streamlit
}

function handleMotion(event) {
    if (isSending) {
        const acceleration = event.acceleration;
        const rotationRate = event.rotationRate;
        motionData.push({
            acceleration: acceleration,
            rotationRate: rotationRate
        });
    }
}

function sendDataToStreamlit(data) {
    return data;  // Return collected motion data to Streamlit
}

startSending();
"""

# Execute the JavaScript code and return the motion data to Streamlit
motion_data = st_javascript(js_code)

# Display the captured motion data in Streamlit
if motion_data:
    st.write("Captured motion data:", motion_data)
else:
    st.write("No motion data captured yet.")
