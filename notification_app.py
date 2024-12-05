import time
import threading
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
from plyer import notification

class NotificationApp:
    def __init__(self, root):  # Corrected constructor
        self.root = root
        self.root.title("Notification App")
        self.root.geometry("300x200")
        
        # Notification variables
        self.is_running = False
        self.interval = StringVar(value="60")  # Default interval (in minutes)

        # GUI Elements
        Label(root, text="Notification Interval (minutes):").pack(pady=10)
        self.interval_entry = Entry(root, textvariable=self.interval, width=10)
        self.interval_entry.pack(pady=5)
        
        self.start_button = Button(root, text="Start Notifications", command=self.start_notifications, bg="green", fg="white")
        self.start_button.pack(pady=5)
        
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
                interval_in_minutes = int(self.interval.get())
                self.send_notification()
                time.sleep(interval_in_minutes * 60)
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter a valid number for the interval.")
                self.stop_notifications()
                break

    def start_notifications(self):
        """Start the notification loop."""
        if self.is_running:
            return
        try:
            # Validate interval
            interval_in_minutes = int(self.interval.get())
            if interval_in_minutes <= 0:
                raise ValueError
            self.is_running = True
            self.status_label.config(text="Status: Running", fg="green")
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
            # Run notification loop in a separate thread
            threading.Thread(target=self.notification_loop, daemon=True).start()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid positive number for the interval.")

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