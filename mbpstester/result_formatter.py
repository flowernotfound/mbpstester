from mbpstester.speed_calculator import calculate_speed

def format_result(download_speed, upload_speed):
    download_speed, download_unit = calculate_speed(download_speed, 1)
    upload_speed, upload_unit = calculate_speed(upload_speed, 1)

    result = f"Download speed: {download_speed:.2f} {download_unit}\n"
    result += f"Upload speed: {upload_speed:.2f} {upload_unit}\n"

    if download_speed > 50 and upload_speed > 10:
        result += "Connection quality: Very Good"
    elif download_speed > 20 and upload_speed > 5:
        result += "Connection quality: Good"
    elif download_speed > 10 and upload_speed > 2:
        result += "Connection quality: Normal"
    else:
        result += "Connection quality: Poor"

    return result