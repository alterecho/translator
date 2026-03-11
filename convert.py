import sys
import os
import pysrt
from pypinyin import lazy_pinyin
from deep_translator import GoogleTranslator

if len(sys.argv) < 2:
    print("Usage: python convert.py <subtitle.srt>")
    sys.exit(1)

input_file = sys.argv[1]

subs = pysrt.open(input_file)

translator = GoogleTranslator(source="zh-CN", target="en")

for sub in subs:
    text = sub.text.replace("\n", " ").strip()
    if not text:
        continue

    pinyin = " ".join(lazy_pinyin(text))
    translation = translator.translate(text)

    sub.text = f"{text}\n{pinyin}\n{translation}"

base, ext = os.path.splitext(input_file)
output_file = base + "_study.srt"

subs.save(output_file)

print("Saved:", output_file)
