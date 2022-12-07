import json
import yaml
from yaml import CLoader, CDumper
from revChatGPT.revChatGPT import Chatbot
import os
from sys import argv
from parse import py

# from argparse import ArgumentParser

# argparser = ArgumentParser(
# 	prog="docugen",
# 	description="generate docs with le AI(tm)",
# 	epilog="https://docugen.com"
# )

# argparser.add_argument("file", required=True)

file_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{file_path}/config.yaml", "r") as file:
    config = yaml.load(file, Loader=CLoader)

infile = open(argv[1], "r")
# print(infile)

# top level functions only for now
functions = py.find_toplevel_funcs(infile)

print(f"Found {len(functions)} functions.")

doc_prompt_head = "Explain what this function does in one short sentence, then give example code that uses the function:\n"
# doc_prompt_example = "Return only example code using this function:\n"

# for function in functions:
# 	print(function["content"])
# 	print("------------------")

bot = Chatbot({
    'Authorization': config['Authorization'],
    'session_token': config['session_token'],
}, conversation_id=None)

bot.refresh_session()

with open(f"{argv[1].split('.')[0]}-doc.md", "w") as outfile:
	outfile.write(f"# Documentation for `{argv[1]}`\n\n")
	for function in functions:
		head_ask = doc_prompt_head + function["content"]
		resp = bot.get_chat_response(head_ask, output="text")
		print(f'Generated documentation for {function["head"]}.')
		# append results to doc
		output = f"## `{function['head']}`\n" + resp['message'] + "\n\n"
		outfile.write(output)
