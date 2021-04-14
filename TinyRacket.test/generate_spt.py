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

DISABLED_ALLOWED = False
FILE_DIRECTORY = '../TinyRacket.example'
OUTPUT_FILE_NAME = 'racket_validation'

FILE_TEMPLATE = Template("""module $file_name

language TinyRacket

$tests""")

TEST_TEMPLATE = Template("""test $file_name [[
$file_contents
]]
analysis succeeds
run compile-and-run to "$file_result"

""")

tests_created = {}

def generate_test(path: str) -> str:
    with open(path, 'r') as file:
        file_name = os.path.basename(path)
        file_contents = file.read().strip()
        if file_contents.startswith(';disabled') and DISABLE_ALLOWED:
            return ''
        result = run(['racket', '-e', file_contents], stdout=PIPE, stderr=STDOUT, universal_newlines=True)
        file_result = result.stdout.replace('#f', '0').replace('#t', '1')
        if not file_result:
            raise ValueError(f'No result generated for: {file_name}. Something is probably broken!')
        if file_contents in tests_created:
            duplicates = tests_created.get(file_contents)
            print(f'Duplicate tests found for {file_name}: {str(duplicates)}')
            tests_created.update({file_contents:duplicates + [file_name]})
        else:
            tests_created.update({file_contents:[file_name]})

        return TEST_TEMPLATE.substitute(file_name=file_name, file_contents=file_contents, file_result=file_result)

tests = ''.join([generate_test(test_file) for test_file in tqdm(sorted(glob.glob(f'{FILE_DIRECTORY}/*.trt')))])
with open(f'{OUTPUT_FILE_NAME}.spt', 'w') as file:
    file.write(FILE_TEMPLATE.substitute(file_name=OUTPUT_FILE_NAME, tests=tests).strip())
