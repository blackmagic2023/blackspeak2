# blackspeak2
A message encryption and decryption script for secure 2-way communication.

# Setup

Download the script

```
git clone
```

Install dependencies

```
pip install pycryptodome
```

Enter working directory for script

```
cd blackspeak2
```

# Usage

Run the script

```
python3 blackspeak2.py
```

Decrypting a message

When a message is encrypted the user is presented with a collection of strings that represent the encrypted data. This is how you break down the strings for the decryption input...

Encrypted string collection example

```
aHDivRXKSwPtyrdl/5oVKioGy/XKn06t3xP1bH3rVmx9qPzoCMRiZo+V0A6g/8i7K+xdW4SYGULYshjNtZ0CgxTBTevEETPQo0tExVtoFzce1lQZO1dmLV2OMeCmi/t8FEK+hsBPcODBUbKwbud8FCqKQ8hEiJGt2AddLzRhaDUtWq4iwAH1iHzQtmrriSr1xXqbm9yyeGZQVj5ZWwYnXIDcfMZ4e4okimzFtV9flkPQSyB/EdJEFOO21+ZeM7JN68rtZpPszjlO3dPkSzmR+Dp5eIn69IlFpnjnE5G37BKF+FREDjGvMcT6xPgXcPVuH0MHI8hdtbP8EdmkDMTYNw== OxvU1cH/XlwF1eFeH7TNjg== k4wwZWao1npEgm285SsFMw== xhKbo5rF11r4GwIOzr2Q79rYrOlwUFQC5sYqsZATkw==
```

Image

![bvs2](https://github.com/blackmagic2023/blackspeak/assets/149164084/4523786b-2d6b-4a38-a6e6-a99fbc5d99fe)

I suggest seperating the encrypted message into the required sections for decryption like so

```
Encrypted session key (beginning of message)

aHDivRXKSwPtyrdl/5oVKioGy/XKn06t3xP1bH3rVmx9qPzoCMRiZo+V0A6g/8i7K+xdW4SYGULYshjNtZ0CgxTBTevEETPQo0tExVtoFzce1lQZO1dmLV2OMeCmi/t8FEK+hsBPcODBUbKwbud8FCqKQ8hEiJGt2AddLzRhaDUtWq4iwAH1iHzQtmrriSr1xXqbm9yyeGZQVj5ZWwYnXIDcfMZ4e4okimzFtV9flkPQSyB/EdJEFOO21+ZeM7JN68rtZpPszjlO3dPkSzmR+Dp5eIn69IlFpnjnE5G37BKF+FREDjGvMcT6xPgXcPVuH0MHI8hdtbP8EdmkDMTYNw==

nonce (directly after session key)

OxvU1cH/XlwF1eFeH7TNjg==

tag (after nonce)

k4wwZWao1npEgm285SsFMw==

ciphertext (after tag)

xhKbo5rF11r4GwIOzr2Q79rYrOlwUFQC5sYqsZATkw==
```

If you noticed they are in order corrosponding to the required input upon decryption!

# Images

![bvs2](https://github.com/blackmagic2023/blackspeak/assets/149164084/4523786b-2d6b-4a38-a6e6-a99fbc5d99fe)

![dsad](https://github.com/blackmagic2023/blackspeak/assets/149164084/3a1fb63c-1cec-49aa-bd72-629b8526feb6)
