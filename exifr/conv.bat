DIR /B /S /ON *.jpg > dir.list

FOR /F %%i IN (dir.list) DO python3 exifr.py %%i