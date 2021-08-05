# cryptopunks-ripper
Dumps cryptopunks at a specified resolution with an optional background

## Installing Dependencies
- Run the following command
```bash
$ pip install -r requirements.txt
```

## Configuring the ripper
- Open `cryptopunks.py` in a code editor
- Here you can configure how the image will be dumped in the last few lines of the code
- The background color of the cryptopunk is originally transparent, however you can customize this look to make it look like how they are displayed on the [website](https://www.larvalabs.com/cryptopunks) or any custom hex color you like. Setting the color as `None`, keeps the background as transparent.
- The size of the cryptopunk is originally 24x24 pixels, however the website displays them as 144x144. You can modify this size to your liking
- Some color hex values are already inserted as part of the code for your convenience. They represent the same colors as seen on the website. Look at images below

![image](https://user-images.githubusercontent.com/17220860/128394022-5869c5b7-d5e7-4708-8c5c-aab228f050c7.png)

The blue red and purple color hex values correspond to these backgrounds: 

![image](https://user-images.githubusercontent.com/17220860/128394217-82eb36cc-f85f-48dc-bc9c-1a12c7267c50.png)


## Running the ripper
- Simply run the following command to execute
```bash
$ python3 cryptopunks.py
```
- This should create a new directory called `cryptopunks` and should dump all the punks in the folder based on the configuration set

## Output
- Once the ripper is done running, you should see an output like this

![image](https://user-images.githubusercontent.com/17220860/128394327-bd3f930a-691b-4fa5-b16d-7860d2e56ab2.png)

## Feature Requests / Feedback
- Feel free to request any features or report any feedback/bugs using GitHub Issues. This project is under the MIT license.
