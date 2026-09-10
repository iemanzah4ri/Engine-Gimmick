from pathlib import Path
import re

html_path = Path(r'c:\Users\Ieman Zahari\OneDrive\Documents\gimik\D10D_ENGINE_COMING_SOON2.HTML')
text = html_path.read_text(encoding='utf-8')
pattern = r'(<img\s+id="finalDriveImg"\s+src=")([^"]+)(")'
replacement = r'\1Designer (10).png\3'
new_text, count = re.subn(pattern, replacement, text, count=1)
if count == 0:
    raise SystemExit('No finalDriveImg tag found to update.')
html_path.write_text(new_text, encoding='utf-8')
print('Updated finalDriveImg to Designer (10).png')
