# for App Screenshot Extractor
folder_apks = "apks"
folder_screenshots = "screenshots"
running_minutes = 5
throttle = 300

# for Document Screenshot Extractor
document_url = 'https://play.google.com/store/apps/details?id=com.midifun'
package_name = 'com.midifun'

# for image_lib
origin_size = (1080, 1920)
target_size_best = [i // 30 for i in origin_size]
crop_ratio = (0.042, 0.078)  # top and bottom
