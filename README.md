# Covid Update Telegram Bot

A telegram bot that gives COVID 19 update

## Requirements:

- Telegram bot API token & bot owner ID
- A postgress db with creditials

## How to deploy

### Linux:

- Make a copy of `creds_local.sample` as `creds_local.py`

```bash
$ cp creds_local.sample creds_local.py
```
- Run `deploy.sh`
```bash
$ chmod +x deploy.sh
$ ./deploy.sh

#or

$ bash deploy.sh