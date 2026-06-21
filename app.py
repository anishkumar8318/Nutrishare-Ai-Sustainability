# NutriShare AI - Core Backend Logic
# Developed for 1M1B AI for Sustainability Virtual Internship

import datetime

print("Initializing NutriShare AI System...")

# Mock database of NGOs and their capacities
ngo_database = [
    {"name": "City Shelter A", "capacity_meals": 50, "distance_km": 2.4},
    {"name": "Hope Foundation Mess", "capacity_meals": 120, "distance_km": 4.1},
    {"name": "Bal Vikas NGO", "capacity_meals": 30, "distance_km": 1.8}
]

def predict_food_surplus(expected_guests, actual_guests):
    """
    Simulating a basic regression model trained on IBM BOB data.
    Predicts leftover meals based on attendance drop.
    """
    if actual_guests >= expected_guests:
        return 0
    
    # On average, 1 un-attended guest = 1.2 wasted plates due to buffer cooking
    leftover_meals = int((expected_guests - actual_guests) * 1.2)
    return max(0, leftover_meals)

def find_nearest_eligible_ngo(surplus_meals):
    """
    AI Optimization concept: Filter NGOs by distance and capacity match
    """
    eligible_ngos = [ngo for ngo in ngo_database if ngo["capacity_meals"] >= surplus_meals]
    
    if not eligible_ngos:
        return "No single NGO has enough capacity. Splitting batches recommended."
        
    # Sort by lowest distance (Nearest Neighbor logic)
    eligible_ngos.sort(key=lambda x: x["distance_km"])
    return eligible_ngos[0]

# --- LIVE TEST SIMULATION ---
if __name__ == "__main__":
    print(f"\n--- Live Run Log: {datetime.date.today()} ---")
    
    # Example scenario: A wedding hall prepared for 500 guests, but only 420 turned up
    expected = 500
    actual = 420
    
    surplus = predict_food_surplus(expected, actual)
    print(f"[AI Model Prediction] Estimated surplus meals: {surplus}")
    
    if surplus > 0:
        best_match = find_nearest_eligible_ngo(surplus)
        print(f"[AI Dispatch Alert] Automated notification sent to: {best_match['name']} ({best_match['distance_km']} km away)")
    else:
        print("[System Status] No surplus detected. No dispatch needed.")
