Simple secure code demonstration how to prevent Shell injections in Python Shell wrappers. This is a wrapper for "ps" system utility which can be used for checking processes of particular user (or all available) but do not allow using Shell special sequences (like && ; > < >>, etc) to inject malicious commands.


Example of usage:

$./ps.py

Select user to get info: avahi

avahi      362  0.0  0.0  47140  3576 ?        Ss   16:46   0:00 avahi-daemon: running [linlap.local]

avahi      379  0.0  0.0  47016   352 ?        S    16:46   0:00 avahi-daemon: chroot helper




$ ./ps.py

Select user to get info: avahi ; rm -rf /*

No such user or wrong parameteres: avahi ; rm -rf /*


