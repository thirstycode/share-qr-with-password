# share-qr-with-password
[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/)  &nbsp;&nbsp; ![Platforms](https://img.shields.io/conda/pn/conda-forge/python.svg)
**Want to share messages from qr but to have have passwords? you're at right place**<br>
This python script makes pdf with password protection and uploads it to dropbox and makes a sharable link of it.

### Installation:
```bash
1. git clone https://github.com/thirstycode/share-qr-with-password
2. cd share-qr-with-password
3. pip3 install -r requirements.txt
```
### Add TOKEN in ```config.py```:
  - Make a dropbox account - [Here](https://www.dropbox.com/).
  - Login to it.
  - Make a DBX app and give it access to dropbox space - [Here](https://www.dropbox.com/developers/apps/create).
    - Choose API - Dropbox API
    - Type of access - Full Dropbox
    - App name : Any name of your choice
  - Goto app in 'my apps' and from 'OAuth 2' generate access token of that app.
  - Copy access token and copy that to ```config.py```

#### Execute It:
```bash
1. python program.py
```


