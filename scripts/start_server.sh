#!/bin/bash

cd ../server
source virtualenv/bin/activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 4000
