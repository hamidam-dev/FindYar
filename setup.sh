#!/data/data/com.termux/files/usr/bin/bash
set -e
pkg update -y && pkg install python git -y
pip install -r requirements.txt
mkdir -p dl
ln -sfn ~/storage/shared ~/dl_shared 2>/dev/null || true
echo "✅ نصب شد."
echo "اجرا: python -m allfinder \"عبارت\""
