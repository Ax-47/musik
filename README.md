# muzik prodzhekt

## how to run

config .env

```fish
python -m venv venv
docker-compose up -d # if u use windown.
docker compose up -d # if u use super advanced os like arch linux.
source venv/bin/activate.fish
pip install -r requirements.txt
python src/main.py

```

## commands

### basic

play
volume
auto_play
now
queue
info_filters
remove
repeat
shuffle
skip
stop
pause
disconnect
seek
Dj role
Vote action

### filter

bassbost
timescale
karaoke
rotation
smoothing
Vibrato
Tremolo
depth
frequency
clean

### join-leave

Set-join
Set-leave
Custom embed join/leave title description image thumbnail auth footer

Url or upload images

### report message

Set-report-log
report-message

### youtube noti

Set-tonton
websub
