import sys
import os
import pysrt
import jieba
from pypinyin import pinyin, Style
from deep_translator import GoogleTranslator

def to_pinyin_word(word: str) -> str:
    parts = pinyin(word, style=Style.TONE, heteronym=False)
    return "".join(syllable[0] for syllable in parts)

if len(sys.argv) < 2:
    print("Usage: python convert.py <subtitle.srt>")
    sys.exit(1)

input_file = sys.argv[1]
subs = pysrt.open(input_file)

translator = GoogleTranslator(source="zh-CN", target="en")
cache = {}

for sub in subs:
    text = sub.text.replace("\n", " ").strip()
    if not text:
        continue

    words = [w for w in jieba.cut(text) if w.strip()]

    pinyin_line = " ".join(to_pinyin_word(w) for w in words)

    word_parts = []
    for w in words:
        py = to_pinyin_word(w)

        if w not in cache:
            try:
                cache[w] = translator.translate(w)
            except:
                cache[w] = ""

        meaning = cache[w]

        word_parts.append(f"{w}({py}:{meaning})")

    word_line = " ".join(word_parts)

    sentence_translation = translator.translate(text)

    sub.text = f"{text}\n{pinyin_line}\n{word_line}\n{sentence_translation}"

base, ext = os.path.splitext(input_file)
output_file = base + "_annotated.srt"

subs.save(output_file)

print("Saved:", output_file)