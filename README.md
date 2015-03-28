# Installation instructions

#### Install Postgres
- [Download installer](git@github.com:Gilroy-Morgan-Hill-Devs/stats-tracker.git)
- Install psycop2
  - Mac: `PATH=/Library/PostgreSQL/9.4/bin/:$PATH pip install psycopg2`
  - [Windows](http://stickpeople.com/projects/python/win-psycopg/)
- Set some environment variables?
  - export DYLD_LIBRARY_PATH=/Library/PostgreSQL/9.3/lib
- At this point I'm kinda stuck due to the following error
```
django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 module: dlopen(/Users/nesan/.virtualenvs/play/lib/python2.7/site-packages/psycopg2/_psycopg.so, 2): Symbol not found: __cg_jpeg_resync_to_restart
```
I suspect the mac install dynamic libraries don't play well with whateve requires them in  psycop2

# stats-tracker
Norm was here  Happy Pi day
