fax-machine
===========

Fax-machine
=====

Small, as-of-yet secret-ish project. But it's basically just a twillio server.


Install
=======

This runs great on Heroku.

You'll need:
* A Twilio account

You'll need to set environment variables with details for those services. You can use the example `setenv.sh` in the repo (obviously, use your own environment variables and run `source setenv.sh`).

Then, install with these commands:

1. Create virtual environment: `mkvirtualenv faxes`

2. `pip install -r requirements.txt` to install the required python packages into the environment

3. Load environment variables. Re-name setenv-sample.sh as setenv.sh, fill in the blanks with your Twilio information, then run `source setenv.sh`.

4. Run `python server.py`

