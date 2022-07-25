#!/bin/bash

cd ../server
virtualenv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
