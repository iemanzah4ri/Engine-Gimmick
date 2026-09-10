from pathlib import Path
import re

path = Path(r'c:\Users\Ieman Zahari\OneDrive\Documents\gimik\D10D_ENGINE_COMING_SOON2.HTML')
text = path.read_text(encoding='utf-8')

# Remove duplicated overlay block if present, keeping a single overlay with subtitle.
pattern = r'(?s)(<div id="overlay">.*?</div>\s*)(<div id="overlay">.*?</div>\s*)(?=\n<script>)'
replacement = r'\1'
new_text, count = re.subn(pattern, replacement, text, count=1)
if count == 0:
    # Fallback: if there is still no subtitle, add it in the first overlay.
    if '<div id="subtext">' not in text:
        new_text = text.replace(
            '<div id="bigtext">D01D ENGINE</div>',
            '<div id="bigtext">D01D ENGINE</div>\n  <div id="subtext">SYSTEM ONLINE</div>',
            1,
        )
    else:
        new_text = text
else:
    if '<div id="subtext">' not in new_text:
        new_text = new_text.replace(
            '<div id="bigtext">D01D ENGINE</div>',
            '<div id="bigtext">D01D ENGINE</div>\n  <div id="subtext">SYSTEM ONLINE</div>',
            1,
        )

path.write_text(new_text, encoding='utf-8')
print(f'Duplicates removed: {count}')
print('Subtitle present:', '<div id="subtext">' in path.read_text(encoding='utf-8'))
