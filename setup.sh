#!/data/data/com.termux/files/usr/bin/bash
set -e
pkg update -y && pkg install python git -y
pip install -r requirements.txt
mkdir -p dl
echo "نصب شد. اجرا: python -m allfinder.cli \"عبارت\""
