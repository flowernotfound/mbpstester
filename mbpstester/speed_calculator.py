BITS_PER_BYTE = 8
KILOBITS_PER_MEGABIT = 1000

def calculate_speed(size_in_bytes, time_in_seconds):
    speed_bps = size_in_bytes * BITS_PER_BYTE / time_in_seconds
    
    if speed_bps < KILOBITS_PER_MEGABIT:
        speed = speed_bps
        unit = "bps"
    elif speed_bps < KILOBITS_PER_MEGABIT * KILOBITS_PER_MEGABIT:
        speed = speed_bps / KILOBITS_PER_MEGABIT
        unit = "Kbps"
    else:
        speed = speed_bps / (KILOBITS_PER_MEGABIT * KILOBITS_PER_MEGABIT)
        unit = "Mbps"
    
    return speed, unit