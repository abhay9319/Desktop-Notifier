from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message="Rest is better for mental health, increased concentration and memory, a healthier immune system, reduced stress, improve mood and even a better metabolism",
            app_icon=r"C:\Users\Abhay Dhiman\PycharmProjects\Python_Projects\person_man_secure_worker_safety_security_employee_icon_261568.ico",
            timeout=5
        )
        time.sleep(60*60)
