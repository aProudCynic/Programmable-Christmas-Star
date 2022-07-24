#!/bin/bash

cd ../server
python -m uvicorn main:app --reload --host 0.0.0.0 --port 4000
