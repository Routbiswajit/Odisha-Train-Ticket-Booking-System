import streamlit as st
from random import randint

# Predefined Odisha railway routes with distances (km)
routes = {
    ("bhubaneswar", "puri"): 60,
    ("bhubaneswar", "cuttack"): 30,
    ("bhubaneswar", "khurda road"): 20,
    ("bhubaneswar", "berhampur"): 170,
    ("cuttack", "sambalpur"): 310,
    ("sambalpur", "jharsuguda"): 50,
    ("sambalpur", "rourkela"): 170,
    ("rourkela", "jharsuguda"): 100,
    ("balasore", "bhadrak"): 60,
    ("berhampur", "rayagada"): 150,
    ("rayagada", "koraput"): 170,
    ("koraput", "jeypore"): 30
}

# Class multipliers
class_multipliers = {
    "Sleeper": 1.0,
    "3AC": 1.5,
    "2AC": 2.0,
    "1AC": 3.0
}

# Streamlit UI
st.set_page_config(page_title="Odisha Railway Booking", page_icon="🚆")
st.title("🚆 Odisha Railway Booking System")
st.markdown("### Book your train ticket easily with distance-based pricing and class selection.")

ticket_no = st.number_input("Enter Ticket No:", min_value=1, step=1)
start = st.selectbox("Choose Starting Station:", sorted(set([s for s, _ in routes.keys()])))
destination = st.selectbox("Choose Destination Station:", sorted(set([d for _, d in routes.keys()])))
travel_class = st.radio("Choose Class:", ["Sleeper", "3AC", "2AC", "1AC"])

if st.button("Book Ticket"):
    start_lower = start.lower()
    dest_lower = destination.lower()
    route = (start_lower, dest_lower)

    if route not in routes:
        st.error("❌ Route not found in database. Please try another.")
    else:
        distance = routes[route]
        train_no = randint(11111, 99999)

        # Base fare
        base_fare = distance * 2 if distance <= 100 else distance * 5
        seat_price = int(base_fare * class_multipliers[travel_class])

        # Ticket Output
        st.success("🎟️ Ticket Confirmed!")
        st.write(f"**Ticket No:** {ticket_no}")
        st.write(f"**Train No:** {train_no}")
        st.write(f"**From:** {start.title()} → **To:** {destination.title()}")
        st.write(f"**Class:** {travel_class}")
        st.write(f"**Distance:** {distance} km")
        st.write(f"**Price:** ₹{seat_price}")
        st.write("✅ Thank you for booking with Odisha Railways")
