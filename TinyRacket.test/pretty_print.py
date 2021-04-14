#!/bin/python
import glob
import os
from subprocess import PIPE, STDOUT, run
from string import Template
try:
    from tqdm import tqdm
except ImportError:
    def tqdm(x):
        return x

DISABLE_ALLOWED = False
FILE_DIRECTORY = '../TinyRacket.example'
PRETTY_PRINT_TEMPLATE = Template("(pretty-write '$file_contents)")

def pretty_print(path: str) -> str:
    with open(path, 'r') as file:
        file_contents = file.read()
    if file_contents.startswith(';disabled') and DISABLE_ALLOWED:
        return
    result = run(['racket', '-e', PRETTY_PRINT_TEMPLATE.substitute(file_contents=file_contents)], stdout=PIPE, stderr=STDOUT, universal_newlines=True)
    pretty_printed = result.stdout.strip()
    if pretty_printed != file_contents:
        with open(path, 'w') as file:
            file.write(pretty_printed)

[pretty_print(test_file) for test_file in tqdm(glob.glob(f'{FILE_DIRECTORY}/*.trt'))]
