from pathlib import Path
text = Path('RomeoAndJuliet.txt').read_text()

import imageio

mask_image = imageio.imread('mask_heart.png')

from wordcloud import WordCloud
wc = WordCloud(colormap = 'prism', mask = mask_image, background_color = 'white')

wc = wc.generate(text)

wc.to_file('RomeoJuliet.png')