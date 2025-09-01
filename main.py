from voice_module import listen_to_user
from vision_module import detect_objects_from_camera
from response_module import respond_to_user

def main():
    while True:
        command = listen_to_user()

        if "camera" in command or "see" in command:
            result = detect_objects_from_camera()
            respond_to_user(result)

        elif "hello" in command:
            respond_to_user("Hi there! How can I assist you today?")

        elif "exit" in command or "quit" in command:
            respond_to_user("Goodbye!")
            break

        else:
            respond_to_user("I'm not sure how to respond to that yet.")

if __name__ == "__main__":
    main()
