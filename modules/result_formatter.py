from modules.speed_calculator import calculate_speed

def format_result(download_speed, upload_speed):
    result = ""

    if download_speed is not None:
        download_speed, download_unit = calculate_speed(download_speed, 1)
        result += f"\nDownload speed: {download_speed:.2f} {download_unit}\n"
        if upload_speed is None:
            if download_speed > 100:
                result += "Download quality: Excellent"
            elif download_speed > 50:
                result += "Download quality: Very Good"
            elif download_speed > 20:
                result += "Download quality: Good"
            elif download_speed > 10:
                result += "Download quality: Average"
            elif download_speed > 5:
                result += "Download quality: Below Average"
            elif download_speed > 1:
                result += "Download quality: Poor"
            else:
                result += "Download quality: Very Poor"

    if upload_speed is not None:
        upload_speed, upload_unit = calculate_speed(upload_speed, 1)
        result += f"Upload speed: {upload_speed:.2f} {upload_unit}\n"
        if download_speed is None:
            if upload_speed > 30:
                result += "Upload quality: Excellent"
            elif upload_speed > 10:
                result += "Upload quality: Very Good"
            elif upload_speed > 5:
                result += "Upload quality: Good"
            elif upload_speed > 2:
                result += "Upload quality: Average"
            elif upload_speed > 1:
                result += "Upload quality: Below Average"
            elif upload_speed > 0.5:
                result += "Upload quality: Poor"
            else:
                result += "Upload quality: Very Poor"

    if download_speed is not None and upload_speed is not None:
        result += "\n"
        if download_speed > 100 and upload_speed > 30:
            result += "Connection quality: Excellent"
        elif download_speed > 50 and upload_speed > 10:
            result += "Connection quality: Very Good"
        elif download_speed > 20 and upload_speed > 5:
            result += "Connection quality: Good"
        elif download_speed > 10 and upload_speed > 2:
            result += "Connection quality: Average"
        elif download_speed > 5 and upload_speed > 1:
            result += "Connection quality: Below Average"
        elif download_speed > 1 and upload_speed > 0.5:
            result += "Connection quality: Poor"
        else:
            result += "Connection quality: Very Poor"

    return result