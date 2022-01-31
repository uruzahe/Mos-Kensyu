#! /bin/bash

ps awx | grep akinator.py | awk '{print $1}' | xargs kill -9
