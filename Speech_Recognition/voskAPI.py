from vosk import Model, KaldiRecognizer
import threading
import os
import json
import pyaudio
from pynput.keyboard import Key, Controller
import time


if (not os.path.exists("Speech_Recognition/Model/Portugues/model") ):
    print ("Please download the model-long-small from https://alphacephei.com/vosk/models and unpack as 'model-long-small' in the current folder.")
    exit (1)

class Speech_Recognition:

    pressed_keys_list = list()
    commands_list_dicionary = dict()
    keyboard = Controller()

    def voice_commands(self,commands_file_name):

        file_path = "../Games/" + commands_file_name

        recognized_commands = ""

        if(os.path.exists(file_path)):

            commands_file = open(file_path,"r")
            file_data = "-@"
            commands_file.readline() # Read the name os columns
            i = 1
            while(file_data != ""): # Fll the command list

                file_data = commands_file.readline()
                if(file_data != ""):

                    commands = file_data.split(",")
                    command1 = commands[0]
                    command2 = commands[1]
                    key = commands[2]
                    key = key.lower()
                    need_to_press = commands[3]
                    need_to_press = need_to_press.split("\n")

                    if(command1 != "-"):
                        recognized_commands = recognized_commands + command1 + " "
                        self.commands_list_dicionary.__setitem__(command1,[key,need_to_press[0]])
                    if (command2 != "-"):
                        recognized_commands = recognized_commands + command2 + " "
                        self.commands_list_dicionary.__setitem__(command2,[key,need_to_press[0]])

            commands_file.close()
            recognized_commands = recognized_commands + "pare finalizar programa"

        model = Model("./Model/Portugues/model")

        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        stream.start_stream()
        speech = ""
        prev_speech = ""
        new_comand = 0
        print(recognized_commands)

        rec = KaldiRecognizer(model, 16000,recognized_commands)
        while True:

            data = stream.read(4000,exception_on_overflow = False)
            if len(data) == 0:
                break
            if  (rec.AcceptWaveform(data)):
                final = rec.Result()
                new_comand = 0
                speech = " "
            else:
                partial = rec.PartialResult()
                result = json.loads(partial)
                speech = result["partial"]

                phrase = speech.split(" ")
                speech = phrase[len(phrase) - 1]


                if (new_comand == len(phrase) and new_comand != 0):
                    speech = " "

                if (speech in self.commands_list_dicionary):
                    command = self.commands_list_dicionary[speech]
                    key = command[0]
                    press_key = command[1]

                    if(key == "space"):
                        if(press_key == "yes"):              # Preciso manter precionada
                            self.keyboard.press(Key.space)
                            self.pressed_keys_list.append(key)
                        else:
                            self.keyboard.press(Key.space)
                            time.sleep(0.500)
                            self.keyboard.release(Key.space)
                    elif(key == "shift"):
                        if (press_key == "yes"):
                            self.keyboard.press(Key.shift)
                            self.pressed_keys_list.append(key)
                        else:
                            self.keyboard.press(Key.shift)
                            time.sleep(0.500)
                            self.keyboard.release(Key.shift)
                    elif(key == "ctrl"):
                        if (press_key == "yes"):
                            self.keyboard.press(Key.ctrl)
                            self.pressed_keys_list.append(key)
                        else:
                            self.keyboard.press(Key.ctrl)
                            time.sleep(0.500)
                            self.keyboard.release(Key.ctrl)
                    elif(key == "tab"):
                        if (press_key == "yes"):
                            self.keyboard.press(Key.tab)
                            self.pressed_keys_list.append(key)
                        else:
                            self.keyboard.press(Key.tab)
                            time.sleep(0.500)
                            self.keyboard.release(Key.tab)

                    else: # Not special commands
                        if (press_key == "yes"):

                            if(key == "a"):

                                if("d" in self.pressed_keys_list):
                                    print("Liberando d")
                                    self.keyboard.release("d")
                                    self.pressed_keys_list.remove("d")

                            if (key == "d"):

                                if ("a" in self.pressed_keys_list):
                                    print("Liberando a")
                                    self.keyboard.release("a")
                                    self.pressed_keys_list.remove("a")

                            if (key == "w"):

                                if ("s" in self.pressed_keys_list):
                                    print("Liberando s")
                                    self.keyboard.release("s")
                                    self.pressed_keys_list.remove("s")

                            if (key == "s"):

                                if ("w" in self.pressed_keys_list):
                                    print("Liberando w")
                                    self.keyboard.release("w")
                                    self.pressed_keys_list.remove("w")

                            self.keyboard.press(key)
                            self.pressed_keys_list.append(key)
                        else:
                            self.keyboard.press(key)
                            time.sleep(0.500)
                            self.keyboard.release(key)

                    new_comand = len(phrase)
                    prev_speech = speech

                elif(speech == "pare"):  # Release all keys that was pressed

                    for key in self.pressed_keys_list:

                        if (key == "space"):
                            self.keyboard.release(Key.space)
                        elif (key == "shift"):
                            self.keyboard.release(Key.shift)
                        elif (key == "ctrl"):
                            self.keyboard.release(Key.ctrl)
                        elif (key == "tab"):
                            self.keyboard.release(Key.tab)
                        else:
                            self.keyboard.release(key)

                    new_comand = len(phrase)
                    prev_speech = speech

                    self.pressed_keys_list.clear()

                if(speech == "finalizar"):
                    prev_speech = "finalizar"

                if(prev_speech == "finalizar" and speech == "programa"):
                    print("Indo finalizar pograma")
                    break;


        print("Finalizando Programa")
        stream.stop_stream()
        stream.close()




# threading.Thread(target=speech.voice_commands("Fall Guy's.csv")).start()


