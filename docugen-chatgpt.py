#!/usr/bin/env python3

import json
import yaml
from yaml import CLoader, CDumper
from revChatGPT.revChatGPT import Chatbot
import os
from sys import argv
import fmtutil
from parse import py
from argparse import ArgumentParser

argparser = ArgumentParser(
	# prog="docugen",
	description="generate docs with le AI(tm)",
	epilog="https://github.com/turtlebasket/docugen"
)

argparser.add_argument("filename")
argparser.add_argument("-o", dest="output directory",  help="directory to write docs to")
argparser.add_argument("-m", dest="model", help="model to use to generate documentation", choices=["chatgpt"])
argparser.add_argument("-f", dest="format", help="formatting of output documentation", choices=["md"])
args = argparser.parse_args()

file_path = os.path.dirname(os.path.realpath(__file__))
with open(f"{file_path}/config.yaml", "r") as file:
    config = yaml.load(file, Loader=CLoader)

infile = open(args.filename, "r")

# python & top level functions only for now
functions = py.find_toplevel_funcs(infile)

print(f"Found {len(functions)} functions.")

if len(functions) >= 3:
	print(f"Grab a cup of coffee, this could take a while.")

doc_prompt_head = "Explain what this function does in one short sentence, then give example code that uses the function:\n"
# doc_prompt_example = "Return only example code using this function:\n"

bot = Chatbot({
    'Authorization': config['Authorization'],
    'session_token': config['session_token'],
}, conversation_id=None)

bot.refresh_session()

with open(f"{args.filename.split('.')[0]}-doc.md", "w") as outfile:
	outfile.write(f"# Documentation for `{argv[1]}`\n\n")
	for function in functions:
		head_ask = doc_prompt_head + function["content"]
		resp = bot.get_chat_response(head_ask, output="text")
		print(f'Generated documentation for {function["head"]}.')
		# append results to doc
		output = f"### `{function['head']}`\n" + fmtutil.highlight_multiline_code_md(resp['message'], "python") + "\n\n"
		outfile.write(output)
