import pyttsx3
import speech_recognition as sr
from LLM_models_api.Mixtral_8x7B_v0_1 import run_inference
import cv2                                                                         
import tkinter as tk 

camera_access_granted=False
microphone_access_granted=False
def speak_text(text):
    """Convert text to speech and speak."""
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Speed of speech
    engine.say(text)                 # Speak the text
    engine.runAndWait()

def grant_microphone_access():
    """Callback function for granting microphone access."""
     
    microphone_access_granted = True
    microphone_window.destroy()  # Close the Tkinter window

def grant_camera_access():
    """Callback function for granting camera access."""
    camera_access_granted = True
    camera_window.destroy()      # Close the Tkinter window

def check_microphone_access():
    """Check microphone access and prompt the user to grant access."""
    global microphone_access_granted
    speak_text("Checking microphone access. Please grant microphone access.")
    
    # Open a Tkinter window to prompt for microphone access
    global microphone_window
    microphone_window = tk.Tk()
    microphone_window.title("Microphone Access")
    microphone_window.geometry("300x150")
    
    label = tk.Label(microphone_window, text="Allow access to microphone?")
    label.pack(pady=20)

    allow_button = tk.Button(microphone_window, text="Allow", command=grant_microphone_access)
    allow_button.pack(side=tk.LEFT, padx=20)

    deny_button = tk.Button(microphone_window, text="Deny", command=microphone_window.destroy)
    deny_button.pack(side=tk.RIGHT, padx=20)
    microphone_window.mainloop()

def check_camera_access():
    """Check camera access and prompt the user to grant access."""
    global camera_access_granted
    
    speak_text("Checking camera access...")
   # Open a Tkinter window to prompt for camera access
    global camera_window
    camera_window = tk.Tk()
    camera_window.title("Camera Access")
    camera_window.geometry("300x150")
        
    label = tk.Label(camera_window, text="Allow access to camera?")
    label.pack(pady=20)

    allow_button = tk.Button(camera_window, text="Allow", command=grant_camera_access)
    allow_button.pack(side=tk.LEFT, padx=20)

    deny_button = tk.Button(camera_window, text="Deny", command=camera_window.destroy)
    deny_button.pack(side=tk.RIGHT, padx=20)

    camera_window.mainloop()
    if(camera_access_granted==True):
        speak_text("Camera access granted.")
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            speak_text("Error: Could not open camera.")
    
    #cap.release()

#code to activate camera 
def activate_camera():
    """Activate the camera and start streaming."""
    speak_text("Activating camera.")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        speak_text("Error: Could not open camera.")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            speak_text("Error: Failed to capture frame.")
            break
        cv2.imshow('Camera', frame) # Display the frame
        
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Break the loop if 'q' is pressed
            break
    cap.release()
cv2.destroyAllWindows()

#code to listen user prompts
def listen_for_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        user_input = recognizer.recognize_google(audio)
        print("Recognized prompt:", user_input)
        return user_input


#code to listen prompts from user
def listen_for_prompt(): 
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Converting speech to audio using Google Speech Recognition
        user_input = recognizer.recognize_google(audio)
        print("Recognized prompt:", user_input)
        return user_input

        #block to handle- unable to hear prompts
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
        #block to handle- Google speech API error
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# Main function logic block
def main():
    # Initialize access flags 

   
    speak_text("Hi, I am Chintu. Your virtual AI assistant")
    # speak_text("please help me with some permissions.")
    # check_microphone_access() # Check microphone access
    # if microphone_access_granted:
    #     check_camera_access() # Check camera access if microphone access is granted
    #     #activate_camera()     #call to start camera
    # speak_text("okay, we are good to go.")
    speak_text("what is your name?")
    name= listen_for_prompt()
    
    speak_text("okay,Good to know hope you are having a good day today.")
    speak_text(f"How can I help you {name} ?")
    speak_text("okay.")
    
    # activating camera- if both microphone and camera access granted
    # if microphone_access_granted or camera_access_granted:
    #     print("debugging")
    #     #infinite loop- keeping assistant active
    #     while True: 
    #         # Listening for the prompt
    #         speak_text("Please speak your query.")
    #         prompt = listen_for_prompt()

    #         if prompt== "exit":
    #             break

    #         elif prompt is not None:
    #             # print("Prompt received:", prompt)
    #             speak_text("Processing your request.")

    #             # Run inference with the received prompt
    #             inference_result = run_inference(prompt)
    #             if inference_result is not None:
    #                 # Get the inference result as text
    #                 # print("Inference result:", inference_text)s
    #                 inference_text = inference_result[0]    
    #                 print(inference_text) 

    #                 for question, answer in inference_text.items():
    #                 # Speak the inference result
    #                     speak_text(answer)

    #             else:
    #                 speak_text("Sorry, I couldn't process your request.")
    while True: 
            # Listening for the prompt
            speak_text("Please speak your query.")
            prompt = listen_for_prompt()

            if prompt== "exit":
                break

            elif prompt is not None:
                # print("Prompt received:", prompt)
                speak_text("Processing your request.")

                # Run inference with the received prompt
                inference_result = run_inference(prompt)
                if inference_result is not None:
                    # Get the inference result as text
                    # print("Inference result:", inference_text)s
                    inference_text = inference_result[0]    
                    print(inference_text) 

                    for question, answer in inference_text.items():
                    # Speak the inference result
                        speak_text(answer)

                else:
                    speak_text("Sorry, I couldn't process your request.")

# dender to ensure decline of import of main.py 
if __name__ == "__main__":  
    main()
