#!/usr/bin/env bash

# your paths will be differnet
top_path=/Users/okken/projects/book/bopytest/Boot
code_path=${top_path}/code
venv_path=${top_path}/venv

tasks_pro_dir=${code_path}/$1
start_tests_dir=${code_path}/$2
results_dir=$3

# click and Python3,
# from http://click.pocoo.org/5/python3
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8

# virtual environment
source ${venv_path}/bin/activate

# install project
pip install -e ${tasks_pro_dir}

# run tests
cd ${start_tests_dir}
pytest --junit-xml=${results_dir}/results.xml
