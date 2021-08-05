import os, requests
from PIL import Image
from io import BytesIO

TOTAL_PUNKS = 10000

# Cryptopunk colors
TRANSPARENT = None
NOT_FOR_SALE = "#638596"
FOR_SALE = "#95554f"
ACTIVE_BID = "#8e6fb6"
WRAPPED = "#66a670"

# set background_hex as None for a transparent image
# base size is 24 x 24 pixels
def download_punks(max_punks = TOTAL_PUNKS, size = 144, background_hex = NOT_FOR_SALE):
    os.makedirs("cryptopunks", exist_ok=True)
    for i in range(max_punks):
        url = f"https://www.larvalabs.com/public/images/cryptopunks/punk{str(i).zfill(4)}.png"
        im_con = requests.get(url).content
        base_img = Image.open(BytesIO(im_con))
        final_img = base_img.resize((size, size), resample=Image.NEAREST)
        if background_hex:
            ni = Image.new("RGBA", final_img.size, color=background_hex)
            ni.paste(final_img, mask=final_img)
            final_img = ni
        final_img.save(os.path.join('cryptopunks', f'punk{str(i).zfill(4)}.png'), format='PNG')
        print(f"Downloaded Cryptopunk {str(i).zfill(4)}")
    print("All punks downloaded")

if __name__ == "__main__":
    download_punks(size=500)