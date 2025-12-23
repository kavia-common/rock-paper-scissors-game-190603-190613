#!/bin/bash
cd /home/kavia/workspace/code-generation/rock-paper-scissors-game-190603-190613/rock_paper_scissors_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

