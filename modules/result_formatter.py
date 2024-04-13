from modules.speed_calculator import calculate_speed

EXCELLENT_QUALITY = "Excellent"
VERY_GOOD_QUALITY = "Very Good"
GOOD_QUALITY = "Good"
AVERAGE_QUALITY = "Average"
BELOW_AVERAGE_QUALITY = "Below Average"
POOR_QUALITY = "Poor"
VERY_POOR_QUALITY = "Very Poor"

def format_result(download_speed, upload_speed):
    result = ""

    if download_speed is not None:
        download_speed, download_unit = calculate_speed(download_speed, 1)
        result += f"\nDownload speed: {download_speed:.2f} {download_unit}\n"
        if upload_speed is None:
            if download_speed > 100:
                result += f"Download quality: {EXCELLENT_QUALITY}"
            elif download_speed > 50:
                result += f"Download quality: {VERY_GOOD_QUALITY}"
            elif download_speed > 20:
                result += f"Download quality: {GOOD_QUALITY}"
            elif download_speed > 10:
                result += f"Download quality: {AVERAGE_QUALITY}"
            elif download_speed > 5:
                result += f"Download quality: {BELOW_AVERAGE_QUALITY}"
            elif download_speed > 1:
                result += f"Download quality: {POOR_QUALITY}"
            else:
                result += f"Download quality: {VERY_POOR_QUALITY}"

    if upload_speed is not None:
        upload_speed, upload_unit = calculate_speed(upload_speed, 1)
        result += f"Upload speed: {upload_speed:.2f} {upload_unit}\n"
        if download_speed is None:
            if upload_speed > 30:
                result += f"Upload quality: {EXCELLENT_QUALITY}"
            elif upload_speed > 10:
                result += f"Upload quality: {VERY_GOOD_QUALITY}"
            elif upload_speed > 5:
                result += f"Upload quality: {GOOD_QUALITY}"
            elif upload_speed > 2:
                result += f"Upload quality: {AVERAGE_QUALITY}"
            elif upload_speed > 1:
                result += f"Upload quality: {BELOW_AVERAGE_QUALITY}"
            elif upload_speed > 0.5:
                result += f"Upload quality: {POOR_QUALITY}"
            else:
                result += f"Upload quality: {VERY_POOR_QUALITY}"

    if download_speed is not None and upload_speed is not None:
        result += "\n"
        if download_speed > 100 and upload_speed > 30:
            result += f"Connection quality: {EXCELLENT_QUALITY}"
        elif download_speed > 50 and upload_speed > 10:
            result += f"Connection quality: {VERY_GOOD_QUALITY}"
        elif download_speed > 20 and upload_speed > 5:
            result += f"Connection quality: {GOOD_QUALITY}"
        elif download_speed > 10 and upload_speed > 2:
            result += f"Connection quality: {AVERAGE_QUALITY}"
        elif download_speed > 5 and upload_speed > 1:
            result += f"Connection quality: {BELOW_AVERAGE_QUALITY}"
        elif download_speed > 1 and upload_speed > 0.5:
            result += f"Connection quality: {POOR_QUALITY}"
        else:
            result += f"Connection quality: {VERY_POOR_QUALITY}"

    return result