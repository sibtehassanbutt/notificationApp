import time
from plyer import notification

def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Hourly Reminder',
        timeout=10  # Notification duration in seconds
    )

# Customize your title and message
notification_title = "Take a Break!"
notification_message = "Stand up, stretch, or grab a glass of water. Stay refreshed!"

try:
    while True:
        send_notification(notification_title, notification_message)
        time.sleep(10)  # Wait for 1 hour (3600 seconds)
except KeyboardInterrupt:
    print("Notification script stopped.")