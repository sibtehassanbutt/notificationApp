import time
import threading
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from plyer import notification

class NotificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notification App")
        self.root.geometry("300x250")
        
        # Notification variables
        self.is_running = False
        self.hours = StringVar(value="0")   # Default hours
        self.minutes = StringVar(value="0")  # Default minutes
        self.seconds = StringVar(value="0")  # Default seconds

        # GUI Elements
        Label(root, text="Set Notification Interval (HH:MM:SS):").pack(pady=10)
        
        # Entry fields for HH:MM:SS
        Label(root, text="Hours:").pack()
        self.hours_entry = Entry(root, textvariable=self.hours, width=5)
        self.hours_entry.pack(pady=2)
        
        Label(root, text="Minutes:").pack()
        self.minutes_entry = Entry(root, textvariable=self.minutes, width=5)
        self.minutes_entry.pack(pady=2)
        
        Label(root, text="Seconds:").pack()
        self.seconds_entry = Entry(root, textvariable=self.seconds, width=5)
        self.seconds_entry.pack(pady=2)
        
        self.start_button = Button(root, text="Start Notifications", command=self.start_notifications, bg="green", fg="white")
        self.start_button.pack(pady=10)
        
        self.stop_button = Button(root, text="Stop Notifications", command=self.stop_notifications, bg="red", fg="white", state="disabled")
        self.stop_button.pack(pady=5)

        self.status_label = Label(root, text="Status: Stopped", fg="red")
        self.status_label.pack(pady=10)
    
    def send_notification(self):
        """Send a desktop notification."""
        notification.notify(
            title="Reminder!",
            message="Take a break, stretch, or drink water.",
            app_name="Notification App",
            timeout=10
        )
    
    def notification_loop(self):
        """Run the notification loop."""
        while self.is_running:
            try:
                hours = int(self.hours.get())
                minutes = int(self.minutes.get())
                seconds = int(self.seconds.get())
                interval_in_seconds = hours * 3600 + minutes * 60 + seconds
                
                if interval_in_seconds <= 0:
                    raise ValueError("Interval must be greater than 0.")
                
                self.send_notification()
                time.sleep(interval_in_seconds)
            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e))
                self.stop_notifications()
                break

    def start_notifications(self):
        """Start the notification loop."""
        if self.is_running:
            return
        try:
            # Validate inputs
            hours = int(self.hours.get())
            minutes = int(self.minutes.get())
            seconds = int(self.seconds.get())
            
            if hours < 0 or minutes < 0 or seconds < 0:
                raise ValueError("Time values must be non-negative.")
            
            interval_in_seconds = hours * 3600 + minutes * 60 + seconds
            if interval_in_seconds <= 0:
                raise ValueError("Interval must be greater than 0.")
            
            self.is_running = True
            self.status_label.config(text="Status: Running", fg="green")
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
            # Run notification loop in a separate thread
            threading.Thread(target=self.notification_loop, daemon=True).start()
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))

    def stop_notifications(self):
        """Stop the notification loop."""
        self.is_running = False
        self.status_label.config(text="Status: Stopped", fg="red")
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

# Main App Execution
if __name__ == "__main__":
    root = Tk()
    app = NotificationApp(root)
    root.mainloop()
