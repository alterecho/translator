# install dependencies
```bash
pip install pypinyin googletrans==4.0.0rc1 pysrt
pip uninstall googletrans
pip install deep-translator
```

# create virtual environment
```bash
python3 -m venv venv
```

# use virtual environment before running the script
```bash
source venv/bin/activate
```

# run the script
```bash
python convert.py input.srt
```