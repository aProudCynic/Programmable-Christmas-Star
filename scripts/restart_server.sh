#!/bin/bash
source /home/project/myenv/bin/activate
cd /home/project/server
PID=$(ps aux | grep 'uvicorn myapp:app' | grep -v grep | awk {'print $2'} | xargs)
if [ "$PID" != "" ]
then
kill -9 $PID
sleep 2
echo "" > nohup.out
echo "Restarting FastAPI server"
else
echo "No such process. Starting new FastAPI server"
fi
nohup uvicorn myapp:app &
