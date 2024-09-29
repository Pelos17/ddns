It will only change the IP if needed. If it finds that the current IP of the devices is already on record, will only log the result.


##Reqs##
It depends on the following python modules:

sys
requests
datetime


##Instruction of use:##

Call ddns.py with domain/TYPE/HOST. Example: kkpj.pro/A/satisfactory.

You need to cron the script. Over the cron you will specify the frecuency of checking.