#!/usr/bin/env python3

from revChatGPT.V3 import Chatbot
import json
import subprocess
import time
import asyncio

# import sys
# if sys.version_info.major == 3:
#     # Python 3.x 版本
#     # reload(sys)
#     sys.setdefaultencoding('utf-8')

import tkinter as tk
import tkinter.font as tkfont

# 配置系统字体

debug = False

history_file = "input_history.txt"

def save_history(input_text):
    with open(history_file, "a") as file:
        file.write(input_text + "\n")

def load_history():
    try:
        with open(history_file, "r") as file:
            history = file.read().splitlines()
    except FileNotFoundError:
        history = []

    return history

# 加载历史输入
history = load_history()

debug = True

"""
Opens the system_prompt.txt file that contains the initial prompt sent to ChatGPT. 
This is where the magic happens.
"""
with open("system_prompt.txt", 'r') as sprompt:
    system_prompt= sprompt.read()


#Connect to the openAI API using your API key
chatbot = Chatbot(api_key="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", system_prompt=system_prompt)


#Main loop
# while True:
#     zenity_command = ["zenity", "--entry", "--title", "Input Dialog", "--text", "Enter your name:", "--entry-text", "s"]

#     result = subprocess.run(zenity_command, capture_output=True, text=True)
#     user_input = result.stdout.strip()
#     if user_input:
#         save_history(user_input)  # 保存用户输入到历史记录
#         print("User input:", user_input)
#     else:
#         print("No input entered.")
#         break

#     prompt = user_input

#     #This part checks whether or not the user typed exit or quit
#     #to exit the script
#     if prompt.lower().strip() in ['exit', 'quit']:
#         exit(0)

#     #And here the query/request/question is sent to chatGPT
#     while True:
#         try:
#             response = chatbot.ask("Human: " + prompt)
#             break
#         except:
#             time.sleep(5)
#             continue

#     #This is in a loop for future proofing reasons in case
#     #chatGPT decides to run another command after running a previous
#     #one, before responding to the user so that the script is not broken.

#     while True:
#         if "@Backend" in response:
#             #Extract the command that chatGPT wants to run and 
#             #deserialize it.
#             res = response.split("@Backend")[1]
#             if debug:
#                 print(res)
#             #if "Backend:" in res and "Proxy Natural Language Processor:" in res:
#             #	print(chatbot.ask("DO NOT REPLY AS BACKEND PLEASE. ONLY REPLY as Proxy Natural Language Processor."))
#             #	break
#             json_str = json.loads(res)
#             command = json_str['command']

#             print("Running command [%s] ..."%(command))
#             #Run the command and store it's outputs for later
#             p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
#             output, err = p.communicate()
#             #Get the exit code
#             exit_code = p.wait()
#             #Send the command results to chatGPT so it can be interpreted by it.
#             try:
#                 response = chatbot.ask('Backend: {"STDOUT":"%s", "EXITCODE":"%s"}'%(output, exit_code))
#             except:
#                 print(f"exception occurred")
#                 continue
#         elif "@Human" in response:
#             if debug:
#                 print(response)
#             chatGPT_reply = "Response:: " + response.split("@Human")[1]
#             print(chatGPT_reply)
#             break
#         else:
#             print("UNEXPECTED RESPONSE:: [%s]"%(response))
#             break

import tkinter as tk
from tkinter import font

async def HumanAsk(prompt):
    print("human 1")
    while True:
        try:
            print("human ask:", prompt)
            response = await chatbot.ask_async("Human: " + prompt)
            print("human ask done, " + response)
            process_response(response)
            break
        except:
            print("error")
            time.sleep(5)
            continue

def process_response(response):
    print(f"resp:{response}\n")
    while True:
        if "@Backend" in response:
            #Extract the command that chatGPT wants to run and 
            #deserialize it.
            res = response.split("@Backend")[1]
            print(f"processing backend\n")
            if debug:
                print(res)
            #if "Backend:" in res and "Proxy Natural Language Processor:" in res:
            #	print(chatbot.ask("DO NOT REPLY AS BACKEND PLEASE. ONLY REPLY as Proxy Natural Language Processor."))
            #	break
            json_str = json.loads(res)
            command = json_str['command']

            print("Running command [%s] ..."%(command))
            #Run the command and store it's outputs for later
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) 
            output, err = p.communicate()
            #Get the exit code
            exit_code = p.wait()
            #Send the command results to chatGPT so it can be interpreted by it.
            try:
                response = chatbot.ask('Backend: {"STDOUT":"%s", "EXITCODE":"%s"}'%(output, exit_code))
            except:
                print(f"exception occurred")
                continue
        elif "@Human" in response:
            if debug:
                print(response)
            print(f"processing human\n")
            chatGPT_reply = "Response:: " + response.split("@Human")[1]
            print(chatGPT_reply)
            append_text(chatGPT_reply)
            break
        else:
            print("UNEXPECTED RESPONSE:: [%s]"%(response))
            break

def append_text(text):
    print("xxxx")
    text_display.insert(tk.END, text + "\n")  # 将文本追加到文本显示框中
    print("xxxx")
    print("run done")
    entry.delete(0, tk.END)  # 清空输入框

def append_input():
    print("xxxx")
    text=entry.get()
    append_text(text)
    asyncio.run(new_task(text))

async def new_task(text):
    print("new_task")
    asyncio.create_task(HumanAsk(text))
    print("new_task done")

# 创建主窗口
window = tk.Tk()
window.title("文本显示窗口")

import tkinter as tk
import tkinter.font as tkfont

# 配置系统字体
tk.font.nametofont("TkDefaultFont").configure(family="FiraCode")

#custom_font = font.Font(family="FiraCode Nerd Font Medium", size=12)
#custom_font = font.Font(family="宋体", size=12)
custom_font = tkfont.Font(family="song ti", size=12)

# 创建文本显示框
text_display = tk.Text(window, font=custom_font)
text_display.grid(row=0, column=0, columnspan=2)

# 创建输入框
entry = tk.Entry(window, font=custom_font)
entry.grid(row=1, column=0)

# 创建追加按钮
button = tk.Button(window, text="追加", command=append_input, font=custom_font)
button.grid(row=1, column=1)

def main():
    # 进入主循环
    window.mainloop()

asyncio.run(main())